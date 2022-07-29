"""
Here is a json file lise this:
{"minutes": 30, "created_at": "2016-05-01 00:00:10", "user_id": 199071, "lab": "\u7528\u6237\u53ca\u6587\u4ef6\u6743\u9650\u7ba1\u7406", "course": "Linux \u57fa\u7840\u5165\u95e8\uff08\u65b0\u7248\uff09"}


user_id      user ID
lab          lab name
course       course name
minutes      study time
created_at   study start time

you can use command to download data file:
powershell -c "invoke-webrequest -uri yoururl -outfile D:\codes\data\test_analysis.json"
    
complete the code on the below,
first parameter is file path, second parameter is user ID,read the json file and return the result of censusing all the of studying.

import json
def analysis(file, user_id):
    times = 0
    minutes = 0
    return times, minutes
"""
import json
class DA_1_analysis():
    def analysis(self, file:str, user_id:int):
        times = 0
        minutes = 0
        with open(file) as f:
            data = json.load(f)
        for info in data:
            if info["user_id"] == user_id:
                times+=1
                minutes += info["minutes"]
        return times, minutes


file = r"D:\Users\Administrator\Source\Repos\ML_DL_DA\DataAnalysing\test_analysis.json"
user_id = 199071

da = DA_1_analysis()
print(da.analysis(file, user_id))