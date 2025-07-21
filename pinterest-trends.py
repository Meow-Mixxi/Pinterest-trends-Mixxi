# pinterest_trends.py

import requests
import json

# --- Configuration ---
# IMPORTANT: KEEP THIS AS A PLACEHOLDER IN GITHUB
ACCESS_TOKEN = "YOUR_PINTEREST_ACCESS_TOKEN" 

# --- FILTERS ---
# Set the region. Examples: "US", "CA", "GB", "DE", "FR"
REGION = "US" 

# Set the time frame. Options: "trending", "growing", "monthly", "yearly"
TIME_FRAME = "monthly" 

# --- Main Functions ---

def get_filtered_trends(token, region, time_frame):
    """
    Calls the Pinterest API to get a list of trending keywords
    based on a specific region and time frame.
    """
    url = f"https://api.pinterest.com/v5/trends/trending?region={region}&trend_type={time_frame}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    print(f"Fetching '{time_frame}' trends for region: '{region}'...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Successfully fetched trends!")
        data = response.json()
        keywords = [trend['keyword'] for trend in data.get('trends', [])]
        return keywords
    else:
        print(f"Error fetching trends: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def search_for_pins(token, keyword, limit=5):
    """
    Searches for the top Pins related to a specific keyword.
    """
    url = f"https://api.pinterest.com/v5/search/pins?query={keyword}&limit={limit}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    print(f"\nSearching for Pins with keyword: '{keyword}'...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Successfully fetched Pins!")
        return response.json().get('items', [])
    else:
        print(f"Error searching for pins: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def main():
    """
    Main function to run the bot.
    """
    if ACCESS_TOKEN == "YOUR_PINTEREST_ACCESS_TOKEN":
        print("ERROR: Please replace 'YOUR_PINTEREST_ACCESS_TOKEN' with your actual token on your local machine before running.")
        return

    trending_keywords = get_filtered_trends(ACCESS_TOKEN, REGION, TIME_FRAME)
    
    if trending_keywords:
        print(f"\n--- Top 10 Keywords for {REGION} ({TIME_FRAME}) ---")
        for i, keyword in enumerate(trending_keywords[:10]):
            print(f"{i+1}. {keyword}")
            
        top_trend = trending_keywords[0]
        pins = search_for_pins(ACCESS_TOKEN, top_trend)
        
        if pins:
            print(f"\n--- Top 5 Pins for '{top_trend}' ---")
            for pin in pins:
                pin_id = pin.get('id')
                pin_link = f"https://www.pinterest.com/pin/{pin_id}/"
                pin_title = pin.get('title', 'No Title')
                print(f"  - Title: {pin_title}")
                print(f"    Link: {pin_link}\n")

if __name__ == "__main__":
    main()
