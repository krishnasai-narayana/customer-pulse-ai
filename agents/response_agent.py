from services.llm_service import ask_llm

def generate_response(text):
    return ask_llm(f"Generate an empathetic support response under 100 words for: {text}")
