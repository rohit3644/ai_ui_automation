## Running the Browser Use Application Using Docker

### Prerequisites
- Ensure Docker is installed on your system.

### Steps

1. **Clone the repository:**
    ```sh
    git clone https://github.com/rohit3644/ai_ui_automation.git
    ```

2. **Navigate to the `browser-use` directory:**
    ```sh
    cd browser-use
    ```

3. **Create a `.env` file and add `OPENAI_API_KEY` and `IS_PROD` variables:**
    ```sh
    touch .env
    echo "OPENAI_API_KEY=your_openai_api_key" >> .env
    echo "IS_PROD='True'" >> .env
    ```

4. **Build the Docker containers:**
    ```sh
    sudo docker compose build
    ```

5. **Run the application using Docker:**
    ```sh
    sudo docker compose run --rm -it app
    ```

6. **Follow the prompt to enter the task you want to perform.**



### Passing sensitive data

```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent

load_dotenv()

# Initialize the model
llm = ChatOpenAI(
    model='gpt-4o',
    temperature=0.0,
)

# Define sensitive data
# The model will only see the keys (x_name, x_password) but never the actual values
sensitive_data = {'x_name': 'magnus', 'x_password': '12345678'}

# Use the placeholder names in your task description
task = 'go to x.com and login with x_name and x_password then write a post about the meaning of life'

# Pass the sensitive data to the agent
agent = Agent(task=task, llm=llm, sensitive_data=sensitive_data)

async def main():
    await agent.run()

if __name__ == '__main__':
    asyncio.run(main())
```