
#TEXT=input()

f=open('two_cities_ascii.txt','r')
TEXT=f.read()

#print(TEXT)
text=TEXT.lower()
a=text.split()
#print (a[0])
from collections import Counter
counts = Counter(a).most_common(10)
print("oi deka dhmofilesteres lekseis",counts)

f2=[]
for char in a:
    if len(char) >= 2:
        f2.append(char[:2])
#print(f2)
counts2 = Counter(f2).most_common(10)

f3=[]
for char in a:
    if len(char) >= 3:
        f3.append(char[:3])
counts3 = Counter(f3).most_common(10)
print("oi deka dhmofilesteroi syndiasmoi prwtwn dyo grammatwn",counts2,"oi deka dhmofilesteroi syndiasmoi prwtwn triwn grammatwn",counts3)





