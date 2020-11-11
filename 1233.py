def fun1():
    return [1,2,3]

def fun2():
    a=fun1()
    print(a)

f=fun2()

# class aa():
#     def __init__(self):
#         print("111111111111")
#     def __del__(self):
#         print("222222222222")
#
#     def fun01(self):
#         print("333333333333")
#
#
# class bb(aa):
#     # def __init__(self):
#     #     pass
#
#     # def __del__(self):
#     #     print("bbbbbbb--")
#     def fun02(self):
#         print("4444444444")
#
#
# class cc(bb):
#     # def __init__(self):
#     #     print("cccccccccc")
#     # def __del__(self):
#     #     print("cccccccccc--")
#     #     pass
#
#     def fun03(self):
#         print("5555555")
#
# dd=cc()




# class mammal:
#       def __init__(self,leg,eye):
#           self.leg=leg
#           self.eye=eye
#           print("调用父类构造函数")
#       def fulei1(self,col):
#           print ("调用父类方法1")
#           print ("col",col)
#       def fulei2(self,weight=80):
#           print ("调用父类方法2")
#           print ("weight:",weight)
# class dog(mammal):
#       def __init__(self):
#           print ("调用子类构造函数")
#       def zilei1(self):
#           print ("调用子类方法1")
#       def zilei2(self):
#           print ("调用子类方法2")
# dog1=dog()
# dog1.zilei1()
# dog1.fulei1('red')
# dog1.fulei2(100)
# dog1.fulei2()