import json

urllist = []
f = open('test.json', 'r')
js = json.loads(f.read())
#print(js[0]['url'])

for col in js:
	urllist.append(col['url'])


print(urllist)

#print("\n".join([col['url'] for col in js])) 
f.close()

