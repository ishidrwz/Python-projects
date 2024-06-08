def check(l,guess,word,tries):
    ch=0
    for i in range (len(word)):
        for j in guess:
            if word[i]==j:
                l[i]=j
                ch+=1
    if ch==0:
        print('WRONG GUESS')
        print()
        print(l)
        tries=1
        return tries,l
    else:
        print('RIGHT GUESS!!')
        print()
        print(l)
        return 0,l

def display(tries):
    if tries==1:
        print('___________')
        print('|       ⦚')
        print('|       ☺︎')
    elif tries==2:
        print('___________')
        print('|       ⦚')
        print('|       ☺︎')
        print('|       | ')
    elif tries==3:
        print('___________')
        print('|       ⦚')
        print('|       ☺︎')
        print('|       | ')
        print('|       ▲')
    elif tries==4:
        print('___________')
        print('|       ⦚')
        print('|       ☺︎')
        print('|       | ')
        print('|       ▲')
        print('|      ⎛  ')
    elif tries==5:
        print('___________')
        print('|       ⦚')
        print('|       ☺︎')
        print('|       | ')
        print('|       ▲')
        print('|      ⎛ ⎞')
    elif tries==6:
        print('___________')
        print('|       ⦚')
        print('|       ☺︎')
        print('|      ⎝| ')
        print('|       ▲')
        print('|      ⎛ ⎞')
    elif tries==7:
        print('___________')
        print('|       ⦚')
        print('|       ☹︎')
        print('|      ⎝|⎠ ')
        print('|       ▲')
        print('|      ⎛ ⎞')
        return 1
    return 0

def main():
    tries=0
    tr=0
    word=input('PLAYER 1 ENTER YOUR WORD:')
    print()
    n=len(word)
    l=list('_'*n)
    print(' PLAYER 2 WILL GUESS','\n','YOU HAVE 7 LIFELINES FOR WRONG ANSWERS!!')
    print(l)
    while True:
        guess=input('PLAYER 2 ENTER YOUR GUESS:') 
        y,L=check(l,guess,word,tries)
        tr+=y
        print()
        if display(tr)==1:
            break
        print()
        print(' PLAYER 2 WILL GUESS','\n','YOU HAVE',7-tr ,'LIFELINES FOR WRONG ANSWERS!!')
        chk=0
        for i in L:
            if i=='_':
                break
            else:
                chk+=1
        if chk==n:
            print('RIGHT GUESS,PLAYER 2 WINS!!')
            return
    print('PLAYER 1 WINS!!')

main()
while True:
    cont=input('Another game??,y/n')
    if cont=='y':
        main()
    else:
        break