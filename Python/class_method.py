class Human:

    class_name = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name_age(self):
        print('インスタンスメソッド実行')
        print(f'name = {self.name}, age = {self.age}')

    @classmethod
    def print_class_name(cls, msg):
        print('クラスメソッド実行')
        print(cls.class_name)
        print(msg)

    @staticmethod
    def print_msg(msg):
        print('スタティックメソッド実行')
        print(msg)


Human.print_class_name('こんにてゃ')
man = Human('桜井', 25)
man.print_name_age()
man.print_msg('Hello MSG')