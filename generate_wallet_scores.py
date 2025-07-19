import json
import pandas as pd
import numpy as np
from datetime import datetime

# Load JSON data
with open("user-wallet-transactions.json", "r") as file:
    data = json.load(file)

df = pd.json_normalize(data)

# Preprocessing
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df['amount'] = pd.to_numeric(df['actionData.amount'], errors='coerce')
df['assetPriceUSD'] = pd.to_numeric(df['actionData.assetPriceUSD'], errors='coerce')
df['usd_value'] = df['amount'] * df['assetPriceUSD']

# Aggregate features
features = df.groupby(['userWallet', 'action']).agg(
    tx_count=('action', 'count'),
    total_usd=('usd_value', 'sum')
).unstack(fill_value=0)
features.columns = [f"{stat}_{action}" for action in features.columns.levels[1] for stat in features.columns.levels[0]]

# Wallet-level metrics
wallet_activity = df.groupby('userWallet').agg(
    total_tx=('action', 'count'),
    first_tx=('timestamp', 'min'),
    last_tx=('timestamp', 'max')
)
wallet_activity['active_days'] = (wallet_activity['last_tx'] - wallet_activity['first_tx']).dt.days + 1

# Merge all features
wallet_features = features.join(wallet_activity)

# Derived metrics
wallet_features['repayment_ratio'] = wallet_features.get('total_usd_repay', 0) / wallet_features.get('total_usd_borrow', 1)
wallet_features['liquidation_rate'] = wallet_features.get('tx_count_liquidationcall', 0) / wallet_features['total_tx']
wallet_features['borrow_to_deposit'] = wallet_features.get('total_usd_borrow', 0) / (wallet_features.get('total_usd_deposit', 1))

# Credit scoring heuristic
def compute_score(row):
    score = 1000
    score -= min(row.get('liquidation_rate', 0) * 1000, 300)
    score += min(row.get('repayment_ratio', 0) * 200, 200)
    score += min(row.get('active_days', 0), 100)
    score -= min(row.get('borrow_to_deposit', 0) * 100, 200)
    return int(np.clip(score, 0, 1000))

wallet_features['credit_score'] = wallet_features.apply(compute_score, axis=1)

# Save to CSV
wallet_features[['credit_score']].to_csv("wallet_credit_scores.csv")
print("Saved wallet_credit_scores.csv")
