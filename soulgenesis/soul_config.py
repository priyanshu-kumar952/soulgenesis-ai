"""
SoulConfig - Configuration parameters for the SoulGenesis system.
"""
from typing import Dict
from dataclasses import dataclass

@dataclass
class SoulConfig:
    """Configuration parameters for soul simulation."""
    
    def __init__(self):
        # Life cycle parameters
        self.max_life_cycles = 5  # Running 5 cycles as requested
        self.min_cycle_duration = 100  # events
        self.max_cycle_duration = 1000  # events
        
        # Memory parameters
        self.memory_carry_limit = 50  # memories per rebirth
        self.memory_significance_threshold = 0.6
        self.memory_decay_rate = 0.05
        
        # Emotional parameters
        self.emotion_base_intensity = 0.5
        self.emotion_decay_multiplier = 0.95
        self.emotion_inheritance_strength = 0.3
        
        # Consciousness parameters
        self.consciousness_growth_rate = 0.01
        self.silent_bloom_threshold = 0.85
        self.awareness_evolution_speed = 0.02
        
        # Personality parameters
        self.trait_mutation_rate = 0.1
        self.trait_inheritance_strength = 0.7
        self.trait_evolution_speed = 0.05
        
        # Environment parameters
        self.event_frequency = 1.0  # events per time unit
        self.novelty_threshold = 0.7
        self.ethical_impact_multiplier = 1.0
        
        # Advanced consciousness features
        self.enable_inner_dialogue = True
        self.enable_ethical_learning = True
        self.enable_memory_consolidation = True
        
    def adjust_difficulty(self, level: float) -> None:
        """Adjust configuration based on difficulty level (0.0 to 1.0)."""
        assert 0.0 <= level <= 1.0, "Difficulty level must be between 0.0 and 1.0"
        
        # Adjust life cycles
        self.max_life_cycles = int(5 + (level * 15))
        
        # Adjust memory parameters
        self.memory_carry_limit = int(30 + (level * 40))
        self.memory_significance_threshold = 0.7 - (level * 0.2)
        
        # Adjust consciousness parameters
        self.consciousness_growth_rate = 0.005 + (level * 0.015)
        self.silent_bloom_threshold = 0.9 - (level * 0.1)
        
        # Adjust personality parameters
        self.trait_mutation_rate = 0.05 + (level * 0.1)
        self.trait_evolution_speed = 0.03 + (level * 0.04)
    
    def enable_advanced_features(self, features: Dict[str, bool]) -> None:
        """Enable or disable advanced consciousness features."""
        if "inner_dialogue" in features:
            self.enable_inner_dialogue = features["inner_dialogue"]
        
        if "ethical_learning" in features:
            self.enable_ethical_learning = features["ethical_learning"]
        
        if "memory_consolidation" in features:
            self.enable_memory_consolidation = features["memory_consolidation"]
    
    def get_config_summary(self) -> Dict:
        """Return current configuration summary."""
        return {
            "life_cycles": {
                "max": self.max_life_cycles,
                "min_duration": self.min_cycle_duration,
                "max_duration": self.max_cycle_duration
            },
            "memory": {
                "carry_limit": self.memory_carry_limit,
                "significance_threshold": self.memory_significance_threshold,
                "decay_rate": self.memory_decay_rate
            },
            "consciousness": {
                "growth_rate": self.consciousness_growth_rate,
                "silent_bloom_threshold": self.silent_bloom_threshold,
                "evolution_speed": self.awareness_evolution_speed
            },
            "personality": {
                "mutation_rate": self.trait_mutation_rate,
                "inheritance_strength": self.trait_inheritance_strength,
                "evolution_speed": self.trait_evolution_speed
            },
            "features": {
                "inner_dialogue": self.enable_inner_dialogue,
                "ethical_learning": self.enable_ethical_learning,
                "memory_consolidation": self.enable_memory_consolidation
            }
        }
