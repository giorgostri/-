summ=0
for x in range (100):
    pl=0
    gram, sthl = (3, 3)
    a= [[" "] * sthl] * gram


    while True:

        while True:
            from random import randint
            row=randint(0,2)
            col=randint(0,2)
            from random import choice
            ep = ["mikro", "mesaio", "megalo"]
            val = choice(ep)
            if a[row][col]==" ":
                a[row][col]=val
                break
            elif a[row][col]!=val:
                if a[row][col]=="mikro":
                    if val=="mesaio":
                        a[row][col] ="mikromesaio"
                        break
                    elif val=="megalo":
                        a[row][col] = "mikromegalo"
                        break
                elif a[row][col]=="mesaio":
                    if val=="megalo":
                        a[row][col]="mesaiomegalo"
                        break
                elif a[row][col]=="mikromesaio":
                    if val=="megalo":
                        a[row][col] = "mikromesaiomegalo"
                        break
                elif a[row][col]=="mikromegalo":
                    if val=="mesaio" :
                        a[row][col] = "mikromesaiomegalo"
                        break

        pl+=1
        for i in range (3):
            if (a[i][0]=="mikro" or a[i][0]=="mikromesaio" or a[i][0]=="mikromegalo" or a[i][0]=="mikromesaiomegalo")\
            and (a[i][1]=="mikro" or a[i][1]=="mikromesaio" or a[i][1]=="mikromegalo" or a[i][1]=="mikromesaiomegalo")\
            and (a[i][2]=="mikro" or a[i][2]=="mikromesaio" or a[i][2]=="mikromegalo" or a[i][2]=="mikromesaiomegalo"):
                #f=True
                break
            elif (a[i][0]=="mesaio" or a[i][0]=="mikrosmesaio" or a[i][0]=="mesaiomegalo" or a[i][0]=="mikromesaiomegalo") \
            and (a[i][1]=="mesaio" or a[i][1]=="mikrosmesaio" or a[i][1]=="mesaiomegalo" or a[i][1]=="mikromesaiomegalo") \
            and (a[i][2]=="mesaio" or a[i][2]=="mikrosmesaio" or a[i][2]=="mesaiomegalo" or a[i][2]=="mikromesaiomegalo"):
               # f=True
                break
            elif (a[i][0]=="megalo" or a[i][0]=="mesaiomegalo" or a[i][0]=="mikromegalo" or a[i][0]=="mikromesaiomegalo") \
            and (a[i][1]=="megalo" or a[i][1]=="mesaiomegalo" or a[i][1]=="mikromegalo" or a[i][1]=="mikromesaiomegalo") \
            and (a[i][2]=="megalo" or a[i][2]=="mesaiomegalo" or a[i][2]=="mikromegalo" or a[i][2]=="mikromesaiomegalo"):
               # f=True
                break
            elif (a[i][0]=="mikro" or a[i][0]=="mikromesaio" or a[i][0]=="mikromegalo" or a[i][0]=="mikromesaiomegalo") \
            and (a[i][1]=="mesaio" or a[i][1]=="mikromesaio" or a[i][1]=="mesaiomegalo" or a[i][1]=="mikromesaiomegalo") \
            and (a[i][2]=="megalo" or a[i][2]=="mesaiomegalo" or a[i][2]=="mikromegalo" or a[i][2]=="mikromesaiomegalo"):
                #f=True
                break




        for j in range (3):
            if  (a[0][j]=="mikro" or a[0][j]=="mikromesaio" or a[0][j]=="mikromegalo" or a[0][j]=="mikromesaiomegalo") \
            and (a[1][j]=="mikro" or a[1][j]=="mikromesaio" or a[1][j]=="mikromegalo" or a[1][j]=="mikromesaiomegalo") \
            and (a[2][j]=="mikro" or a[2][j]=="mikromesaio" or a[2][j]=="mikromegalo" or a[2][j]=="mikromesaiomegalo"):
                #f=True
                break
            elif (a[0][j]=="mesaio" or a[0][j]=="mikromesaio" or a[0][j]=="mesaiomegalo" or a[0][j]=="mikromesaiomegalo") \
            and (a[1][j]=="mesaio" or a[1][j]=="mikromesaio" or a[1][j]=="mesaiomegalo" or a[1][j]=="mikromesaiomegalo")\
            and (a[2][j]=="mesaio" or a[2][j]=="mikromesaio" or a[2][j]=="mesaiomegalo" or a[2][j]=="mikromesaiomegalo"):
                #f=True
                break
            elif (a[0][j]=="megalo" or a[0][j]=="mesaiomegalo" or a[0][j]=="mikromegalo" or a[0][j]=="mikromesaiomegalo") \
            and (a[1][j]=="megalo" or a[1][j]=="mesaiomegalo" or a[1][j]=="mikromegalo" or a[1][j]=="mikromesaiomegalo") \
            and (a[2][j]=="megalo" or a[2][j]=="mesaiomegalo" or a[2][j]=="mikromegalo" or a[2][j]=="mikromesaiomegalo"):
                #f=True
                break
            elif (a[0][j]=="mikro" or a[0][j]=="mikromesaio" or a[0][j]=="mikromegalo" or a[0][j]=="mikromesaiomegalo") \
            and (a[1][j]=="mesaio" or a[1][j]=="mikromesaio" or a[1][j]=="mesaiomegalo" or a[1][j]=="mikromesaiomegalo") \
            and (a[2][j]=="megalo" or a[2][j]=="mesaiomegalo" or a[2][j]=="mikromegalo" or a[2][j]=="mikromesaiomegalo"):
                #f=True
                break

        if (a[0][0]=="mikro" or a[0][0]=="mikromesaio" or a[0][0]=="mikromegalo" or a[0][0]=="mikromesaiomegalo") \
        and (a[1][1]=="mikro" or a[1][1]=="mikromesaio" or a[1][1]=="mikromegalo" or a[1][1]=="mikromesaiomegalo") \
        and(a[2][2]=="mikro" or a[2][2]=="mikromesaio" or a[2][2]=="mikromegalo" or a[2][2]=="mikromesaiomegalo"):
           # f=True
            break
        if (a[0][0] == "mesaio" or a[0][0] == "mikromesaio" or a[0][0] == "mesaiomegalo" or a[0][0] == "mikromesaiomegalo") \
        and (a[1][1] == "mesaio" or a[1][1] == "mikromesaio" or a[1][1] == "mesaiomegalo" or a[1][1] == "mikromesaiomegalo") \
        and (a[2][2] == "mesaio" or a[2][2] == "mikromesaio" or a[2][2] == "mesaiomegalo" or a[2][2] == "mikromesaiomegalo"):
           # f=True
            break
        if (a[0][0] == "megalo" or a[0][0] == "mesaiomegalo" or a[0][0] == "mikromegalo" or a[0][0] == "mikromesaiomegalo") \
        and (a[1][1] == "megalo" or a[1][1] == "mesaiomegalo" or a[1][1] == "mikromegalo" or a[1][1] == "mikromesaiomegalo") \
        and (a[2][2] == "megalo" or a[2][2] == "mesaiomegalo" or a[2][2] == "mikromegalo" or a[2][2] == "mikromesaiomegalo"):
           # f=True
            break
        if (a[0][0] == "mikro" or a[0][0] == "mikromesaio" or a[0][0] == "mikromegalo" or a[0][0] == "mikromesaiomegalo") \
        and (a[1][1] == "mesaio" or a[1][1] == "mikromesaio" or a[1][1] == "mesaiomegalo" or a[1][1] == "mikromesaiomegalo") \
        and (a[2][2] == "megalo" or a[2][2] == "mesaiomegalo" or a[2][2] == "mikromegalo" or a[2][2] == "mikromesaiomegalo"):
           # f=True
            break

        if (a[0][2]=="mikro" or a[0][2]=="mikromesaio" or a[0][2]=="mikromegalo" or a[0][2]=="mikromesaiomegalo") \
        and (a[2][2]=="mikro" or a[2][2]=="mikromesaio" or a[2][2]=="mikromegalo" or a[2][2]=="mikromesaiomegalo") \
        and(a[2][1]=="mikro" or a[2][0]=="mikromesaio" or a[2][0]=="mikromegalo" or a[2][0]=="mikromesaiomegalo"):
          #  f=True
            break
        if (a[0][2] == "mesaio" or a[0][2] == "mikromesaio" or a[0][2] == "mesaiomegalo" or a[0][2] == "mikromesaiomegalo") \
        and (a[2][2] == "mesaio" or a[2][2] == "mikromesaio" or a[2][2] == "mesaiomegalo" or a[2][2] == "mikromesaiomegalo") \
        and (a[2][0] == "mesaio" or a[2][0] == "mikromesaio" or a[2][0] == "mesaiomegalo" or a[2][0] == "mikromesaiomegalo"):
           # f=True
            break
        if (a[0][2] == "megalo" or a[0][2] == "mesaiomegalo" or a[0][2] == "mikromegalo" or a[0][2] == "mikromesaiomegalo") \
        and (a[2][2] == "megalo" or a[2][2] == "mesaiomegalo" or a[2][2] == "mikromegalo" or a[2][2] == "mikromesaiomegalo") \
        and (a[2][0] == "megalo" or a[2][0] == "mesaiomegalo" or a[2][0] == "mikromegalo" or a[2][0] == "mikromesaiomegalo"):
           # f=True
            break
        if (a[0][2] == "mikro" or a[0][2] == "mikromesaio" or a[0][2] == "mikromegalo" or a[0][2] == "mikromesaiomegalo") \
        and (a[2][2] == "mesaio" or a[2][2] == "mikromesaio" or a[2][2] == "mesaiomegalo" or a[2][2] == "mikromesaiomegalo") \
        and (a[2][0] == "megalo" or a[2][0] == "mesaiomegalo" or a[2][0] == "mikromegalo" or a[2][0] == "mikromesaiomegalo"):
          #  f=True
            break

    summ = summ+pl
print("o mesos oros einai", summ/100)




