from services.llm_service import ask_llm

def predict_churn(text):
    return ask_llm(f"Predict churn risk percentage for customer statement: {text}. Return risk percentage and reason.")
