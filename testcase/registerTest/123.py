import os


#获取目录
print(os.path.dirname(__file__))
print(os.getcwd())


#上层目录
print(os.path.dirname(os.getcwd()))
print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

#上上层
print(os.path.abspath(os.path.join(os.getcwd(),"../..")))
print(os.path.dirname(os.path.abspath(__file__)))