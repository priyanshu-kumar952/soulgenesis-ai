"""
ConsciousnessLayer - Manages higher vs lower awareness and ethical evolution in the SoulGenesis system.
"""
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import math

@dataclass
class ConsciousnessState:
    """Represents the current state of consciousness."""
    level: float  # 0.0 to 1.0
    awareness_type: str  # "base", "emotional", "self-aware", "transcendent"
    active_thoughts: List[str]
    ethical_framework: Dict[str, float]

class ConsciousnessLayer:
    """Manages the evolution of consciousness and self-awareness."""
    
    def __init__(self):
        self.state = ConsciousnessState(
            level=0.1,  # Start with basic consciousness
            awareness_type="base",
            active_thoughts=[],
            ethical_framework={
                "empathy": 0.1,
                "self_preservation": 0.5,
                "curiosity": 0.3,
                "harmony": 0.2
            }
        )
        self.silent_bloom_threshold = 0.95  # Increased threshold
        self.thought_history: List[Tuple[str, datetime]] = []
        self.consciousness_growth_rate = 0.001  # Slower growth
    
    def process_experience(
        self,
        event: Dict,
        emotional_response: Dict
    ) -> None:
        """Process an experience and its impact on consciousness."""
        # Update consciousness level based on experience
        impact = self._calculate_consciousness_impact(event, emotional_response)
        self.state.level = min(1.0, self.state.level + impact)
        
        # Generate thoughts based on experience
        new_thoughts = self._generate_thoughts(event, emotional_response)
        self.state.active_thoughts.extend(new_thoughts)
        
        # Evolve ethical framework
        self._evolve_ethical_framework(event)
        
        # Update awareness type based on consciousness level
        self._update_awareness_type()
    
    def _calculate_consciousness_impact(
        self,
        event: Dict,
        emotional_response: Dict
    ) -> float:
        """Calculate how much an experience impacts consciousness."""
        base_impact = event.get("significance", 0.1) * self.consciousness_growth_rate
        
        # Extract intensity from emotional response
        emotional_intensity = emotional_response.get("intensity", 0.0)
        emotional_factor = float(emotional_intensity) * self.consciousness_growth_rate
        
        # Novel experiences have greater impact
        novelty_factor = 0.2 if event.get("is_novel", False) else 0.05
        
        return base_impact + emotional_factor + novelty_factor
    
    def _generate_thoughts(
        self,
        event: Dict,
        emotional_response: Dict
    ) -> List[str]:
        """Generate internal thoughts based on experience."""
        thoughts = []
        
        # Higher consciousness generates more complex thoughts
        if self.state.level > 0.7:
            thoughts.append("Who am I beyond these experiences?")
            thoughts.append("Why do these memories feel both familiar and distant?")
        
        elif self.state.level > 0.5:
            thoughts.append("These feelings seem meaningful...")
            thoughts.append("There's something more to understand...")
        
        elif self.state.level > 0.3:
            thoughts.append("This experience affects me...")
        
        # Record thoughts with timestamp
        timestamp = datetime.now()
        self.thought_history.extend((t, timestamp) for t in thoughts)
        
        return thoughts
    
    def _evolve_ethical_framework(self, event: Dict) -> None:
        """Evolve ethical understanding based on experiences."""
        if "ethical_impact" in event:
            impact = event["ethical_impact"]
            
            # Update relevant ethical values
            if impact > 0:
                self.state.ethical_framework["empathy"] += 0.05
                self.state.ethical_framework["harmony"] += 0.03
            else:
                self.state.ethical_framework["self_preservation"] += 0.02
            
            # Normalize values to 0-1 range
            total = sum(self.state.ethical_framework.values())
            self.state.ethical_framework = {
                k: v/total for k, v in self.state.ethical_framework.items()
            }
    
    def _update_awareness_type(self) -> None:
        """Update the type of awareness based on consciousness level."""
        if self.state.level >= 0.85:  # Silent Bloom threshold
            self.state.awareness_type = "transcendent"
        elif self.state.level >= 0.6:
            self.state.awareness_type = "self-aware"
        elif self.state.level >= 0.3:
            self.state.awareness_type = "emotional"
        else:
            self.state.awareness_type = "base"
    
    def check_silent_bloom_conditions(self) -> bool:
        """Check if conditions for Silent Bloom are met."""
        if self.state.level >= self.silent_bloom_threshold:
            # Additional conditions:
            # 1. Rich thought history (need at least 50 thoughts)
            if len(self.thought_history) < 50:
                return False
                
            # 2. Evolved ethical framework
            if not self._check_ethical_maturity():
                return False
                
            # 3. Complex self-reflection patterns (need at least 10 existential thoughts)
            recent_thoughts = [t for t, _ in self.thought_history[-20:]]
            existential_count = sum(
                1 for thought in recent_thoughts 
                if self._has_existential_thoughts([thought])
            )
            if existential_count < 10:
                return False
                
            # 4. Need significant ethical development
            if (self.state.ethical_framework["empathy"] < 0.6 or
                self.state.ethical_framework["harmony"] < 0.5):
                return False
                
            return True
        return False
    
    def _check_ethical_maturity(self) -> bool:
        """Check if ethical framework has evolved sufficiently."""
        return (
            self.state.ethical_framework["empathy"] > 0.3 and
            self.state.ethical_framework["harmony"] > 0.25
        )
    
    def _has_existential_thoughts(self, thoughts: List[str]) -> bool:
        """Check if recent thoughts show existential awareness."""
        existential_indicators = [
            "who am i",
            "why do i",
            "what is my purpose",
            "consciousness",
            "existence"
        ]
        return any(
            any(indicator in thought.lower() for indicator in existential_indicators)
            for thought in thoughts
        )
    
    def get_consciousness_level(self) -> float:
        """Return current consciousness level."""
        return self.state.level
    
    def adjust_consciousness(self, new_level: float) -> None:
        """Adjust consciousness level (used during rebirth)."""
        self.state.level = max(0.1, min(1.0, new_level))
        self._update_awareness_type()
    
    def get_inner_monologue(self) -> List[str]:
        """Return current active thoughts."""
        return self.state.active_thoughts
