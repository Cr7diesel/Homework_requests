import requests
from datetime import datetime


def get_questions(tag, days):

    end_day = int(datetime.timestamp(datetime.now()))
    today = end_day - days * 86400

    url = 'https://api.stackexchange.com/2.3/questions'

    params = {
        'fromdate': today,
        'todate': end_day,
        'tagged': tag,
        'site': 'stackoverflow'
    }

    response = requests.get(url=url, params=params)

    for question in response.json().get('items'):
        print(f"Question: {question['title']}\nTag: {str(question['tags'])}"
              if tag.lower() in str(question['tags']) else 'Error')


get_questions('python', 2)
