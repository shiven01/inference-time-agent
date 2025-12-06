# Inference-Time Agent

## Prerequisites

- Python 3.7+
- Access to ASU VPN
- `requests` library

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd inference-time-agent
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage

### Running the Agent

To process questions and generate answers:

```bash
python3 generate_answer_template.py
```

### How It Works

1. **Input**: The script reads questions from `cse_476_final_project_test_data.json`
2. **Processing**: For each question:
   - `rag()`: Extracts LaTeX commands and retrieves relevant context from the knowledge base
   - `chain_of_thought()`: Generates a step-by-step reasoning process
   - `self_refinement()`: Refines the initial answer for better accuracy
3. **Output**: Answers are written to `cse_476_final_project_answers.json`

## Project Structure

```
inference-time-agent/
├── api_client.py                    # API client for LLM chat completions
├── inference_agent.py               # Core agent logic (RAG, CoT, self-refinement)
├── generate_answer_template.py      # Main script to process questions and generate answers
├── latex_knowledge_base.json        # LaTeX command knowledge base for RAG
├── cse_476_final_project_test_data.json  # Test questions (input)
├── cse_476_final_project_answers.json   # Generated answers (output)
└── README.md                       
```