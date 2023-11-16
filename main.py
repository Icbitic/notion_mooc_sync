import requests
import json
import jsonpath
import datetime
from datetime import timezone, timedelta

URL = 'https://www.icourse163.org/web/j/courseBean.getLastLearnedMocTermDto.rpc?csrfKey=7e181cf9d0d04d7da857364ddd793490';

courses = [
    # C programming language
    {
        'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36',
            'cookie': 'EDUWEBDEVICE=b783d63483f94b77bb313390ee1837ed; __yadk_uid=uAou02Xv0dIZViNMBrrRgHZ6qtnQkixG; WM_TID=QsWQG9ENDl1EQVFEQUKAiE9ompEwVlVV; MOOC_PRIVACY_INFO_APPROVED=true; videoRate=2; hasVolume=false; videoVolume=0.00; NTES_YD_PASSPORT=c98SH5yM2Z6us0HoqgJ2Py91_nOovorxxxQH4EW_kTpQiAPuiaN2.HPeserIW_eEm7276CUrVgZe6Xa3ZVBWmlJ4NLFDiaSrvl0Ub2IMhKYvMm4CeU7QtuxrO.kFSA3ESs1Hj3NnxMf3KoAs9IQGIBk0G.IWBb2K3XMGBaHHI4rHIepsM6FYaQ1aPNPYHgrqNlmW9yT.V.lz.Um9rUrSCySUv; WM_NI=RMux2OrAjBvoFtDUaMqaAe6%2FlHy9llPK3MtRbv1q%2F%2FnXD%2Fv9phqUkueEHAT0TSgWZN5pO1yO7vH0nFFKoqb%2BMqY22ckF6IyCHOyqUTXDywAHLsjKXEuYWA3nVxoS5f0rRDE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eedab73ca3edbfa7cf52b78e8eb3d54b828b8b87d866f6bd828ab86df6be8cb9f02af0fea7c3b92a9293bb99b145b29fa6a3f56586ac8cb6e447b3bf8f86b525b098b7daef689495fdaef75aa2aaff92ae25ae888cd0f533b4b8bfb6ea7fa79b88a2d73c988da9b8d946f7b081d2fc45f5aa88d1ed4e8695a192e1218faf97d3b169a99afaaafc498c91b792d8609c9cb798c44490ada6acdb4fb78799a2b26696a8a1b4b86ef4ae9ea5c837e2a3; NTESSTUDYSI=7e181cf9d0d04d7da857364ddd793490; STUDY_INFO="yd.db0238f6f68841cd8@163.com|8|1554290878|1700048544801"; STUDY_SESS="h1DQYcHsEGJUOhrolEjEiqa1/CIy50YTnTz9pl8IDPqS/5gLiu2bZBhMYOGOgYynQugytBHuOBMbci47mA9v2HHabi8/k3CrUTw70+I3LUDoTsEXIDE2twIvkqbxhYOYJybzTKP/rPiRHhH6o/Sy+i5QKx87Jxms4AbeGgSuoVILhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="Zgk8INAIy1JMpfMnKOG9NSjRcO0ZztEpYXZRywLjenxNR/kb85lZqGIcZ8YhCIaw4J7hEfchcsFLPeY7Vsidbs2diES9EeXS3oVrnATk3x/XDftDMs1KroUUpwLgcicpmZf/AYgEw0+rKPSUEsmFkl6Vt/kg8v1SYjhjHi1kX3FG89WM0HWldzvaeijme/JjQivSf7Xq2ZVOJ190+9MZFhg7b8IrZS9rHXiRRtC0HTPZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1554290878#|#1688826034359; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1699888071,1699961201,1700047517,1700048546; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1700050532'
        },
        'data': {
            'termId': '1471026489'
        },
        'URL': 'https://www.icourse163.org/spoc/learn/NEU-1469677177?tid=1471026489#/learn/testlist',
        'tags': ["Programming"]
    },

    # Single-variable Calculus
    {
        'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36',
            'cookie': 'EDUWEBDEVICE=b783d63483f94b77bb313390ee1837ed; __yadk_uid=uAou02Xv0dIZViNMBrrRgHZ6qtnQkixG; WM_TID=QsWQG9ENDl1EQVFEQUKAiE9ompEwVlVV; MOOC_PRIVACY_INFO_APPROVED=true; videoRate=2; hasVolume=false; videoVolume=0.00; NTES_YD_PASSPORT=c98SH5yM2Z6us0HoqgJ2Py91_nOovorxxxQH4EW_kTpQiAPuiaN2.HPeserIW_eEm7276CUrVgZe6Xa3ZVBWmlJ4NLFDiaSrvl0Ub2IMhKYvMm4CeU7QtuxrO.kFSA3ESs1Hj3NnxMf3KoAs9IQGIBk0G.IWBb2K3XMGBaHHI4rHIepsM6FYaQ1aPNPYHgrqNlmW9yT.V.lz.Um9rUrSCySUv; WM_NI=RMux2OrAjBvoFtDUaMqaAe6%2FlHy9llPK3MtRbv1q%2F%2FnXD%2Fv9phqUkueEHAT0TSgWZN5pO1yO7vH0nFFKoqb%2BMqY22ckF6IyCHOyqUTXDywAHLsjKXEuYWA3nVxoS5f0rRDE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eedab73ca3edbfa7cf52b78e8eb3d54b828b8b87d866f6bd828ab86df6be8cb9f02af0fea7c3b92a9293bb99b145b29fa6a3f56586ac8cb6e447b3bf8f86b525b098b7daef689495fdaef75aa2aaff92ae25ae888cd0f533b4b8bfb6ea7fa79b88a2d73c988da9b8d946f7b081d2fc45f5aa88d1ed4e8695a192e1218faf97d3b169a99afaaafc498c91b792d8609c9cb798c44490ada6acdb4fb78799a2b26696a8a1b4b86ef4ae9ea5c837e2a3; NTESSTUDYSI=7e181cf9d0d04d7da857364ddd793490; STUDY_INFO="yd.db0238f6f68841cd8@163.com|8|1554290878|1700048544801"; STUDY_SESS="h1DQYcHsEGJUOhrolEjEiqa1/CIy50YTnTz9pl8IDPqS/5gLiu2bZBhMYOGOgYynQugytBHuOBMbci47mA9v2HHabi8/k3CrUTw70+I3LUDoTsEXIDE2twIvkqbxhYOYJybzTKP/rPiRHhH6o/Sy+i5QKx87Jxms4AbeGgSuoVILhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="Zgk8INAIy1JMpfMnKOG9NSjRcO0ZztEpYXZRywLjenxNR/kb85lZqGIcZ8YhCIaw4J7hEfchcsFLPeY7Vsidbs2diES9EeXS3oVrnATk3x/XDftDMs1KroUUpwLgcicpmZf/AYgEw0+rKPSUEsmFkl6Vt/kg8v1SYjhjHi1kX3FG89WM0HWldzvaeijme/JjQivSf7Xq2ZVOJ190+9MZFhg7b8IrZS9rHXiRRtC0HTPZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1554290878#|#1688826034359; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1699888071,1699961201,1700047517,1700048546; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1700050497'
        },
        'data': {
            'termId': '1470936482'
        },
        'URL': 'https://www.icourse163.org/learn/NEU-1001639002?tid=1470936482#/learn/testlist',
        'tags': ["Calculus"]
    },

    # Linear Algebra
    {
        'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36',
            'cookie': 'EDUWEBDEVICE=b783d63483f94b77bb313390ee1837ed; __yadk_uid=uAou02Xv0dIZViNMBrrRgHZ6qtnQkixG; WM_TID=QsWQG9ENDl1EQVFEQUKAiE9ompEwVlVV; MOOC_PRIVACY_INFO_APPROVED=true; videoRate=2; hasVolume=false; videoVolume=0.00; NTES_YD_PASSPORT=c98SH5yM2Z6us0HoqgJ2Py91_nOovorxxxQH4EW_kTpQiAPuiaN2.HPeserIW_eEm7276CUrVgZe6Xa3ZVBWmlJ4NLFDiaSrvl0Ub2IMhKYvMm4CeU7QtuxrO.kFSA3ESs1Hj3NnxMf3KoAs9IQGIBk0G.IWBb2K3XMGBaHHI4rHIepsM6FYaQ1aPNPYHgrqNlmW9yT.V.lz.Um9rUrSCySUv; WM_NI=RMux2OrAjBvoFtDUaMqaAe6%2FlHy9llPK3MtRbv1q%2F%2FnXD%2Fv9phqUkueEHAT0TSgWZN5pO1yO7vH0nFFKoqb%2BMqY22ckF6IyCHOyqUTXDywAHLsjKXEuYWA3nVxoS5f0rRDE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eedab73ca3edbfa7cf52b78e8eb3d54b828b8b87d866f6bd828ab86df6be8cb9f02af0fea7c3b92a9293bb99b145b29fa6a3f56586ac8cb6e447b3bf8f86b525b098b7daef689495fdaef75aa2aaff92ae25ae888cd0f533b4b8bfb6ea7fa79b88a2d73c988da9b8d946f7b081d2fc45f5aa88d1ed4e8695a192e1218faf97d3b169a99afaaafc498c91b792d8609c9cb798c44490ada6acdb4fb78799a2b26696a8a1b4b86ef4ae9ea5c837e2a3; NTESSTUDYSI=7e181cf9d0d04d7da857364ddd793490; STUDY_INFO="yd.db0238f6f68841cd8@163.com|8|1554290878|1700048544801"; STUDY_SESS="h1DQYcHsEGJUOhrolEjEiqa1/CIy50YTnTz9pl8IDPqS/5gLiu2bZBhMYOGOgYynQugytBHuOBMbci47mA9v2HHabi8/k3CrUTw70+I3LUDoTsEXIDE2twIvkqbxhYOYJybzTKP/rPiRHhH6o/Sy+i5QKx87Jxms4AbeGgSuoVILhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="Zgk8INAIy1JMpfMnKOG9NSjRcO0ZztEpYXZRywLjenxNR/kb85lZqGIcZ8YhCIaw4J7hEfchcsFLPeY7Vsidbs2diES9EeXS3oVrnATk3x/XDftDMs1KroUUpwLgcicpmZf/AYgEw0+rKPSUEsmFkl6Vt/kg8v1SYjhjHi1kX3FG89WM0HWldzvaeijme/JjQivSf7Xq2ZVOJ190+9MZFhg7b8IrZS9rHXiRRtC0HTPZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1554290878#|#1688826034359; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1699888071,1699961201,1700047517,1700048546; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1700050432'
        },
        'data': {
            'termId': '1470952455'
        },
        'URL': 'https://www.icourse163.org/learn/NEU-1001638002?tid=1470952455#/learn/testlist',
        'tags': ["Linear Algebra"]
    },

    # Military Theory
    {
        'headers': {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0 Safari/537.36',
            'cookie': 'EDUWEBDEVICE=b783d63483f94b77bb313390ee1837ed; __yadk_uid=uAou02Xv0dIZViNMBrrRgHZ6qtnQkixG; WM_TID=QsWQG9ENDl1EQVFEQUKAiE9ompEwVlVV; MOOC_PRIVACY_INFO_APPROVED=true; videoRate=2; hasVolume=false; videoVolume=0.00; NTES_YD_PASSPORT=c98SH5yM2Z6us0HoqgJ2Py91_nOovorxxxQH4EW_kTpQiAPuiaN2.HPeserIW_eEm7276CUrVgZe6Xa3ZVBWmlJ4NLFDiaSrvl0Ub2IMhKYvMm4CeU7QtuxrO.kFSA3ESs1Hj3NnxMf3KoAs9IQGIBk0G.IWBb2K3XMGBaHHI4rHIepsM6FYaQ1aPNPYHgrqNlmW9yT.V.lz.Um9rUrSCySUv; WM_NI=RMux2OrAjBvoFtDUaMqaAe6%2FlHy9llPK3MtRbv1q%2F%2FnXD%2Fv9phqUkueEHAT0TSgWZN5pO1yO7vH0nFFKoqb%2BMqY22ckF6IyCHOyqUTXDywAHLsjKXEuYWA3nVxoS5f0rRDE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eedab73ca3edbfa7cf52b78e8eb3d54b828b8b87d866f6bd828ab86df6be8cb9f02af0fea7c3b92a9293bb99b145b29fa6a3f56586ac8cb6e447b3bf8f86b525b098b7daef689495fdaef75aa2aaff92ae25ae888cd0f533b4b8bfb6ea7fa79b88a2d73c988da9b8d946f7b081d2fc45f5aa88d1ed4e8695a192e1218faf97d3b169a99afaaafc498c91b792d8609c9cb798c44490ada6acdb4fb78799a2b26696a8a1b4b86ef4ae9ea5c837e2a3; NTESSTUDYSI=7e181cf9d0d04d7da857364ddd793490; STUDY_INFO="yd.db0238f6f68841cd8@163.com|8|1554290878|1700048544801"; STUDY_SESS="h1DQYcHsEGJUOhrolEjEiqa1/CIy50YTnTz9pl8IDPqS/5gLiu2bZBhMYOGOgYynQugytBHuOBMbci47mA9v2HHabi8/k3CrUTw70+I3LUDoTsEXIDE2twIvkqbxhYOYJybzTKP/rPiRHhH6o/Sy+i5QKx87Jxms4AbeGgSuoVILhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="Zgk8INAIy1JMpfMnKOG9NSjRcO0ZztEpYXZRywLjenxNR/kb85lZqGIcZ8YhCIaw4J7hEfchcsFLPeY7Vsidbs2diES9EeXS3oVrnATk3x/XDftDMs1KroUUpwLgcicpmZf/AYgEw0+rKPSUEsmFkl6Vt/kg8v1SYjhjHi1kX3FG89WM0HWldzvaeijme/JjQivSf7Xq2ZVOJ190+9MZFhg7b8IrZS9rHXiRRtC0HTPZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1554290878#|#1688826034359; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1699888071,1699961201,1700047517,1700048546; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1700050608'
        },
        'data': {
            'termId': '1471611445'
        },
        'URL': 'https://www.icourse163.org/spoc/learn/NEU-1002713003?tid=1471611445#/learn/testlist',
        'tags': []
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
def addTask(databaseID, headers, start_date, end_date, name, is_done, course: dict):
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
            },
            "URL": {
                'url': course['URL']
            },
            "Tags": {
                "multi_select": []
            }
        }
    }
    for tag in course['tags']:
        newPageData['properties']['Tags']['multi_select'].append({'name': tag})
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
dict_of_tasks = {}
for i in existing_tasks['results']:
    dict_of_tasks[i['properties']['Name']['title'][0]['text']['content']] = True


for course in courses:
    tasks = []
    page = requests.post(URL, headers=course['headers'], data=course['data'])
    dict = json.loads(page.text)
    tasks.extend(jsonpath.jsonpath(dict, '$..test'))

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
                       'evaluateEnd': task['evaluateEnd'],
                       'course': course}
            if task['userScore'] is None:
                content['is_done'] = False
            result.append(content)

    for task in result:
        addTask(databaseID, headers, task['release_time'], task['deadline'], task['name'], task['is_done'], task['course'])
        print("Added: " + task['name'])
        if task['evaluateStart'] is not None:
            addTask(databaseID, headers, task['evaluateStart'], task['evaluateEnd'], '互评' + task['name'], task['is_done'], task['course'])
            print("Added: " + '互评' + task['name'])
