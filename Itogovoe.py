# Инициализация карты
maps = [0, 1, 2,
        3, 4, 5,
        6, 7, 8]

# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод карты на экран
def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])
# функция проверки на число
def input_digit():
    a = input()
    while not a.isdigit():
        print("Вы ввели не число, попробуйте снова")
        a = input()
    return int(a)
#функция диапазона
def input_cell_number():
    a = input_digit()
    while a < 0 or a > 8:
        print("Вы ввели число вне диапазона, попробуйте снова")
        a = input_digit()
    return a
#функция внесения символа в maps по индексу
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol


# Получить текущий результат игры
def get_result():
   win = ""

   for i in victories:
      if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
         win = "Игра завершена,победил X"
      if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
         win = "Игра завершена,победил O"

   return win
#Ход крестика,функция
def hod_x():
   print("Ходит крестик")
   print("Введите номер клетки:")
   a = input_cell_number()
   while maps[a] == "X" or maps[a] == "O":
       print("Клетка занята, введите другое число:")
       a = input_cell_number()
   step_maps(a,"X")
#ход нолика, функция
def hod_O():
   print("Ходит нолик")
   print("Введите номер клетки:")
   a = input_cell_number()
   while maps[a] == "X" or maps[a] == "O":
       print("Клетка занята, введите другое число:")
       a = input_cell_number()
   step_maps(a, "O")

# Основная программа
sum_iter_o=0
while sum_iter_o != 5:  #Так как крестик ходит первый, ноликов не может быть больше 4
    print_maps()
    hod_x()
    if get_result() != "": #если не false, выводим ответ
        print_maps()
        print(get_result())
        break
    print_maps()
    if sum_iter_o == 4: # Если ноликов 4, и get_result false, то все клетки заняты, никто не победил
        if get_result() == "":
            print("Ничья")
            print_maps()
        print(get_result())
        break
    hod_O()
    if get_result() != "": #если не false, выводим ответ
        print_maps()
        print(get_result())
        break
    sum_iter_o += 1     #счетчик нолика +=1










