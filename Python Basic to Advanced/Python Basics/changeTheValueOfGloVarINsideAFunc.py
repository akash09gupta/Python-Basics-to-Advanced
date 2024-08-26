x = "I am a global"

def check():
    global x
    x = "Now i am changed"
    print(x)

check()
print(x)