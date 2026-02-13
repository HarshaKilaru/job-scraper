import requests
import os

# Ensure these match your GitHub Secret names exactly
WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK')
API_KEY = os.getenv('GOOGLE_API_KEY')
CX = os.getenv('GOOGLE_CX')

def find_jobs():
    # Focused search for 0-5 years exp in the US
    # We use boolean operators: OR to expand, minus (-) to exclude
    queries = [
        'intitle:"Data Analyst" "5 years" OR "entry level" -senior -sr site:lever.co OR site:greenhouse.io',
        'intitle:"Software Engineer" "junior" OR "associate" -senior site:workday.com',
        'intitle:"Data Engineer" "entry level" OR "junior" -senior site:lever.co',
        'intitle:"Data Scientist" "entry level" OR "junior" -senior site:greenhouse.io'
    ]
    
    for q in queries:
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={q}&gl=us&sort=date"
        try:
            res = requests.get(url)
            data = res.json()
            
            if 'items' in data:
                for item in data['items']:
                    send_to_discord(item['title'], item['link'])
        except Exception as e:
            print(f"Error searching {q}: {e}")

def send_to_discord(title, link):
    # One last safety check to skip senior roles
    if "senior" in title.lower() or "sr." in title.lower():
        return

    payload = {
        "embeds": [{
            "title": title,
            "url": link,
            "color": 5814783,
            "footer": {"text": "New Job Found"}
        }]
    }
    requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    find_jobs()
