
summ=0
for x in range (100):

  #  f=False
    pl=0
    gram, sthl = (3, 3)
    a= [[" "] * sthl] * gram

 #   for i in range (2):
 #     for j in range (2):
  #          a[i][j]= " "
    while True:

        while True:
            from random import randint

            row = randint(0, 2)
            col = randint(0, 2)


            from random import choice
            ep = ["mikros", "mesaios", "megalos"]
            val = choice(ep)
            if a[row][col]==" ":
                a[row][col]=val
                break
            elif a[row][col]!=val:
                if a[row][col]=="mikros":
                    if val=="mesaios":
                        a[row][col] ="mikrosmesaios"
                        break
                    elif val=="megalos":
                        a[row][col] = "mikrosmegalos"
                        break
                elif a[row][col]=="mesaios":
                    if val=="mikros":
                        a[row][col] = "mikrosmesaios"
                        break
                    elif val=="megalos":
                        a[row][col]="mesaiosmegalos"
                        break
                elif a[row][col]=="megalos":
                    if val=="mikros":
                        a[row][col] ="mikrosmegalos"
                        break
                    elif val=="mesaios":
                        a[row][col] = "mesaiosmegalos"
                        break
                elif a[row][col]=="mikrosmesaios":
                    if val=="megalos":
                        a[row][col] = "mikrosmesaiosmegalos"
                        break
                elif a[row][col]=="mikrosmegalos":
                    if val=="mesaios" :
                        a[row][col] = "mikrosmesaiosmegalos"
                        break
                elif a[row][col]=="mesaiosmegalos":
                    if val=="mikros":
                        a[row][col]="mikrosmesaiosmegalos"
                        break

        pl+=1
        for i in range (3):
            if (a[i][0]=="mikros" or a[i][0]=="mikrosmesaios" or a[i][0]=="mikrosmegalos" or a[i][0]=="mikrosmesaiosmegalos")\
            and (a[i][1]=="mikros" or a[i][1]=="mikrosmesaios" or a[i][1]=="mikrosmegalos" or a[i][1]=="mikrosmesaiosmegalos")\
            and (a[i][2]=="mikros" or a[i][2]=="mikrosmesaios" or a[i][2]=="mikrosmegalos" or a[i][2]=="mikrosmesaiosmegalos"):
                #f=True
                break
            elif (a[i][0]=="mesaios" or a[i][0]=="mikrosmesaios" or a[i][0]=="mesaiosmegalos" or a[i][0]=="mikrosmesaiosmegalos") \
            and (a[i][1]=="mesaios" or a[i][1]=="mikrosmesaios" or a[i][1]=="mesaiosmegalos" or a[i][1]=="mikrosmesaiosmegalos") \
            and (a[i][2]=="mesaios" or a[i][2]=="mikrosmesaios" or a[i][2]=="mesaiosmegalos" or a[i][2]=="mikrosmesaiosmegalos"):
               # f=True
                break
            elif (a[i][0]=="megalos" or a[i][0]=="mesaiosmegalos" or a[i][0]=="mikrosmegalos" or a[i][0]=="mikrosmesaiosmegalos") \
            and (a[i][1]=="megalos" or a[i][1]=="mesaiosmegalos" or a[i][1]=="mikrosmegalos" or a[i][1]=="mikrosmesaiosmegalos") \
            and (a[i][2]=="megalos" or a[i][2]=="mesaiosmegalos" or a[i][2]=="mikrosmegalos" or a[i][2]=="mikrosmesaiosmegalos"):
               # f=True
                break
            elif (a[i][0]=="mikros" or a[i][0]=="mikrosmesaios" or a[i][0]=="mikrosmegalos" or a[i][0]=="mikrosmesaiosmegalos") \
            and (a[i][1]=="mesaios" or a[i][1]=="mikrosmesaios" or a[i][1]=="mesaiosmegalos" or a[i][1]=="mikrosmesaiosmegalos") \
            and (a[i][2]=="megalos" or a[i][2]=="mesaiosmegalos" or a[i][2]=="mikrosmegalos" or a[i][2]=="mikrosmesaiosmegalos"):
                #f=True
                break




        for j in range (3):
            if  (a[0][j]=="mikros" or a[0][j]=="mikrosmesaios" or a[0][j]=="mikrosmegalos" or a[0][j]=="mikrosmesaiosmegalos") \
            and (a[1][j]=="mikros" or a[1][j]=="mikrosmesaios" or a[1][j]=="mikrosmegalos" or a[1][j]=="mikrosmesaiosmegalos") \
            and (a[2][j]=="mikros" or a[2][j]=="mikrosmesaios" or a[2][j]=="mikrosmegalos" or a[2][j]=="mikrosmesaiosmegalos"):
                #f=True
                break
            elif (a[0][j]=="mesaios" or a[0][j]=="mikrosmesaios" or a[0][j]=="mesaiosmegalos" or a[0][j]=="mikrosmesaiosmegalos") \
            and (a[1][j]=="mesaios" or a[1][j]=="mikrosmesaios" or a[1][j]=="mesaiosmegalos" or a[1][j]=="mikrosmesaiosmegalos") \
            and (a[2][j]=="mesaios" or a[2][j]=="mikrosmesaios" or a[2][j]=="mesaiosmegalos" or a[2][j]=="mikrosmesaiosmegalos"):
                #f=True
                break
            elif (a[0][j]=="megalos" or a[0][j]=="mesaiosmegalos" or a[0][j]=="mikrosmegalos" or a[0][j]=="mikrosmesaiosmegalos") \
            and (a[1][j]=="megalos" or a[1][j]=="mesaiosmegalos" or a[1][j]=="mikrosmegalos" or a[1][j]=="mikrosmesaiosmegalos") \
            and (a[2][j]=="megalos" or a[2][j]=="mesaiosmegalos" or a[2][j]=="mikrosmegalos" or a[2][j]=="mikrosmesaiosmegalos"):
                #f=True
                break
            elif (a[0][j]=="mikros" or a[0][j]=="mikrosmesaios" or a[0][j]=="mikrosmegalos" or a[0][j]=="mikrosmesaiosmegalos") \
            and (a[1][j]=="mesaios" or a[1][j]=="mikrosmesaios" or a[1][j]=="mesaiosmegalos" or a[1][j]=="mikrosmesaiosmegalos") \
            and (a[2][j]=="megalos" or a[2][j]=="mesaiosmegalos" or a[2][j]=="mikrosmegalos" or a[2][j]=="mikrosmesaiosmegalos"):
                #f=True
                break

        if (a[0][0]=="mikros" or a[0][0]=="mikrosmesaios" or a[0][0]=="mikrosmegalos" or a[0][0]=="mikrosmesaiosmegalos") \
        and (a[1][1]=="mikros" or a[1][1]=="mikrosmesaios" or a[1][1]=="mikrosmegalos" or a[1][1]=="mikrosmesaiosmegalos") \
        and(a[2][2]=="mikros" or a[2][2]=="mikrosmesaios" or a[2][2]=="mikrosmegalos" or a[2][2]=="mikrosmesaiosmegalos"):
           # f=True
            break
        if (a[0][0] == "mesaios" or a[0][0] == "mikrosmesaios" or a[0][0] == "mesaiosmegalos" or a[0][0] == "mikrosmesaiosmegalos") \
        and (a[1][1] == "mesaios" or a[1][1] == "mikrosmesaios" or a[1][1] == "mesaiosmegalos" or a[1][1] == "mikrosmesaiosmegalos") \
        and (a[2][2] == "mesaios" or a[2][2] == "mikrosmesaios" or a[2][2] == "mesaiosmegalos" or a[2][2] == "mikrosmesaiosmegalos"):
           # f=True
            break
        if (a[0][0] == "megalos" or a[0][0] == "mesaiosmegalos" or a[0][0] == "mikrosmegalos" or a[0][0] == "mikrosmesaiosmegalos") \
        and (a[1][1] == "megalos" or a[1][1] == "mesaiosmegalos" or a[1][1] == "mikrosmegalos" or a[1][1] == "mikrosmesaiosmegalos") \
        and (a[2][2] == "megalos" or a[2][2] == "mesaiosmegalos" or a[2][2] == "mikrosmegalos" or a[2][2] == "mikrosmesaiosmegalos"):
           # f=True
            break
        if (a[0][0] == "mikros" or a[0][0] == "mikrosmesaios" or a[0][0] == "mikrosmegalos" or a[0][0] == "mikrosmesaiosmegalos") \
        and (a[1][1] == "mesaios" or a[1][1] == "mikrosmesaios" or a[1][1] == "mesaiosmegalos" or a[1][1] == "mikrosmesaiosmegalos") \
        and (a[2][2] == "megalos" or a[2][2] == "mesaiosmegalos" or a[2][2] == "mikrosmegalos" or a[2][2] == "mikrosmesaiosmegalos"):
           # f=True
            break

        if (a[0][2]=="mikros" or a[0][2]=="mikrosmesaios" or a[0][2]=="mikrosmegalos" or a[0][2]=="mikrosmesaiosmegalos") \
        and (a[2][2]=="mikros" or a[2][2]=="mikrosmesaios" or a[2][2]=="mikrosmegalos" or a[2][2]=="mikrosmesaiosmegalos") \
        and(a[2][1]=="mikros" or a[2][0]=="mikrosmesaios" or a[2][0]=="mikrosmegalos" or a[2][0]=="mikrosmesaiosmegalos"):
          #  f=True
            break
        if (a[0][2] == "mesaios" or a[0][2] == "mikrosmesaios" or a[0][2] == "mesaiosmegalos" or a[0][2] == "mikrosmesaiosmegalos") \
        and (a[2][2] == "mesaios" or a[2][2] == "mikrosmesaios" or a[2][2] == "mesaiosmegalos" or a[2][2] == "mikrosmesaiosmegalos") \
        and (a[2][0] == "mesaios" or a[2][0] == "mikrosmesaios" or a[2][0] == "mesaiosmegalos" or a[2][0] == "mikrosmesaiosmegalos"):
           # f=True
            break
        if (a[0][2] == "megalos" or a[0][2] == "mesaiosmegalos" or a[0][2] == "mikrosmegalos" or a[0][2] == "mikrosmesaiosmegalos") \
        and (a[2][2] == "megalos" or a[2][2] == "mesaiosmegalos" or a[2][2] == "mikrosmegalos" or a[2][2] == "mikrosmesaiosmegalos") \
        and (a[2][0] == "megalos" or a[2][0] == "mesaiosmegalos" or a[2][0] == "mikrosmegalos" or a[2][0] == "mikrosmesaiosmegalos"):
           # f=True
            break
        if (a[0][2] == "mikros" or a[0][2] == "mikrosmesaios" or a[0][2] == "mikrosmegalos" or a[0][2] == "mikrosmesaiosmegalos") \
        and (a[2][2] == "mesaios" or a[2][2] == "mikrosmesaios" or a[2][2] == "mesaiosmegalos" or a[2][2] == "mikrosmesaiosmegalos") \
        and (a[2][0] == "megalos" or a[2][0] == "mesaiosmegalos" or a[2][0] == "mikrosmegalos" or a[2][0] == "mikrosmesaiosmegalos"):
          #  f=True
            break

    summ = summ+pl
print("o mesos oros einai", summ/100)
























































