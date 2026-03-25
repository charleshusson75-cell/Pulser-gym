# Master Blueprint & PRD: Project "Omni-Twin" (Local AI Clone)

## 1. Architectural Blueprint & Coding Philosophy
Agent, this represents my strict standard for project structure. All code generated MUST adhere to these principles:
* **The Numbered Pipeline:** Every project must be broken down into a strict, numbered sequence of execution.
* **Single Responsibility:** Each script must have one clearly defined job. 
* **Master Orchestrator:** There must always be a root-level master orchestrator (`run_app.py`).

## 2. Product Requirements
**Objective:** Build a fully local desktop application that creates a "Digital Twin." The system will ingest data from WhatsApp, ChatGPT, and Gemini, unify it, and build a dual-layer intelligence system:
1. **The Memory (RAG via `mem0ai`):** Do not build a vector DB from scratch. You MUST use the `mem0ai` Python package to extract entities and build a memory graph from my chat history.
2. **The Vibe (LoRA via Unsloth - Cloud Export):** Because local GPUs are weak, the app will not train locally. It will format the data and generate a "Cloud Training Kit" (data + Unsloth Jupyter Notebook) to be run on a remote A100 (e.g., RunPod). 
3. **Local Inference:** Use the `ollama` Python library to handle running the final downloaded model inside our CustomTkinter UI.

**Data Prefiltering (The "Ultimate Mirror" Rules):**
The `clean_03_unify_format.py` script must be smart. Implement these specific rules:
* **Keep** time delays (long pauses between texts are fine).
* **Keep** reaction texts if parsable to show spirit.
* **Group Chat Filter:** Keep group chats ONLY IF my specific message count in that group is > 10. Discard groups where I am a ghost.
* Merge rapid-fire double/triple texts from the same user into single blocks.

## 3. The Overleaf / Whitepaper Requirement
I require a continuously updated academic paper for this project. I have provided a `LATEX_TEMPLATE.tex` file in the workspace containing my preferred style. Every time you successfully complete a numbered step in the Python pipeline, you MUST update a `main.tex` file in the root directory documenting the engineering decisions, data shapes, and pipeline architecture.

## 4. Required Directory Structure
Scaffold the project using the following exact structure:

Omni-Twin-App/
├── README.md
├── requirements.txt
├── run_app.py                                     
│
├── Data_Local/                                    
│   ├── 01_raw_exports/                            
│   ├── 02_unified_jsonl/                          
│   └── 03_cloud_training_kit/                     # Exported .jsonl + unsloth_train.ipynb
│
├── Models_Local/                                  
│   └─ twin_4bit_lora/                             # Where I will drop the cloud-trained model
│
└── Src/                                           
    ├─ ui_00_main_window.py                        
    ├─ ingest_01_socials.py                        
    ├─ ingest_02_ai_history.py                     
    ├─ clean_03_unify_format.py                    
    ├─ memory_04_build_mem0.py                     # Integrates mem0ai
    ├─ export_05_cloud_training_kit.py             # Packages data + Unsloth notebook
    └─ infer_06_agentic_chat.py                    # Integrates mem0 + Ollama

## First Task
Agent, review this entire document. Acknowledge my numbered pipeline philosophy, the strict reliance on `mem0ai` and `ollama` packages, the remote A100 training workflow, the specific data cleaning rules, and the LaTeX documentation rule. 

Then, independently scaffold the folder structure, write `requirements.txt` (including mem0ai, ollama, custom-tkinter, pandas), generate `ui_00_main_window.py` (matching the pipeline steps), and generate the initial `main.tex` file based on my template.