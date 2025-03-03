from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
import time, os
from dotenv import load_dotenv
load_dotenv()

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        time_taken = end_time - start_time  # Calculate time taken
        print(f"Function '{func.__name__}' took {time_taken:.2f} seconds to execute.")
        return result
    return wrapper

async def main(task):
    import requests

    ANCHOR_API_KEY = os.getenv("ANCHOR_API_KEY")

    response = requests.post(
        "https://api.anchorbrowser.io/api/sessions",
        headers={
            "anchor-api-key": ANCHOR_API_KEY,
            "Content-Type": "application/json",
        },
        json={
        "headless": False, # Use headless false to view the browser when combining with browser-use
        }).json()

    browser = Browser(
        config=BrowserConfig(
            headless=True if os.getenv("IS_PROD") == "True" else False,
            cdp_url=f"wss://connect.anchorbrowser.io?apiKey={ANCHOR_API_KEY}&sessionId={response['id']}"
        )
    )
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model="gpt-4o-mini"),
        browser=browser
    )
    result = await agent.run()
    # Uncomment the line below to print the result if needed
    print(result.errors())

@time_it
def start_task_execution(task):
    loop = asyncio.new_event_loop()  # Create a new event loop
    asyncio.set_event_loop(loop)  # Set it as the current event loop
    loop.run_until_complete(main(task))  # Run the coroutine
    

if __name__ == "__main__":
    user_task = input("Enter the task you want to perform: ")  # Take task input from the user
    start_task_execution(user_task)
