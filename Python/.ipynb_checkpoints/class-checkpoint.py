class Car:
    """車クラス"""
    country = 'Japan'
    year = 2021
    name = 'Prius' #プロパティ

    def print_name(self):
        print('Print_name実行')
        print(self.name)

my_car = Car() #インスタンス化
print(my_car.year)
my_car.print_name()