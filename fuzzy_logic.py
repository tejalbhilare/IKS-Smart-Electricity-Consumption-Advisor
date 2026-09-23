import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def create_fuzzy_system():
    """
    Creates the fuzzy inference system for electricity wastage risk.

    Inputs:
        - Daily electricity consumption in kWh
        - Average appliance usage duration in hours/day

    Output:
        - Energy wastage risk from 0 to 100
    """

    # -----------------------------
    # 1. Define input and output variables
    # -----------------------------

    consumption = ctrl.Antecedent(
        np.arange(0, 31, 1),
        "consumption"
    )

    usage_duration = ctrl.Antecedent(
        np.arange(0, 13, 1),
        "usage_duration"
    )

    wastage_risk = ctrl.Consequent(
        np.arange(0, 101, 1),
        "wastage_risk"
    )

    # -----------------------------
    # 2. Define membership functions
    # -----------------------------

    # Daily electricity consumption
    consumption["low"] = fuzz.trimf(
        consumption.universe,
        [0, 0, 10]
    )

    consumption["medium"] = fuzz.trimf(
        consumption.universe,
        [5, 15, 25]
    )

    consumption["high"] = fuzz.trimf(
        consumption.universe,
        [20, 30, 30]
    )

    # Appliance usage duration
    usage_duration["short"] = fuzz.trimf(
        usage_duration.universe,
        [0, 0, 4]
    )

    usage_duration["medium"] = fuzz.trimf(
        usage_duration.universe,
        [2, 6, 10]
    )

    usage_duration["long"] = fuzz.trimf(
        usage_duration.universe,
        [8, 12, 12]
    )

    # Energy wastage risk
    wastage_risk["low"] = fuzz.trimf(
        wastage_risk.universe,
        [0, 0, 40]
    )

    wastage_risk["medium"] = fuzz.trimf(
        wastage_risk.universe,
        [25, 50, 75]
    )

    wastage_risk["high"] = fuzz.trimf(
        wastage_risk.universe,
        [60, 100, 100]
    )

    # -----------------------------
    # 3. Define fuzzy rules
    # -----------------------------

    rule1 = ctrl.Rule(
        consumption["low"] & usage_duration["short"],
        wastage_risk["low"]
    )

    rule2 = ctrl.Rule(
        consumption["low"] & usage_duration["medium"],
        wastage_risk["low"]
    )

    rule3 = ctrl.Rule(
        consumption["low"] & usage_duration["long"],
        wastage_risk["medium"]
    )

    rule4 = ctrl.Rule(
        consumption["medium"] & usage_duration["short"],
        wastage_risk["medium"]
    )

    rule5 = ctrl.Rule(
        consumption["medium"] & usage_duration["medium"],
        wastage_risk["medium"]
    )

    rule6 = ctrl.Rule(
        consumption["medium"] & usage_duration["long"],
        wastage_risk["high"]
    )

    rule7 = ctrl.Rule(
        consumption["high"] & usage_duration["short"],
        wastage_risk["medium"]
    )

    rule8 = ctrl.Rule(
        consumption["high"] & usage_duration["medium"],
        wastage_risk["high"]
    )

    rule9 = ctrl.Rule(
        consumption["high"] & usage_duration["long"],
        wastage_risk["high"]
    )

    # -----------------------------
    # 4. Create fuzzy control system
    # -----------------------------

    risk_control_system = ctrl.ControlSystem([
        rule1,
        rule2,
        rule3,
        rule4,
        rule5,
        rule6,
        rule7,
        rule8,
        rule9
    ])

    return risk_control_system


def calculate_wastage_risk(daily_consumption, usage_hours):
    """
    Calculates electricity wastage risk using fuzzy inference.

    Parameters:
        daily_consumption: electricity consumption in kWh/day
        usage_hours: average appliance usage duration in hours/day

    Returns:
        Numerical risk score between 0 and 100.
    """

    control_system = create_fuzzy_system()

    simulation = ctrl.ControlSystemSimulation(control_system)

    # Provide input values
    simulation.input["consumption"] = daily_consumption
    simulation.input["usage_duration"] = usage_hours

    # Perform fuzzy inference and defuzzification
    simulation.compute()

    risk_score = simulation.output["wastage_risk"]

    return round(float(risk_score), 2)


def get_risk_level(risk_score):
    """
    Converts the numerical risk score into a readable category.
    """

    if risk_score < 40:
        return "Low"

    elif risk_score < 70:
        return "Medium"

    else:
        return "High"


# -----------------------------
# Test the fuzzy system
# -----------------------------

if __name__ == "__main__":

    test_consumption = 22
    test_usage_hours = 9

    risk = calculate_wastage_risk(
        test_consumption,
        test_usage_hours
    )

    level = get_risk_level(risk)

    print("Electricity Consumption:", test_consumption, "kWh/day")
    print("Appliance Usage Duration:", test_usage_hours, "hours/day")
    print("Energy Wastage Risk:", risk)
    print("Risk Level:", level)