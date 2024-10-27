import requests

r = requests.get("https://www.ksh.hu/stadat_files/ele/hu/ele0033.xlsx")

print(r.status_code)

with open('ele0033.xlsx', 'wb') as f:
    f.write(r.content)
