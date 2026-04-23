string=input()
bomb=list(input())
bomb_length=len(bomb)
bomb_last=bomb[-1]
tmp=[]
for s in string:
    tmp.append(s)
    if tmp[-bomb_length:]==bomb:
        for _ in range(bomb_length):
            tmp.pop()
if tmp:
    print(''.join(tmp))
else:
    print('FRULA')