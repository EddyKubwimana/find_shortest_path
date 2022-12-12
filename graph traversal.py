
text = "forxxorfxdofr"
pat = "for"
p1=0
p2 = 3
anogram= 0

while p2 <= len(text):
    print(text[p1:p2])
    if sorted(text[p1:p2])== sorted(pat):
       p1+= 1
       anogram += 1
       p2 +=1
    else:
        p1 += 1
        p2 +=1
print(anogram)
