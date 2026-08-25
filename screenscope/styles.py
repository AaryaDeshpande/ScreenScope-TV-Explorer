"""Shared ScreenScope visual tokens and minimal Streamlit styling."""

import streamlit as st


def apply_global_styles() -> None:
    """Apply the shared light ScreenScope visual direction."""
    st.markdown(
        """
        <style>
        :root {
            --screenscope-bg: #f8fafc;
            --screenscope-panel: #ffffff;
            --screenscope-blue: #3b82f6;
            --screenscope-gold: #d97706;
            --screenscope-coral: #e11d48;
            --screenscope-teal: #0f766e;
        }
        .stApp {
            background: var(--screenscope-bg);
        }
        .stApp h1, .stApp h2, .stApp h3, [data-testid="stCaptionContainer"] p { color: #172033; }
        [data-testid="stHeader"] {
            background: rgba(248, 250, 252, 0.92);
        }
        [data-testid="stSidebar"] {
            background: #eef2f7;
        }
        .stButton > button[kind="primary"] {
            background: var(--screenscope-blue);
            border-color: var(--screenscope-blue);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

