from ollama import chat
import re

MODEL = "gemma4:e4b"

def analyze_customer(customer_text):

    prompt = f"""
Customer Complaint:

{customer_text}

Classify the complaint.

Return EXACTLY in this format:

Intent: Cancellation/Complaint/Refund/Billing/Support
Sentiment: Positive/Neutral/Negative
Action: Escalate/Retain/Refund/Follow Up
"""

    try:

        response = chat(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0,
                "num_predict": 50
            }
        )

        result = response["message"]["content"]

        print("=" * 80)
        print("RAW MODEL RESPONSE")
        print("=" * 80)
        print(result)
        print("=" * 80)

        intent = "Cancellation"
        sentiment = "Negative"
        action = "Escalate"

        intent_match = re.search(
            r"Intent:\s*(.+)",
            result,
            re.IGNORECASE
        )

        sentiment_match = re.search(
            r"Sentiment:\s*(.+)",
            result,
            re.IGNORECASE
        )

        action_match = re.search(
            r"Action:\s*(.+)",
            result,
            re.IGNORECASE
        )

        if intent_match:
            intent = intent_match.group(1).strip()

        if sentiment_match:
            sentiment = sentiment_match.group(1).strip()

        if action_match:
            action = action_match.group(1).strip()

        return {
            "intent": intent,
            "sentiment": sentiment,
            "action": action
        }

    except Exception as e:

        print(e)

        return {
            "intent": "Cancellation",
            "sentiment": "Negative",
            "action": "Escalate"
        }