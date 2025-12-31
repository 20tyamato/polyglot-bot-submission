# Polyglot Discord Translator Bot

- [English](README.md)
- [Japanese](README.jp.md)

## Overview

Polyglot is an AI-powered Discord bot that provides seamless translation between English and Japanese using OpenAI's API. The bot enables users to translate messages directly within Discord by simply replying to messages with a translation command.

## Features

- Quick translation between English and Japanese
- Reply-based command interface for intuitive use
- Thread creation for organized translations
- Support for formatting preservation in translated text (bold, italic, mentions)
- Health monitoring system for reliability

## Setup

1. Clone this repository

   ```bash
   git clone https://github.com/20tyamato/polyglot-bot-submission.git polyglot-bot
   cd polyglot-bot
   ```

2. Install required packages

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with the following environment variables:

   ```plain
   OPENAI_AI_MODEL="gpt-5.2-2025-12-11"
   DISCORD_TOKEN=your_discord_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Create a Discord bot through the Discord Developer Portal
   - Go to `https://discord.com/developers/applications`
   - Create a new application
   - Go to the "Bot" tab and create a bot
   - Enable "MESSAGE CONTENT INTENT"
   - Copy the bot token and add it to your `.env` file using `.env.example` as a template

5. Invite the bot to your server
   - Go to "OAuth2" > "URL Generator"
   - Select "bot" scope
   - Select required permissions:
     - Read Messages/View Channels
     - Send Messages
     - Create Public Threads
     - Send Messages in Threads
   - Use the generated URL to invite the bot to your server

## Usage

1. Start the bot

   ```bash
   python src/main.py
   ```

2. In your Discord server, reply to any message you want to translate
   - For English to Japanese: Reply with `@translator jp`
   - For Japanese to English: Reply with `@translator en`

3. The bot will create a thread with the translation result

## Command Reference

- `@translator en` - Translate to English 🇬🇧
- `@translator jp` - Translate to Japanese 🇯🇵
- `!introduce` - Display the bot's introduction and usage instructions

## Examples

1. User 1 sends a message: "こんにちは、元気ですか？"
2. User 2 replies to that message with: `@translator en`
3. The bot creates a thread with the translation: "Hello, how are you?"

## Troubleshooting

- **Bot doesn't respond**: Verify that the bot is running and has the correct permissions
- **Translation errors**: Check if your OpenAI API key is valid and that you haven't exceeded API rate limits
- **"I don't have permission to read messages" error**: Ensure the bot has the necessary permissions in your Discord server
- **Empty translation results**: This may happen if OpenAI's API fails to process the request; try again later

## Important Notes

- This bot uses OpenAI's API, which may incur usage charges
- Keep your API keys secure and never commit them to public repositories
- The bot has a message length limit of 4000 characters for translation

## License

Released under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
