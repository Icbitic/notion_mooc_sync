import requests
import json
import jsonpath
import datetime
from datetime import timezone, timedelta

URL = 'https://www.icourse163.org/web/j/courseBean.getLastLearnedMocTermDto.rpc?csrfKey=638557db0daf4b398fc1b2399414cd73';

courses = [
    # C programming language
    {
        'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36',
            'cookie': 'EDUWEBDEVICE=b783d63483f94b77bb313390ee1837ed; __yadk_uid=uAou02Xv0dIZViNMBrrRgHZ6qtnQkixG; WM_TID=QsWQG9ENDl1EQVFEQUKAiE9ompEwVlVV; MOOC_PRIVACY_INFO_APPROVED=true; videoRate=2; hasVolume=false; videoVolume=0.00; NTES_YD_PASSPORT=c98SH5yM2Z6us0HoqgJ2Py91_nOovorxxxQH4EW_kTpQiAPuiaN2.HPeserIW_eEm7276CUrVgZe6Xa3ZVBWmlJ4NLFDiaSrvl0Ub2IMhKYvMm4CeU7QtuxrO.kFSA3ESs1Hj3NnxMf3KoAs9IQGIBk0G.IWBb2K3XMGBaHHI4rHIepsM6FYaQ1aPNPYHgrqNlmW9yT.V.lz.Um9rUrSCySUv; WM_NI=i06l%2BFZd6uGYI3AyOVBV2ITMYqh6Q2CHQChkZUaPz5D7J7NoKFMnRhpsQo5dP10E4Ti5ftU94WrePu2dDl7qYvnffYrjs44ONXhhnZtb%2Bwb8CgSCe2OzSnHEJIC0Sa5ES20%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb1f748ab90fa97d733b1868ba6c55b878f8bb0c167e9898fb4f06da9b2f9d1bc2af0fea7c3b92aabf0fa8daa4e9abcfa96c6538bed8f9ace5e828afeaad7479bafa8d7d43a81989fa4eb619a8bafb1f93f88e986d8cd65899a838fd164b4ad9f90b87094ef00a6b760abebaa95d833f889be86d37ff2bc8c8db67b9baaa287e553b2b6bdd5b7458e88a889ed52b8bee598e13481b99da4e83a8da69d8fcb4f8a978dd1d26bf79b9dd3b337e2a3; NTESSTUDYSI=638557db0daf4b398fc1b2399414cd73; STUDY_INFO="yd.db0238f6f68841cd8@163.com|8|1554290878|1699871499458"; STUDY_SESS="h1DQYcHsEGJUOhrolEjEiqa1/CIy50YTnTz9pl8IDPqS/5gLiu2bZBhMYOGOgYynBD3naF4yF2qje6pqZkTSAfsc5DbtGR5DKbSD8iXCUXJ0otK4UDQNp2Nqq9XU2sqrP8innV0c78Mr7mwEpwdPeNPQ5TZMTrFmyQO9ZPvZ2XwLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="Zgk8INAIy1JMpfMnKOG9NSjRcO0ZztEpYXZRywLjenxNR/kb85lZqGIcZ8YhCIaw4J7hEfchcsFLPeY7Vsidbuz5hc+VzulNer0p/pmNx0/cQY1FmlWVtLbNEWePmW2uBu1N4vvN+JB6OyVGGkky/GyUfOTA4MsvDNCMLhfv5FWjlJ1gsP5pCumh8/ltKk3VHrEKzHu2vGNlxOWbtjNTyS04/wsscEqyRoYxf0ipdePZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1554290878#|#1688826034359; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1699685628,1699795672,1699871081,1699871501; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1699875138'
        },
        'data': {
            'termId': '1471026489'
        }
    },

    # Single-variable Calculus
    {
        'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36',
            'cookie': 'EDUWEBDEVICE=b783d63483f94b77bb313390ee1837ed; __yadk_uid=uAou02Xv0dIZViNMBrrRgHZ6qtnQkixG; WM_TID=QsWQG9ENDl1EQVFEQUKAiE9ompEwVlVV; MOOC_PRIVACY_INFO_APPROVED=true; videoRate=2; hasVolume=false; videoVolume=0.00; NTES_YD_PASSPORT=c98SH5yM2Z6us0HoqgJ2Py91_nOovorxxxQH4EW_kTpQiAPuiaN2.HPeserIW_eEm7276CUrVgZe6Xa3ZVBWmlJ4NLFDiaSrvl0Ub2IMhKYvMm4CeU7QtuxrO.kFSA3ESs1Hj3NnxMf3KoAs9IQGIBk0G.IWBb2K3XMGBaHHI4rHIepsM6FYaQ1aPNPYHgrqNlmW9yT.V.lz.Um9rUrSCySUv; WM_NI=i06l%2BFZd6uGYI3AyOVBV2ITMYqh6Q2CHQChkZUaPz5D7J7NoKFMnRhpsQo5dP10E4Ti5ftU94WrePu2dDl7qYvnffYrjs44ONXhhnZtb%2Bwb8CgSCe2OzSnHEJIC0Sa5ES20%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb1f748ab90fa97d733b1868ba6c55b878f8bb0c167e9898fb4f06da9b2f9d1bc2af0fea7c3b92aabf0fa8daa4e9abcfa96c6538bed8f9ace5e828afeaad7479bafa8d7d43a81989fa4eb619a8bafb1f93f88e986d8cd65899a838fd164b4ad9f90b87094ef00a6b760abebaa95d833f889be86d37ff2bc8c8db67b9baaa287e553b2b6bdd5b7458e88a889ed52b8bee598e13481b99da4e83a8da69d8fcb4f8a978dd1d26bf79b9dd3b337e2a3; NTESSTUDYSI=638557db0daf4b398fc1b2399414cd73; STUDY_INFO="yd.db0238f6f68841cd8@163.com|8|1554290878|1699871499458"; STUDY_SESS="h1DQYcHsEGJUOhrolEjEiqa1/CIy50YTnTz9pl8IDPqS/5gLiu2bZBhMYOGOgYynBD3naF4yF2qje6pqZkTSAfsc5DbtGR5DKbSD8iXCUXJ0otK4UDQNp2Nqq9XU2sqrP8innV0c78Mr7mwEpwdPeNPQ5TZMTrFmyQO9ZPvZ2XwLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="Zgk8INAIy1JMpfMnKOG9NSjRcO0ZztEpYXZRywLjenxNR/kb85lZqGIcZ8YhCIaw4J7hEfchcsFLPeY7Vsidbuz5hc+VzulNer0p/pmNx0/cQY1FmlWVtLbNEWePmW2uBu1N4vvN+JB6OyVGGkky/GyUfOTA4MsvDNCMLhfv5FWjlJ1gsP5pCumh8/ltKk3VHrEKzHu2vGNlxOWbtjNTyS04/wsscEqyRoYxf0ipdePZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1554290878#|#1688826034359; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1699685628,1699795672,1699871081,1699871501; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1699875270'
        },
        'data': {
            'termId': '1470936482'
        }
    },

    # Linear Algebra
    {
        'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36',
            'cookie': 'EDUWEBDEVICE=b783d63483f94b77bb313390ee1837ed; __yadk_uid=uAou02Xv0dIZViNMBrrRgHZ6qtnQkixG; WM_TID=QsWQG9ENDl1EQVFEQUKAiE9ompEwVlVV; MOOC_PRIVACY_INFO_APPROVED=true; videoRate=2; hasVolume=false; videoVolume=0.00; NTES_YD_PASSPORT=c98SH5yM2Z6us0HoqgJ2Py91_nOovorxxxQH4EW_kTpQiAPuiaN2.HPeserIW_eEm7276CUrVgZe6Xa3ZVBWmlJ4NLFDiaSrvl0Ub2IMhKYvMm4CeU7QtuxrO.kFSA3ESs1Hj3NnxMf3KoAs9IQGIBk0G.IWBb2K3XMGBaHHI4rHIepsM6FYaQ1aPNPYHgrqNlmW9yT.V.lz.Um9rUrSCySUv; WM_NI=i06l%2BFZd6uGYI3AyOVBV2ITMYqh6Q2CHQChkZUaPz5D7J7NoKFMnRhpsQo5dP10E4Ti5ftU94WrePu2dDl7qYvnffYrjs44ONXhhnZtb%2Bwb8CgSCe2OzSnHEJIC0Sa5ES20%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb1f748ab90fa97d733b1868ba6c55b878f8bb0c167e9898fb4f06da9b2f9d1bc2af0fea7c3b92aabf0fa8daa4e9abcfa96c6538bed8f9ace5e828afeaad7479bafa8d7d43a81989fa4eb619a8bafb1f93f88e986d8cd65899a838fd164b4ad9f90b87094ef00a6b760abebaa95d833f889be86d37ff2bc8c8db67b9baaa287e553b2b6bdd5b7458e88a889ed52b8bee598e13481b99da4e83a8da69d8fcb4f8a978dd1d26bf79b9dd3b337e2a3; NTESSTUDYSI=638557db0daf4b398fc1b2399414cd73; STUDY_INFO="yd.db0238f6f68841cd8@163.com|8|1554290878|1699871499458"; STUDY_SESS="h1DQYcHsEGJUOhrolEjEiqa1/CIy50YTnTz9pl8IDPqS/5gLiu2bZBhMYOGOgYynBD3naF4yF2qje6pqZkTSAfsc5DbtGR5DKbSD8iXCUXJ0otK4UDQNp2Nqq9XU2sqrP8innV0c78Mr7mwEpwdPeNPQ5TZMTrFmyQO9ZPvZ2XwLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="Zgk8INAIy1JMpfMnKOG9NSjRcO0ZztEpYXZRywLjenxNR/kb85lZqGIcZ8YhCIaw4J7hEfchcsFLPeY7Vsidbuz5hc+VzulNer0p/pmNx0/cQY1FmlWVtLbNEWePmW2uBu1N4vvN+JB6OyVGGkky/GyUfOTA4MsvDNCMLhfv5FWjlJ1gsP5pCumh8/ltKk3VHrEKzHu2vGNlxOWbtjNTyS04/wsscEqyRoYxf0ipdePZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1554290878#|#1688826034359; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1699685628,1699795672,1699871081,1699871501; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1699875424'
        },
        'data': {
            'termId': '1470952455'
        }
    }
]


# Constants for uploading tasks
token = ''
databaseID = "f6cbd9e15885497e918a2b2a97b23bc8"
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
    page = requests.post(URL, headers=course['headers'], data=course['data'])
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
