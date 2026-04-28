import streamlit as st
import streamlit.components.v1 as components

# 1. Configure the page to take up the full width
st.set_page_config(layout="wide", page_title="Bio-Hythane Synthesis | Jacob Mathew")

# 2. Hide Streamlit's default UI elements (header, footer, menu) and remove padding
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            /* This removes the default padding so your website touches the edges */
            .block-container {
                padding-top: 0rem; 
                padding-bottom: 0rem; 
                padding-left: 0rem; 
                padding-right: 0rem;
            }
            iframe {
                border: none;
                height: 100vh; /* Make iframe take full screen height */
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. Read your HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 4. Render the HTML using Streamlit Components
# scrolling=True allows the user to scroll through your landing page and simulator
components.html(html_content, height=1200, scrolling=True)
