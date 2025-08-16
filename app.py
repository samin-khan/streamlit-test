import streamlit as st
from anthropic import Anthropic

st.title("Claude Chat Interface")

user_input = st.text_area("Enter your message:", placeholder="Type your message here...")

if st.button("Send to Claude"):
    if user_input:
        try:
            client = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
            
            with st.spinner("Getting response from Claude..."):
                message = client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=1000,
                    messages=[{"role": "user", "content": user_input}]
                )
            
            st.write("**Claude's Response:**")
            st.write(message.content[0].text)
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text before submitting.")