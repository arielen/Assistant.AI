# Assistant.AI

Welcome to **Assistant.AI** - a cutting-edge personal assistant that is revolutionizing the way you interact with information on the web. Powered by advanced artificial intelligence technology and directly integrated with OpenAI, Assistant.AI goes beyond simply delivering search results. It understands and interprets user queries in real-time, providing precise and contextualized answers that cater to your specific needs.

## Features
- Real-Time Interaction: Get instant, contextualized answers to your questions without the need for manual search.
- AI-Powered Responses: Leverage the power of OpenAI to receive intelligent and meaningful responses.
- Customizable Experience: Tailor the assistant's responses by configuring environment variables to suit your preferences.

## Project Configuration

Follow these steps to set up and run **Assistant.AI** on your local machine.

### Prerequisites

- Python 3.8 or higher.
- A valid API key from Serper.dev and OpenAI Platform.

### Setup Instructions

1. **Cloning the Repository**
    
    Start by cloning the Assistant.AI repository to your local machine using the following command:

    ```bash
    git clone https://github.com/arielen/Assistant.AI.git
    cd Assistant.AI
    ```

2. **Configuring Environment Variables**

    To configure the environment variables:

    - Duplicate the `.env.example` file in the root directory and rename the copy to `.env`.

    - Open the `.env` file and fill in the required environment variables as follows:
        
        - `SERVER_API_DEV`: Obtain this API key for free from [Serper.dev](https://serper.dev/).
        - `OPEN_API_KEY`: Generate an API key from [OpenAI Platform](https://platform.openai.com/api-keys).
        
    This configuration ensures that Assistant.AI can securely connect to the necessary external services.

3. **Installing Dependencies**

    Install the required dependencies by running the following command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```
    
    This will install all the necessary Python packages to run Assistant.AI.

## Running the Project

With the environment variables configured and dependencies installed, you can start the Assistant.AI project by navigating to the project directory and executing:

```bash
python main.py
```

## Using Assistant.AI

Once the project is up and running, you can interact with Assistant.AI directly through your terminal:

- **Ask Questions**: Simply type your question, and Assistant.AI will provide you with the best possible answer.
- **End the Session**: To exit the program, type `exit`.

## Troubleshooting

- **Connection Issues**: If you encounter issues connecting to the API, double-check the API keys in your `.env` file and ensure your internet connection is stable.
- **Dependency Errors**: Ensure that all dependencies are properly installed by re-running `pip install -r requirements.txt`.
