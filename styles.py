import streamlit as st

def load_css():
    """Load Canvas-style CSS for the application"""
    st.markdown("""
    <style>
    /* Main app background */
    .stApp {
        background-color: #f5f5f5;
    }

    /* Sidebar styling - Canvas white theme */
    .css-1d391kg, .css-1lcbmhc, .css-17eq0hr {
        background-color: white !important;
    }

    .sidebar .sidebar-content {
        background-color: white !important;
    }

    /* Sidebar text styling */
    section[data-testid="stSidebar"] {
        background-color: white !important;
        border-right: 1px solid #E2E8F0 !important;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    section[data-testid="stSidebar"] h3 {
        color: #2B5797 !important;
        font-weight: 600;
        margin-bottom: 1rem;
        font-size: 18px;
    }

    /* Sidebar navigation buttons */
    section[data-testid="stSidebar"] .stButton > button {
        background-color: transparent !important;
        border: none !important;
        color: #2B5797 !important;
        font-weight: 400 !important;
        text-align: left !important;
        padding: 8px 16px !important;
        width: 100% !important;
        border-radius: 0 !important;
        margin-bottom: 2px !important;
        transition: all 0.2s ease !important;
        font-size: 14px !important;
        justify-content: flex-start !important;
    }

    section[data-testid="stSidebar"] .stButton > button:hover {
        background-color: #F7FAFC !important;
        color: #3182CE !important;
        text-decoration: underline !important;
    }

    section[data-testid="stSidebar"] .stButton > button:focus {
        background-color: #F7FAFC !important;
        color: #3182CE !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* Active/current page styling - for Claude */
    section[data-testid="stSidebar"] .stButton:last-child > button {
        color: #2D3748 !important;
        font-weight: 600 !important;
    }

    /* Sidebar divider */
    section[data-testid="stSidebar"] hr {
        border-color: #E2E8F0 !important;
        margin: 1rem 0 !important;
    }

    /* Main content area styling */
    .main .block-container {
        padding-top: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
        background-color: #f5f5f5;
    }

    /* Header styling */
    h1, h2, h3 {
        color: #2D3748 !important;
    }

    /* Improve text readability */
    .stMarkdown, .stText {
        color: #2D3748 !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif !important;
        line-height: 1.6 !important;
    }

    /* Ensure dataframes are readable */
    .stDataFrame {
        background-color: white !important;
        border-radius: 8px !important;
    }

    /* Fix metric text visibility */
    .metric-container {
        background-color: white !important;
        padding: 1rem !important;
        border-radius: 8px !important;
    }

    /* Ensure metric values and labels are visible - multiple selector approaches */
    [data-testid="metric-container"] {
        background-color: white !important;
        border: 1px solid #E2E8F0 !important;
        padding: 1rem !important;
        border-radius: 8px !important;
    }

    /* Target all text in metric containers */
    [data-testid="metric-container"], 
    [data-testid="metric-container"] * {
        color: #2D3748 !important;
    }

    /* Multiple approaches to target metric values */
    [data-testid="metric-container"] [data-testid="metric-value"],
    [data-testid="metric-value"],
    .metric-value,
    div[data-testid="metric-container"] > div:first-child {
        color: #2D3748 !important;
        font-weight: 600 !important;
        font-size: 1.875rem !important;
    }

    /* Multiple approaches to target metric labels */
    [data-testid="metric-container"] [data-testid="metric-label"],
    [data-testid="metric-label"],
    .metric-label,
    div[data-testid="metric-container"] > div:last-child {
        color: #2D3748 !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
    }

    /* Target metric delta values */
    [data-testid="metric-container"] [data-testid="metric-delta"],
    [data-testid="metric-delta"],
    .metric-delta {
        color: #10B981 !important;
        font-weight: 500 !important;
    }

    /* Force visibility for all metric text elements */
    .stMetric,
    .stMetric * {
        color: #2D3748 !important;
    }

    /* Aggressive approach - target all text in columns */
    div[data-testid="column"] div,
    div[data-testid="column"] span,
    div[data-testid="column"] p {
        color: #2D3748 !important;
    }

    /* Specific targeting for metric components */
    [data-baseweb="block"] div,
    [data-baseweb="block"] span {
        color: #2D3748 !important;
    }

    /* Try different metric selectors based on Streamlit's current structure */
    .css-1wivap2,
    .css-1wivap2 *,
    .css-metric-container,
    .css-metric-container * {
        color: #2D3748 !important;
    }

    /* Target text within tab content specifically */
    .stTabs [data-baseweb="tab-panel"] div,
    .stTabs [data-baseweb="tab-panel"] span,
    .stTabs [data-baseweb="tab-panel"] p {
        color: #2D3748 !important;
    }

    /* Improve warning box readability */
    .stAlert {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif !important;
    }

    /* Fix selectbox label visibility */
    .stSelectbox > label {
        color: #2D3748 !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        margin-bottom: 0.5rem !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif !important;
    }

    /* Fix tab header visibility */
    .stTabs [data-baseweb="tab-list"] button {
        color: #2D3748 !important;
        font-weight: 500 !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif !important;
    }

    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #2B5797 !important;
        font-weight: 600 !important;
    }

    /* Fix subheader visibility */
    .stMarkdown h2, .stMarkdown h3 {
        color: #2D3748 !important;
        font-weight: 600 !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif !important;
    }

    /* Ensure all form labels are visible */
    label {
        color: #2D3748 !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif !important;
    }

    /* Chat container styling - Canvas white content area */
    .chat-container {
        background-color: white !important;
        border-radius: 8px !important;
        padding: 24px !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
        margin-top: 20px !important;
    }

    /* Text area styling */
    .stTextArea > div > div > textarea {
        border-radius: 6px !important;
        border: 1px solid #CBD5E0 !important;
        font-size: 14px !important;
    }

    /* Button styling for chat actions */
    .stButton > button {
        background-color: #f7fafc !important;
        color: #2D3748 !important;
        border: 1px solid #CBD5E0 !important;
        border-radius: 6px !important;
        font-weight: 500 !important;
        padding: 8px 16px !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:hover {
        background-color: #EDF2F7 !important;
        border-color: #A0AEC0 !important;
    }

    /* Info boxes styling */
    .stInfo {
        background-color: white !important;
        border: 1px solid #BEE3F8 !important;
        border-radius: 8px !important;
    }

    /* Fix info box content visibility */
    [data-testid="stAlert"] {
        background-color: white !important;
        border: 1px solid #BEE3F8 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }

    [data-testid="stAlert"] p {
        color: #2D3748 !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif !important;
        line-height: 1.6 !important;
        margin: 0 !important;
    }

    [data-testid="stAlert"] div {
        color: #2D3748 !important;
    }

    /* Fix warning box content */
    [data-testid="stAlert"][data-baseweb="notification"] {
        background-color: #FFF3CD !important;
        border: 1px solid #FFEAA7 !important;
        color: #8B5A00 !important;
    }

    [data-testid="stAlert"][data-baseweb="notification"] p {
        color: #8B5A00 !important;
    }

    /* Support button styling for Claude interface */
    div[data-testid="column"] .stButton[data-testid="baseButton-primary"] > button[key="assignment_help"],
    div[data-testid="column"] .stButton[data-testid="baseButton-primary"] > button[key="lecture_help"],
    div[data-testid="column"] .stButton[data-testid="baseButton-primary"] > button[key="reading_help"] {
        background-color: #E6F3FF !important;
        color: #2B5797 !important;
        border: 1px solid #2B5797 !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
        padding: 12px 16px !important;
        transition: all 0.2s ease !important;
    }

    div[data-testid="column"] .stButton[data-testid="baseButton-primary"] > button[key="assignment_help"]:hover,
    div[data-testid="column"] .stButton[data-testid="baseButton-primary"] > button[key="lecture_help"]:hover,
    div[data-testid="column"] .stButton[data-testid="baseButton-primary"] > button[key="reading_help"]:hover {
        background-color: #2B5797 !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(43, 87, 151, 0.2) !important;
    }
                
    /* Restore Streamlit default code block styles */
    code, pre, pre code {
        all: revert !important;  /* resets to Streamlit's defaults */
    }

    /* Optional: only reset colors while keeping your font stack */
    code, pre, pre code {
        color: unset !important;
        background: unset !important;
        font-family: monospace !important;
    }
        /* Don't override code blocks */
    .stMarkdown, .stText {
        color: #2D3748 !important;
    }

    .stMarkdown code, .stMarkdown pre {
        color: inherit !important;   /* let Streamlit handle it */
    }
    </style>
    """, unsafe_allow_html=True)