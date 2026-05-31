# 🎙️ Voice Customer Recovery Agent

## Overview

Voice Customer Recovery Agent is an AI-powered customer experience platform designed to identify dissatisfied customers, predict churn risk, and recommend recovery actions before customer loss occurs.

The platform enables customers to communicate naturally using voice in multiple languages such as Telugu, Hindi, and English. The system converts speech into text, analyzes customer intent and sentiment using AI agents, evaluates business risk, and generates personalized recovery recommendations.

---

## Problem Statement

Customer support teams often struggle to identify frustrated customers early enough to prevent churn. Traditional support systems focus on issue resolution but lack proactive intelligence to detect dissatisfaction and trigger recovery actions.

---

## Solution

Voice Customer Recovery Agent acts as an intelligent customer recovery assistant by:

* Accepting customer voice conversations
* Converting speech into text
* Understanding customer intent
* Detecting sentiment and emotional state
* Predicting churn risk
* Recommending recovery strategies
* Generating manager insights
* Creating personalized customer responses

---
## Architecture

```text
┌──────────────────────────────┐
│      Customer Voice Input    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Faster-Whisper Engine    │
│  Telugu | Hindi | English    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Translation Layer        │
│ Speech → Text Conversion     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Gemma 4 Agent Layer    │
├──────────────────────────────┤
│ • Intent Agent              │
│ • Sentiment Agent           │
│ • Decision Agent            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Customer Intelligence Layer  │
├──────────────────────────────┤
│ • Churn Risk Prediction     │
│ • Recovery Score           │
│ • Escalation Detection     │
│ • Customer Classification  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Recovery Recommendation Hub  │
├──────────────────────────────┤
│ • Recommended Actions       │
│ • Manager Summary           │
│ • Customer Response         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Streamlit Dashboard      │
├──────────────────────────────┤
│ Intent                       │
│ Sentiment                    │
│ Churn Risk                   │
│ Recovery Score               │
│ Escalation Alerts            │
│ Multi-Language Response      │
└──────────────────────────────┘
```
## Key Features

### 🎤 Voice-First Experience

* Voice Input Support
* Speech-to-Text Conversion
* Multilingual Conversations
* Customer-Friendly Interaction

### 🤖 AI Agent Framework

#### Intent Agent

Identifies customer objectives such as:

* Cancellation
* Support Request
* Complaint
* Billing Issue
* Refund Request

#### Sentiment Agent

Analyzes customer sentiment:

* Positive
* Neutral
* Negative

#### Decision Agent

Determines the most appropriate recovery action.

---

## Customer Intelligence Layer

* Churn Risk Prediction
* Recovery Score Calculation
* Escalation Detection
* Customer Health Classification
* Business Impact Assessment

---

## Recovery Engine

The recovery engine generates:

* Recommended Actions
* Manager Summaries
* Customer Recovery Responses
* Escalation Recommendations

---

## System Architecture

Customer Voice

↓
Speech Recognition Layer (Faster-Whisper)

↓

Translation & Processing Layer

↓

Gemma 4 Agent Layer

* Intent Agent
* Sentiment Agent
* Decision Agent

↓

Customer Intelligence Layer

* Churn Prediction
* Recovery Scoring
* Escalation Detection

↓

Recovery Recommendation Engine

↓

Interactive Streamlit Dashboard

---

## Technology Stack

| Component            | Technology             |
| -------------------- | ---------------------- |
| Frontend             | Streamlit              |
| Speech Recognition   | Faster-Whisper         |
| AI Model             | Gemma 4                |
| LLM Runtime          | Ollama                 |
| Programming Language | Python                 |
| Voice Capture        | Streamlit Mic Recorder |

---

## Business Value

### For Customer Support Teams

* Faster issue identification
* Reduced customer churn
* Improved customer satisfaction
* Automated recovery recommendations

### For Organizations

* Better customer retention
* Reduced support costs
* Improved service quality
* Actionable customer intelligence

---

## Future Enhancements

* Sarvam AI Integration
* Real-Time Voice Conversations
* Twilio Voice Calling
* CRM Integration
* Supervisor Monitoring Dashboard
* Live Agent Handoff
* Customer Journey Analytics
* Real-Time Escalation Alerts

---

## Local Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Gemma 4

```bash
ollama run gemma4:e4b
```

### 3. Launch Application

```bash
streamlit run app.py
```

---

## Demo Flow

1. Customer speaks in Telugu, Hindi, or English
2. Speech is converted into text
3. AI agents analyze the conversation
4. Churn risk and recovery score are calculated
5. Recommended actions are generated
6. Customer response is created
7. Results are displayed in an interactive dashboard

---

## License

This project is licensed under the MIT License.
