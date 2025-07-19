# DeFi-Wallet-Credit-Scoring---Aave-V2
This system assigns a credit score between 0 and 1000 to DeFi wallets based on historical transaction behavior on Aave V2.

## Key Features Used

- Number of transactions per action type (deposit, borrow, repay, liquidation).
- Total USD volume of deposits, borrows, and repayments.
- Ratios: repayment-to-borrow, borrow-to-deposit.
- Liquidation event frequency.
- Wallet activity span (in days).

## Scoring Heuristic

- +200 for high repayment ratio.
- +100 for long active history.
- −300 max penalty for high liquidation frequency.
- −200 for aggressive borrow-to-deposit ratio.

## Output

CSV file `wallet_credit_scores.csv` with columns: `userWallet`, `credit_score`.
