import re
F=open('access.log','r')
mass1 = []
mass2 = []
for line in F.readlines():
    mass=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',line)
    for x in mass:
        if x not in mass1:
            mass1.append(x)
    mass=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.',line)
    for x in mass:
        if x not in mass2:
            mass2.append(x)
for x in mass2:
   print("Подсеть: ",x)
   for y in mass1:
       if y.startswith(x):
           print(y)
