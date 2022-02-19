pl1=0
pl2=0
plx=0
for met in range(100):

    import random

    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        print(sum1)

    if sum1>21:
        print("P2 wins!")
        pl2+=1
        
    else:
        '''
        sxolia pollwn
        grammwn
        '''

        print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            pl1=pl1+1
        elif sum2>sum1:
            print("P2 wins!")
            pl2=pl2+1
        else:
            print("draw!")
            plx=plx+1
print("o prwtos paixths kerdizei:",pl1,"fores. o deyteros:",pl2,"kai isofarizoyn:",plx)






pl12=0
pl22=0
plx2=0
for met in range(100):
    import random

    xartia = []
    xartia2=[]
    xartia22=[]
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    xarti2= [i for i in range(1,9)]
    xarti22=[i for i in range (10,11)] + figures
    for i in xarti22:
        for j in color:
            xartia22.append([i, j])
    random.shuffle(xartia22)

    for i in xarti2:
        for j in color:
            xartia2.append([i, j])
    random.shuffle(xartia2)
    for i in xarti:
        for j in color:
            xartia.append([i, j])
    random.shuffle(xartia)
    player1 = []
    sum1 = 0
    d=0
    while sum1 < 16:
        sum1 = 0
        if d==0:
            g=xartia22.pop()
            player1.append(g)
            xartia.remove(g)

            d+=1
        else:
            v=xartia.pop()
            player1.append(v)

            if v in xartia22:
                xartia22.remove(v)
            elif v in xartia2:
                xartia2.remove(v)


        print (player1)
        for card in player1:
            if card[0] in figures:
                sum1 = sum1 + 10
            else:
                sum1 = sum1 + card[0]
        print(sum1)

    if sum1 > 21:
        print("P2 wins!")
        pl22 += 1

    else:
        '''
        sxolia pollwn
        grammwn
        '''

        print("P2 joins the game")  # let me add one more player
        player2 = []
        sum2 = 0
        k=0
        while sum2 < 16 :
            sum2 = 0
            if k==0:
                l=xartia2.pop()
                player2.append(l)
                xartia.remove(l)
                k+=1

            else:
                x=xartia.pop()
                player2.append(x)
                if x in xartia22:
                    xartia22.remove(x)
                elif x in xartia2:
                    xartia2.remove(x)

            print(player2)
            for card in player2:
                if card[0]in figures:
                    sum2=sum2+10
                else:
                    sum2 = sum2 + card[0]
                print(sum2)
        if sum2 > 21:
            sum2 = 0
        if sum1 > sum2:
            print("P1 wins!")
            pl12 = pl12 + 1
        elif sum2 > sum1:
            print("P2 wins!")
            pl22 = pl22 + 1
        else:
            print("draw!")
            plx2 = plx2 + 1
print("o prwtos paixths kerdizei me arxiko deka h figoura:", pl12, "fores. o deyteros xwris arxiko deka kerdizei:", pl22, "kai isofarizoyn:", plx2)
print("o prwtos paixths kerdizei:",pl1,"fores. o deyteros:",pl2,"kai isofarizoyn:",plx)