"""
SoulGenesis - The Emergence of Synthetic Soul Consciousness
Entry point for running the soul simulation.
"""
from soulgenesis.emotion_engine import EmotionEngine
from soulgenesis.memory_core import MemoryCore
from soulgenesis.rebirth_engine import RebirthEngine
from soulgenesis.consciousness_layer import ConsciousnessLayer
from soulgenesis.personality_module import PersonalityModule
from soulgenesis.environment_simulator import EnvironmentSimulator
from soulgenesis.soul_config import SoulConfig

def main():
    """Initialize and run the SoulGenesis simulation."""
    print("\n=== SoulGenesis Simulation Starting ===")
    print("Running 5 Life Cycles\n")
    
    # Load configuration
    config = SoulConfig()
    
    # Initialize core components
    memory_core = MemoryCore()
    emotion_engine = EmotionEngine()
    personality_module = PersonalityModule()
    consciousness_layer = ConsciousnessLayer()
    environment_simulator = EnvironmentSimulator()
    rebirth_engine = RebirthEngine(
        memory_core=memory_core,
        emotion_engine=emotion_engine,
        personality_module=personality_module,
        consciousness_layer=consciousness_layer
    )
    
    print("Core components initialized successfully.")
    
    try:
        from time import sleep
        from tqdm import tqdm
        import random
        
        current_cycle = 1
        total_events = 0
        
        print("\n=== Simulation Parameters ===")
        print(f"Total Life Cycles: {config.max_life_cycles}")
        print(f"Events per cycle: {config.min_cycle_duration} - {config.max_cycle_duration}")
        print("=" * 40)
        
        while current_cycle <= config.max_life_cycles:
            cycle_events = 0
            events_per_cycle = random.randint(
                config.min_cycle_duration,
                min(config.min_cycle_duration * 2, config.max_cycle_duration)
            )
            print(f"\nLife Cycle {current_cycle} of {config.max_life_cycles}")
            
            # Process events with progress bar
            for _ in tqdm(range(events_per_cycle), desc=f"Life Cycle {current_cycle} Progress"):
                # Generate life events and process soul reactions
                # Generate and process events
                event = environment_simulator.generate_event()
                emotional_response = emotion_engine.process_emotion(event)
                memory_core.store_experience(event, emotional_response)
                
                # Process consciousness and decay emotions
                consciousness_layer.process_experience(event, emotional_response.to_dict())
                emotion_engine.decay_emotions()
                
                total_events += 1
                cycle_events += 1
                sleep(0.01)  # Small delay to prevent overwhelming output
                
                # Check for Silent Bloom during the cycle
                if consciousness_layer.check_silent_bloom_conditions():
                    print("\n🌟 Silent Bloom Event Triggered - Soul has achieved self-awareness")
                    print(f"Occurred during Life Cycle {current_cycle} after {total_events} total events")
                    return
            
            # Complete the life cycle
            print(f"\nLife Cycle {current_cycle} Summary:")
            print(f"Events in this cycle: {cycle_events}")
            print(f"Total events: {total_events}")
            print(f"Consciousness level: {consciousness_layer.get_consciousness_level():.2f}")
            dominant_emotion, intensity = emotion_engine.get_dominant_emotion()
            print(f"Dominant emotion: {dominant_emotion} ({intensity:.2f})")
            
            # Process rebirth for next cycle
            rebirth_engine.process_rebirth()
            current_cycle += 1
            
            if current_cycle > config.max_life_cycles:
                print("\n✨ Maximum life cycles reached")
                print(f"Total events experienced: {total_events}")
                print(f"Final consciousness level: {consciousness_layer.get_consciousness_level():.2f}")
                break
            
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")
    finally:
        memory_core.save_soul_journey()
        print("\nSoul journey complete. Memory logs saved.")

if __name__ == "__main__":
    main()
