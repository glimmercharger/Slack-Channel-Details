# Slack Channel Details Exporter

A Python tool that exports comprehensive details about all public Slack channels in your workspace to a CSV file. Perfect for workspace auditing, analytics, and reporting.

## 📋 Overview

This tool uses the Slack Web API to fetch information about all public channels in your workspace and exports it to a structured CSV file. The exported data includes:

- **Channel Name** - The human-readable name of each channel
- **Channel ID** - The unique identifier for each channel
- **Member Count** - The total number of members in each channel

## ✨ Features

- 🚀 **Fast & Efficient**: Uses pagination to handle workspaces with hundreds of channels
- 📊 **CSV Export**: Creates a clean, easy-to-analyze CSV file
- 🔄 **Rate Limit Aware**: Automatically respects Slack API rate limits
- 🎯 **Public Channels Only**: Focuses on public channels, excludes archived channels
- 📝 **Progress Tracking**: Real-time console output showing which channels are being processed
- ⚠️ **Error Handling**: Clear error messages with helpful troubleshooting hints

## 🔧 Prerequisites

- Python 3.6 or higher
- A Slack workspace where you have permissions to create apps/bots
- A Slack Bot Token with the required permissions

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/glimmercharger/Slack-Channel-Details.git
   cd Slack-Channel-Details
   ```

2. **Install the required dependencies:**
   ```bash
   pip install slack_sdk
   ```

## 🔑 Slack Bot Setup

### 1. Create a Slack App

1. Go to [https://api.slack.com/apps](https://api.slack.com/apps)
2. Click **"Create New App"**
3. Choose **"From scratch"**
4. Enter an app name (e.g., "Channel Details Exporter")
5. Select your workspace
6. Click **"Create App"**

### 2. Add Bot Token Scopes

1. In your app settings, navigate to **"OAuth & Permissions"**
2. Scroll down to **"Scopes"** → **"Bot Token Scopes"**
3. Add the following scope:
   - `channels:read` - View basic information about public channels

### 3. Install the App to Your Workspace

1. Navigate to **"OAuth & Permissions"**
2. Click **"Install to Workspace"**
3. Review the permissions and click **"Allow"**
4. Copy the **"Bot User OAuth Token"** (starts with `xoxb-`)

## ⚙️ Configuration

1. Open `main/Main.py` in a text editor
2. Replace the placeholder token with your actual bot token:
   ```python
   SLACK_TOKEN = "xoxb-your-actual-bot-token-here"
   ```
3. (Optional) Customize the output filename:
   ```python
   CSV_FILE_NAME = "slack_public_channels_details.csv"
   ```

> **⚠️ Security Note**: For production use, consider using environment variables instead of hardcoding your token:
> ```python
> import os
> SLACK_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
> ```

## 🚀 Usage

Run the script from the repository root:

```bash
python main/Main.py
```

### Expected Output

```
🚀 Starting to fetch public channels...

--- Fetching Page 1 of channels from Slack API... ---
   [+] Processing #general
   [+] Processing #random
   [+] Processing #announcements
   ...

Total Channels Found: 42

✅ Success! Channel details exported to **slack_public_channels_details.csv**
```

### Output File Format

The generated CSV file will have the following structure:

```csv
Channel Name,Channel ID,Member Count
general,C01234ABCDE,150
random,C01234FGHIJ,98
announcements,C01234KLMNO,203
```

## 🔍 Troubleshooting

### Error: "Please replace 'xoxb-YOUR-TOKEN-HERE' with your actual Slack Bot Token"
- You forgot to update the `SLACK_TOKEN` variable with your actual bot token

### Error: "Ensure your bot token has the 'channels:read' scope"
- Your bot doesn't have the required permissions
- Go back to **OAuth & Permissions** in your Slack app settings and add the `channels:read` scope
- Reinstall the app to your workspace

### Warning: "Found zero public channels"
- Check if your bot token is valid
- Verify that your workspace has public channels
- Ensure the bot has been installed to your workspace

### Rate Limit Errors
- The script includes a 1-second delay between API calls to respect rate limits
- If you still encounter rate limit errors, increase the `time.sleep(1)` value in the code

## 📊 Use Cases

- **Workspace Audits**: Get a complete inventory of all public channels
- **Analytics**: Analyze channel membership patterns and engagement
- **Reporting**: Create reports on workspace structure for management
- **Cleanup**: Identify underutilized channels for potential archival
- **Migration**: Prepare channel data for workspace migrations

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs by opening an issue
- Suggest new features
- Submit pull requests with improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Created by [Will](https://github.com/glimmercharger)

## 🙏 Acknowledgments

- Built with the [Slack SDK for Python](https://github.com/slackapi/python-slack-sdk)
- README remake by GitHub Copilot

---

**Note**: This tool only accesses public channel information and does not read any message content. It respects user privacy and Slack's API guidelines.
