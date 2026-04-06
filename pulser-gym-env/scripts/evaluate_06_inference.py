import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# Connect module structurally from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stable_baselines3 import PPO
from pulser_gym.env_01_core import PulserEnv

if __name__ == '__main__':
    print("--- Phase 6: PPO Agent Inference & Evaluation ---")
    
    # 1. Instantiate the physical bridge environment
    env = PulserEnv(n_qubits=9)
    
    # 2. Load the trained model artifacts
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(project_root, "Models_Local", "ppo_pulser_mis_v1")
    save_path = os.path.join(project_root, "Models_Local", "eval_plot.png")
    
    print(f"Loading trained model mapping from: {model_path}")
    model = PPO.load(model_path)
    
    # 3. The Evaluation Loop
    obs, info = env.reset()
    
    amplitudes = []
    rewards = []
    steps = []
    
    terminated = False
    truncated = False
    step_num = 0
    
    print("Executing Deterministic Physics Graph Evaluation...")
    while not (terminated or truncated):
        step_num += 1
        
        # Grab deterministic decision vectors strictly
        action, _states = model.predict(obs, deterministic=True)
        
        # Sequence translation & emulation mapping
        obs, reward, terminated, truncated, info = env.step(action)
        
        # Track scaled conceptual graphs [action[0] * 10.0]
        amplitudes.append(action[0] * 10.0)
        rewards.append(reward)
        steps.append(step_num)
        
    print(f"\nFinal Terminal Observation (Quantum State Representation): {obs}")
    
    # 4. Visualization Matrix
    try:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Subplot 1: Amplitudes
        ax1.plot(steps, amplitudes, 'b-', marker='o')
        ax1.set_title("Physical Laser Amplitude Iteration Vector")
        ax1.set_ylabel("Amplitude (rad/µs)")
        ax1.grid(True)
        
        # Subplot 2: Rewards
        ax2.plot(steps, rewards, 'g-', marker='s')
        ax2.set_title("Maximum Independent Set (MIS) Constraint Score")
        ax2.set_xlabel("Gymnasium Pipeline Iterations")
        ax2.set_ylabel("MIS Mathematical Score")
        ax2.grid(True)
        
        plt.tight_layout()
        plt.savefig(save_path)
        print(f"\n[SUCCESS] Deterministic physics mapping plotted perfectly onto: {save_path}")
    except Exception as e:
        print(f"\n[WARNING] Plot generation failed mathematically: {e}")
