gradelist = input().split()
count = 0
for i in gradelist:
    i = int(i)
    if i <60:
        count+=1
print(count)
