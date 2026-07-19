

from google import genai

API_KEY = "AQ.A/b8RN6I1kugNIAw1QRErnnTEQEV9hdx_jYBRrXK69fTsA4Cttw"
client = genai.Client(api_key=API_KEY)

models = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.5-pro",
    "gemini-2.0-flash",
    "gemini-flash-latest",
]

for model in models:
    print(f"\nTesting: {model}")
    try:
        response = client.models.generate_content(
            model=model,
            contents="Reply with only: OK",
        )
        print("✅ Supported")
        print(response.text)
    except Exception as e:
        print(f"❌ {e}")