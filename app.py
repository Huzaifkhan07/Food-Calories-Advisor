
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Set Streamlit page configuration as the first Streamlit command
st.set_page_config(page_title="My Health App")

# Load environment variables and configure the API key
load_dotenv()  # Loads all the variables from the environment (.env) file.
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to get response from Gemini model
def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_prompt, image[0]])
    return response.text

# Function to handle uploaded images
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit app starts here
st.header("Food Calories Advisor")

# Upload an image
uploaded_file = st.file_uploader("Choose an image.. ", type=["jpg", "png", "jpeg"])
image = ""

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image Uploaded!", use_column_width=True)

# Submit button
submit = st.button("Get Total Calories")

# Prompt for the Gemini model
input_prompt = """
You are an expert nutritionist. You need to analyze the food items from the image and calculate the total calories. Provide details of each food item with calorie intake in the following format:
1. Item 1 - number of calories
2. Item 2 - number of calories
---
Finally, mention whether the food is healthy or not.
"""

# Handle form submission
if submit:
    image_data = input_image_setup(uploaded_file)
    st.header("Here is the Total Calories!")
    response = get_gemini_response(input_prompt, image_data)
    st.write(response)
