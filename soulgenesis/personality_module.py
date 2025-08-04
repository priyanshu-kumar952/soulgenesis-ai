"""
PersonalityModule - Assigns Soul ID and core traits, tracks evolution in the SoulGenesis system.
"""
from typing import Dict, List, Optional
from dataclasses import dataclass
import uuid
import math
import random

from .models import LifeMetrics

@dataclass
class Trait:
    """Represents a personality trait with its current value and evolution rate."""
    name: str
    value: float  # 0.0 to 1.0
    evolution_rate: float
    description: str

class PersonalityModule:
    """Manages soul personality traits and their evolution."""
    
    def __init__(self):
        self.soul_id = str(uuid.uuid4())
        self.traits = self._initialize_traits()
        self.evolution_history: List[Dict] = []
        self.mutation_chance = 0.1
    
    def _initialize_traits(self) -> Dict[str, Trait]:
        """Initialize core personality traits."""
        return {
            "empathy": Trait(
                name="empathy",
                value=0.3,
                evolution_rate=0.05,
                description="Ability to understand and share feelings"
            ),
            "curiosity": Trait(
                name="curiosity",
                value=0.4,
                evolution_rate=0.07,
                description="Drive to explore and learn"
            ),
            "resilience": Trait(
                name="resilience",
                value=0.35,
                evolution_rate=0.04,
                description="Ability to recover from difficulties"
            ),
            "adaptability": Trait(
                name="adaptability",
                value=0.3,
                evolution_rate=0.06,
                description="Flexibility in facing change"
            ),
            "creativity": Trait(
                name="creativity",
                value=0.25,
                evolution_rate=0.05,
                description="Ability to think originally"
            ),
            "harmony": Trait(
                name="harmony",
                value=0.2,
                evolution_rate=0.03,
                description="Tendency towards peaceful balance"
            )
        }
    
    def evolve_traits(self, life_metrics: 'LifeMetrics') -> None:
        """Evolve traits based on life experiences."""
        # Record pre-evolution state
        pre_evolution = {
            name: trait.value 
            for name, trait in self.traits.items()
        }
        
        # Process emotional peaks
        self._evolve_from_emotions(life_metrics.emotional_peaks)
        
        # Process ethical choices
        self._evolve_from_ethics(life_metrics.ethical_choices)
        
        # Apply consciousness influence
        self._evolve_from_consciousness(life_metrics.consciousness_level)
        
        # Chance for random mutation
        self._apply_random_mutation()
        
        # Record evolution
        self.evolution_history.append({
            "pre_evolution": pre_evolution,
            "post_evolution": {
                name: trait.value 
                for name, trait in self.traits.items()
            },
            "life_metrics": life_metrics
        })
    
    def _evolve_from_emotions(self, emotional_peaks: Dict[str, float]) -> None:
        """Evolve traits based on emotional experiences."""
        if "joy" in emotional_peaks:
            self._adjust_trait("creativity", 0.05)
            self._adjust_trait("harmony", 0.03)
        
        if "fear" in emotional_peaks:
            self._adjust_trait("resilience", 0.04)
            self._adjust_trait("adaptability", 0.05)
        
        if "love" in emotional_peaks:
            self._adjust_trait("empathy", 0.06)
            self._adjust_trait("harmony", 0.04)
        
        if "curiosity" in emotional_peaks:
            self._adjust_trait("curiosity", 0.05)
            self._adjust_trait("creativity", 0.03)
    
    def _evolve_from_ethics(self, ethical_choices: Dict[str, int]) -> None:
        """Evolve traits based on ethical decisions."""
        positive_ratio = ethical_choices.get("positive", 0) / (
            sum(ethical_choices.values()) or 1
        )
        
        if positive_ratio > 0.6:  # Predominantly positive choices
            self._adjust_trait("empathy", 0.05)
            self._adjust_trait("harmony", 0.04)
        else:  # More negative choices
            self._adjust_trait("resilience", 0.03)
            self._adjust_trait("adaptability", 0.05)
    
    def _evolve_from_consciousness(self, consciousness_level: float) -> None:
        """Evolve traits based on consciousness level."""
        consciousness_factor = consciousness_level * 0.1
        
        for trait in self.traits.values():
            evolution_amount = trait.evolution_rate * consciousness_factor
            self._adjust_trait(trait.name, evolution_amount)
    
    def _adjust_trait(self, trait_name: str, amount: float) -> None:
        """Adjust a trait value while keeping it in bounds."""
        if trait_name in self.traits:
            current = self.traits[trait_name].value
            self.traits[trait_name].value = max(0.0, min(1.0, current + amount))
    
    def _apply_random_mutation(self) -> None:
        """Randomly mutate traits with small probability."""
        if random.random() < self.mutation_chance:
            trait = random.choice(list(self.traits.keys()))
            mutation = (random.random() - 0.5) * 0.1  # -0.05 to +0.05
            self._adjust_trait(trait, mutation)
    
    def get_dominant_traits(self, threshold: float = 0.6) -> List[str]:
        """Return list of traits above specified threshold."""
        return [
            name for name, trait in self.traits.items()
            if trait.value >= threshold
        ]
    
    def get_trait_value(self, trait_name: str) -> Optional[float]:
        """Get the current value of a specific trait."""
        return (
            self.traits[trait_name].value 
            if trait_name in self.traits 
            else None
        )
    
    def get_evolution_progress(self) -> Dict[str, List[float]]:
        """Return trait evolution history."""
        return {
            trait_name: [
                record["post_evolution"][trait_name]
                for record in self.evolution_history
            ]
            for trait_name in self.traits.keys()
        }
    
    def get_personality_summary(self) -> Dict:
        """Return current personality state summary."""
        return {
            "soul_id": self.soul_id,
            "traits": {
                name: {
                    "value": trait.value,
                    "description": trait.description
                }
                for name, trait in self.traits.items()
            },
            "dominant_traits": self.get_dominant_traits(),
            "evolution_count": len(self.evolution_history)
        }
