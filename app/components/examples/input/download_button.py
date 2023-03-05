import streamlit as st
import pandas as pd

def put():
    @st.cache_data
    def convert_df(df):
        """
        This function converts a pandas DataFrame to CSV format and encodes it in UTF-8.
        It is decorated with `st.cache_data` to prevent re-computation on every rerun.

        Parameters:
            - df (pandas DataFrame): The input DataFrame to convert.

        Returns:
            - (bytes): The CSV-encoded bytes of the input DataFrame.
        """
        return df.to_csv().encode('utf-8')
    
    df = pd.read_csv('assets/sample.csv')

    # Call the conversion function and cache its result
    csv = convert_df(df)

    # Create a download button that serves the CSV file
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='large_df.csv',
        mime='text/csv',
    )
