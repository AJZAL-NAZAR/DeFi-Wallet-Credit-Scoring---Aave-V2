# DeFi-Wallet-Credit-Scoring---Aave-V2
This system assigns a credit score between 0 and 1000 to DeFi wallets based on historical transaction behavior on Aave V2.

## Key Features Used

- Number of transactions per action type (deposit, borrow, repay, liquidation).
- Total USD volume of deposits, borrows, and repayments.
- Ratios: repayment-to-borrow, borrow-to-deposit.
- Liquidation event frequency.
- Wallet activity span (in days).

---

##  Objective

Enable on-chain creditworthiness analysis for:
- Trust scoring of users in lending platforms
- Whitelisting reliable wallets
- Detecting bots or exploit attempts
- Building risk-informed DeFi analytics

---

##  Methodology

We apply a **heuristic-based scoring model** using engineered behavioral features from raw Aave V2 transaction logs. These features capture wallet intent, financial balance, risk appetite, and repayment discipline.

---

##  Feature Engineering

Extracted from raw user transaction logs (`actionData`), grouped by `userWallet`:

| Category        | Features                                                                 |
|-----------------|--------------------------------------------------------------------------|
| Count Features  | Total transactions, action type counts (deposit, borrow, repay, liquidation) |
| Financials      | USD volume of deposits, borrows, repayments                              |
| Ratios          | Repayment-to-borrow ratio, borrow-to-deposit ratio                      |
| Risk Signals    | Liquidation frequency, inactivity, short wallet life                     |
| Temporal        | Wallet age, active days span                                             |

---

## Scoring Heuristic

| Metric                     | Weight / Penalty |
|----------------------------|------------------|
|  High repayment ratio     | +200             |
| Long wallet activity span | +100             |
|  Liquidation frequency    | −300 max         |
| Aggressive leverage      | −200 max         |


## Scoring Heuristic

- +200 for high repayment ratio.
- +100 for long active history.
- −300 max penalty for high liquidation frequency.
- −200 for aggressive borrow-to-deposit ratio.

## Output

CSV file `wallet_credit_scores.csv` with columns: `userWallet`, `credit_score`.
