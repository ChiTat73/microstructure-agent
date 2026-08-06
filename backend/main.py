from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="APAC Microstructure Agent Gateway")

# Allow your frontend dashboard to fetch data safely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "ONLINE", "active_markets": ["HKEX", "JPX", "SGX"]}

@app.get("/api/v1/hkex/macro")
def get_hkex_macro():
    """Simulated current macro regime statistics for HKEX."""
    return {
        "market": "HKEX",
        "turnover_hkd_bn": 283.0,
        "turnover_usd_bn": 36.2,
        "southbound_flow_pct": 43.0,
        "dominant_sector": "Financials",
        "highest_volume_sector": "Information Technology",
        "agent_regime_status": "NORMAL_EXECUTION"
    }
