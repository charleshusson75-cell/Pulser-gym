# Pulser-Gym: Quantum RL Wrapper

This project acts as a bridge between classical Deep Reinforcement Learning and Neutral Atom Quantum Computing by wrapping Pasqal's `Pulser` simulator inside an OpenAI `Gymnasium` environment.

## Installation Instructions

Install the necessary dependencies to run the physics simulation and reinforcement learning environment natively:
```bash
pip install -r pulser-gym-env/requirements.txt
```

## Pipeline Status

* [x] **Phase 1:** Scaffold directory structure and create foundational documentation.
* [x] **Phase 2:** Develop the core Gymnasium environment with mock numpy arrays.
* [x] **Phase 3:** Integrate Pulser sequence translation.
* [x] **Phase 4:** Physics Engine Integration - Wired `env_01_core.py` with `QutipEmulator` and 100-shot deterministic sampling alongside MIS rewards.
* [x] **Phase 5:** Develop Stable-Baselines3 training and inference scripts. Verified local 2,000-timestep execution stability via PPO.
* [x] **Phase 6:** Inference Validation - Fully scripted deterministic tracking and Matplotlib rendering outputting direct `eval_plot.png` results.
