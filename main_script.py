import os, requests as r

xml = 'xml'

names = os.listdir(xml)
for name in names:
    fullname = os.path.join(xml, name)
    with open(fullname, 'rb') as f:
        r.post('http://localhost:10001/upload', files={name: f})