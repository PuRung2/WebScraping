import json
from newspaper import Article
from collections import Counter
from konlpy.tag import Twitter
import pytagcloud


urllist = []
text = ""
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
    text += a.text[:3000]


nlp = Twitter()
nouns = nlp.nouns(text)
    
count = Counter(nouns)

tag2 = count.most_common(20)
#taglist = pytagcloud.make_tags(tag2, maxsize=80)
#pytagcloud.create_tag_image(taglist, 'wordcloud.jpg', size=(900, 600), fontname='Nobile', rectangular=False)















