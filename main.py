import requests
import json
import jsonpath
import datetime
from datetime import timezone, timedelta

# Enter your url, cookies, term_id here
courses = [
    
]

# Constants for uploading tasks
# Fill in the ones you get according to notion's tutorial
token = ''
databaseID = ""
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}


# Create a Page
def addTask(databaseID, headers, start_date, end_date, name, is_done):
    createUrl = 'https://api.notion.com/v1/pages'
    newPageData = {
        "parent": {"database_id": databaseID},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Deadline": {
                "date": {
                    "start": start_date,
                    "end": end_date
                }
            },
            "Done": {
                "checkbox": is_done
            }
        }
    }
    data = json.dumps(newPageData)
    res = requests.request("POST", createUrl, headers=headers, data=data)
    print(res.status_code)


def readDatabase(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('./full-properties.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    return data


existing_tasks = readDatabase(databaseID, headers)
tasks = []

for course in courses:
    page = requests.post(course['URL'], headers=course['headers'], data=course['data'])
    dict = json.loads(page.text)
    tasks.extend(jsonpath.jsonpath(dict, '$..test'))

dict_of_tasks = {}
for i in existing_tasks['results']:
    dict_of_tasks[i['properties']['Name']['title'][0]['text']['content']] = True

result = []
for task in tasks:
    if task is None or dict_of_tasks.get(task['name']) == True:
        continue
    else:
        if task['evaluateStart'] is not None:
            task['evaluateStart'] = datetime.datetime.fromtimestamp(task['evaluateStart'] / 1000).astimezone(
                timezone(timedelta(hours=8))).isoformat()

        if task['evaluateEnd'] is not None:
            task['evaluateEnd'] = datetime.datetime.fromtimestamp(task['evaluateEnd'] / 1000).astimezone(
                timezone(timedelta(hours=8))).isoformat()

        content = {'name': task['name'],
                   'release_time': datetime.datetime.fromtimestamp(task['releaseTime'] / 1000).astimezone(
                       timezone(timedelta(hours=8))).isoformat(),
                   'deadline': datetime.datetime.fromtimestamp(task['deadline'] / 1000).astimezone(
                       timezone(timedelta(hours=8))).isoformat(),
                   'is_done': True,
                   'evaluateStart': task['evaluateStart'],
                   'evaluateEnd': task['evaluateEnd']}
        if task['userScore'] is None:
            content['is_done'] = False
        result.append(content)

for task in result:
    addTask(databaseID, headers, task['release_time'], task['deadline'], task['name'], task['is_done'])
    print("Added: " + task['name'])
    if task['evaluateStart'] is not None:
        addTask(databaseID, headers, task['evaluateStart'], task['evaluateEnd'], '互评' + task['name'], task['is_done'])
        print("Added: " + '互评' + task['name'])
