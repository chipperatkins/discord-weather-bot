# Discord Weather Bot

Discord Weather Bot is a powerful bot that integrates real-time weather data from the National Weather Service (NWS) with the AI capabilities of ChatGPT to provide custom weather forecasts. The bot is built to cater to specific requests and provides detailed weather updates via a Discord bot account.

## Features

- **Real-time Weather Data:** The bot scrapes weather data from the National Weather Service to ensure that all forecasts are accurate and up-to-date.
- **Custom Forecasts:** By feeding the real-time data to ChatGPT, the bot can generate detailed and custom weather forecasts tailored to the user's needs.
- **Discord Integration:** Users can interact with the bot on Discord to receive weather updates, ask for custom forecasts, and more.

## Installation
### Option 1: Using Docker (Preferred)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/discord-weather-bot.git
   cd discord-weather-bot
   ```

2. **Build the Docker image:**

   Run the following command to build the Docker image:

   ```bash
   docker build -t discord-weather-bot .
   ```

3. **Set up your environment variables:**

   The application uses environment variables at run-time to store your Discord bot token and OpenAI API token. One way to ensure these are set at runtime is with a custom docker compose.secret.yml file that can be merged into the docker compose config. 

   ```yaml
      services:
        weather-willie-discord-bot:
            environment:
            BOT_TOKEN: <TOKEN>
            OPENAI_API_KEY: <TOKEN> 
   ```
   ```bash
    docker compose -f compose.yml -f compose.secret.yml up
   ```

4. **Run the bot using Docker Compose:**

   Use Docker Compose to start the bot:

   ```bash
   docker compose up
   ```

   The `compose.yml` file and `dockerfile` are configured to set up the bot and its dependencies automatically.

Using Docker simplifies the process of managing dependencies and ensures the bot runs consistently across different environments.

### Option 2: Manual Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/discord-weather-bot.git
   cd discord-weather-bot
   ```

2. **Install the necessary dependencies:**

   Ensure you have Node.js and npm installed, then run:

   ```bash
   npm install
   ```

3. **Set up your environment variables:**

   Create a `.env` file in the root directory with your Discord bot token:

   ```bash
   BOT_TOKEN=<YOUR_TOKEN>
   OPENAI_API_KEY=<YOUR_API_KEY>
   ```

4. **Install Python dependencies:**

   Ensure you have Python installed on your system. Then, you can install the required Python libraries by running:

   ```bash
   pip install requests matplotlib numpy pandas beautifulsoup4 openai
   ```

   These dependencies are used in the Python scripts to handle weather data scraping, processing, and interaction with the OpenAI API.

5. **Run the bot:**

   Start the bot by running:

   ```bash
   node index.js
   ```

## Usage

### Commands

The bot responds to specific commands in Discord. Below are some of the key commands:

1. **Weather Update:**

   - Command: `/weather-update`
   - Description: Replies with a custom weather update based on your input.
   - Example Usage: `/weather-update 15:00`
   - How it Works: The bot prompts ChatGPT to generate a weather forecast for the specified time using real-time data scraped from NWS.

2. **Mention-Based Interaction:**

   - Trigger: Mention the bot in any message.
   - How it Works: When mentioned, the bot will respond with a custom weather forecast or general response, depending on the content of the message.

### Cooldown

To avoid spamming, a cooldown period of 60 seconds is enforced between commands per user. If a user tries to execute a command before the cooldown period ends, they will be notified of the remaining wait time.

## File Structure

- **discord-bot/index.js:** The main entry point for the bot. It initializes the bot, loads commands, and sets up event listeners for Discord interactions.
- **discord-bot/events/messageCreate.js:** Handles the `messageCreate` event, where the bot processes direct mentions and user messages.
- **discord-bot/commands/utility/weatherUpdate.js:** Defines the `/weather-update` command, allowing users to request weather forecasts for specific times.
- **chatGPTIntegration.py:** Contains Python code that interacts with ChatGPT to generate responses based on the weather data, using libraries such as `requests`, and `openai`.
- **chatGTPUtil.js:** Contains the node javascript utility function for spawning a python process for the python data scrapeing and OpenAI integration.

## Contributing

Contributions are welcome! Please submit a pull request with any changes or improvements.

## License

This project is licensed under the  GNU GENERAL PUBLIC LICENSE Version 3.