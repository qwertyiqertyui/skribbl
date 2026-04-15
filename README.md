# Scribbl Drawing Bot

## Installation
To install the Scribbl Drawing Bot, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/qwertyiqertyui/skribbl.git
   cd skribbl
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To start the Scribbl Drawing Bot, run the following command:
```bash
python scribbl_drawing_bot.py
```
Once the bot is running, it will connect to the Scribbl game server.

## Command Reference
- `/start`: Initializes the bot and connects to the game.
- `/help`: Provides a list of available commands.
- `/stop`: Disconnects the bot from the game.
- `/settings`: Opens the configuration settings for customization.

## Examples
1. **Starting the Bot:**
   ```bash
   python scribbl_drawing_bot.py
   ```
   This will initiate the bot and connect it to the game.

2. **Stopping the Bot:**
   ```bash
   /stop
   ```
   This command will stop the bot.

3. **Adjusting Settings:**
   ```bash
   /settings
   ```
   Use this command to modify your bot settings.

## Configuration
Configuration options can be modified in the `config.json` file. Ensure to define the following fields:
- `token`: Your bot token for authentication.
- `gameUrl`: The URL of the Scribbl game to connect.
- `username`: The desired username for the bot.

## Troubleshooting
- **Bot Not Starting:**  Ensure all dependencies are installed correctly. Check for errors in the console output and resolve them. 
- **Connection Issues:** Verify that you are using the correct game URL and that the server is online.
- **Command Not Recognized:** Make sure you are typing the commands correctly with appropriate permissions.

## Safety Information
Please ensure to use the Scribbl Drawing Bot responsibly:
- Do not use it to disrupt games or harm the experience of other players.
- Always follow the community guidelines of the Scribbl game.
- Report any bugs or issues to the repository's issue tracker to help improve the bot.
