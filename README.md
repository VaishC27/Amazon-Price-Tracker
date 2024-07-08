# 📉 Amazon Price Tracker 📬

This project tracks the price of a specified Amazon product and sends an email alert when the price drops below a defined threshold.

## ✨ Features

- 🕵️‍♂️ Scrapes the price of an Amazon product using BeautifulSoup.
- 📧 Sends an email alert when the product price drops below a specified amount.
- 🌐 Uses `requests` for fetching the Amazon product page.
- ✉️ Uses `smtplib` for sending email notifications.

## 🛠️ Prerequisites

- 🐍 Python 3.x
- 📦 Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `smtplib` (standard library, no need to install)

## 📥 Installation

1. 📂 Clone the repository:

```bash
git clone https://github.com/yourusername/amazon-price-tracker.git
cd amazon-price-tracker
```

2. 📦 Install the required packages:

```bash
pip install requests beautifulsoup4
```

## 🚀 Usage

1. ✏️ Update your email credentials and product URL in the script:

```python
YOUR_EMAIL = "your_email@gmail.com"
YOUR_PASSWORD = "your_email_password"
PRODUCT_URL = "https://www.amazon.in/your-product-url"
```

2. ▶️ Run the script:

```bash
AmazonTracker.py
```
