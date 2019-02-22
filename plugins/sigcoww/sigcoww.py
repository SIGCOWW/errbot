from errbot import BotPlugin, botcmd
import os
import re
import csv
import random
from googleapiclient.discovery import build

def yourname(filename, args):
    likes = []
    with open(os.path.dirname(os.path.abspath(__file__)) + '/' + filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if len(row) == 4: likes.append(row)

    r = re.compile(r'^(?:20)?(\d\d)(冬|春|夏|秋|Q1|Q2|Q3|Q4)?$')
    if len(args) == 0:
        year = None
        season = None
        title = None
    elif r.match(args[0]):
        m = r.findall(args[0])[0]
        year = '20' + m[0]
        season = {'':None, 'Q1':'Q1', 'Q2':'Q2', 'Q3':'Q3', 'Q4':'Q4', '冬':'Q1', '春':'Q2', '夏':'Q3', '秋':'Q4'}[m[1]]
        title = None
    else:
        year = None
        season = None
        title = re.compile('.*' + '.*'.join(list(args[0])) + '.*')

    if year is not None: likes = list(filter(lambda x:x[2] == year, likes))
    if season is not None: likes = list(filter(lambda x:x[3] == season, likes))
    if title is not None: likes = list(filter(lambda x:title.match(x[1]), likes))
    if len(likes) == 0: return None
    return random.choice(likes)

def get_imageurl(query):
    if 'CUSTOM_SEARCH_APIKEY' not in os.environ: return None
    if 'CUSTOM_SEARCH_ENGINEID' not in os.environ: return None

    apikey = os.environ['CUSTOM_SEARCH_APIKEY']
    engineid = os.environ['CUSTOM_SEARCH_ENGINEID']

    service = build('customsearch', 'v1', developerKey=apikey)
    result = service.cse().list(q=query, cx=engineid, searchType='image').execute()
    if len(result['items']) == 0: return None
    return random.choice(result['items'])['link']


class Sigcoww(BotPlugin):
    @botcmd
    def daedline(self, msg, args):
        return os.environ['DAEDLINE'] if 'DAEDLINE' in os.environ else '???'

    @botcmd(split_args_with=None)
    def lrks(self, msg, args):
        character = yourname('lrks.csv', args)
        if character is None: return 'ないです。'
        imageurl = get_imageurl(' '.join(character[0:2]))
        if imageurl is None: return 'ないです。'
        return imageurl
