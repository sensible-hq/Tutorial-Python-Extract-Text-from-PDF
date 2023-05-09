import json
import requests

URL = "https://api.sensible.so/v0/extract/invoices?environment=development"
# Your pdf file path
DOCUMENT_PATH = "test.pdf"
# Your Sensible API key
SENSIBLE_API_KEY = "INSERT YOUR KEY HERE"

headers = {
     'Authorization': 'Bearer {}'.format(SENSIBLE_API_KEY),
    'Content-Type': 'application/pdf'
}
with open(DOCUMENT_PATH, 'rb') as pdf_file:
    body = pdf_file.read()
response = requests.request(
    "POST",
    URL,
    headers=headers,
    data=body)
try:
    response.raise_for_status()
except requests.RequestException:
    print(response.text)
else:
    print(json.dumps(response.json(), indent=2))