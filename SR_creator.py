'''
SR creator
takes the UR list, at all_URs.txt, for each one of them it runs the obj-maker, at obj-maker.py
producing, hopefully, a list of SRs/SOWs
'''

from obj_maker  import produce
from nodes      import nodes

URs = open("all_URs.txt")
all_URs     = []
for UR in URs.readlines():
    all_URs.append(UR)
#pick a language
all_lang       = open("all_langs.txt")
all_langs = []
for lang in all_lang.readlines():
    lang = lang.strip()
    all_langs.append(lang)
current_langs   = all_langs
#current_langs   = ["0001001100011"]
all_forces      = ["I","D","Q"]
with open("all_all.txt", 'w') as f:
    for language in current_langs:
        for force in all_forces:
            for ur in all_URs:
                node = nodes(ur)
                # SR = produce(language, force, UR, nodes)
                f.write(language+"\t")
                f.write(force+"\t")
                f.write(ur)
                #f.write(UR+"\t")
                #f.write(SR)

def assert_length(doc):
    with open(doc, "r") as r:
        for i, l in enumerate(r):
                pass
    assert i+1 == (len(all_forces)*len(current_langs)*len(all_URs))
assert_length("all_all.txt")

