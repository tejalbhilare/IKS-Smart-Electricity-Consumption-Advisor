# IKS Smart Electricity Consumption Advisor

## Project Description

The IKS Smart Electricity Consumption Advisor is an AI-assisted web application developed as an individual TY IT - IKS project.

The application uses fuzzy logic to estimate electricity wastage risk based on daily electricity consumption and average appliance usage duration. It then uses Google Gemini AI through LangChain to provide personalized electricity-saving recommendations.

The project encourages mindful electricity consumption, energy conservation, and responsible use of resources.

## Features

- Accepts daily electricity consumption in kWh/day
- Accepts average appliance usage duration in hours/day
- Uses fuzzy logic for electricity wastage risk estimation
- Generates a risk score from 0 to 100
- Classifies risk as Low, Medium, or High
- Uses Google Gemini AI for personalized recommendations
- Provides practical electricity-saving suggestions
- Includes an IKS connection
- Promotes responsible and sustainable energy use
- Provides a simple Streamlit web interface

## Technologies Used

- Python
- Streamlit
- NumPy
- scikit-fuzzy
- LangChain
- Google Gemini AI

## Project Structure

```text
IKS Smart Electricity Consumption Advisor/
|
|-- app.py
|-- fuzzy_logic.py
|-- ai_agent.py
|-- requirements.txt
|-- README.md
`-- .gitignore