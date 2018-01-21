import json
from newspaper import Article

urllist = []
f = open('test.json', 'r')
js = json.loads(f.read())
#print(js[0]['url'])

for col in js:
	urllist.append(col['url'])

#print("\n".join([col['url'] for col in js])) 
f.close()

for url in urllist:
    a = Article(url, language = 'ko')
    a.download()
    a.parse()
    print(a.title)
    print(a.text[:3000])









