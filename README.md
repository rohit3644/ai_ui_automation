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
