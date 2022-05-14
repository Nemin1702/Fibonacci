numbers=[0,1]
while len (numbers)<10:
    next=numbers[-1]+numbers[-2]
    numbers.append(next)
for i in numbers:
    print(i)