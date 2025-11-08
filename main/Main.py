import csv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import time

# --- Configuration ---
# 🚨 WARNING: REPLACE 'xoxb-YOUR-TOKEN-HERE' WITH YOUR ACTUAL SLACK BOT TOKEN 🚨
# This is less secure than using environment variables.
SLACK_TOKEN = "xoxb-you-bot-token"

# Name for the output CSV file
CSV_FILE_NAME = "slack_public_channels_details.csv"

def get_public_channels_details_and_export():
    """
    Fetches public channels' Name, ID, and Member Count, 
    prints progress, and exports to CSV.
    """
    if SLACK_TOKEN == "xoxb-YOUR-TOKEN-HERE":
        print("🛑 ERROR: Please replace 'xoxb-YOUR-TOKEN-HERE' with your actual Slack Bot Token.")
        return

    # Initialize the Slack WebClient
    client = WebClient(token=SLACK_TOKEN)
    channel_list_data = []
    cursor = None
    page_count = 0

    print("🚀 Starting to fetch public channels...")
    
    try:
        while True:
            page_count += 1
            print(f"\n--- Fetching Page {page_count} of channels from Slack API... ---")

            # 1. Call the conversations.list API method
            response = client.conversations_list(
                types="public_channel",
                exclude_archived=True,
                limit=200, 
                cursor=cursor
            )
            
            # 2. Extract the required data from the response and print progress
            channels_on_page = response.data.get('channels', [])
            
            for channel in channels_on_page:
                channel_name = channel.get('name')
                
                # Progress Output
                print(f"   [+] Processing #{channel_name}") 
                
                channel_list_data.append([
                    channel_name,           # Channel Name
                    channel.get('id'),      # Channel ID
                    channel.get('num_members', 0)  # Member Count
                ])

            # 3. Handle Pagination
            cursor = response.data.get('response_metadata', {}).get('next_cursor')

            if not cursor:
                # No more pages to fetch
                break
            
            # 4. Wait to respect Slack's rate limits
            time.sleep(1) 

        # --- Write to CSV File ---
        
        # Check if any data was collected before attempting to write
        if not channel_list_data:
            print("\n⚠️ Warning: Found zero public channels. Check your token scopes and workspace membership.")
            return

        print(f"\nTotal Channels Found: {len(channel_list_data)}")
        
        with open(CSV_FILE_NAME, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write header row
            writer.writerow(['Channel Name', 'Channel ID', 'Member Count']) 
            # Write all channel data rows
            writer.writerows(channel_list_data)

        print(f"\n✅ Success! Channel details exported to **{CSV_FILE_NAME}**")

    except SlackApiError as e:
        print(f"\n❌ Slack API Error ({e.response.get('error')}):")
        print("HINT: Ensure your bot token has the **'channels:read'** scope.")
        print(f"Full Error: {e.response}")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    get_public_channels_details_and_export()