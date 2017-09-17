import collections
class Text(collections.UserString):
    def __repr__(self):
        return 'Text({})'.format(self.data)

    def reverse(self):
        return self[::-1]

word=Text("forward")
print(word)
print(word.reverse())

#python  的console 输出的是object的__repr__
#程序中print(obj) 输出的是obj的__str__ 的输出结果




# class spam:
#     def __init__(self,data):
#         self.data=data
#
#     def __str__(self):
#         return "hello python!\n"+self.data
#
#     def printSelf(self):
#         print(self)
#
#
# s=spam("hello world!")
# s.printSelf()