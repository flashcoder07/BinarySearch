
def navive_search(l, target):
    for i in range(len(l)):
        if l[i]==target:
            return i+1
    return -1


def binary_search(l , target, low=None, high=None):
    if low==None:
        low=0
    if high ==None:
        high = len(l)-1
    if high<low:
        return -1
    midpoint=(low + high) // 2
    if l[midpoint]== target:
        return midpoint
    elif target<=l[midpoint]:
        return binary_search(l, target,low, midpoint-1)
    else :
        return binary_search(l, target,midpoint+1, high)

l=[1,2,3,4,5,6,7,8,9,]
target =7
#print(navive_search(l,target))
print(binary_search(l , target))

