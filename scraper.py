import requests
import os
from datetime import datetime

# Grab your secret keys from GitHub environment
WEBHOOK_URL = os.getenv('https://discord.com/api/webhooks/1471665117505650780/yKyTfjWGb-zVFwdNgy4WAZOjRGB5jO6SEB237aWCch-tHuHLtodeRJ9YEIaMHKxlajRw')
API_KEY = os.getenv('AIzaSyA3AUpZAajjgoV69-5ifxJAECMM5kZrqfA')
CX = os.getenv('<script async src="https://cse.google.com/cse.js?cx=36373a8cb3b41415f">
</script>
<div class="gcse-search"></div>
')

def find_jobs():
    # Tailored query for 0-5 years exp in the US
    queries = [
        'intitle:"Data Analyst" "5 years" OR "entry level" -senior -sr site:lever.co OR site:greenhouse.io',
        'intitle:"Software Engineer" "junior" OR "associate" -senior site:workday.com'
    ]
    
    for q in queries:
        # gl=us restricts to USA; sort=date ensures newest first
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={q}&gl=us&sort=date"
        data = requests.get(url).json()
        
        if 'items' in data:
            for item in data['items']:
                send_to_discord(item['title'], item['link'])

def send_to_discord(title, link):
    payload = {
        "embeds": [{
            "title": title,
            "url": link,
            "color": 5814783,
            "footer": {"text": "Job found via Google API"}
        }]
    }
    requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    find_jobs()
