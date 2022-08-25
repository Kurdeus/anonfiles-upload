import requests, html

class anonfiles():
    def __init__(self):
        self.drive_service = self.service()

    def dl(self, url):
        r = requests.get(url).content
        tree = html.fromstring(r)
        dlink = tree.xpath('//a[@class="btn btn-primary btn-block"]/@href')
        return str(dlink[0]).replace(' ','%20')


    def upload(self, file):
        callapi = requests.post("https://api.anonfiles.com/upload", 
        files={'file': open(file, 'rb')}).json()
        url = (callapi['data']['file']['url']['full'])
        return url

path = 'YOUR_FILE_PATH'

af = anonfiles()
anon_link = af.upload(path)
direct_link = af.dl(anon_link)


print(anon_link, direct_link)
