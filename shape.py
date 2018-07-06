f = open('text.txt','r',encoding='utf-8')
g = open('textafter.txt','w',encoding='utf-8')

for char in f:
    if char == ' ':
        g.write('\n')
    else:
        g.write(char)

f.close
