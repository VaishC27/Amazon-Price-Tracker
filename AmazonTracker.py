import requests
from bs4 import BeautifulSoup
import smtplib

YOUR_EMAIL = "vc.nitin.01@gmail.com"
YOUR_PASSWORD = "zqcf ytwb yfsj beip"

PRODUCT_URL = "https://www.amazon.in/Philips-HP8302-Essential-Selfie-Straightener/dp/B00TGXJBNE/ref=sr_1_7?crid=26H3JZ4JIDQZ1&dib=eyJ2IjoiMSJ9.uwO1UV15OsLQnet6lARBsMjE6U4MWKEavsa14RQgtO6WuWboQqqXF_o_rbX5C7EkEN6yC0pUbLw2BJeLOCAdXPDHeYWNVR6ObUn-7b32rCZBB3kvxd89hNML_B-2xhB9kVisVszk2Nyuwc0aNEvZ1qwNdTPacV1agFzCXV2q53UtmtU44cRmy3kdhlwvhqkzRkb84pw1_p2JqTXtadIyMJF3IKUk6PHPxewtEHztBAqtAftVX3PSuOGuydTNSObBf5xa1kgyPRZR81W3lEL7F6wUNMQeLlxrfJouYmFE9Z4.oHziI58vt3kP5JbU-KTf3ltQEa0AIvs8I_TkGaNqqUg&dib_tag=se&keywords=phillips+hair+straightening+brush+with+keratin+infused+bristle&nsdOptOutParam=true&qid=1720449745&sprefix=phillips+%2Caps%2C215&sr=8-7"

headers = {
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
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
