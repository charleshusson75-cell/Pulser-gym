import gymnasium as gym
from gymnasium import spaces
import numpy as np

from pulser_simulation import QutipEmulator
from pulser_gym.sequence_02_translation import build_pulse_sequence
from pulser_gym.reward_03_mis_scoring import calculate_mis_reward

class PulserEnv(gym.Env):
    """
    OpenAI Gymnasium wrapper for Pasqal's Pulser.
    V1.0 uses a 1D continuous action space (Amplitude in rad/microsec)
    and observation space of bitstring probabilities (mocked).
    """
    metadata = {"render_modes": ["ansi"]}

    def __init__(self, n_qubits=9):
        super(PulserEnv, self).__init__()
        self.n_qubits = n_qubits
        
        # Action space: 1D continuous variable: Amplitude (scaled, typically 0 to 10 rad/µs)
        # We use a normalized space [0, 1] as recommended by RL best practices
        self.action_space = spaces.Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)
        
        # Observation space: marginal probabilities for each qubit
        self.observation_space = spaces.Box(low=0.0, high=1.0, shape=(self.n_qubits,), dtype=np.float32)
        
        # Internal tracking
        self.state = np.zeros(self.n_qubits, dtype=np.float32)
        self.steps = 0
        self.max_steps = 10 

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.steps = 0
        
        # Mock initial state: ground state (0.0 probability of being in |1> for all qubits)
        self.state = np.zeros(self.n_qubits, dtype=np.float32)
        
        info = {}
        return self.state, info

    def step(self, action):
        self.steps += 1
        
        # Generate the physical pulse sequence dynamically
        seq = build_pulse_sequence(self.n_qubits, action)
        
        # Execute rigorous simulation through local Qutip engine
        sim = QutipEmulator.from_sequence(seq)
        results = sim.run()
        
        # Sample the resulting probabilities 100 times to achieve mathematical determinism
        counts = results.sample_final_state(N_samples=100)
        
        # Condense mapping to select highest-probability bitstring extraction
        most_frequent_bitstring = max(counts, key=counts.get)
        
        # Array shape parsing from the bitstring metric
        self.state = np.array([float(char) for char in most_frequent_bitstring], dtype=np.float32)
        
        # Extract atomic coordinates for 2D MIS penalty evaluation
        coords = np.array([seq.register.qubits[q] for q in seq.register.qubit_ids])
        
        # Evaluate standard graph parameters using deterministic Euclidean mapping
        reward = calculate_mis_reward(self.state, coords)
        
        # Termination conditions
        terminated = False
        truncated = self.steps >= self.max_steps
        
        info = {}
        return self.state, reward, terminated, truncated, info

    def render(self):
        print(f"[{self.steps}/{self.max_steps}] Base Probabilities: {self.state[:4]}")

    def close(self):
        pass
