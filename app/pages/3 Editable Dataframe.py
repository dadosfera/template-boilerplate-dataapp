import streamlit as st
import pandas as pd

# Create a pandas DataFrame with some example data
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

# Create an editable dataframe using the Streamlit data editor
edited_df = st.experimental_data_editor(df, num_rows="dynamic", use_container_width=True)
# Arguments:
# - df (pandas.DataFrame): The dataframe to be edited.
# - num_rows (int or str): The number of rows to display in the editor. If "dynamic", the editor will display all rows.
# - use_container_width (bool): Whether to use the full width of the Streamlit app.
# Returns: pandas.DataFrame. The edited dataframe.
# Raises: ValueError if num_rows is not "dynamic" and is not a positive integer.

# Find the command with the highest rating in the edited dataframe
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
# Returns: str. The command with the highest rating.

# Display the favorite command as a Markdown string
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
# Arguments: favorite_command (str). The command with the highest rating.
