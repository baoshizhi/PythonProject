import re
text="htt"
text_tmp=""
text1=re.sub(text_tmp, "2", text)
print("text1:",text1)
print(len(text1))
def add(tx1):
    return tx1+"333"

class text:
    text1="666"
    def __init__(self):
        pass
    def __del__(self):
        pass

    def fun1(self,text01):
        if 1==1:
            self.text1 = "777"
            print("self.text1:",self.text1)
            self.text_tmp="999"
            print("text_tmp1:",self.text_tmp)


    def fun2(self):
        if 2==2:
            print("text_tmp2:",text_tmp)
            self.text2=add(self.text1)
            print("self.text2:",self.text2)

t=text()
t.fun1("1234")
t.fun2()
