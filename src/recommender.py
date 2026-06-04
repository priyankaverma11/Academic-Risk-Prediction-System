def generate_recommendations(
    lunch,
    test_prep,
    risk_level
):
    recommendations = []

    if risk_level == "High":
        recommendations.append(
            "Increase study hours and seek academic support."
        )

    if test_prep == "none":
        recommendations.append(
            "Complete a test preparation course."
        )

    if lunch == "free/reduced":
        recommendations.append(
            "Monitor academic progress closely."
        )

    return recommendations


print(
    generate_recommendations(
        "free/reduced",
        "none",
        "High"
    )
)