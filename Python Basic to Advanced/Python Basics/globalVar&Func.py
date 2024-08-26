#defines outside of a func
gloVar = "I am a Global Varable"
#defines inside of a func
def hey():
    locVar = "I am a Local Varable"
    gloVar = "I am not a glo var but i am defined with same name which is already defined outside of a func"
    print(locVar)
    print(gloVar)
print(gloVar)
hey()