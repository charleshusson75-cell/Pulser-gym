# ⚛️ Pulser-Gym: Quantum RL wrapper

## Overview
This repository contains the architecture bridging classical Deep Reinforcement Learning with Neutral Atom Quantum Computing. By wrapping Pasqal's Pulser emulator inside a strict OpenAI Gymnasium environment, we dynamically translate RL deterministic parameters directly into physical laser waveforms operating over an $N$-qubit Register.

📄 Read the full academic research paper: [bridging_rl_quantum_paper.pdf](bridging_rl_quantum_paper.pdf)

## 📂 Project Structure
The architecture is strictly modular following the Single Responsibility Principle, separating sequence translation, physics emulation, and scoring into sequential execution topologies to prevent decoupled data leakage.

```text
Pulser-gym/
├── main.tex                                       # Full academic whitepaper detailing architecture
├── ARCHITECTURE_AND_PRD.md                        # Internal technical blueprint and API metrics
├── README.md                                      # This file
│
└── pulser-gym-env/                                # Submodule core
    ├── requirements.txt                           # Python dependencies (pulser, gymnasium, etc.)
    │
    ├── Models_Local/                              # Serialized machine learning artifacts
    │   ├── ppo_pulser_mis_v1.zip                  # Checkpointed PPO weights
    │   └── eval_plot.png                          # Inference physical plotting matrix
    │
    ├── pulser_gym/                                # Core environment package
    │   ├── __init__.py                                
    │   ├── env_01_core.py                         # Gymnasium class encapsulating QutipEmulator
    │   ├── sequence_02_translation.py             # Strictly mapping float actions to Pulser Sequences
    │   └── reward_03_mis_scoring.py               # Graph mathematical Maximum Independent Set penalties
    │
    ├── tests/                                     # Validation environments
    │   └── test_04_env_validation.py              # Live physics execution checks
    │
    └── scripts/                                   # RL interaction and inference layer
        ├── train_05_ppo_agent.py                  # Stable-Baselines3 PPO generation
        └── evaluate_06_inference.py               # Inference tracking over deterministic graphs
```

## ⚙️ Methodology
The pipeline executes chaotic continuous gradients into mathematically bounded quantum topologies:
1. **The Action Space:** The agent controls a continuous mathematical vector (normalized to [0, 1]), deterministically mapped onto a physical amplitude laser pulse bounded inside [0, 10] rad/us.
2. **The Observation Protocol:** Exponential Hilbert-space scaling bottlenecks ($2^N$) are avoided by mapping the active physics into a condensed marginal probability array length $N$. Max-count 100-shot probability thresholds extracted natively inside the emulation physics cleanly filter quantum superposition to active discrete states natively.
3. **The Penalty Layer:** Evaluating target structures across a 1D lattice strictly enforces +1.0 algorithmic rewards on independent excitations alongside -2.0 penalties on geometrically adjacent conflicts cleanly.
4. **Machine Learning Integrations:** Stable-Baselines3 Proximal Policy Optimization (PPO) matrices explicitly navigate this space sequentially mapping continuous gradient descents dynamically cleanly without latency deadlock natively over the core emulator cleanly.

## 🧪 How to Run / Reproduce
This environment is orchestrated sequentially.

1. **Install Dependencies \& Enter Submodule:**
Launch standard terminal interfaces traversing explicitly inside the encapsulated Python pipeline:
```bash
cd pulser-gym-env/
pip install -r requirements.txt
```

2. **Run the Validation and Physics Protocol (Phase 4):**
Verify that the Gymnasium mathematical topology correctly maps into the backend Qutip physics emulation layer independently reliably accurately:
```bash
python tests/test_04_env_validation.py
```

3. **Train the RL Agent (Phase 5 Proof of Concept):**
Execute the continuous parameter optimization layer utilizing Stable-Baselines3 natively correctly. Generates weights locally inside Models_Local:
```bash
python scripts/train_05_ppo_agent.py
```

4. **Launch Inference \& Visualization (Phase 6):**
Conclusively link generated parameters properly into deterministically rendering offline charts. Final logic maps automatically to natively explicitly generate eval_plot.png.
```bash
python scripts/evaluate_06_inference.py
```
