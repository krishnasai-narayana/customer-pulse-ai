from services.llm_service import ask_llm

def detect_sentiment(text):
    return ask_llm(f"Analyze sentiment and emotion from: {text}. Return sentiment, score out of 10 and reason.")
