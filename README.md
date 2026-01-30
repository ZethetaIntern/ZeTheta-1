# Algorithmic Trading Engine  
Project 1A – Zetheta WorkBridge  

## Confidentiality Notice  
This repository contains strictly private and confidential work developed exclusively for **Zetheta Algorithms Private Limited**.  
All code, logic, and implementations are proprietary and must not be shared publicly.  

## Project Summary  
This project implements an end-to-end **algorithmic trading engine** with:  
- Strategy development framework  
- Historical backtesting engine  
- Order management system (OMS)  
- Risk management and capital controls  
- Performance analytics  
- **Live paper trading using CCXT (sandbox mode)**  

The system is designed to mirror real-world trading infrastructure while remaining modular, auditable, and production-oriented.  

## Core Components  
- Strategy Engine (signal generation)  
- Risk Manager (position limits, daily loss kill-switch)  
- Order Management System  
- Execution Engine (CCXT paper trading)  
- Portfolio & PnL tracking  
- Performance metrics (equity, Sharpe, drawdown)  

## Repository Structure  
- config.py  
- data.py  
- strategy.py  
- risk.py  
- oms.py  
- portfolio.py  
- execution.py  
- backtest.py  
- analytics.py  
- live_paper_trading.py  

## How to Run  
```bash
pip install -r requirements.txt
python live_paper_trading.py

```bash
pip install -r requirements.txt
python live_paper_trading.py
