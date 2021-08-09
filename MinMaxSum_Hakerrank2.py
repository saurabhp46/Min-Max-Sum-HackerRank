arr=[1,2,3,4,5]
sum1=[]
n=len(arr)-1
count=0
for i in arr:
    for j in arr:
        if i!=j:
            sum1.append(j)
        else:
            sum1.append(j)
            count=1
if count==1:
    sum1.pop()
x = [sum1[i:i + n] for i in range(0, len(sum1), n)]
for j in range(len(x)):
    x[j]=sum(x[j])
print(min(x),max(x))