# python type of function:-----

#   2)  user-define function:---

#    with return---
#     with argument , 
#    withput argument
#   without return--
#    with argument , 
#    withput argument

# 1) in-build   :---
     
# type()
# len()
# min()
# max()
#print()                                                         
# id()                                                         

# with arguments with  return:---
# def sub(a,b):
#     return(a-b)
# print(sub(2,4))

# without argument with  return:--
# def add():
#     return 6+8
# print(add())

# without argument without return:--
# def hell():
#     print("hello")
# hell()

# with argumnet without return:--
# def go(a,b):
#     print(a+b)
# go(20,10)


# relation btw parameter and arguments:----
# ----defpult argument
# ---- positional argument
# ----variable length argument(*args)
# ---keyword positional argument
# ---keyword defoult positional argument
# ---variable length keyword argument(**kwargs)

# two tearms--:
# ===packing (*args)
# ===unpacking(**kwargs)

# 1)--positinal arguments
# def show(x,y,z):
#     print("x",x)
#     print("y",y)
#     print("z",z)
# show(10,20,30)
# show()o/p: 3 rwquired arguments are missing
# show(10)o/p:2 required arguments are missing
# show(10,20)o/p:1 required argument is missing
# show(10,20,30,40)o/p:3 positional arguments but 4 were given
