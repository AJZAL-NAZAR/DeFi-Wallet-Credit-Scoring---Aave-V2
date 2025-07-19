# Wallet Credit Score Analysis - Aave V2

This document analyzes the credit score distribution of wallets interacting with Aave V2 based on historical DeFi transaction behavior.

---

## 📊 Score Distribution

| Score Range | Number of Wallets |
|-------------|-------------------|
| 0–100       | `1,238`            |
| 101–200     | `2,617`            |
| 201–300     | `4,849`            |
| 301–400     | `7,015`            |
| 401–500     | `8,122`            |
| 501–600     | `9,034`            |
| 601–700     | `10,297`           |
| 701–800     | `8,865`            |
| 801–900     | `5,377`            |
| 901–1000    | `2,541`            |


---

##  Behavior of Wallets in the Lower Score Range (0–300)

Wallets in this range typically show one or more of the following traits:
- **High liquidation frequency** — frequent inability to maintain collateral.
- **Low or zero repayment ratio** — borrow without repaying.
- **Short activity window** — usually active for only a few days.
- **High borrow-to-deposit ratio** — aggressive leverage.
- **Minimal participation** — a single risky or exploit-like action.

These may include:
- Bot-like behavior.
- Attempted exploits.
- Abandoned wallets post-liquidation.

---

## Behavior of Wallets in the Higher Score Range (700–1000)

Wallets in this range consistently display:
- **High repayment ratios** — they repay what they borrow.
- **Sustained engagement** — activity across weeks or months.
- **Minimal or zero liquidation events**.
- **Balanced borrow-to-deposit ratio** — cautious financial behavior.
- **Diversified actions** — depositing, borrowing, repaying regularly.

These are likely:
- Power users.
- Smart-contract driven vaults with safety logic.
- DeFi-native users with high on-chain reputation.
- Scores below 300: Often bots, exploiters, or abandoned wallets.
-Scores above 700: Strong signal of trustworthy users and power DeFi participants.
-The middle ranges (400–700) contain mixed signals typically moderate-risk but still functional DeFi users.
-Total wallets scored: 60,000+

-Mean score: ~560

-Median score: ~600

-Standard deviation: ~170
---



