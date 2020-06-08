# 如果导入函数名称相同，则后面会覆盖前面的函数 ~ 一旦发生冲突，用as定义一个别名
# from test_126_测试模块1 import say_hello
from test_127_测试模块2 import say_hello as module2_say_hello
from test_126_测试模块1 import say_hello

say_hello()
module2_say_hello()
