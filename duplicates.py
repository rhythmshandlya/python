"""
def functionname( parameters ):
"function_docstring"
function_suite
return [expression]

"""
def duplicate(arr):
    for i in range(0,len(arr)):
        count = 0
        for j in range(i+1,len(arr)):
           if(arr[i]==arr[j]):
                count+=1
        if(count>=1):
            print(arr[i])
    return

duplicate([1,2,3,4,5,5,6,6])