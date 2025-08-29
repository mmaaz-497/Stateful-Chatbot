import chainlit as cl
import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import Optional, Dict

# Load environment variables
load_dotenv()

# Get API key
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

# Use a correct model name
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    user_raw_data: Dict[str, str],
    default_user: cl.user,
) -> Optional[cl.user]:
    """
    Handle the OAuth callback from GitHub.
    Return the user object if authentication succeeds, otherwise return None.
    """
    print(f"Provider: {provider_id}")
    print(f"User Data: {user_raw_data}")

    return default_user

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! How can I help you?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")

    # Append user message to history
    history.append({"role": "user", "content": message.content})

    # Format history for Gemini API
    formatted_history = [
        {"role": msg["role"], "parts": [{"text": msg["content"]}]}
        for msg in history
    ]

    # Generate response
    response = model.generate_content(formatted_history)

    # Extract response text safely
    response_text = response.text if hasattr(response, "text") else "No response text available"

    # Append assistant response to history
    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)

    # Send response
    await cl.Message(content=response_text).send()