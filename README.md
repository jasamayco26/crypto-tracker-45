# crypto-tracker-45

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

crypto-tracker-45 is a Python command-line tool for real-time cryptocurrency price monitoring and portfolio management. It retrieves live market data from public APIs and helps users stay informed about price changes without requiring external accounts or paid services.

## Features

- Real-time price updates and 24h percentage changes via the CoinGecko API
- Local portfolio tracking with automatic USD valuation across multiple assets
- Configurable price alerts that trigger on user-defined percentage thresholds
- Export price history and portfolio snapshots to CSV format

## Installation

```bash
git clone https://github.com/Developer/crypto-tracker-45.git
cd crypto-tracker-45
pip install -r requirements.txt
```

## Basic Usage

Track live prices:

```bash
python crypto_tracker.py --coins BTC ETH SOL
```

View portfolio value:

```bash
python crypto_tracker.py --portfolio
```

Set a price alert:

```bash
python crypto_tracker.py --alert BTC 5
```

## License

MIT License