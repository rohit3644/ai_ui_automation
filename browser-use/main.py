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
    if os.getenv("IS_PROD") == "True":
        browser = Browser(
            config=BrowserConfig(
                headless=True
            )
        )
    else:
        browser = Browser(
            config=BrowserConfig(
                headless=False
            )
        )
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model="gpt-4o-mini"),
        browser=browser
    )
    result = await agent.run()
    # Uncomment the line below to print the result if needed
    # print(result)

@time_it
def start_task_execution(task):
    loop = asyncio.new_event_loop()  # Create a new event loop
    asyncio.set_event_loop(loop)  # Set it as the current event loop
    loop.run_until_complete(main(task))  # Run the coroutine
    

if __name__ == "__main__":
    user_task = input("Enter the task you want to perform: ")  # Take task input from the user
    start_task_execution(user_task)
