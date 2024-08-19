with open("sample.txt","w") as f:
    f.write("Hi Everyone\nWe are learning FILE I/O\nusing JAVA\nI like programming in JAVA")

with open("sample.txt","r") as f:
    data = f.read()
    print(data)

data1 = data.replace("JAVA","Python")

with open("sample.txt","w") as f:
    f.write(data1)

def check_word():
    with open("sample.txt","r") as f:
        data2 = f.read()
        print(data2)
        if(data2.find("learning") != -1):
            print("\nFound")
        else:
            print("\nNot Found")

check_word()

def check_line():
    with open("sample.txt","r") as f:
        data2 = True
        line_no = 1
        while data2:
            data2 = f.readline()
            if("learning" in data2):
                print("Found in line number",line_no)
                return
            else:
                line_no+=1
        print("Not Found")

check_line()