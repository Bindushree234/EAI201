# youtube_search.py

from browser_use_sdk import BrowserUse

def main():
    # Initialize client with your API key
    client = BrowserUse(api_key="your_api_key_here")

    # Define the browser automation task
    task = """
    1. Open https://www.youtube.com.
    2. Search for "Python programming tutorial".
    3. Click on the first video result.
    4. Provide a short summary including the video title and channel name.
    """

    # Execute the task
    result = client.run(task=task)

    # Print the final summary
    print("=== Final Summary ===")
    print(result.output_text)

    # Print step-by-step summaries
    print("\n=== Step-by-Step Execution ===")
    for idx, step in enumerate(result.steps, start=1):
        print(f"Step {idx}: {step['action']}")
        print(f"Summary: {step['summary']}\n")

if __name__ == "__main__":
    main()
