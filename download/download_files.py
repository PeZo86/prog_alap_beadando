import requests

r = requests.get("https://www.ksh.hu/stadat_files/lak/en/lak0001.csv")
print(r.status_code)

with open('files/lak0001.csv', 'wb') as f:
    f.write(r.content)
    f.close()

