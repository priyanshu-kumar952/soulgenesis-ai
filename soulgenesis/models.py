"""
Common data structures used across the SoulGenesis system.
"""
from typing import Dict
from dataclasses import dataclass

@dataclass
class LifeMetrics:
    """Tracks metrics for a single life cycle."""
    emotional_peaks: Dict[str, float]
    consciousness_level: float
    significant_experiences: int
    life_duration: float
    ethical_choices: Dict[str, int]
