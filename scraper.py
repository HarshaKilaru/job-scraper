import requests
import os

def find_jobs():
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('GOOGLE_CX')
    webhook = os.getenv('DISCORD_WEBHOOK')
    
    # Very broad search to guarantee results for our test
    query = '"Data Analyst" OR "Software Engineer"'

    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    
    print("Testing connection to Google...")
    res = requests.get(url)
    data = res.json()

    if 'items' in data:
        print(f"SUCCESS! Found {len(data['items'])} jobs.")
        for item in data['items']:
            payload = {"content": f"🎯 **Job Found:** {item['title']}\n{item['link']}"}
            requests.post(webhook, json=payload)
    else:
        print("API connected, but no results found. Check your 'Sites to search' in Google CSE.")
        print(f"Debug Info: {data}")

if __name__ == "__main__":
    find_jobs()
