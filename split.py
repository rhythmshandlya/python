# # Write a function group (list, size) that take a list and splits into smaller lists of given size.
test = ['1','2','3','4','5','6','7','8','9','10']

def splitAll(k,test):
   i, arr = 0, []
   while i < len(test):
       temp = []
       j = i
       while j < i+k and j<len(test):
            temp.append(test[j])
            j+=1   
       i+=k
       arr.append(temp)
   return arr


print(splitAll(2,test))