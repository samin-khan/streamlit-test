import streamlit as st
from anthropic import Anthropic

def show_claude():
    # Canvas-style breadcrumb header
    st.markdown("""
    <div style="padding: 20px 0; border-bottom: 1px solid #E2E8F0; margin-bottom: 20px;">
        <div style="color: #718096; font-size: 14px; margin-bottom: 8px;">
            CS101 › Claude
        </div>
        <div style="display: flex; align-items: center; gap: 12px;">
            <h1 style="color: #2D3748; font-size: 2rem; font-weight: 400; margin: 0;">Claude CS101 Tutor</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Greeting section to match Canvas Claude interface
    st.markdown("""
    <div style="text-align: center; padding: 60px 20px; background-color: #F5F1EB; border-radius: 12px; margin-bottom: 30px;">
        <div style="display: flex; justify-content: center; align-items: center; gap: 16px; margin-bottom: 20px;">
            <div style="font-size: 2.5rem; font-weight: 300; color: #4A4A4A; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;">
                Good afternoon, Kevin
            </div>
        </div>
        <div style="font-size: 1.2rem; color: #8A8A8A; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; margin-top: 20px;">
            How can I help you today?
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Claude chat interface
    with st.container():
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        user_input = st.text_area(
            "Enter your message:", 
            placeholder="Type your message here...",
            key="claude_input",
            height=120
        )
        
        # Support buttons
        st.markdown("**Quick Help Options:**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📚 Assignment Support", use_container_width=True, key="assignment_help"):
                st.session_state.claude_input = "I need help with my current CS101 assignment. Can you help me understand the requirements and provide guidance on how to approach the problem?"
                st.rerun()
        
        with col2:
            if st.button("🎓 Lecture Review", use_container_width=True, key="lecture_help"):
                st.session_state.claude_input = "I'd like to review the key concepts from our recent CS101 lectures. Can you help me understand the main topics and provide examples?"
                st.rerun()
        
        with col3:
            if st.button("📖 Reading Assistant", use_container_width=True, key="reading_help"):
                st.session_state.claude_input = "I need help understanding the course readings and textbook material. Can you explain the concepts in simpler terms?"
                st.rerun()
        
        st.markdown("---")
        
        # Main chat controls
        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            send_button = st.button("🔍 Research", use_container_width=True)
        with col2:
            clear_button = st.button("🗑️ Clear", use_container_width=True)
        
        if clear_button:
            st.session_state.claude_input = ""
            st.rerun()
        
        if send_button:
            if user_input:
                try:
                    client = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
                    
                    with st.spinner("Getting response from Claude..."):
                        message = client.messages.create(
                            model="claude-3-haiku-20240307",
                            max_tokens=1000,
                            messages=[{"role": "user", "content": user_input}]
                        )
                    
                    st.markdown("**Claude's Response:**")
                    st.markdown(message.content[0].text)
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter some text before submitting.")
        
        st.markdown('</div>', unsafe_allow_html=True)