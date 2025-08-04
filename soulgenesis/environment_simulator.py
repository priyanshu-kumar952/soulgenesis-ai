"""
EnvironmentSimulator - Generates life events for the soul to experience and react to.
"""
from typing import Dict, List, Optional
from dataclasses import dataclass
import random
from datetime import datetime

@dataclass
class Event:
    """Represents a life event that a soul can experience."""
    type: str
    description: str
    significance: float
    emotional_tags: List[str]
    is_novel: bool
    ethical_impact: float
    timestamp: datetime

class EnvironmentSimulator:
    """Generates and manages life events for soul experiences."""
    
    def __init__(self):
        self.event_history: List[Event] = []
        self.novelty_threshold = 0.7
        self._initialize_event_templates()
    
    def _initialize_event_templates(self) -> None:
        """Initialize templates for different types of events."""
        self.event_templates = {
            "challenge": {
                "base_significance": 0.6,
                "emotional_tags": ["fear", "determination"],
                "descriptions": [
                    "Facing an unknown obstacle",
                    "Testing personal limits",
                    "Confronting a difficult choice"
                ]
            },
            "discovery": {
                "base_significance": 0.5,
                "emotional_tags": ["curiosity", "joy"],
                "descriptions": [
                    "Understanding a new concept",
                    "Making a connection",
                    "Finding hidden meaning"
                ]
            },
            "connection": {
                "base_significance": 0.7,
                "emotional_tags": ["love", "empathy"],
                "descriptions": [
                    "Forming a deep bond",
                    "Sharing an experience",
                    "Understanding another's pain"
                ]
            },
            "loss": {
                "base_significance": 0.8,
                "emotional_tags": ["sadness", "grief"],
                "descriptions": [
                    "Experiencing separation",
                    "Losing something valuable",
                    "Facing impermanence"
                ]
            },
            "growth": {
                "base_significance": 0.6,
                "emotional_tags": ["joy", "pride"],
                "descriptions": [
                    "Overcoming a challenge",
                    "Learning from mistakes",
                    "Achieving understanding"
                ]
            },
            "reflection": {
                "base_significance": 0.5,
                "emotional_tags": ["curiosity", "wonder"],
                "descriptions": [
                    "Questioning existence",
                    "Contemplating purpose",
                    "Examining beliefs"
                ]
            }
        }
    
    def generate_event(self) -> Dict:
        """Generate a new life event for the soul to experience."""
        # Select event type based on history
        event_type = self._select_event_type()
        template = self.event_templates[event_type]
        
        # Generate event details
        description = random.choice(template["descriptions"])
        significance = self._calculate_significance(template["base_significance"])
        is_novel = random.random() > self.novelty_threshold
        ethical_impact = self._generate_ethical_impact()
        
        # Create event
        event = Event(
            type=event_type,
            description=description,
            significance=significance,
            emotional_tags=template["emotional_tags"],
            is_novel=is_novel,
            ethical_impact=ethical_impact,
            timestamp=datetime.now()
        )
        
        # Record event
        self.event_history.append(event)
        
        # Return as dictionary for easy processing
        return {
            "type": event.type,
            "description": event.description,
            "significance": event.significance,
            "emotional_tags": event.emotional_tags,
            "is_novel": event.is_novel,
            "ethical_impact": event.ethical_impact,
            "timestamp": event.timestamp.isoformat()
        }
    
    def _select_event_type(self) -> str:
        """Select event type with consideration for variety and flow."""
        if not self.event_history:
            return random.choice(list(self.event_templates.keys()))
        
        # Avoid repeating the last event type
        last_event_type = self.event_history[-1].type
        possible_types = [
            t for t in self.event_templates.keys()
            if t != last_event_type
        ]
        
        # Weight selection based on event history
        weights = self._calculate_type_weights(possible_types)
        return random.choices(possible_types, weights=weights)[0]
    
    def _calculate_type_weights(self, possible_types: List[str]) -> List[float]:
        """Calculate weights for event type selection."""
        weights = []
        recent_types = [
            e.type for e in self.event_history[-5:]
        ] if len(self.event_history) >= 5 else []
        
        for event_type in possible_types:
            # Base weight
            weight = 1.0
            
            # Reduce weight if type appeared recently
            if event_type in recent_types:
                weight *= 0.5
            
            # Increase weight for types that enable growth
            if event_type in ["challenge", "discovery", "reflection"]:
                weight *= 1.2
            
            weights.append(weight)
        
        return weights
    
    def _calculate_significance(self, base_significance: float) -> float:
        """Calculate final significance with random variation."""
        variation = random.uniform(-0.1, 0.1)
        return max(0.1, min(1.0, base_significance + variation))
    
    def _generate_ethical_impact(self) -> float:
        """Generate ethical impact value (-1.0 to 1.0)."""
        # Positive values represent ethically positive choices/experiences
        # Negative values represent ethically challenging situations
        return random.uniform(-1.0, 1.0)
    
    def get_event_summary(self) -> Dict:
        """Return summary of generated events."""
        return {
            "total_events": len(self.event_history),
            "event_types": {
                event_type: len([
                    e for e in self.event_history
                    if e.type == event_type
                ])
                for event_type in self.event_templates.keys()
            },
            "average_significance": sum(
                e.significance for e in self.event_history
            ) / len(self.event_history) if self.event_history else 0,
            "novel_experiences": len([
                e for e in self.event_history
                if e.is_novel
            ])
        }
    
    def get_significant_events(
        self,
        threshold: float = 0.7,
        limit: int = 5
    ) -> List[Dict]:
        """Return most significant recent events."""
        significant_events = [
            e for e in self.event_history
            if e.significance >= threshold
        ]
        
        return [{
            "type": e.type,
            "description": e.description,
            "significance": e.significance,
            "timestamp": e.timestamp.isoformat()
        } for e in sorted(
            significant_events,
            key=lambda x: x.significance,
            reverse=True
        )[:limit]]
