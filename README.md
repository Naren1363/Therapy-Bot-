Therapy Bot

Therapy Bot is a modular AI-driven conversational system designed to explore emotionally-aware dialogue with structured memory and safety controls.
The project focuses on system architecture — separating authentication, emotional inference, conversation memory, and response generation into independent layers.

Rather than being a simple chatbot, this project experiments with how multiple AI components can work together to simulate responsible and context-aware interaction.

Architecture Overview

The application is structured into clearly separated modules:

app.py — Streamlit UI layer and session management

llm_engine.py — Core language model interaction

emotion.py — Emotional signal analysis

memory.py — Conversation state persistence

safety.py — Input validation and response filtering

supabase_client.py — User authentication backend

This separation allows each layer to evolve independently and keeps the system maintainable.

Tech Stack

Python

Streamlit

Supabase

Environment-based configuration

Running Locally

Clone the repository

Create a virtual environment

Install dependencies

Add environment variables in .env

Run:

streamlit run app.py

Future Improvements

Improved emotional confidence scoring

Context window optimization

Conversation summarization

Cloud deployment