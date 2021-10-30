class SmpleA():
    class_val = 'class_val'

    def set_val(self):
        self.instance_val = 'instance_val'

    def print_val(self):
        print(f'クラス変数 ＝ {self.class_val}')
        print(f'インスタンス変数 = {self.instance_val}')

instance_a = SmpleA() #インスタンス化
instance_a.set_val()
print(instance_a.instance_val)
instance_a.print_val()

#クラス変数の呼び出し
print(SmpleA.class_val)
print(instance_a.__class__.class_val)

instance_b = SmpleA()  # インスタンス化
instance_b.set_val()
instance_b.print_val()
instance_a.__class__.class_val = 'class val 2'
instance_b.print_val()
print('????????????????????????')
print(id(instance_a.__class__.class_val))
print(id(instance_b.__class__.class_val))
