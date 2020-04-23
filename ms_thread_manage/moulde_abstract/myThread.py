import threading
from time import ctime

"""
    现在，对 MyThread 类进行修改，增加一些调试信息的输出，
    并将其存储为一个名为 myThread 的独立模块，以便在接下来的例子中导入这个类。
    
    除了简单地调用函数外，还将把结果保存在实例属性 self.res 中，
    并创建一个新的方法 getResult()来获取这个值。
"""


class MyThread(threading.Thread):
    def __init__(self, func, args, name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    """
    
    https://www.python.org/dev/peps/pep-0008/
    
    函数和变量名函数名称应小写，必要时用下划线分隔单词，以提高可读性。
    
    # 函数和方法参数
    始终将self作为实例方法的第一个参数。
    始终对类方法的第一个参数使用cls。
    
    如果函数参数的名称与保留关键字发生冲突，
    通常最好在其后附加一个下划线，而不要使用缩写或拼写错误。因此，class_优于clss。
    （也许最好通过使用同义词来避免此类冲突。）
    
    # 方法名称和实例变量
    # 常数
    常量通常在模块级别定义，并以所有大写字母书写，并用下划线分隔单词。示例包括 MAX_OVERFLOW和TOTAL。
    
    
    # Python准则：

    公共属性不应有前导下划线。
    如果您的公共属性名称与保留关键字冲突，
    请在属性名称后附加一个下划线。这比缩写或拼写错误更可取。
    （但是，尽管有此规则，但对于任何已知是类的变量或参数，尤其是类方法的第一个参数，“ cls”是首选的拼写。）

    """
    def get_result(self):
        """
            # 若命名为 getResult —— 提示命名不规范

            Function name should be lowercase
            Inspection info: This inspection checks the PEP8 naming conventions.
            See PEP 8 for more details.
        """
        return self.res

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print('finished', self.name, 'at:', ctime())
