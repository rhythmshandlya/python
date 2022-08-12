import os

with open('./test/example.txt', 'r') as f:
    data = f.read()
    print(data)

with open('./test/example.txt', 'w') as f:
    data = f.write("Hello World!")

entries = os.listdir()
print(entries)