import requests
from secret import sess_token
from datetime import datetime, date

headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json"
    }

att_url = "http://projectschool.kmitonline.com/getdaywiseatt&performance/{sess_token}/{roll}/12"


def get_sess_token(roll, passwd):
    res = requests.post(
        "http://projectschool.kmitonline.com/login",
        headers=headers,
        json={
            "username": roll,
            "password": passwd
        }
    )
    return res.json()["Token"]


def get_ps_att(rollno):
    res = requests.get(
        att_url.format(
            sess_token=sess_token,
            roll = rollno
        )
    )
    result =  map(lambda x: [x["attdate"],x["attendance"], x["aft_attendance"], ],res.json()["dayWiseAttPerformance"])

    return list(result)

# print(get_ps_att("22BD1A051G"))

"""✓✔✗"""

def get_formatted(att):
    lst = []
    for i in att:
        lst += [[
            datetime.strptime(i[0], "%d-%m-%Y"),
            "✓" if i[1] == 1 else "✗"
        ]]
    return lst

def get_percent(att):
    length = len(att)
    percent = 0
    for i in att:
        percent += i[1]
    percent = percent*100/length
    return percent


# print(get_formatted(get_ps_att("22BD1A0517")))



