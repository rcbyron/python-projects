""" A simple tweet text shrinker """
import re

num_subs = {
    '1': r"(one|\bwon)\b",
    '2': r"\b(to+|two)\b",
    '3': r"(three)",
    '4': r"((ph|f)oa?u?re?)",
    '5': r"(five)\b",
    '6': r"(six)\b",
    '7': r"(seven)\b",
    '8': r"(eight\b|ate(?:ly)\b|ait\b)",
    '9': r"(nine)\b",
    '0': r"(zero)"
}

general = {
    '&': r'(and)',
    '@': r'\b(at)\b',
    'yw': r'((you(\')?re?|ur) welcome)',
    'wtf': r'(what the fuck)',
    'wth': r'(what the he(ll|ck))',
    'wo': r'(with out)',
    'w': r'(with)',
    'we': r'(what(\s)?ever)',
    'gtg': r'(got to go)',
    'bbl': r'(be back later)',
    'til': r'(today I learned)',
    'thx': r'(thanks)',
    'ty': r'(thank you)',
    'tbh': r'(to be honest)',
    'x': r'(cks)',
    'sup': r'(wh?at(\')?s?(\s)?up)',
    'rl': r'(real+)',
    'srs': r'(serious)',
    'ppl': r'(people)',
    'plz': r'(please)',
    'pov': r'(point of view)',
    'oyo': r'(on your own)',
    'omg': r'(oh my go(d|sh))',
    'nm': r'(not(hing)? much)',
    'ne': r'(any)',
    'mgmt': r'(management)',
    'ez': r'(easy)',
    'cu': r'(see you)',
    'ba': r'(bad(\s)+ass)',
    'bc': r'(because)',
    'dis': r'(this)',
    'lyk': r'(like)',
    'wat': r'(what)',
    'b': r'(be)',
    'c': r'(see)',
    'g': r'(gee)',
    'k': r'\b(o?k+(ay)?)',
    'o': r'(oh+)',
    'p': r'(pee+)',
    'x': r'(ex)',
    'y': r'(why)',
    'z': r'(the+)',
    'u': r'(you)',
    'r': r'(are)',
    'tho': r'(though)',
    'n': r'(in)',
    'ya': r'(ye?ah?)',
    # 'ã�„': r'(cc)',
    # 'ãŽ³': r'(ms)',
    # 'ãŽ±': r'(ns)',
    # 'ãŽ°': r'(ps)',
    # 'ã�Œ': r'(in)',
    # 'Êª': r'(ls)',
    # 'ï¬�': r'(fi)',
    # 'Ñ¹': r'(oy)',
    # 'â…±': r'(ii)',
    # 'â…º': r'(xi)',
    # 'ÇŒ': r'(nj)',
    # 'ï¼Ž': r'(\. )',
}


def init():
    """ Initialize and compile regex patterns """
    global num_subs, general
    for k, v in general.items():
        general[k] = re.compile(v, re.IGNORECASE)
    for k, v in num_subs.items():
        num_subs[k] = re.compile(v, re.IGNORECASE)


def fix(tweet):
    """ Fix the tweet to be smaller """
    old_len = len(tweet)
    for k, v in num_subs.items():
        tweet = v.sub(k, tweet)

    for k, v in general.items():
        tweet = v.sub(k, tweet)
    return tweet, old_len-len(tweet)

init()
while True:
    tweet = input('Tweet: ')
    tweet, saved = fix(tweet)
    print("\nSaved "+str(saved)+":", tweet, "\n")
