from services.llm_service import ask_llm

def detect_intent(text):
    return ask_llm(f"Classify customer intent from: {text}. Return one of: Cancellation, Refund, Complaint, Billing, Support, Upgrade.")
