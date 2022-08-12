test = ["abtyjytjtrrc","zybj","xxgfrthyhrthrthyhx","sehhrt"]

files = [
    'Z:/users/john/apples.jpg',
    'Z:/users/john/apples.bbx',
    'Z:/users/john/apples.exr',
    'Z:/users/john/apples.abc',
]

def lenSort(arr):
    arr.sort(key = lambda x: len(x))

def extSort(files):
    files.sort(key = lambda x: x.rsplit('.',1)[1])

extSort(files)
lenSort(test)

print(test)
print(files)