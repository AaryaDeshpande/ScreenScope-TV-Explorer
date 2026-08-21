"""Shared ScreenScope visual tokens and minimal Streamlit styling."""

import streamlit as st


def apply_global_styles() -> None:
    """Apply the agreed dark ScreenScope visual direction."""
    st.markdown(
        """
        <style>
        :root {
            --screenscope-bg: #0f172a;
            --screenscope-panel: #1e293b;
            --screenscope-blue: #3b82f6;
            --screenscope-gold: #fbbf24;
            --screenscope-coral: #fb7185;
            --screenscope-teal: #2dd4bf;
        }
        .stApp {
            background: var(--screenscope-bg);
        }
        [data-testid="stHeader"] {
            background: rgba(15, 23, 42, 0.92);
        }
        [data-testid="stSidebar"] {
            background: #111827;
        }
        .stButton > button[kind="primary"] {
            background: var(--screenscope-blue);
            border-color: var(--screenscope-blue);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

