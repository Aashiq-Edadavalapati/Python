p = '''
Hello minna how are you
watashiwa uzumaki naruto dattebayo
ureva kyubi jinchuriki daa shostee
seventh Hokage dattebyoo
I am the most unpredictable ninja of Konoha '''
p1=p.split()
for ch in range(0,len(p1),2):
        for e in p1[ch]:
                if (e in  ['a','e','i','o','u','A','E','I','O','U']):
                        i=e.upper()
                        p1[ch]=p1[ch].replace(e,i)
        print(p1[ch])