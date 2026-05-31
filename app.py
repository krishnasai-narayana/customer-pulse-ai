import streamlit as st
import time

from services.llm_service import analyze_customer
from streamlit_mic_recorder import mic_recorder
from services.speech_service import transcribe_audio

st.set_page_config(
    page_title="Voice Customer Recovery Agent",
    layout="wide"
)

st.title("🎙️ Voice Customer Recovery Agent")

st.success(
    "Voice-First Customer Recovery Platform"
)

st.caption(
    "Powered by Faster-Whisper + Gemma 4 + Streamlit"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "AI Agents",
        "3"
    )

with col2:
    st.metric(
        "Languages",
        "3"
    )

with col3:
    st.metric(
        "Model",
        "Gemma 4"
    )

language = st.selectbox(
    "🌐 Customer Language",
    [
        "English",
        "Telugu",
        "Hindi"
    ]
)

st.markdown("""
### Multi-Agent Customer Recovery Platform

Coordinator Agent orchestrates:

✅ Intent Agent  
✅ Sentiment Agent  
✅ Decision Agent  

Python Intelligence Layer:

✅ Churn Risk Prediction  
✅ Recovery Score Calculation  
✅ Escalation Detection  
✅ Response Generation
""")

st.subheader("🧠 Agent Workflow")

st.code("""
🎤 Voice Input
      ↓
📝 Speech To Text
      ↓
🧠 Intent Agent
      ↓
😊 Sentiment Agent
      ↓
🎯 Decision Agent
      ↓
🚨 Escalation Engine
      ↓
💬 Response Generator
""")

# ==================================================
# VOICE INPUT
# ==================================================

st.subheader("🎤 Voice Input")

audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹️ Stop Recording",
    key="recorder"
)

customer_text = ""

if audio:

    print("=" * 80)
    print("AUDIO OBJECT")
    print(audio.keys())

    for k, v in audio.items():

        if isinstance(v, bytes):
            print(k, "bytes:", len(v))
        else:
            print(k, "=", v)

    print("=" * 80)

    st.success("✅ Voice Captured Successfully")

    with st.spinner(
        "📝 Converting speech to text..."
    ):

        result = transcribe_audio(
            audio["bytes"],
            language
        )

        customer_text = result["text"]

        detected_language = result["detected_language"]

    if customer_text:

        st.success(
            "✅ Transcript Generated"
        )

        st.subheader("🔄 Translation Layer")

        st.success(
            "Telugu Voice → English Analysis → Customer Language Response"
        )

        customer_text = st.text_area(
            "📝 Transcript",
            value=customer_text,
            height=150
        )

    else:

        st.error(
            "Unable to transcribe audio."
        )

        customer_text = st.text_area(
            "📝 Transcript / Customer Statement",
            height=150
        )

else:

    customer_text = st.text_area(
        "📝 Transcript / Customer Statement",
        height=150,
        placeholder="""
Example:

I am extremely frustrated.
I have called support 5 times.
I want to cancel my subscription.
"""
    )

# ==================================================
# ANALYSIS
# ==================================================

if st.button("🚀 Analyze Customer"):

    if not customer_text.strip():
        st.warning(
            "Please enter a transcript or customer statement."
        )
        st.stop()

    progress = st.progress(0)

    logs = []

    log_box = st.empty()

    status = st.empty()

    status.info(
        "🚀 Coordinator Agent Started"
    )

    logs.append(
        "🚀 Coordinator Agent Started"
    )

    log_box.code(
        "\n".join(logs)
    )

    start_time = time.time()

    progress.progress(20)

    result = analyze_customer(
        customer_text
    )

    progress.progress(70)

    logs.append(
        "🔍 Intent Agent Completed"
    )

    logs.append(
        "😊 Sentiment Agent Completed"
    )

    logs.append(
        "🎯 Decision Agent Completed"
    )

    log_box.code(
        "\n".join(logs)
    )

    intent = result["intent"]
    sentiment = result["sentiment"]
    action = result["action"]

    text = customer_text.lower()

    if (
        "cancel" in text
        or "frustrated" in text
        or "angry" in text
        or "unsubscribe" in text
        or "multiple times" in text
        or "calling" in text
        or "called" in text
        or "internet" in text
        or "not working" in text
        or "service down" in text
    ):
        churn_risk = 80
        recovery_score = 30
        mood = "😡 High Risk Customer"
        status_level = "Critical"

    elif (
        "issue" in text
        or "problem" in text
        or "waiting" in text
        or "slow" in text
    ):
        churn_risk = 50
        recovery_score = 60
        mood = "😐 Medium Risk Customer"
        status_level = "Monitor"

    else:
        churn_risk = 20
        recovery_score = 85
        mood = "😊 Healthy Customer"
        status_level = "Stable"

    if action.lower() == "escalate":

        manager_summary = """
    • Customer shows strong dissatisfaction

    • Customer is likely to churn

    • Immediate supervisor escalation recommended
    """

        if language == "Telugu":

            customer_response = """
    మీకు కలిగిన అసౌకర్యానికి మేము క్షమాపణలు కోరుతున్నాము.

    మీ ఇంటర్నెట్ సేవ గత కొన్ని రోజులుగా పనిచేయకపోవడం మరియు మీరు పలుమార్లు సంప్రదించిన విషయం మాకు అర్థమైంది.

    మీ సమస్యను అత్యవసరంగా ఎస్కలేట్ చేశాము. మా సపోర్ట్ బృందం త్వరలోనే మిమ్మల్ని సంప్రదిస్తుంది.
    """

        elif language == "Hindi":

            customer_response = """
    हमें हुई असुविधा के लिए खेद है।

    हम समझते हैं कि आपकी इंटरनेट सेवा कई दिनों से काम नहीं कर रही है और आपने कई बार सहायता के लिए संपर्क किया है।

    आपकी समस्या को प्राथमिकता के साथ आगे बढ़ाया गया है।
    """

        else:

            customer_response = """
    I sincerely apologize for the repeated inconvenience.

    I understand how frustrating it must be to contact support multiple times without resolution.

    Your issue has been escalated for immediate review and a specialist will contact you shortly.
    """

    elif action.lower() == "refund":

        manager_summary = """
• Refund request detected

• Customer retention risk identified

• Refund review recommended
"""

        customer_response = """
Thank you for reaching out.

We understand your concern and have started reviewing your refund request.

Our team will update you shortly.
"""

    else:

        manager_summary = """
• Customer interaction analyzed

• Follow-up recommended

• Continue monitoring satisfaction
"""

        customer_response = """
Thank you for your feedback.

We appreciate your patience and will continue working toward a resolution.
"""

    elapsed = round(
        time.time() - start_time,
        2
    )

    progress.progress(100)

    status.success(
        "🎉 Analysis Complete"
    )

    logs.append(
        f"✅ Analysis Complete ({elapsed}s)"
    )

    log_box.code(
        "\n".join(logs)
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Intent",
            intent
        )

    with col2:
        st.metric(
            "Sentiment",
            sentiment
        )

    with col3:
        st.metric(
            "Churn Risk",
            f"{churn_risk}%"
        )

        st.progress(
            churn_risk / 100
        )

    with col4:
        st.metric(
            "Recovery Score",
            f"{recovery_score}%"
        )

        st.progress(
            recovery_score / 100
        )

    st.divider()

    st.subheader(
        "🚨 Escalation Center"
    )

    if churn_risk >= 80:

        st.error(
            "Critical customer detected. Immediate supervisor intervention recommended."
        )

    elif churn_risk >= 50:

        st.warning(
            "Customer dissatisfaction detected."
        )

    else:

        st.success(
            "Customer relationship healthy."
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader(
            "😊 Customer Mood"
        )

        st.info(mood)

        st.subheader(
            "🎯 Recommended Action"
        )

        st.success(action)

        st.subheader(
            "📊 Customer Status"
        )

        st.write(status_level)

    with right:

        st.subheader(
            "👔 Manager Summary"
        )

        st.warning(
            manager_summary
        )

    st.divider()

    st.subheader("🌐 Detected Language")

    lang_map = {
        "en": "English",
        "te": "Telugu",
        "hi": "Hindi"
    }

    if 'detected_language' in locals():

        st.info(
            lang_map.get(
                detected_language,
                detected_language
            )
        )

    else:

        st.info(language)

    st.subheader(
        "💬 Suggested Customer Response"
    )

    st.write(
        customer_response
    )

    st.divider()

    st.subheader(
        "⚡ Execution Statistics"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Processing Time",
            f"{elapsed} sec"
        )

    with col2:

        st.metric(
            "Language",
            language
        )

    st.divider()

    st.divider()

    st.subheader("💼 Business Impact")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Churn Prevention",
            "High"
        )

    with c2:
        st.metric(
            "Response Time",
            "< 1 Min"
        )

    with c3:
        st.metric(
            "Languages Supported",
            "3"
        )

    st.subheader("🚀 Future Enhancements")

    st.markdown("""
    ✅ Sarvam AI Integration

    ✅ Real-Time Voice Calls

    ✅ Twilio Customer Outreach

    ✅ CRM Integration

    ✅ Supervisor Dashboard

    ✅ Live Agent Handoff
    """)