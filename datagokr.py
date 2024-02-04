import requests

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey=Qm%2FSxTC4k4vYtw5LKeqyTg%2FQ8vtQXBAP6PQFRjWClRCd7sFMNMlwW9x6%2BmsUEv0pObk76HsEYyhCueQU7RLfNQ%3D%3D'
params ={'pageNo' : '1', 'numOfRows' : '10', 'LAWD_CD' : '11110', 'DEAL_YMD' : '201512' }

response = requests.get(url, params=params)
print(response.content)