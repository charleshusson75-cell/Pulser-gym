# Pulser-gym: Quantum RL wrapper

**Status: Under construction**

## Overview
This repository contains the architecture bridging classical deep reinforcement learning with neutral atom quantum computing. By wrapping Pasqal's Pulser emulator inside a Gymnasium environment, the project translates RL parameters into physical laser waveforms operating over an $N$-qubit register.

## Try it out
| Interactive demo | Academic paper |
| :--- | :--- |
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/charleshusson75-cell/Pulser-gym/blob/main/demo.ipynb) | [📄 Download PDF](bridging_rl_quantum_paper.pdf) |

You can explore the full quantum RL pipeline (visualizations, training, and inference) directly in your browser via Google Colab, or run the `demo.ipynb` locally.

## Project structure
The architecture is modular, separating sequence translation, physics emulation, and scoring to prevent data leakage.

```text
Pulser-gym/
├── bridging_rl_quantum_paper.pdf                  # Academic whitepaper
├── demo.ipynb                                     # Interactive Jupyter demo
├── README.md                                      # Project documentation
│
└── pulser-gym-env/                                # Environment submodule
    ├── requirements.txt                           # Python dependencies
    │
    ├── pulser_gym/                                # Core environment package
    │   ├── __init__.py                                
    │   ├── env_01_core.py                         # Gymnasium environment
    │   ├── sequence_02_translation.py             # Action-to-pulse mapping
    │   └── reward_03_mis_scoring.py               # MIS scoring logic
    │
    ├── tests/                                     # Validation environments
    │   └── test_04_env_validation.py              # Physics execution checks
    │
    └── scripts/                                   # Interaction layer
        ├── train_05_ppo_agent.py                  # PPO training script
        └── evaluate_06_inference.py               # Evaluation and plotting
```

## Methodology
The pipeline maps continuous gradients into quantum topologies:
1. **Action space:** The agent controls a 2D vector for Amplitude ([0, 10] rad/us) and Detuning ([-20, 20] rad/us), mapped from a normalized [0, 1] range.
2. **Observation protocol:** Hilbert-space scaling bottlenecks ($2^N$) are avoided by mapping the physics into a condensed marginal probability array of length $N$. Shot-based probability thresholds from the emulation layer filter quantum superposition to discrete states.
3. **Penalty layer:** The reward function evaluates the measured bitstring over 2D atom coordinates. Each excited atom contributes +1.0; any two excited atoms within the $7.0\,\mu m$ Rydberg blockade radius incur a -2.0 penalty.
4. **Machine learning integration:** Uses Stable-Baselines3 Proximal Policy Optimization (PPO) to navigate the Hamiltonian parameter space without compute deadlocks.

## How to run / reproduce
This environment is orchestrated sequentially.

1. **Install dependencies:**
```bash
cd pulser-gym-env/
pip install -r requirements.txt
```

2. **Run the validation suite:**
Verify that the Gymnasium topology correctly maps into the backend physics layer:
```bash
python tests/test_04_env_validation.py
```

3. **Train the RL agent:**
Execute the parameter optimization layer using Stable-Baselines3:
```bash
python scripts/train_05_ppo_agent.py
```

4. **Launch inference & visualization:**
Link generated parameters into rendering scripts to produce `eval_plot.png`:
```bash
python scripts/evaluate_06_inference.py
```
