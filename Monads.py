#Монады: Реализуйте класс IO (ввод-вывод), который будет представлять действие ввода-вывода.
#Создайте функцию-редуктор, которая будет принимать список IO и последовательно выполнять каждое действие, сохраняя результаты в список.

class IO:
    def __init__(self, effect):
        self.effect = effect
    def __call__(self):
        return self.effect()

def Input():
    def Input_effect():
        return input()
    return IO(Input_effect)

def Output(contents):
    def Output_effect():
        print(contents)
    return IO(Output_effect)

def reductor(IO_List):
    contents = []
    result = []
    for command in IO_List:
        if command == "Input":
            contents = Input()()
            result.append(contents)
        elif command == "Output":
            print("Вывод: " ,end = "")
            Output(contents)()
        else :
            print("Неопознная команда")
    return result          

IO_List = ["Input","Input","Output","Input"]
print(f"Результат: {reductor(IO_List)}")
