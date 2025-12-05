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

def chain_of_thought(question: str) -> str:
    pass

def self_refinement(question: str) -> str:
    pass