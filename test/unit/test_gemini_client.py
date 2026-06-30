from app.llm.gemini_client import GeminiClient


def main():
    print("=" * 60)
    print("Gemini Client Unit Test")
    print("=" * 60)

    # Initialize client
    client = GeminiClient()

    print("✓ GeminiClient initialized successfully.")

    # Health Check
    print("\nRunning health check...")

    if client.health_check():
        print("✓ Gemini API is available.")
    else:
        print("✗ Gemini API is unavailable.")
        return

    # Generate Response
    print("\nGenerating sample response...")

    response = client.generate(
        system_prompt=(
            "You are a helpful AI assistant."
        ),
        user_prompt=(
            "Reply with exactly one sentence: "
            "'Enterprise AI Agents is ready.'"
        ),
    )

    # Validation
    assert isinstance(response, str), (
        "Response must be a string."
    )

    assert response.strip(), (
        "Response should not be empty."
    )

    print("\nResponse")
    print("-" * 60)
    print(response)
    print("-" * 60)

    print("\n✓ Response validation passed.")

    print("=" * 60)
    print("Gemini Client Test Passed")
    print("=" * 60)


if __name__ == "__main__":
    main()