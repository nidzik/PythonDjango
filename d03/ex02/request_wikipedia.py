import requests, json, dewiki.parser, sys

def op():
    gg = requests.api.get('https://fr.wikipedia.org/w/api.php?action=query&titles=chocolatine&prop=revisions&redirects=&rvprop=content&format=json&formatversion=2&utf8=')
    dic = json.loads(gg.text)
    res = dic['query']['pages'][0]['revisions'][0]['content']
    name = dic['query']['pages'][0]['title']
    str = dewiki.parser.Parser().parse_string(res)
    with open("test.wiki", 'w') as f:
        f.write(str+ "\n")

if __name__ == '__main__':
    op()
