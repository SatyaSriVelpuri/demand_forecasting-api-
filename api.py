from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load demand data
df = pd.read_csv("demand_data.csv")

@app.get("/demand")
def get_demand():
    return df.to_dict(orient="records")
