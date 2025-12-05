import json
import re
from api_client import call_model_chat_completions

with open('latex_knowledge_base.json', 'r') as f:
    LATEX_KB = json.load(f)

def rag(question: str) -> str:
    latex_pattern = r'\\([a-zA-Z]+)(?:\{[^}]*\})?(?:\{[^}]*\})?'
    found_commands = set(re.findall(latex_pattern, question))
    
    retrieved_context = []
    
    for category in LATEX_KB.get('categories', {}).values():
        for latex_command, symbol_data in category.get('symbols', {}).items():
            base_cmd = latex_command.split('{')[0].replace('\\', '')
            if base_cmd in found_commands:
                meaning = symbol_data.get('meaning', '')
                rendered = symbol_data.get('rendered', '')
                retrieved_context.append(f"{latex_command}: {rendered} - {meaning}")
    
    context_text = ""
    if retrieved_context:
        context_text = "LaTeX Math Notation Reference:\n" + "\n".join(retrieved_context[:20]) + "\n\n"
    
    augmented_question = context_text + question
    
    return augmented_question

def chain_of_thought(augmented_question: str) -> str:
    system_message = (
        "You are a helpful assistant. Think through problems step by step. "
        "Show your reasoning process clearly, then provide the final answer "
        "in the format: 'Final Answer: [answer]'"
    )
    
    # Make LLM call
    response = call_model_chat_completions(
        prompt=augmented_question,
        system=system_message
    )
    
    if response["ok"] and response["text"]:
        response_text = response["text"].strip()
        
        if "Final Answer:" in response_text:
            parts = response_text.split("Final Answer:", 1)
            answer = parts[1].strip()
        else:
            answer = response_text
        
        return answer
    else:
        return ""

def self_refinement(question: str) -> str:
    pass