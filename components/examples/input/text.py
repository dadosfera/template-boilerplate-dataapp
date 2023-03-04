import streamlit as st

def put():
    # Store the initial value of widgets in session state
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    # Create two columns for the widgets
    col1, col2 = st.columns(2)

    # Add widgets to the first column
    with col1:
        # Checkbox to toggle text input widget disablement
        st.checkbox("Disable text input widget", key="disabled")
        # Radio buttons to set text input label visibility
        st.radio(
            "Set text input label visibility 👉",
            key="visibility",
            options=["visible", "hidden", "collapsed"],
        )
        # Text input widget placeholder
        st.text_input(
            "Placeholder for the other text input widget",
            "This is a placeholder",
            key="placeholder",
        )

    # Add text input widget to the second column
    with col2:
        # Create text input widget with its properties set from session state
        text_input = st.text_input(
            "Enter some text 👇",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder=st.session_state.placeholder,
        )

        # Show the entered text if there's any
        if text_input:
            st.write("You entered: ", text_input)
