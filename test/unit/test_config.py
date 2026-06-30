from app.utils.config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    DEFAULT_MODEL,
    GEMINI_API_KEY,
)

print(f"Project : {PROJECT_NAME}")
print(f"Version : {PROJECT_VERSION}")
print(f"Model   : {DEFAULT_MODEL}")

if GEMINI_API_KEY:
    print("✅ Gemini API Key Loaded Successfully")
else:
    print("❌ Gemini API Key Not Found")