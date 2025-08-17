import streamlit as st
from assignments import show_assignments
from syllabus import show_syllabus
from lectures import show_lectures
from claude_interface import show_claude
from styles import load_css

# Page configuration
st.set_page_config(
    page_title="CS101",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Canvas-style CSS
load_css()

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Claude'

# Sidebar Navigation
with st.sidebar:
    st.markdown("### CS101")
    st.markdown("---")
    
    # Navigation buttons
    if st.button("Assignments", use_container_width=True):
        st.session_state.current_page = 'Assignments'
    
    if st.button("Syllabus", use_container_width=True):
        st.session_state.current_page = 'Syllabus'
    
    if st.button("Lectures", use_container_width=True):
        st.session_state.current_page = 'Lectures'
    
    if st.button("Claude", use_container_width=True):
        st.session_state.current_page = 'Claude'

# Main content area - functions imported from separate modules

# Display current page
if st.session_state.current_page == 'Assignments':
    show_assignments()
elif st.session_state.current_page == 'Syllabus':
    show_syllabus()
elif st.session_state.current_page == 'Lectures':
    show_lectures()
elif st.session_state.current_page == 'Claude':
    show_claude()