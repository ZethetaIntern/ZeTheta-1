# Portfolio Construction AI – Robo-Advisory Platform

## Project Overview

This project implements an AI-powered portfolio advisory system designed to simulate a real-world robo-advisor used in the BFSI domain. The platform integrates risk profiling, goal-based investing, portfolio optimization, tax-aware rebalancing, and client reporting into a single end-to-end workflow.

The objective of this project is to demonstrate practical portfolio construction logic under realistic constraints, rather than theoretical or purely academic optimization.

---

## Core Features

### 1. Risk Profiling
- Questionnaire-based investor risk assessment
- Weighted scoring model
- Classification into Conservative, Moderate, or Aggressive profiles
- Risk category directly influences portfolio risk aversion

### 2. Goal-Based Investing
- Computes required annualized return (CAGR) for a given financial goal
- Evaluates feasibility of achieving the goal under the current risk profile
- Provides advisory guidance when goals are not realistically achievable

### 3. Portfolio Construction
- Mean–Variance Optimization using CVXPY
- Long-only, fully invested portfolios
- Maximum asset weight constraint to prevent concentration
- Optional turnover constraint to limit excessive rebalancing
- Risk aversion dynamically mapped from investor risk profile

### 4. Rebalancing Engine
- Threshold-based rebalancing logic
- Transaction cost adjustment
- Simplified tax impact modeling
- Produces net trades rather than naïve target weights

### 5. Performance & Risk Metrics
- Expected portfolio return
- Volatility
- Sharpe ratio
- Value at Risk (VaR)
- Maximum drawdown (based on available data)

### 6. Robo-Advisory Decision Logic
- Compares portfolio return with required goal return
- Generates human-readable advisory recommendations
- Avoids overstating performance or guarantees

### 7. Client Reporting
- Structured client report object
- Includes portfolio metrics, allocations, and advisory notes
- Designed for easy extension to dashboards or APIs

---

## How the System Works (End-to-End)

1. Investor completes a risk profiling questionnaire  
2. System classifies investor risk category  
3. Financial goal is analyzed for required return  
4. Portfolio is optimized under risk, diversification, and turnover constraints  
5. Rebalancing engine generates cost- and tax-aware trades  
6. Performance and risk metrics are computed  
7. Robo-advisor produces a client recommendation  
8. Final client report is generated

---

## Design Philosophy

- Focus on **practical realism**, not academic perfection  
- Explicit assumptions and constraints  
- Deterministic, testable logic  
- No over-reliance on black-box AI models  
- Emphasis on robustness, interpretability, and professional discipline

---

## Notes & Limitations

- Sample data is intentionally small and illustrative  
- Drawdown and risk metrics depend on data availability  
- Tax and transaction cost models are simplified representations  
- This project is a simulation and **not investment advice**

---

## Confidentiality & Usage

This repository is **STRICTLY PRIVATE** and intended solely for evaluation under the Zetheta WorkBridge Project framework.

- No public sharing of code or concepts  
- No redistribution or reuse outside the project scope  
- All intellectual property belongs to Zetheta Algorithms Private Limited  

---

## Execution

Install dependencies:
```bash
pip install -r requirements.txt
