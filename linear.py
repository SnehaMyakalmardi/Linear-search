import matplotlib
import  matplotlib.pyplot as plt
matplotlib.use('TKAgg')

def linearsearch(a,key):
    n=len(a)
    for i in range(n):
        if a[i]==key:
            return True
        return False

a=[10,50,60,70,80,90,100]
key=20
if linearsearch(a,key):
    print("taget value found in list")
else:
    print("target value is not found in list")

x=list(range(1,100000))
plt.plot(x,[y for y in x])
plt.title("linear search - time complexity is O(n)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
