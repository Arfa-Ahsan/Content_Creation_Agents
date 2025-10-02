import streamlit as st
from datetime import datetime
from src.posttrend.crew import Posttrend
import pyperclip

st.set_page_config(page_title="AI Content Creator", layout="wide")

# ================= CSS STYLES ================= #
st.markdown("""
    <style>
        /* Set the main background to white */
        .stApp {
            background-color: #fff !important;
        }
        /* Sidebar background to light pink */
        section[data-testid="stSidebar"] {
            background-color: #fc9aa9 !important;
        }
        /* Sidebar header and text color for contrast */
        .sidebar-content, .css-1d391kg, .css-1v3fvcr {
            color: #232946 !important;
        }
        /* Main content area card look */
        .main .block-container {
            background-color: #fff !important;
            border-radius: 16px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.04);
            padding: 2rem 2rem 2rem 2rem;
        }
        h1 {
            margin-bottom: 0;
        }
        .subtitle {
            margin-top: 0;
            font-size: 16px;
        }
        .copy-section {
            margin-top: 24px;
            margin-bottom: 12px;
        }
        .stTextArea textarea {
            font-family: 'Consolas', 'Menlo', 'Monaco', 'Courier New', monospace;
            font-size: 1em;
        }
        .copy-btn {
            background-color: #e75480;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px 18px;
            font-size: 1em;
            cursor: pointer;
            margin-bottom: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# ================= HEADER ================= #
st.markdown(
    "<h1 style='text-align: center; color: #e75480;'>AI Content Creator</h1>"
    "<p class='subtitle' style='text-align: center; color: #232946;'>Generate high-quality, engaging content tailored to your platform of choice</p>",
    unsafe_allow_html=True
)

# ================= SIDEBAR CONFIG ================= #
st.sidebar.header("Content Configuration")

topic = st.sidebar.text_input("Topic", placeholder="Enter your content topic...")
content_type = st.sidebar.selectbox(
    "Content Type",
    [
        "Select content type...",
        "Blog Post",
        "Instagram Caption",
        "Facebook Post",
        "TikTok Caption",
        "Twitter/X Post",
        "LinkedIn Post"
    ]
)
generate_btn = st.sidebar.button("✨ Generate Content", use_container_width=True)

# ================= MAIN PAGE OUTPUT ================= #
st.markdown("### 📄 Generated Content")


if generate_btn and topic and content_type != "Select content type...":
    with st.spinner("Crew is researching, writing, and optimizing..."):
        posttrend = Posttrend()
        crew_instance = posttrend.crew()
        current_year = datetime.now().year

        result = crew_instance.kickoff(inputs={
            "topic": topic,
            "content_type": content_type,
            "current_year": current_year
        })

    # Extract string content from CrewOutput object
    output_text = getattr(result, "content", None) or getattr(result, "result", None) or str(result)
    st.session_state["output_text"] = output_text  # Save to session state

# Use the saved content if available
output_text = st.session_state.get("output_text", "")

if output_text:
    st.toast('Content Ready', icon="✅")
    st.markdown(output_text, unsafe_allow_html=True)

    # Copy button for output_text 
    if st.button('Copy'):
        pyperclip.copy(output_text)
        st.toast('Text copied successfully!', icon="✅")
        st.toast('The content copied is in Markdown format. Use a Markdown editor to convert it into rich text.', icon="ℹ️")
    
else:
    st.info("Enter a topic and select a content type in the sidebar to generate content.")