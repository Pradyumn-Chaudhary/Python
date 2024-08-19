# f = open("text_file.txt","r")
# # data = f.readline()
# data = f.read()
# print(data)
# print(type(data))
# f.close()

with open("text_file.txt","r") as f:
    data1 = f.readline()
    print(data1)
    data2 = f.readline()
    print(data2)

# import os
# os.remove("sample.txt")
