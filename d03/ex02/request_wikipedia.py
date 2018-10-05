import requests, json, dewiki.parser, sys

def op():
    if len(sys.argv) != 2 :
        print("Usage : python3 request_wikipedia.py <word to search>")
        exit()
    link = 'https://fr.wikipedia.org/w/api.php?action=query&titles=' + sys.argv[1] + '&prop=revisions&redirects=&rvprop=content&format=json&formatversion=2&utf8='
    gg = requests.api.get(link)
    if gg.status_code != 200:
        raise Exception ("status code error: " + str(gg.status_code))
    dic = json.loads(gg.text)
    try:
        if 'missing' in dic['query']['pages'][0]:
            raise Exception ("L'article « " + sys.argv[1] + " » n'existe pas sur ce wiki !")
            return
        res = dic['query']['pages'][0]['revisions'][0]['content']
        name = dic['query']['pages'][0]['title']
        str = dewiki.parser.Parser().parse_string(res)
        namefile= sys.argv[1] + ".wiki"
        namefile = namefile.replace(' ', '_')
        with open(namefile, 'w') as f:
            f.write(str+ "\n")
    except Exception as e:
        print (e)

if __name__ == '__main__':
    op()
