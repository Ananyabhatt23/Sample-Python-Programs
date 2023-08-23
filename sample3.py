def uniqueList():
    list1 = [1,1,1,2]
    list2 = []
    for i in list1:
        if(list1.count(i)==1):
           list2.append(i)
    return list2

def dups():
    list1 = [1,2,2,2,3,3,3]
    list2 = []
    for i in list1:
        if(list1.count(i) > 1):
            if(i in list2):
                continue
            list2.append(i)
    return list2


def splitList(inputlist,size):
    # list1 = [12,45,67,56,56,56]
    # size = 3
    # for i in range(0,len(list1),size):
    #     res = list1[i:i+size]
    #     print(res)
    result = [inputlist[i:i+size] for i in range(0, len(inputlist), size)]
    return result