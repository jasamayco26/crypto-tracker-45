# crypto-tracker-45

Crypto-tracker-45 is a high-performance Python utility designed to monitor real-time cryptocurrency price fluctuations and portfolio valuation. It leverages asynchronous API calls to provide low-latency market data for traders who require immediate insights into their asset performance.

## Features

*   **Multi-Exchange Support:** Fetch live pricing data from major exchanges like Binance, Coinbase, and Kraken via a unified interface.
*   **Asynchronous Processing:** Utilizes `aiohttp` and `asyncio` to handle concurrent API requests, ensuring minimal impact on system resources.
*   **Portfolio Tracking:** Automatically calculates total net worth and individual asset gains based on user-defined holdings.
*   **Alerting System:** Configure custom price thresholds to receive console notifications when target market values are hit.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/crypto-tracker-45.git
cd crypto-tracker-45
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Initialize the tracker by creating a `config.json` file with your preferred assets, then run the monitoring engine:

```bash
# Example command to start the tracker
python main.py --config config.json --interval 60
```

The application will output real-time updates to your terminal. To generate a summary report of your current portfolio, use the `--report` flag:

```bash
python main.py --report --format csv
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.