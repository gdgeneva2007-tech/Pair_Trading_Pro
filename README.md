# Statistical Arbitrage: Pairs Trading (KO & PEP)

## Overview
This project implements a classic Mean-Reversion strategy (Pairs Trading) using Python. It monitors the price ratio between Coca-Cola (KO) and PepsiCo (PEP).

## Logic
- **Z-Score Calculation**: Uses a 30-day rolling window to normalize the price ratio.
- **Trading Signals**: 
  - Sell Ratio (Short KO, Long PEP) when Z-Score > 2.0.
  - Buy Ratio (Long KO, Short PEP) when Z-Score < -2.0.

## Project Structure
- `src/`: Core logic including data processing and signal generation.
- `notebooks/`: Research and data visualization.
- `data/`: Local cache for historical price data.
- `main.py`: Entry point to run the full strategy.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Configure your proxy in `src/utils.py`
3. Run: `python main.py`