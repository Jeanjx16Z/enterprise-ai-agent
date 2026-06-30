from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# ==========================
# Project Configuration
# ==========================

PROJECT_NAME = "Enterprise AI Agents"
PROJECT_VERSION = "0.1.0"

# ==========================
# Gemini Configuration
# ==========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"

# ==========================
# Output Directories
# ==========================

REPORT_OUTPUT_DIR = "data/output/reports"
JSON_OUTPUT_DIR = "data/output/json"