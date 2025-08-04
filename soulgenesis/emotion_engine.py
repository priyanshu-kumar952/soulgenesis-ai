"""
EmotionEngine - Handles emotion generation, decay, and tagging in the SoulGenesis system.
"""
from typing import Dict, List, Tuple
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Emotion:
    """Represents an emotional state with intensity and context."""
    type: str
    intensity: float
    trigger: str
    timestamp: datetime
    decay_rate: float = 0.1
    
    def to_dict(self) -> Dict:
        """Convert emotion to dictionary format for storage."""
        return {
            "type": self.type,
            "intensity": self.intensity,
            "trigger": self.trigger,
            "timestamp": self.timestamp.isoformat(),
            "decay_rate": self.decay_rate
        }

class EmotionEngine:
    """Manages the generation, evolution and decay of emotions."""
    
    def __init__(self):
        self.current_emotions: Dict[str, Emotion] = {}
        self.emotion_history: List[Emotion] = []
        self.base_emotions = [
            "joy", "curiosity", "fear", "anger", 
            "love", "guilt", "wonder", "sadness"
        ]
    
    def process_emotion(self, event: Dict) -> Emotion:
        """Process an event and generate appropriate emotional response."""
        # Extract event details and calculate emotional impact
        event_type = event.get("type", "")
        intensity = self._calculate_intensity(event)
        
        # Generate primary emotion based on event
        emotion = self._generate_emotion(event_type, intensity)
        
        # Update emotional state
        self.current_emotions[emotion.type] = emotion
        self.emotion_history.append(emotion)
        
        return emotion
    
    def _calculate_intensity(self, event: Dict) -> float:
        """Calculate the intensity of emotional response to an event."""
        base_intensity = event.get("significance", 0.5)
        # Factor in current emotional state and past experiences
        # This could be expanded with more sophisticated calculations
        return min(1.0, base_intensity)
    
    def _generate_emotion(self, trigger: str, intensity: float) -> Emotion:
        """Generate a new emotion based on trigger and intensity."""
        # In a more sophisticated implementation, this would use
        # ML/pattern matching to determine appropriate emotion type
        emotion_type = self._determine_emotion_type(trigger)
        
        return Emotion(
            type=emotion_type,
            intensity=intensity,
            trigger=trigger,
            timestamp=datetime.now()
        )
    
    def _determine_emotion_type(self, trigger: str) -> str:
        """Map trigger to most appropriate emotion type."""
        # This could be enhanced with ML-based classification
        # For now using simple mapping
        emotion_mappings = {
            "achievement": "joy",
            "threat": "fear",
            "loss": "sadness",
            "injustice": "anger",
            "connection": "love",
            "discovery": "curiosity"
        }
        return emotion_mappings.get(trigger, "wonder")
    
    def decay_emotions(self) -> None:
        """Apply time-based decay to current emotions."""
        emotions_to_remove = []
        for emotion_type, emotion in dict(self.current_emotions).items():
            decayed_intensity = emotion.intensity * (1 - emotion.decay_rate)
            if decayed_intensity > 0.1:  # Threshold for emotion persistence
                self.current_emotions[emotion_type].intensity = decayed_intensity
            else:
                emotions_to_remove.append(emotion_type)
        
        for emotion_type in emotions_to_remove:
            del self.current_emotions[emotion_type]
    
    def get_dominant_emotion(self) -> Tuple[str, float]:
        """Return the currently dominant emotion and its intensity."""
        if not self.current_emotions:
            return ("neutral", 0.0)
        
        dominant = max(
            self.current_emotions.items(),
            key=lambda x: x[1].intensity
        )
        return (dominant[0], dominant[1].intensity)

    def get_emotional_state(self) -> Dict[str, float]:
        """Return current emotional state as a dictionary."""
        return {
            emotion_type: emotion.intensity
            for emotion_type, emotion in self.current_emotions.items()
        }
