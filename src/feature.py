import pandas as pd
import numpy as np

num_records = 500


synthetic_data = {
    "Customer_ID": [f"CUST_{i:05d}" for i in range(1, num_records + 1)],
    "Age": np.random.randint(18, 65, num_records),
    "Gender": np.random.choice(["Male", "Female"], num_records, p=[0.5, 0.5]),
    "Occupation": np.random.choice(["Student", "Professional", "Retired", "Unemployed"], num_records),
    "Income_Bracket": np.random.choice(["<$50K", "$50K–$100K", ">$100K"], num_records, p=[0.5, 0.4, 0.1]),
    "Family_Size": np.random.randint(1, 6, num_records),
    "Marital_Status": np.random.choice(["Single", "Married", "Divorced"], num_records),
    "Education_Level": np.random.choice(["High School", "Bachelor’s", "Master’s", "PhD"], num_records),
    "Region": np.random.choice(["North", "South", "East", "West"], num_records),
    "Monthly_Revenue": np.random.uniform(50, 1000, num_records),
    "CLTV": np.random.uniform(1000, 20000, num_records),
    "Avg_Monthly_Data_Usage_GB": np.random.uniform(1, 200, num_records),
    "Avg_Call_Duration_Minutes": np.random.uniform(1, 60, num_records),
    "Monthly_Transactions": np.random.randint(1, 50, num_records),
    "Churn_Status": np.random.choice(["Yes", "No"], num_records, p=[0.2, 0.8]),
    "Subscription_Type": np.random.choice(["Prepaid", "Postpaid", "Family Plan", "Corporate Plan"], num_records),
    "Retention_Offers_Availed": np.random.randint(0, 5, num_records),
    "Feedback_Score": np.random.randint(1, 11, num_records),
    "Preferred_Product_Type": np.random.choice(["Voice Plan", "Data-Only Plan", "Voice-Data Plan"], num_records),
    "Peak_Usage_Time": np.random.choice(["Morning", "Afternoon", "Evening", "Night"], num_records),
    "Last_Interaction_Days": np.random.randint(0, 365, num_records),
    "Number_of_Complaints": np.random.randint(0, 10, num_records),
    "Payment_Method": np.random.choice(["Credit Card", "Debit Card", "Net Banking", "UPI"], num_records),
    "Bill_Payment_Timeliness": np.random.choice(["On Time", "Late by <5 Days", "Late by >5 Days"], num_records),
    "Outstanding_Balance": np.random.uniform(0, 500, num_records),
    "Loyalty_Points": np.random.randint(0, 1000, num_records),
    "Campaign_Responses": np.random.randint(0, 10, num_records),
    "Social_Media_Activity": np.random.choice(["High", "Moderate", "Low"], num_records),
    "Network_Complaints": np.random.randint(0, 10, num_records),
    "Service_Downtime_Impact": np.random.choice(["Low", "Medium", "High"], num_records),
}


full_data = pd.DataFrame(synthetic_data)
full_data.to_csv("../Data/customer_segment_data.csv", index=False)
