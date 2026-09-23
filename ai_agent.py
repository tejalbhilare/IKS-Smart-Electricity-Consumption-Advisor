import os

from langchain_google_genai import ChatGoogleGenerativeAI


# ---------------------------------------
# Create Gemini AI model
# ---------------------------------------

def create_ai_model():
    """
    Creates the Gemini model using the API key
    stored in the Windows environment variable.
    """

    if not os.getenv("GEMINI_API_KEY"):
        raise ValueError(
            "GEMINI_API_KEY was not found."
        )

    model = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash"
    )

    return model


# ---------------------------------------
# Extract text from Gemini response
# ---------------------------------------

def extract_response_text(response):
    """
    Extracts readable text from the Gemini response.
    """

    content = response.content

    # If Gemini returns normal text
    if isinstance(content, str):
        return content

    # If Gemini returns structured content blocks
    if isinstance(content, list):

        text_parts = []

        for block in content:

            if isinstance(block, dict):

                if block.get("type") == "text":
                    text_parts.append(
                        block.get("text", "")
                    )

            elif isinstance(block, str):
                text_parts.append(block)

        return "\n".join(text_parts)

    return str(content)


# ---------------------------------------
# Generate electricity advice
# ---------------------------------------

def generate_advice(
    daily_consumption,
    usage_hours,
    risk_score,
    risk_level
):
    """
    Generates personalized electricity-saving advice
    using Gemini through LangChain.
    """

    model = create_ai_model()

    prompt = f"""
You are an AI-based Smart Electricity Consumption Advisor.

Analyze the user's electricity usage.

Daily electricity consumption:
{daily_consumption} kWh/day

Average appliance usage duration:
{usage_hours} hours/day

Energy wastage risk score:
{risk_score}/100

Risk level:
{risk_level}

Provide a simple personalized recommendation.

Include:

1. Explanation of the risk level.
2. Possible reasons for electricity wastage.
3. 3 to 5 practical electricity-saving suggestions.
4. A short sustainability message.

Do not invent electricity bills or exact monetary savings.

Keep the explanation simple and practical.
"""

    response = model.invoke(prompt)

    return extract_response_text(response)


# ---------------------------------------
# Test Gemini connection
# ---------------------------------------

if __name__ == "__main__":

    test_consumption = 22
    test_usage_hours = 9
    test_risk_score = 64.04
    test_risk_level = "Medium"

    advice = generate_advice(
        test_consumption,
        test_usage_hours,
        test_risk_score,
        test_risk_level
    )

    print("\n--- AI Electricity Advice ---\n")
    print(advice)