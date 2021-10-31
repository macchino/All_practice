class SampleClass:

    def __init__(self, msg, name=None): #コンストラクタ
        print('コンストラクタが呼ばれました')
        self.msg = msg #インスタンス変数
        self.name = name  # インスタンス変数

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)

var_1 = SampleClass('Hello', 'Jiro')
var_1.print_msg()
var_1.print_name()
