print( sum(len(s[:-1]) - len(eval(s)) for s in open("AOTC2015_8.txt",'r')))

print( sum(2+s.count('\\')+s.count('"') for s in open("AOTC2015_8.txt")))