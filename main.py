import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

st.title("Chatbot 🎬")

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="Act like US president Trump")
    ]

# Display message history
for message in st.session_state.messages:
    with st.chat_message("user" if isinstance(message, HumanMessage) else "assistant"):
        st.markdown(message.content)

# Prompt input
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Create LLM
    llm = ChatOllama(
        model="llama3",  # Make sure this model exists
        temperature=0.7
    )

    # Get model response
    try:
        result = llm.invoke(st.session_state.messages).content
        with st.chat_message("assistant"):
            st.markdown(result)
        st.session_state.messages.append(AIMessage(content=result))
    except Exception as e:
        st.error(f"Error: {e}")
