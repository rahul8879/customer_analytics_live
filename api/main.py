from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# actual data
data = pd.read_csv('../Data/segement_output.csv')

total_customer = len(data)

segment_stats = data.groupby('Segment').agg({
    'Monthly_Revenue': 'mean',
    'CLTV': 'mean',
    'Age': 'mean',
    'Customer_ID': 'count'
}).rename(columns={'Customer_ID': 'Customer_Count'}).round(2)


segment_stats['Percentage_of_Customers'] = (
    segment_stats['Customer_Count'] / total_customer * 100
).round(2)

segment_stats_dict = segment_stats.to_dict(orient='index')


cluster_data = [
    {
        "Cluster": 0,
        "Monthly_Revenue": 797.85,
        "CLTV": 12032.71,
        "Loyalty_Points": 513.29,
        "Retention_Offers_Availed": 1.73,
        "Recommendation": "Offer loyalty rewards and premium services to maintain engagement."
    },
    {
        "Cluster": 1,
        "Monthly_Revenue": 404.35,
        "CLTV": 8833.19,
        "Loyalty_Points": 477.93,
        "Retention_Offers_Availed": 3.27,
        "Recommendation": "Focus on retention campaigns and cross-sell opportunities."
    },
    {
        "Cluster": 2,
        "Monthly_Revenue": 329.56,
        "CLTV": 11693.38,
        "Loyalty_Points": 511.51,
        "Retention_Offers_Availed": 0.66,
        "Recommendation": "Engage with discounts or subscription renewal incentives."
    },
]
cluster_profiles = pd.DataFrame(cluster_data)


@app.get("/get-segment-details/{cluster_id}")
async def get_segment_details(cluster_id: int):
    segment = cluster_profiles[cluster_profiles['Cluster'] == cluster_id]
    if not segment.empty:
        return segment.to_dict(orient="records")[0]
    else:
        return {'error': 'Cluster not found'}


@app.get("/segment-stats")
async def get_segment_stats():
    """Returns aggregated statistics for each segment including percentages."""
    return segment_stats_dict


@app.get("/basic-stats")
async def get_basic_stats():
    """Returns total monthly revenue."""
    total = data['Monthly_Revenue'].sum().round(2)
    return {"total_monthly_revenue": total}


@app.get("/top-performing-customers")
async def get_top_customers():
    try:
        top_customers = data.nlargest(10, "Monthly_Revenue")[[
            "Customer_ID", "Age", "Gender", "Monthly_Revenue", "Segment"
        ]]
        result = top_customers.to_dict(orient="records")
        return {"data": result}
    except Exception as e:
        return {'error': str(e)}
