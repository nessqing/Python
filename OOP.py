####----------Private 私有 : 允許訪問的權限 start----------##

##----------ex1.----------
##----------可以直接使用----------
# class Animal:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
# a = Animal("dog",15)
# print(a.weight)

##----------ex2.----------
##----------以下就不能直接使用了----------
# class Animal:
#     def __init__(self, name, weight):
#         self.__name = name
#         self.__weight = weight
#
# a = Animal("dog",15)
# print(a.weight)

##----------ex3.----------
##----------在 class 同層寫一個 get_function 才能讀取----------
class Animal:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight
    def get_function(self):
        return self.__name

a = Animal("dog",15)
print(a.get_function())

####----------Private 私有 : 允許訪問的權限 end----------##