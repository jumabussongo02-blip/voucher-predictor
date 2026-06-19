# Voucher Code Predictor

Predicts valid telecom voucher codes for networks like Vodacom, Airtel, YAS.

## Features
- Web scraping
- ML prediction
- REST API

## Setup
```bash
git clone https://github.com/username/voucher-predictor.git
cd voucher-predictor
pip install -r requirements.txt


## 5. Add Git Ignore

Create `.gitignore`:

## 6. Create Base Scripts

Create `scripts/collect_data.py`:
```python
import requests
from bs4 import BeautifulSoup

def scrape_codes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return [code.text for code in soup.find_all('div', class_='voucher-code')]
