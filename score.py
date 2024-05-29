gradelist = input().split()
count = 1
for i in gradelist:
    if int(i)<60:
        count+=1
print(count)