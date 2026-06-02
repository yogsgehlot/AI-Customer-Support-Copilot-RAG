import json
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="AI Customer Support Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Customer Support Copilot")

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and "sources" in message
        ):

            st.caption("Sources")

            for source in message["sources"]:
                st.write(f"📄 {source}")

# User Input
question = st.chat_input(
    "Ask your question..."
)

if question:

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    try:

        payload = {
            "question": question,
            "history": st.session_state.messages
        }

        with st.spinner("Thinking..."):

            response = requests.post(
                API_URL,
                json=payload
            )

            result = response.json()

        answer = result.get(
            "answer",
            "No answer returned"
        )

        sources = result.get(
            "sources",
            []
        )

    except Exception as e:

        answer = f"Error: {str(e)}"
        sources = []

    # Display Assistant Response
    with st.chat_message("assistant"):

        st.markdown(answer)

        if sources:

            st.caption("Sources")

            for source in sources:
                st.write(f"📄 {source}")

    # Save Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources
        }
    )

# Download Chat History
st.sidebar.download_button(
    label="Download Chat History",
    data=json.dumps(
        st.session_state.messages,
        indent=4
    ),
    file_name="chat_history.json",
    mime="application/json"
)