# Pulser-gym: Quantum RL Environment

🚧 **Status: Active Development (Work in Progress)**

> This repository is currently under active development. The core Gymnasium wrapper (v2.0) is functional, and we have successfully integrated simultaneous Amplitude and Detuning control. Further research into multi-qubit lattice optimization is ongoing.

## Overview
This repository provides a Gymnasium-compatible wrapper for Pasqal's Pulser library, enabling the application of Deep Reinforcement Learning (DRL) to neutral atom quantum control. The environment translates agent actions into physical laser waveforms targeting an $N$-qubit register.

## Interactive Demo and Documentation
- 📄 **Whitepaper**: [Download PDF](bridging_rl_quantum_paper.pdf)
- 📈 **Interactive Demo**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/charleshusson75-cell/Pulser-gym/blob/main/demo.ipynb)

## Project Structure
The repository is organized into a core environment package and auxiliary scripts for training and evaluation.

```text
Pulser-gym/
├── bridging_rl_quantum_paper.pdf    # Academic whitepaper
├── demo.ipynb                       # Interactive Jupyter notebook
├── README.md                        # Documentation
└── pulser-gym-env/                  # Environment submodule
    ├── requirements.txt             # Dependencies
    ├── pulser_gym/                  # Core logic
    │   ├── env_01_core.py           # Gymnasium class
    │   ├── sequence_02_translation.py # Physics mapping
    │   └── reward_03_mis_scoring.py # MIS scoring logic
    ├── tests/                       # Validation suite
    └── scripts/                     # RL implementation
        ├── train_05_ppo_agent.py    # PPO training
        └── evaluate_06_inference.py # Inference and plotting
```

## Methodology
The environment maps classical control parameters into a quantum Hamiltonian simulation:

1. **Action Space**: A 2D continuous vector representing laser Amplitude ([0, 10] rad/us) and Detuning ([-20, 20] rad/us).
2. **Observation Space**: A vector of length $N$ representing the marginal probabilities of each qubit being in the Rydberg state ($|1\rangle$).
3. **Reward Function**: Assigned for the Maximum Independent Set (MIS) problem on 2D Euclidean lattices. Assigns +1.0 for each excited atom and a -2.0 penalty for blockade violations.

## Usage

### 1. Installation
```bash
cd pulser-gym-env/
pip install -r requirements.txt
```

### 2. Validation
```bash
python tests/test_04_env_validation.py
```

### 3. Training
```bash
python scripts/train_05_ppo_agent.py
```

### 4. Inference
```bash
python scripts/evaluate_06_inference.py
```
