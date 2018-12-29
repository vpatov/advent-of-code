data = [line.strip() for line in open('day7.txt','r')]
import re
pat = re.compile(r'[\[\]]')


abba = lambda x: x[0] == x[3] and x[1] == x[2] and x[0] != x[1]
aba = lambda x: x if (x[0] == x[2] and x[0] != x[1]) else False
def supports_tls(ip):
    outside = []
    inside = []
    cur = ''
    for ch in ip:
        if cur != '' and ch == '[':
            outside.append(cur)
            cur = ''
            continue
        if ch == ']':
            inside.append(cur)
            cur = ''
        else:
            cur += ch
    outside.append(cur)
    for word in inside:
        for i in range(0,len(word) - 3):
            if abba(word[i:i+4]):
                return False
    for word in outside:
        for i in range(0,len(word) - 3):
            if abba(word[i:i+4]):
                return True
    return False

def supports_ssl(ip):
    global aba
    outside = []
    inside = []
    cur = ''
    for ch in ip:
        if cur != '' and ch == '[':
            outside.append(cur)
            cur = ''
            continue
        if ch == ']':
            inside.append(cur)
            cur = ''
        else:
            cur += ch
    outside.append(cur)
    abas = []
    for word in outside:
        for i in range(0,len(word) - 2):
            res = aba(word[i:i+3])
            if (res):
                abas.append(res)
    for word in inside:
        for i in range(0,len(word) -2):
            res = aba(word[i:i+3])
            if res:
                for aba_ in abas:
                    if res[0] == aba_[1] and res[1] == aba_[0]:
                        return True
    return False




print 'Part I'
print len(filter(supports_tls,data))
print 'Part II'
print len(filter(supports_ssl,data))
