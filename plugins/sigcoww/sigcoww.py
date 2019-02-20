from errbot import BotPlugin, botcmd
import os
import re
import csv

class Sigcoww(BotPlugin):
    @botcmd
    def tryme(self, msg, args):
        return 'It *works* !'

    @botcmd(split_args_with=None)
    def lrks(self, msg, args):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/lrks.csv', 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                print(row)

        r = re.compile(r'^(?:20)?(\d\d)(冬|春|夏|秋|Q1|Q2|Q3|Q4)?$')
        if len(args) == 0:
            print('LATEST')
        elif r.match(args[0]):
            print(r.findall(args[0]))
        else:
            return args[0]
