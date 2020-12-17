list1 = [1,2,3,4,5,6,7,8,9,0]
list2 = ['one','two','three','four','five','six','seven','eight','nine','zero']

zipped = list(zip(list1, list2))

print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)

for (l1, l2) in zip(list1,list2):
    print(l1)
    print(l2)
    
     