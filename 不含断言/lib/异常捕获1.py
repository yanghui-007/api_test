# try :
#     num = int(input("请输入数字:"))
# except:
#     print("请输入数字")


def demo1():
    return int(input("请输入一个整数："))
# print(demo1())
def demo2():
    return demo1()
# print(demo2())

try:
    print(demo2())
except ValueError:
    print("请输入正确的数字")
except Exception as result:
    print("未知错误 %s" %result)

# if __name__=='__main__':
#  print(demo1())