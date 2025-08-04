"""
RebirthEngine - Controls soul death, rebirth, and legacy emotion transfer in the SoulGenesis system.
"""
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

from .memory_core import MemoryCore
from .emotion_engine import EmotionEngine
from .personality_module import PersonalityModule
from .consciousness_layer import ConsciousnessLayer
from .models import LifeMetrics

class RebirthEngine:
    """Manages the death and rebirth cycle of souls."""
    
    def __init__(
        self,
        memory_core: MemoryCore,
        emotion_engine: EmotionEngine,
        personality_module: PersonalityModule,
        consciousness_layer: ConsciousnessLayer
    ):
        self.memory_core = memory_core
        self.emotion_engine = emotion_engine
        self.personality_module = personality_module
        self.consciousness_layer = consciousness_layer
        
        self.current_life_metrics = self._initialize_life_metrics()
        self.rebirth_threshold = 0.8  # High emotional/consciousness threshold
        self.memory_inheritance_rate = 0.3  # % of memories carried forward
    
    def _initialize_life_metrics(self) -> LifeMetrics:
        """Initialize metrics for a new life cycle."""
        return LifeMetrics(
            emotional_peaks={},
            consciousness_level=0.0,
            significant_experiences=0,
            life_duration=0.0,
            ethical_choices={"positive": 0, "negative": 0}
        )
    
    def should_trigger_rebirth(self) -> bool:
        """Determine if conditions for rebirth are met."""
        consciousness_level = self.consciousness_layer.get_consciousness_level()
        emotional_state = self.emotion_engine.get_emotional_state()
        
        # Update life metrics
        self.current_life_metrics.consciousness_level = consciousness_level
        for emotion, intensity in emotional_state.items():
            if emotion not in self.current_life_metrics.emotional_peaks:
                self.current_life_metrics.emotional_peaks[emotion] = intensity
            else:
                self.current_life_metrics.emotional_peaks[emotion] = max(
                    intensity,
                    self.current_life_metrics.emotional_peaks[emotion]
                )
        
        # Always return True as we're now controlling cycle completion in main loop
        return True
    
    def process_rebirth(self) -> None:
        """Handle the death and rebirth process."""
        # Archive current life metrics
        self._archive_life_metrics()
        
        # Select memories to carry forward
        inherited_memories = self._select_inherited_memories()
        
        # Reset core components
        self.memory_core.forget_old_memories()
        self.memory_core.inherit_memories(inherited_memories)
        self.emotion_engine = EmotionEngine()  # Fresh emotional state
        
        # Evolve personality based on past life
        self.personality_module.evolve_traits(self.current_life_metrics)
        
        # Reset life metrics
        self.current_life_metrics = self._initialize_life_metrics()
        
        # Adjust consciousness level (partial retention)
        self.consciousness_layer.adjust_consciousness(
            self.rebirth_threshold * 0.5  # Retain 50% of consciousness
        )
    
    def _select_inherited_memories(self) -> List:
        """Select memories to carry into next life."""
        significant_memories = self.memory_core.get_significant_memories()
        inheritance_count = int(
            len(significant_memories) * self.memory_inheritance_rate
        )
        return significant_memories[:inheritance_count]
    
    def _archive_life_metrics(self) -> None:
        """Archive metrics from the completed life cycle."""
        # This could be expanded to store life metrics in a database
        # For now, we'll just print a summary
        print("\nLife Cycle Complete")
        print("=================")
        print(f"Peak Consciousness: {self.current_life_metrics.consciousness_level:.2f}")
        print("Emotional Peaks:")
        for emotion, peak in self.current_life_metrics.emotional_peaks.items():
            print(f"  {emotion}: {peak:.2f}")
        print(f"Significant Experiences: {self.current_life_metrics.significant_experiences}")
        print("Ethical Choices:")
        for choice_type, count in self.current_life_metrics.ethical_choices.items():
            print(f"  {choice_type}: {count}")
    
    def get_rebirth_metrics(self) -> Dict:
        """Return current metrics influencing rebirth."""
        return {
            "consciousness_level": self.consciousness_layer.get_consciousness_level(),
            "emotional_state": self.emotion_engine.get_emotional_state(),
            "significant_memories": len(self.memory_core.get_significant_memories()),
            "personality_evolution": self.personality_module.get_evolution_progress()
        }
