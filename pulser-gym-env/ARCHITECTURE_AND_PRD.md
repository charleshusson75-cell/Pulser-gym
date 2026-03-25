# Architecture and Product Requirements Document (PRD)

## 1. Architectural Blueprint & Coding Philosophy
- **The Numbered Pipeline:** Every project must be broken down into a strict, numbered sequence of execution. We will not write the whole codebase at once.
- **Single Responsibility:** Each script has one clearly defined job.
- **OpenAI Gymnasium Compliance:** The core environment strictly adheres to the `gymnasium.Env` API standard, allowing any off-the-shelf RL library to interact with it natively.

## 2. Product Requirements
**Objective:** Build a fully local, `pip`-installable Python package that acts as a bridge between classical Deep Reinforcement Learning and Neutral Atom Quantum Computing via wrapping Pasqal's `Pulser` simulator inside an OpenAI `Gymnasium` environment.

### Definition of Boundaries
1. **The Action Space:** For Version 1.0, the RL agent controls a 1D continuous variable: the **Amplitude** of a laser pulse (in rad/µs) applied to a register of atoms. Implemented as `gymnasium.spaces.Box`.
2. **The Observation Space:** The marginal probabilities of each qubit being in the $|1\rangle$ state from the `Pulser` simulation. Length linearly scales with `n_qubits`. Implemented as `gymnasium.spaces.Box`.
3. **The Reward Function:** A mathematical score evaluating how close the final quantum state is to solving a Maximum Independent Set (MIS) graph problem.
4. **The Mock-First Rule:** Before integrating the heavy Pulser physics engine, `env_01_core.py` must be written and validated using dummy numpy arrays to ensure API compliance.

## 3. Current Status & Next Steps
- **Current Phase:** Phase 2 complete. The core `PulserEnv` wrapper is fully validated against Gymnasium standards using mocked state outputs. The 1D Amplitude action space is successfully constrained to normalized limits `[0, 1]`.
- **Next Step (Phase 3):** Implement `sequence_02_translation.py` and connect the actual Pulser physics engine into `env_01_core.py`.
