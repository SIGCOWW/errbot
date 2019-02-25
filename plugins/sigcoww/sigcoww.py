from errbot import BotPlugin, botcmd
import os
import otaku

class Sigcoww(BotPlugin):
    @botcmd
    def deadline(self, msg, args):
        return os.environ['DEADLINE'] if 'DEADLINE' in os.environ else '???'

    @botcmd
    def motivation(self, msg, args):
        return otaku.get_imageurl('モチベーションアップ ポスター')

    @botcmd(split_args_with=None)
    def lrks(self, msg, args):
        character = otaku.yourname('lrks.csv', args)
        if character is None: return 'ないです。'
        imageurl = otaku.get_imageurl(' '.join(character[0:2]))
        if imageurl is None: return 'ないです。'
        return imageurl
