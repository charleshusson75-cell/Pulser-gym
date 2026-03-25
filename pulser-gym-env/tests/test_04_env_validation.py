import sys
import os

# Ensure pulser_gym module is visible to test runner
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gymnasium.utils.env_checker import check_env
from pulser_gym.env_01_core import PulserEnv

if __name__ == '__main__':
    print("Instantiating PulserEnv for Physics Execution...")
    env = PulserEnv(n_qubits=4)
    
    print("\nRunning gymnasium.utils.env_checker.check_env()...")
    # This might print warnings if purely deterministic observations aren't perfectly met 
    # but guarantees the environment structurally matches Gym API signature.
    check_env(env)
    
    print("\n[SUCCESS] Environment validation passed formulation. Commencing live loop:")
    
    obs, info = env.reset()
    for step_num in range(1, 4):
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        print(f"Step {step_num}:")
        print(f"  Action (Normalized Amplitude): {action[0]:.4f}")
        print(f"  Observation Bitstring Array:   {obs}")
        print(f"  Graph Score (MIS Reward):      {reward}")
        
        if terminated or truncated:
            obs, info = env.reset()
