

def func(arg, *args, **kwargs): # arg/args/kwargs只是参数名字 可以随意命名
    print(arg, args, kwargs)
    print(type(arg), type(args), type(kwargs))
# def func(*args, **kwargs):
#     print(args, kwargs)

func(1, 2, 3, 4, c=5, b=6)


# arg 表示单一的任意数据 以对应数据类型存储
# args 表示数据的集合 以 元组 形式存储
# kwargs 表示数据的集合 以 字典 形式存储

