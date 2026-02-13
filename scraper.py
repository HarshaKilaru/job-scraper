import requests
import os

def find_jobs():
    # We'll use a very simple query first to see if it works
    query = 'Data Analyst "entry level"'
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('GOOGLE_CX')
    webhook = os.getenv('DISCORD_WEBHOOK')

    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    
    print(f"Triggering search for: {query}")
    res = requests.get(url)
    data = res.json()

    if 'items' in data:
        print(f"Success! Found {len(data['items'])} items.")
        for item in data['items']:
            payload = {"content": f"🎯 **New Job:** {item['title']}\n{item['link']}"}
            requests.post(webhook, json=payload)
    else:
        print("No jobs found. Check if 'Sites to search' are added in Google CSE.")
        print(f"Google Response: {data}") # This will show us the error in GitHub logs

if __name__ == "__main__":
    find_jobs()
