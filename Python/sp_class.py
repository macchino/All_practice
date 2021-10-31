class Human:

    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self) -> str:
        return self.name + ',' + str(self.age) + ',' + self.phone_number

    def __eq__(self, other) -> bool:
        return (self.name == other.name) and (self.phone_number == other.phone_number) and (self.age == other.age)

    def __hash__(self) -> int:
        return hash(self.name + self.phone_number)

    def __bool__(self):
        return True if self.age >= 20 else False

    def __len__(self):
        return len(self.name)


man = Human('Taro', 20, '09000000000')
man2 = Human('Taro', 2, '09000000000')
man3 = Human('Jioro', 12, '09011100000')
man_str = str(man)
print(type(man_str))
print(man_str)

print(man == man2)
set_men = {man, man2, man3}
for x in set_men:
    print(x)


if man:
    print('manはTrue')

if man2:
    print('man2はTrue')

print(len(man))
print(len(man2))
print(len(man3))