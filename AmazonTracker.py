import requests
from bs4 import BeautifulSoup
import smtplib

YOUR_EMAIL = "your_email@gmail.com"
YOUR_PASSWORD = "your_email_password"
PRODUCT_URL = "https://www.amazon.in/your-product-url"

headers = {
    "You'll need to pass along some headers in order for the request to return the actual website HTML. At minimum you'll need to give your "User-Agent" and "Accept-Language" values in the request header."
    "You can see your browser headers by going to this website: 'http://myhttpheader.com/' "
    
}

response = requests.get(PRODUCT_URL, headers=headers)

# If the request was successful, parse the page
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Try to find the price element
    price_element = soup.find(class_="a-offscreen")

    if price_element:
        price = price_element.get_text()
        # Assuming the price is in Indian Rupees format: ₹1,999.00
        price_without_currency = price.replace("₹", "").replace(",", "").strip()
        price_as_float = float(price_without_currency)
        print(price_as_float)
    else:
        print("Price element not found")
        price_as_float = None  # Set to None to handle in later logic

    # Try to find the product title
    title_element = soup.find(id="productTitle")
    if title_element:
        title = title_element.get_text().strip()
        print(title)
    else:
        print("Product title not found")
        title = "Unknown Product"  # Fallback title
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    price_as_float = None  # Set to None to handle in later logic
    title = "Unknown Product"  # Fallback title

BUY_PRICE = 1140

if price_as_float is not None and price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRODUCT_URL}".encode("utf-8")
        )
