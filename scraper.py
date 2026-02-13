import requests
import os

def find_jobs():
    api_key = os.getenv('GOOGLE_API_KEY')
    cx = os.getenv('GOOGLE_CX')
    webhook = os.getenv('DISCORD_WEBHOOK')
    
    # Simple query to test the new "Sites to Search" configuration
    query = 'Data Analyst' 

    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    
    print(f"Testing search with CX: {cx}")
    res = requests.get(url)
    data = res.json()

    if 'items' in data:
        print(f"SUCCESS! Found {len(data['items'])} jobs.")
        for item in data['items']:
            # Send to Discord
            requests.post(webhook, json={"content": f"🚀 **Job found:** {item['title']}\n{item['link']}"})
    else:
        print("STILL NO JOBS. Here is the exact response from Google:")
        print(data) # This will show us the specific error in GitHub Actions

if __name__ == "__main__":
    find_jobs()
