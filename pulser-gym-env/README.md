# Pulser-Gym: Quantum RL Wrapper

This project acts as a bridge between classical Deep Reinforcement Learning and Neutral Atom Quantum Computing by wrapping Pasqal's `Pulser` simulator inside an OpenAI `Gymnasium` environment.

## Pipeline Status

* **Phase 1:** Scaffold directory structure and create foundational documentation.
* **Phase 2 (Completed):** Develop the core Gymnasium environment with mock numpy arrays.
* **Phase 3 (Completed):** Integrate Pulser sequence translation.
* **Phase 4 (Completed):** Physics Engine Integration - Wired `env_01_core.py` with `QutipEmulator` and 100-shot deterministic sampling alongside MIS rewards.
* **Phase 5:** Develop Stable-Baselines3 training and inference scripts.

## Setup Instructions
```bash
pip install -r requirements.txt
```
