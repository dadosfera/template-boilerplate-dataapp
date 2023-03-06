import streamlit as st
from pydantic import BaseModel, Field, HttpUrl
from pydantic.color import Color
import streamlit_pydantic as sp

class ExampleModel(BaseModel):
    """
    Example Pydantic model for a form-based data app.

    Attributes:
        url (HttpUrl): A URL field.
        color (Color): A color field.
        email (str): An email field with a maximum length of 100 and a regex pattern to validate the email format.
    """
    url: HttpUrl
    color: Color
    email: str = Field(..., max_length=100, regex=r"^\S+@\S+$")

data = sp.pydantic_form(key="my_form", model=ExampleModel)
if data:
    """
    Displays the submitted data as a JSON object.

    Args:
        data (ExampleModel): A Pydantic model instance representing the submitted form data.
    """
    st.json(data.json())
