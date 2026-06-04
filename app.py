import streamlit as st
st.sidebar.title("About")

st.sidebar.info(
    """
    Academic Risk Prediction System

    Built using:
    - Python
    - Pandas
    - Scikit-learn
    - Streamlit

    Predicts student risk levels and
    generates intervention recommendations.
    """
)

st.metric(
    "Model Accuracy",
    "44.5%"
)

st.title("🎓 Academic Risk Detection System")

st.write(
    "Predict student academic risk and generate recommendations."
)

gender = st.selectbox(
    "Gender",
    ["female", "male"]
)

lunch = st.selectbox(
    "Lunch Type",
    ["standard", "free/reduced"]
)

test_prep = st.selectbox(
    "Test Preparation Course",
    ["completed", "none"]
)


def predict_risk(lunch, test_prep):

    score = 0

    if lunch == "free/reduced":
        score += 1

    if test_prep == "none":
        score += 1

    if score == 0:
        return "Low"

    elif score == 1:
        return "Medium"

    return "High"


def generate_recommendations(
    lunch,
    test_prep,
    risk
):

    recommendations = []

    if test_prep == "none":
        recommendations.append(
            "Complete a test preparation course."
        )

    if lunch == "free/reduced":
        recommendations.append(
            "Monitor academic progress closely."
        )

    if risk == "High":
        recommendations.append(
            "Increase study hours and seek academic support."
        )

    return recommendations


if st.button("Predict Risk"):

    risk = predict_risk(
        lunch,
        test_prep
    )

    st.subheader(
        f"Predicted Risk Level: {risk}"
    )

    recs = generate_recommendations(
        lunch,
        test_prep,
        risk
    )

    st.subheader("Recommendations")

    if len(recs) == 0:
        st.success(
            "No major concerns detected. Keep up the good work!"
        )
    else:
        for rec in recs:
            st.write("✅", rec)