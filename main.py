import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os
OLLAMA_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434")
st.title("Chatbot 🎬")
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="Act like jarvis in ironman movie")
    ]
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)
prompt = st.chat_input("Type your message...")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))
    # llm = ChatOllama(
    #     model="llama3.2:latest",  # Change model if needed
    #     temperature=0.7
    # )
    llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0.7,
    base_url=os.getenv("OLLAMA_API_URL", "http://localhost:11434")
)
    result = llm.invoke(st.session_state.messages).content
    with st.chat_message("assistant"):
        st.markdown(result)
    st.session_state.messages.append(AIMessage(content=result))