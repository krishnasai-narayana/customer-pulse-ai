from services.llm_service import ask_llm

def retention_strategy(text):
    return ask_llm(f"Suggest retention strategy for customer statement: {text}. Include offer, escalation needed and reason.")
