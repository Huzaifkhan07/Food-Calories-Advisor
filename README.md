# Food Calories Advisor

Hi! 👋 This is my **Food Calories Advisor** app, built with Python and Streamlit. This app helps users get a quick nutritional analysis by uploading images of food items. Using Google’s Gemini API, the app identifies each item, calculates calories, and gives a recommendation on whether the food is healthy or not.

You can check out the live project here: [Food Calories Advisor](https://food-calories-advisor-huzaif-khan.streamlit.app/).  **Note**: Please wait for the project to load as it is hosted on a free tier Account.

[Linkedin Engagement](https://food-calories-advisor-huzaif-khan.streamlit.app/)

## What I've Done
- **Image Upload & Display**: Allows users to upload food images (JPG, PNG, JPEG) and shows the image on the screen.
- **Calorie Calculation**: Uses the Google Gemini model to identify food items from the image and calculate calories for each one.
- **Health Recommendation**: Based on calorie information, the app gives an assessment of whether the food is healthy.

## Technologies Used
- **Python**: All the backend logic and API integration.
- **Streamlit**: For the user interface, making it easy to upload and view images.
- **Google Cloud (Gemini API)**: To process and analyze the image content.
- **Pillow (PIL)**: For image processing in Python.
- **dotenv**: To securely load environment variables like API keys.

## Key Functions
- **get_gemini_response()**: This function connects with the Google Gemini model to analyze food images and get calorie info.
- **input_image_setup()**: Prepares the uploaded image in the format required for analysis.

## Installation

To get started, clone the repository:

```bash
git clone https://github.com/your-username/Food-Calories-Advisor.git
cd Food-Calories-Advisor
