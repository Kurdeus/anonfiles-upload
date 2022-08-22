import requests, html



def direct(i):
    r = requests.get(i).content
    tree = html.fromstring(r)
    dlink = tree.xpath('//a[@class="btn btn-primary btn-block"]/@href')
    return str(dlink[0]).replace(' ','%20')


def upload(file):
    callapi = requests.post("https://api.anonfiles.com/upload", 
    files={'file': open(file, 'rb')}).json()
    url = (callapi['data']['file']['url']['full'])
    return [url, direct(url)]



output = upload('your_file')
print(output)
