# Quantitative Risk Dashboard  
### Strategy Evaluation & Risk Analytics Platform  
**Project 1C – Zetheta WorkBridge**

---

## Overview

This project implements a quantitative strategy evaluation and comparison platform designed to simulate real-world risk analytics workflows within the BFSI domain.

The dashboard enables rigorous evaluation of multiple trading strategies using statistical performance testing, risk diagnostics, correlation analysis, regime segmentation, and capacity estimation.

The objective is to move beyond simple backtesting metrics and introduce statistical validation and practical constraints into strategy assessment.

---

## Core Features

### 1. Performance Metrics
- Annualized Return
- Annualized Volatility
- Sharpe Ratio (annualized)
- Max Drawdown

### 2. Sharpe Ratio Significance Testing
Implements an approximate Jobson–Korkie style statistical test:

\[
Z = \frac{Sharpe}{\sqrt{(1 + 0.5 \cdot Sharpe^2)/T}}
\]

Outputs:
- Z-statistic
- Two-sided p-value

This evaluates whether the observed Sharpe ratio is statistically different from zero.

---

### 3. Correlation Analysis
- Full strategy correlation matrix
- Diversification insight
- Heatmap visualization

---

### 4. Drawdown Analytics
- Equity curve computation
- Peak tracking
- Drawdown series
- Maximum drawdown extraction

\[
Drawdown_t = \frac{Equity_t - Peak_t}{Peak_t}
\]

---

### 5. Regime-Based Performance
Market regimes are classified using rolling mean of market returns:

- Bull regime → positive rolling mean
- Bear regime → negative rolling mean

Strategy returns are evaluated separately under each regime.

---

### 6. Capacity Estimation

Estimated using:

\[
Capacity = \frac{ADV \times ParticipationRate}{Turnover}
\]

Where:
- ADV = Average Daily Volume
- ParticipationRate = assumed liquidity fraction (default 5%)
- Turnover = capital turnover assumption

This introduces realistic scalability constraints.

---

### 7. Strategy Ranking Engine

Strategies are ranked using a composite score:
This penalizes excessive drawdowns while rewarding risk-adjusted returns.


---

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv

## Installation & Run

Follow the steps below to set up and run the project locally.

### 1️⃣ Create a Virtual Environment

```bash
python -m venv .venv

2️⃣ Activate the Environment

Windows (CMD):

.venv\Scripts\activate

Windows (PowerShell):

.venv\Scripts\Activate.ps1

Mac / Linux:

source .venv/bin/activate

3️⃣ Upgrade pip
python -m pip install --upgrade pip

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run the Dashboard
streamlit run dashboard/app.py

The application will launch at:
http://localhost:8501