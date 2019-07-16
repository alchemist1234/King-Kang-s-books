members = ['cyy', 'dyh', 'zwa', 'zyy']

f = open('book.md','r')
content = f.read()
score = {n:content.count(n) for n in members}
f.close()

with open('readme.md', 'w') as f:
    for name in score:
        f.write('%s: %s%s\n' % (name, score[name], '次'))


