import requests
import json
import jsonpath
import datetime
from datetime import timezone, timedelta

courses = [
    # C programming language
    {
        'URL': 'https://www.icourse163.org/web/j/courseBean.getLastLearnedMocTermDto.rpc?csrfKey=f37d526a2ceb4521876a56be6286251e',
        'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36',
            'cookie': 'EDUWEBDEVICE=b783d63483f94b77bb313390ee1837ed; __yadk_uid=uAou02Xv0dIZViNMBrrRgHZ6qtnQkixG; WM_TID=QsWQG9ENDl1EQVFEQUKAiE9ompEwVlVV; MOOC_PRIVACY_INFO_APPROVED=true; videoRate=2; hasVolume=false; videoVolume=0.00; WM_NI=RzWerlZP8DALSrW6Zs0nJOlbYaVeW1h7XziB1n51pHFSH9OrUh%2Bg%2Fskw7n8L8trf22GcuXddIgZto7qvDXTzbSIGl6SWAm355RD0q88KXbATJ8IZ16oAm2AzQV8525NbNjU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea3ef3488ecbca3e83eb8e78aa2d84f839e9f82d172adb0e5d4c4348995e5aecb2af0fea7c3b92a92a69986f1689a90f8a5c44891ae99d7d979f4b286b0ef6a9bbf9a86d63bace9989bec4af3b2fbd2f344868d88dace7a97b8e588ae79a9a9f98fbb48fcacbe87b13a85bdbbb9e7708bb99695ee3db3aa8cb9d772a28d87a8ef3e91898f8eb23ff78e8cd1f434fc959883c4608ae887bbb43ead9fa3d3c472938af8d6b13f8ebe828bd837e2a3; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1699453454,1699502335,1699593005,1699609396; NTESSTUDYSI=f37d526a2ceb4521876a56be6286251e; NTES_YD_SESS=rv8YCC3cKJm75nlJaFzV.w6fyUr0cKCP7YuJi2QtiWdTxaw1xYbLvewQcQCN5sQ.TtLt4gACPy7QEjQJlngoydzYrLeMjD7cQhzSCtl4pUsa9es5jVDRKRKIzZn2cJDyzPTrrMQQXftberJIYHhZSnn2oJAcYkJfML70KLcNtgahuKiH1X0ESlfiw6TShAWpVZ6IZSCxpQTM2orFnOX93yvlkig5sTNBM0Sx_wqDCuDPS; NTES_YD_PASSPORT=c98SH5yM2Z6us0HoqgJ2Py91_nOovorxxxQH4EW_kTpQiAPuiaN2.HPeserIW_eEm7276CUrVgZe6Xa3ZVBWmlJ4NLFDiaSrvl0Ub2IMhKYvMm4CeU7QtuxrO.kFSA3ESs1Hj3NnxMf3KoAs9IQGIBk0G.IWBb2K3XMGBaHHI4rHIepsM6FYaQ1aPNPYHgrqNlmW9yT.V.lz.Um9rUrSCySUv; STUDY_INFO="yd.db0238f6f68841cd8@163.com|8|1554290878|1699629745940"; STUDY_SESS="h1DQYcHsEGJUOhrolEjEiqa1/CIy50YTnTz9pl8IDPqS/5gLiu2bZBhMYOGOgYynBD3naF4yF2qje6pqZkTSAcXgOWcvgiLmUIbaA53D1GvERC3I/C81HNAoalXg0U99JakMBErU9kJHNE3VkTfJmNywD5gJOxKfCxAEj6Emsj0Lhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="Zgk8INAIy1JMpfMnKOG9NSjRcO0ZztEpYXZRywLjenxNR/kb85lZqGIcZ8YhCIaw4J7hEfchcsFLPeY7Vsidbuz5hc+VzulNer0p/pmNx08zeABf5GiBP7oHh0F1N1RKvINxmt6z34QDYbrbVJHVzkpJyyTQbWe4vNCYGWd6U3FT4P9y/Kp2lFbrSmdS3kTmANEv9Hr8C5GKFbPGzEjJlXMQqxYhFkVN7UwoaQqRo1rZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1554290878#|#1688826034359; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1699642900'
        },
        'data': {
            'termId': '1471026489'
        }
    },

    # Single-variable Calculus
    {
        'URL': 'https://www.icourse163.org/web/j/courseBean.getLastLearnedMocTermDto.rpc?csrfKey=ccd9e16fff004eff92dff2e8dc6d3e2c',
        'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36',
            'cookie': 'EDUWEBDEVICE=b783d63483f94b77bb313390ee1837ed; __yadk_uid=uAou02Xv0dIZViNMBrrRgHZ6qtnQkixG; WM_TID=QsWQG9ENDl1EQVFEQUKAiE9ompEwVlVV; MOOC_PRIVACY_INFO_APPROVED=true; videoRate=2; hasVolume=false; videoVolume=0.00; NTES_YD_PASSPORT=c98SH5yM2Z6us0HoqgJ2Py91_nOovorxxxQH4EW_kTpQiAPuiaN2.HPeserIW_eEm7276CUrVgZe6Xa3ZVBWmlJ4NLFDiaSrvl0Ub2IMhKYvMm4CeU7QtuxrO.kFSA3ESs1Hj3NnxMf3KoAs9IQGIBk0G.IWBb2K3XMGBaHHI4rHIepsM6FYaQ1aPNPYHgrqNlmW9yT.V.lz.Um9rUrSCySUv; WM_NI=f613K4BH4eTfCVNncNIs5zIPCqUYzxpGjpeCMhindNM%2BWXsLP5ilxzG3CIz0hxoqljZrGI1S3zfrE3FhQAwOTZs3Uf%2BEe0pSyitFXYZIAeyO86fv7mq151K%2F9bLn%2FAzRSEM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee91f853f69be188b67d9ae78bb3d14b968b8aacc539f8aeffb7e266b1b8bfabd12af0fea7c3b92aa6eaffd4ca408298fc86d76e818a828fe2468badfb9bcc5c81af9bbaf974b499a691e8498fb8a78fe7468ff599b9f24894eba78dfb7285ed8daaf93caca8a192ef629aae89aab459f1a6aa93c83986b89fa2f6459886bdd4d86ee99babd1f359bbb7bca7db539a978f86fc45fceaaa97b667b3effbd2ca25fbbe848fae4bba8e9da6d037e2a3; NTESSTUDYSI=ccd9e16fff004eff92dff2e8dc6d3e2c; STUDY_INFO="yd.db0238f6f68841cd8@163.com|8|1554290878|1699685625390"; STUDY_SESS="h1DQYcHsEGJUOhrolEjEiqa1/CIy50YTnTz9pl8IDPqS/5gLiu2bZBhMYOGOgYynBD3naF4yF2qje6pqZkTSARhDSMwyo4hL64cV9FhT7fxO00d0MuPq+/U1YI7o7HQ71uDboatwU0ozXH1Z1v5o+a4vh5wL3VmCm5cxPIR0g1oLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="Zgk8INAIy1JMpfMnKOG9NSjRcO0ZztEpYXZRywLjenxNR/kb85lZqGIcZ8YhCIaw4J7hEfchcsFLPeY7Vsidbuz5hc+VzulNer0p/pmNx089tNQtunFmNnTrd+ej5LGOKSsNf+rIwnXTOH/OP4D/l4sNOSjyNHLeGNEXGgCxf1P9IT7oI0oQTzwvTaOxO3FDkk8S+EHi4CivBzbNi5fwzzLrtZa510uwd9GiptPqOtTZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1554290878#|#1688826034359; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1699502335,1699593005,1699609396,1699685628; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1699685637'
        },
        'data': {
            'termId': '1470936482'
        }
    },

    # Linear Algebra
    {
        'URL': 'https://www.icourse163.org/web/j/courseBean.getLastLearnedMocTermDto.rpc?csrfKey=ccd9e16fff004eff92dff2e8dc6d3e2c',
        'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36',
            'cookie': 'EDUWEBDEVICE=b783d63483f94b77bb313390ee1837ed; __yadk_uid=uAou02Xv0dIZViNMBrrRgHZ6qtnQkixG; WM_TID=QsWQG9ENDl1EQVFEQUKAiE9ompEwVlVV; MOOC_PRIVACY_INFO_APPROVED=true; videoRate=2; hasVolume=false; videoVolume=0.00; NTES_YD_PASSPORT=c98SH5yM2Z6us0HoqgJ2Py91_nOovorxxxQH4EW_kTpQiAPuiaN2.HPeserIW_eEm7276CUrVgZe6Xa3ZVBWmlJ4NLFDiaSrvl0Ub2IMhKYvMm4CeU7QtuxrO.kFSA3ESs1Hj3NnxMf3KoAs9IQGIBk0G.IWBb2K3XMGBaHHI4rHIepsM6FYaQ1aPNPYHgrqNlmW9yT.V.lz.Um9rUrSCySUv; WM_NI=f613K4BH4eTfCVNncNIs5zIPCqUYzxpGjpeCMhindNM%2BWXsLP5ilxzG3CIz0hxoqljZrGI1S3zfrE3FhQAwOTZs3Uf%2BEe0pSyitFXYZIAeyO86fv7mq151K%2F9bLn%2FAzRSEM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee91f853f69be188b67d9ae78bb3d14b968b8aacc539f8aeffb7e266b1b8bfabd12af0fea7c3b92aa6eaffd4ca408298fc86d76e818a828fe2468badfb9bcc5c81af9bbaf974b499a691e8498fb8a78fe7468ff599b9f24894eba78dfb7285ed8daaf93caca8a192ef629aae89aab459f1a6aa93c83986b89fa2f6459886bdd4d86ee99babd1f359bbb7bca7db539a978f86fc45fceaaa97b667b3effbd2ca25fbbe848fae4bba8e9da6d037e2a3; NTESSTUDYSI=ccd9e16fff004eff92dff2e8dc6d3e2c; STUDY_INFO="yd.db0238f6f68841cd8@163.com|8|1554290878|1699685625390"; STUDY_SESS="h1DQYcHsEGJUOhrolEjEiqa1/CIy50YTnTz9pl8IDPqS/5gLiu2bZBhMYOGOgYynBD3naF4yF2qje6pqZkTSARhDSMwyo4hL64cV9FhT7fxO00d0MuPq+/U1YI7o7HQ71uDboatwU0ozXH1Z1v5o+a4vh5wL3VmCm5cxPIR0g1oLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="Zgk8INAIy1JMpfMnKOG9NSjRcO0ZztEpYXZRywLjenxNR/kb85lZqGIcZ8YhCIaw4J7hEfchcsFLPeY7Vsidbuz5hc+VzulNer0p/pmNx089tNQtunFmNnTrd+ej5LGOKSsNf+rIwnXTOH/OP4D/l4sNOSjyNHLeGNEXGgCxf1P9IT7oI0oQTzwvTaOxO3FDkk8S+EHi4CivBzbNi5fwzzLrtZa510uwd9GiptPqOtTZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1554290878#|#1688826034359; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1699502335,1699593005,1699609396,1699685628; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1699685810'
        },
        'data': {
            'termId': '1470952455'
        }
    }
]

# Constants for uploading tasks
token = 'secret_coAT2UhN6kZ8MBiJXap5Vsn9qEivkO6CNf4wCzGBdmD'
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
