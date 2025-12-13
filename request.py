import requests

url = "http://localhost:8000/ingest"

with open("2025_아주대학교_요람_소프트웨어학과.txt", "r", encoding="utf-8") as f:
    text_data = f.read()

payload = {
    "source": "2025 아주대학교 요람_소프트웨어학과",
    "text": text_data
}

response = requests.post(url, json=payload)
print(response.json())
