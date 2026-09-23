import streamlit as st

from fuzzy_logic import calculate_wastage_risk, get_risk_level
from ai_agent import generate_advice


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="IKS Electricity Advisor",
    page_icon="⚡",
    layout="centered"
)


# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("⚡ IKS Smart Electricity Consumption Advisor")

st.write(
    "An AI-assisted electricity consumption advisor that "
    "uses fuzzy logic to estimate energy wastage risk "
    "and provides practical electricity-saving suggestions."
)

st.divider()


# -------------------------------------------------
# USER INPUT
# -------------------------------------------------

st.subheader("🔌 Enter Your Electricity Usage")

daily_consumption = st.number_input(
    "Daily Electricity Consumption (kWh/day)",
    min_value=0.0,
    max_value=30.0,
    value=10.0,
    step=0.5
)

usage_hours = st.number_input(
    "Average Appliance Usage Duration (hours/day)",
    min_value=0.0,
    max_value=12.0,
    value=6.0,
    step=0.5
)


# -------------------------------------------------
# ANALYZE BUTTON
# -------------------------------------------------

if st.button("🔍 Analyze Electricity Usage", use_container_width=True):

    # ---------------------------------------------
    # FUZZY LOGIC CALCULATION
    # ---------------------------------------------

    try:

        risk_score = calculate_wastage_risk(
            daily_consumption,
            usage_hours
        )

        risk_level = get_risk_level(risk_score)

    except Exception as error:

        st.error("Unable to calculate the electricity risk.")
        st.exception(error)
        st.stop()


    # ---------------------------------------------
    # DISPLAY RISK RESULT
    # ---------------------------------------------

    st.divider()

    st.subheader("📊 Energy Wastage Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Risk Score",
            f"{risk_score}/100"
        )

    with col2:
        st.metric(
            "Risk Level",
            risk_level
        )


    # ---------------------------------------------
    # RISK MESSAGE
    # ---------------------------------------------

    if risk_level == "Low":

        st.success(
            "Your estimated electricity wastage risk is Low. "
            "Continue following energy-efficient habits."
        )

    elif risk_level == "Medium":

        st.warning(
            "Your estimated electricity wastage risk is Medium. "
            "Some changes in appliance usage may reduce wastage."
        )

    else:

        st.error(
            "Your estimated electricity wastage risk is High. "
            "Consider reducing unnecessary appliance usage."
        )


    # ---------------------------------------------
    # AI ADVICE
    # ---------------------------------------------

    st.divider()

    st.subheader("🤖 AI Electricity Advice")

    with st.spinner("Generating personalized advice..."):

        try:

            advice = generate_advice(
                daily_consumption,
                usage_hours,
                risk_score,
                risk_level
            )

            st.write(advice)

        except Exception:

            # -------------------------------------
            # FALLBACK ADVICE
            # -------------------------------------

            st.info(
                "The AI service is temporarily unavailable. "
                "The following recommendations are generated "
                "from the electricity risk analysis."
            )

            st.write("### Practical Electricity-Saving Suggestions")

            if risk_level == "Low":

                st.write(
                    "• Continue switching off appliances when not in use.\n"
                    "• Use energy-efficient LED lighting.\n"
                    "• Avoid leaving chargers connected unnecessarily.\n"
                    "• Make use of natural daylight when possible."
                )

            elif risk_level == "Medium":

                st.write(
                    "• Switch off fans, lights and appliances when not required.\n"
                    "• Reduce unnecessary appliance operating hours.\n"
                    "• Prefer energy-efficient appliances.\n"
                    "• Avoid standby power consumption.\n"
                    "• Monitor daily electricity consumption regularly."
                )

            else:

                st.write(
                    "• Reduce unnecessary appliance usage immediately.\n"
                    "• Switch off appliances instead of leaving them on standby.\n"
                    "• Reduce excessive use of high-power appliances.\n"
                    "• Use LED bulbs and energy-efficient appliances.\n"
                    "• Monitor electricity consumption every day."
                )

            st.write(
                "**Sustainability Message:** "
                "Responsible energy use helps reduce electricity wastage "
                "and supports sustainable living."
            )


# -------------------------------------------------
# IKS CONNECTION
# -------------------------------------------------

st.divider()

st.subheader("🪷 IKS Connection")

st.write(
    "The project connects the modern use of Artificial Intelligence "
    "and computational intelligence with the broader Indian Knowledge "
    "Systems principle of responsible and sustainable use of resources. "
    "The application encourages mindful electricity consumption and "
    "resource conservation while using modern fuzzy logic and AI "
    "technologies for personalized guidance."
)


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.divider()

st.caption(
    "TY IT – IKS Individual Project | "
    "Smart Electricity Consumption Advisor"
)