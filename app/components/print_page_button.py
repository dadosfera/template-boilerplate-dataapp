from streamlit.components.v1 import html
import streamlit as st


def put():
    with st.sidebar:
        st.sidebar.markdown(
            """
            <style>
                @media print {
                    [data-testid="stSidebar"] {
                        display: none !important;
                    }
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        html(
            """
            <style>
                body {
                    margin: 0px;
                }
                button {
                    align-items: center;
                    appearance: button;
                    background-color: rgb(249, 249, 251);
                    border-bottom-color: rgba(49, 51, 63, 0.2);
                    border-bottom-left-radius: 4px;
                    border-bottom-right-radius: 4px;
                    border-bottom-style: solid;
                    border-bottom-width: 1px;
                    border-image-outset: 0;
                    border-image-repeat: stretch;
                    border-image-slice: 100%;
                    border-image-source: none;
                    border-image-width: 1;
                    border-left-color: rgba(49, 51, 63, 0.2);
                    border-left-style: solid;
                    border-left-width: 1px;
                    border-right-color: rgba(49, 51, 63, 0.2);
                    border-right-style: solid;
                    border-right-width: 1px;
                    border-top-color: rgba(49, 51, 63, 0.2);
                    border-top-left-radius: 4px;
                    border-top-right-radius: 4px;
                    border-top-style: solid;
                    border-top-width: 1px;
                    box-sizing: border-box;
                    color: rgb(49, 51, 63);
                    cursor: pointer;
                    display: inline-flex;
                    font-family: "Source Sans Pro", sans-serif;
                    font-feature-settings: normal;
                    font-kerning: auto;
                    font-optical-sizing: auto;
                    font-size: 16px;
                    font-stretch: 100%;
                    font-style: normal;
                    font-variant-alternates: normal;
                    font-variant-caps: normal;
                    font-variant-east-asian: normal;
                    font-variant-ligatures: normal;
                    font-variant-numeric: normal;
                    font-variation-settings: normal;
                    font-weight: 400;
                    height: 35.5938px;
                    justify-content: center;
                    letter-spacing: normal;
                    line-height: 25.6px;
                    margin-bottom: 0px;
                    margin-left: 0px;
                    margin-right: 0px;
                    margin-top: 0px;
                    overflow-x: visible;
                    overflow-y: visible;
                    padding-bottom: 4px;
                    padding-left: 12px;
                    padding-right: 12px;
                    padding-top: 4px;
                    text-align: center;
                    text-indent: 0px;
                    text-rendering: auto;
                    text-shadow: none;
                    text-size-adjust: 100%;
                    text-transform: none;
                    user-select: none;
                    width: 100px;
                }
                button p{
                    box-sizing: border-box;
                    color: rgb(49, 51, 63);
                    display: block;
                    font-family: "Source Sans Pro", sans-serif;
                    font-feature-settings: normal;
                    font-kerning: auto;
                    font-optical-sizing: auto;
                    font-size: 15px;
                    font-stretch: 100%;
                    font-style: normal;
                    font-variant-alternates: normal;
                    font-variant-caps: normal;
                    font-variant-east-asian: normal;
                    font-variant-ligatures: normal;
                    font-variant-numeric: normal;
                    font-variation-settings: normal;
                    font-weight: 400;
                    letter-spacing: normal;
                    line-height: 25.6px;
                    padding-bottom: 0px;
                    padding-left: 0px;
                    padding-right: 0px;
                    padding-top: 0px;
                    text-align: center;
                    text-indent: 0px;
                    text-rendering: auto;
                    text-shadow: none;
                    text-size-adjust: 100%;
                    text-transform: none;
                    user-select: none;
                    word-break: break-word;
                    word-spacing: 0px;
                    writing-mode: horizontal-tb;
                    -webkit-font-smoothing: auto;
                    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
                }
            </style>
            <button id="print-button" onclick="parent.window.print()">
                <p>Gerar PDF</p>
            </button>
        """,
            None,
            75,
        )
