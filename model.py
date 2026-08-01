"""
Credit Card Customer Segmentation Predictor

Loads the trained scaler and K-Means model
and predicts the customer segment for a new customer.
"""

# ============================================================
# IMPORT LIBRARIES
# ============================================================

from pathlib import Path
import pandas as pd
import joblib

# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_PATH = Path(__file__).parent
MODELS_PATH = PROJECT_PATH / "models"

# ============================================================
# LOAD TRAINED MODELS
# ============================================================

print("=" * 60)
print("LOADING TRAINED MODELS")
print("=" * 60)

scaler = joblib.load(MODELS_PATH / "scaler.joblib")
kmeans = joblib.load(MODELS_PATH / "kmeans_model.joblib")

print("Models loaded successfully.")

# ============================================================
# CUSTOMER INPUT
# ============================================================

print("\n" + "=" * 60)
print("NEW CUSTOMER INFORMATION")
print("=" * 60)

credit_limit = float(input("Average Credit Limit      : "))
credit_cards = int(input("Total Credit Cards        : "))
bank_visits = int(input("Total Bank Visits         : "))
online_visits = int(input("Total Online Visits       : "))
calls_made = int(input("Total Calls Made          : "))

# ============================================================
# CREATE CUSTOMER DATAFRAME
# ============================================================

customer = pd.DataFrame({
    "Avg_Credit_Limit": [credit_limit],
    "Total_Credit_Cards": [credit_cards],
    "Total_visits_bank": [bank_visits],
    "Total_visits_online": [online_visits],
    "Total_calls_made": [calls_made]
})

# ============================================================
# SCALE CUSTOMER DATA
# ============================================================

customer_scaled = scaler.transform(customer)

# ============================================================
# PREDICT CLUSTER
# ============================================================

predicted_cluster = int(kmeans.predict(customer_scaled)[0])

# ============================================================
# INTERPRET RESULT
# ============================================================

segments = {
    0: "Middle Customer",
    1: "Premium Customer",
    2: "Low Priority Customer"
}

recommendations = {
    0: [
        "Medium-value customer",
        "Regular banking behaviour",
        "Suitable for standard banking products",
        "Good opportunity for upselling"
    ],

    1: [
        "High-value customer",
        "Highest spending capacity",
        "Eligible for premium banking services",
        "Ideal candidate for exclusive offers"
    ],

    2: [
        "Low-value customer",
        "Lowest spending capacity",
        "Suitable for basic banking products",
        "Requires more customer support"
    ]
}

# ============================================================
# DISPLAY RESULT
# ============================================================

print("\n" + "=" * 60)
print("PREDICTION RESULT")
print("=" * 60)

print(f"Predicted Cluster : {predicted_cluster}")
print(f"Customer Segment  : {segments[predicted_cluster]}")

print("\nRecommendation")

for item in recommendations[predicted_cluster]:
    print(f"• {item}")

print("=" * 60)
print("Prediction Completed Successfully.")
print("=" * 60)
