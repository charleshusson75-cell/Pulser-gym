# Pulser-Gym: Quantum RL Wrapper

This project acts as a bridge between classical Deep Reinforcement Learning and Neutral Atom Quantum Computing by wrapping Pasqal's `Pulser` simulator inside an OpenAI `Gymnasium` environment.

## Pipeline Status

* **Phase 1:** Scaffold directory structure and create foundational documentation.
* **Phase 2 (Completed):** Develop the core Gymnasium environment with mock numpy arrays.
* **Phase 3 (Completed):** Integrate Pulser sequence translation.
* **Phase 4 (Completed):** Physics Engine Integration - Wired `env_01_core.py` with `QutipEmulator` and 100-shot deterministic sampling alongside MIS rewards.
* **Phase 5 (Completed):** Develop Stable-Baselines3 training and inference scripts. Verified local 2,000-timestep execution stability via PPO mapping without computational deadlock.
* **Phase 6 (Completed):** Inference Validation - Fully scripted deterministic tracking and Matplotlib rendering outputting direct `eval_plot.png` results.

## Setup Instructions
```bash
pip install -r requirements.txt
```

### Execution (Phase 5 Proof of Concept)
Run the training algorithm from the repository root directory to validate end-to-end mapping:
```bash
python scripts/train_05_ppo_agent.py
```

### Results & Visualization (Phase 6)
To seamlessly orchestrate a strict deterministic evaluation rendering the quantum emulator arrays over scaled physical laser parameters:
```bash
python scripts/evaluate_06_inference.py
```
This final script tracks the raw mathematical physics payload natively and maps a dedicated visualization chart correctly exported into: `Models_Local/eval_plot.png`.
