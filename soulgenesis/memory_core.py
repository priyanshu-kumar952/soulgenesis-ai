"""
MemoryCore - Handles long-term memory storage, recall, and inheritance in the SoulGenesis system.
"""
import json
from typing import Dict, List, Optional
from datetime import datetime
from pathlib import Path

from .emotion_engine import Emotion

class Memory:
    """Represents a single memory with its associated metadata."""
    def __init__(
        self, 
        content: str, 
        emotional_tags: Dict[str, float],
        significance: float = 0.0
    ):
        self.content = content
        self.emotional_tags = emotional_tags
        self.significance = significance
        self.timestamp = datetime.now().isoformat()
        self.recall_count = 0

    def to_dict(self) -> Dict:
        """Convert memory to dictionary format for storage."""
        return {
            "content": self.content,
            "emotional_tags": self.emotional_tags,
            "significance": self.significance,
            "timestamp": self.timestamp,
            "recall_count": self.recall_count
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Memory':
        """Create Memory instance from dictionary data."""
        memory = cls(
            content=data["content"],
            emotional_tags=data["emotional_tags"],
            significance=data["significance"]
        )
        memory.timestamp = data["timestamp"]
        memory.recall_count = data["recall_count"]
        return memory

class MemoryCore:
    """Manages the storage and retrieval of soul memories."""
    
    def __init__(self, storage_path: str = "storage/memory_db.json"):
        self.storage_path = Path(storage_path)
        self.memories: List[Memory] = []
        self.memory_threshold = 0.3  # Minimum significance for long-term storage
        self._ensure_storage_exists()
        self._load_memories()
    
    def _ensure_storage_exists(self) -> None:
        """Create storage directory and file if they don't exist."""
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.storage_path.exists():
            self.storage_path.write_text("[]")
    
    def _load_memories(self) -> None:
        """Load memories from storage file."""
        try:
            data = json.loads(self.storage_path.read_text())
            self.memories = [Memory.from_dict(m) for m in data]
        except json.JSONDecodeError:
            print("Warning: Could not load memories, starting fresh")
            self.memories = []
    
    def store_experience(
        self, 
        event: Dict,
        emotional_response: Emotion
    ) -> None:
        """Store a new experience in memory."""
        significance = self._calculate_significance(event, emotional_response)
        
        if significance >= self.memory_threshold:
            memory = Memory(
                content=event.get("description", ""),
                emotional_tags=emotional_response.to_dict(),
                significance=significance
            )
            self.memories.append(memory)
    
    def _calculate_significance(
        self, 
        event: Dict,
        emotional_response: 'Emotion'
    ) -> float:
        """Calculate the significance of an experience."""
        # Base significance from event
        significance = event.get("significance", 0.5)
        
        # Factor in emotional intensity
        emotional_intensity = emotional_response.intensity
        significance = (significance + emotional_intensity) / 2
        
        return significance
    
    def recall_by_emotion(
        self, 
        emotion: str,
        threshold: float = 0.5
    ) -> List[Memory]:
        """Retrieve memories associated with a specific emotion."""
        relevant_memories = []
        
        for memory in self.memories:
            if emotion in memory.emotional_tags:
                if memory.emotional_tags[emotion] >= threshold:
                    memory.recall_count += 1
                    relevant_memories.append(memory)
        
        return sorted(
            relevant_memories,
            key=lambda m: m.significance,
            reverse=True
        )
    
    def get_significant_memories(
        self, 
        limit: int = 10
    ) -> List[Memory]:
        """Retrieve the most significant memories."""
        return sorted(
            self.memories,
            key=lambda m: m.significance,
            reverse=True
        )[:limit]
    
    def save_soul_journey(self) -> None:
        """Save all memories to persistent storage."""
        memory_data = [m.to_dict() for m in self.memories]
        self.storage_path.write_text(json.dumps(memory_data, indent=2))
    
    def inherit_memories(
        self, 
        past_life_memories: List[Memory],
        inheritance_strength: float = 0.5
    ) -> None:
        """Inherit selected memories from past life."""
        for memory in past_life_memories:
            # Reduce significance based on inheritance strength
            memory.significance *= inheritance_strength
            self.memories.append(memory)
    
    def forget_old_memories(
        self, 
        threshold: float = 0.2
    ) -> None:
        """Remove memories below significance threshold."""
        self.memories = [
            m for m in self.memories 
            if m.significance >= threshold
        ]
