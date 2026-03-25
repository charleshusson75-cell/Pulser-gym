import os
import sys

# Connect module structurally to allow standard pipeline execution from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stable_baselines3 import PPO
from pulser_gym.env_01_core import PulserEnv

if __name__ == '__main__':
    print("--- Phase 5: PPO Agent Training Initialization ---")
    
    # 1. Instantiate the physical bridge environment deterministically
    env = PulserEnv(n_qubits=4)
    
    # 2. Setup the Proximal Policy Optimization (PPO) agent
    print("Loading Stable-Baselines3 PPO algorithm mapped with MlpPolicy...")
    model = PPO("MlpPolicy", env, verbose=1)
    
    # 3. Train the model parameters
    # The step count is tightly constrained to 2000 limit locally to prove integration 
    # computational stability without triggering compute-resource lockups.
    print("Commencing Execution via Continuous Qutip Emulator Feedback Loops...")
    model.learn(total_timesteps=2000)
    
    # 4. Save Local Artifacts
    save_dir = "Models_Local"
    
    # Ensure targeted save directory builds reliably at the project-root framework
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_save_dir = os.path.join(project_root, save_dir)
    os.makedirs(full_save_dir, exist_ok=True)
    
    save_path = os.path.join(full_save_dir, "ppo_pulser_mis_v1")
    model.save(save_path)
    
    print(f"\n[SUCCESS] Pipeline Complete. Generated Agent Model seamlessly packaged into: {save_path}.zip")
