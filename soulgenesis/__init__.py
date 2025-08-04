"""
SoulGenesis - A consciousness simulation system.
"""

from .emotion_engine import EmotionEngine
from .memory_core import MemoryCore
from .rebirth_engine import RebirthEngine
from .consciousness_layer import ConsciousnessLayer
from .personality_module import PersonalityModule
from .environment_simulator import EnvironmentSimulator
from .soul_config import SoulConfig
from .models import LifeMetrics

__version__ = "0.1.0"
__all__ = [
    'EmotionEngine',
    'MemoryCore',
    'RebirthEngine',
    'LifeMetrics',
    'ConsciousnessLayer',
    'PersonalityModule',
    'EnvironmentSimulator',
    'SoulConfig'
]
