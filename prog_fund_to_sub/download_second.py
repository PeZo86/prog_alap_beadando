import requests

def download_file(url):
    filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    if r.ok:
        with open(filename, 'wb') as file:
            for chunk in r.iter_content(chunk_size=1024):
                file.write(chunk)
    else:
        print('Ooops! Something wrong!')



def main():
    url = 'https://www.ksh.hu/stadat_files/ele/hu/ele0033.csv'
    download_file(url)


if __name__ == '__main__':
    main()