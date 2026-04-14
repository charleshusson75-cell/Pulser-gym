# Pulser-Gym: Quantum RL Environment

## Overview
This repository provides a Gymnasium-compatible wrapper for Pasqal's Pulser library, enabling the application of Deep Reinforcement Learning (DRL) to neutral atom quantum control. The environment translates agent actions into physical laser waveforms targeting an $N$-qubit register.

## Interactive Demo and Documentation
- **Interactive Demo**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/charleshusson75-cell/Pulser-gym/blob/main/demo.ipynb)
- **Whitepaper**: [Download PDF](bridging_rl_quantum_paper.pdf)

## Project Structure
The repository is organized into a core environment package and auxiliary scripts for training and evaluation.

```text
Pulser-gym/
├── bridging_rl_quantum_paper.pdf    # Academic whitepaper
├── demo.ipynb                       # Interactive Jupyter notebook
├── README.md                        # Project documentation
└── pulser-gym-env/                  # Environment submodule
    ├── requirements.txt             # Dependencies
    ├── pulser_gym/                  # Core logic
    │   ├── env_01_core.py           # Gymnasium environment class
    │   ├── sequence_02_translation.py # Action-to-Pulse mapping
    │   └── reward_03_mis_scoring.py # MIS reward/penalty logic
    ├── tests/                       # Validation suite
    └── scripts/                     # RL implementation
        ├── train_05_ppo_agent.py    # PPO training script
        └── evaluate_06_inference.py # Evaluation and plotting
```

## Methodology
The environment maps classical control parameters into a quantum Hamiltonian simulation:

1. **Action Space**: A 2D continuous vector representing laser **Amplitude** ([0, 10] rad/us) and **Detuning** ([-20, 20] rad/us).
2. **Observation Space**: A vector of length $N$ representing the marginal probabilities of each qubit being in the Rydberg state ($|1\rangle$). Data is extracted via QutipEmulator using 100 shots per step.
3. **Reward Function**: Designed for the Maximum Independent Set (MIS) problem on 2-D Euclidean lattices. It assigns +1.0 for each excited atom and a -2.0 penalty for any pair of excited atoms within the 7.0 $\mu$m blockade radius.
4. **Learning Framework**: Uses the Proximal Policy Optimization (PPO) algorithm from Stable-Baselines3.

## Usage

### 1. Installation
Navigate to the environment directory and install the required packages:
```bash
cd pulser-gym-env/
pip install -r requirements.txt
```

### 2. Environment Validation
Run the validation script to verify the integration between Gymnasium and the Pulser backend:
```bash
python tests/test_04_env_validation.py
```

### 3. Training
To train a PPO agent on a default 9-qubit grid:
```bash
python scripts/train_05_ppo_agent.py
```

### 4. Inference and Plotting
To evaluate a trained model and generate control waveforms:
```bash
python scripts/evaluate_06_inference.py
```
