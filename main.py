print('Приветствую Вас в кибервинтажной игре "Крестики-Нолики"')
print('Для начала давайте познакомимся!')
player1 = str(input('Введите имя игрока, играющего крестиками "x" -->'))
player2 = str(input('Введите имя игрока, играющего ноликами "о" -->'))
print(f'Привет {player1} и {player2}!!!')
print('Теперь давайте посмотрим где Вы будете играть.')
print('Это поле для игры "Крестики-Нолики":')
win = 0
step_count = 0
step = []
list_of_step = []
field_to_play = [
    [' ', 0, 1, 2]
   ,[0, '-', '-', '-']
   ,[1, '-', '-', '-'],
    [2, '-', '-', '-']
]
def get_field():
    for row in field_to_play:
        for element in row:
            print(element, end = " ")
        print()
get_field()
print('Размер поля 3х3. Координаты строк и столбцов пронумерованы от "0" до "2".')
print('Для выполнения хода необходимо ввести сначала координату по вертикали от 0 до 2 (0, 1 или 2),')
print('а затем по горизонтали от 0 до 2 (0, 1 или 2)')
print('Итак начнем!')

def input_check(lit):
    global step
    global step_count
    player = None
    literal = None
    if lit == "x":
        player = player1
        literal = 'крестиками'
    elif lit == 'o':
        player = player2
        literal = 'ноликами'
    else:
        pass
    step = input(f'{player}, Вы играете {literal}! Cделайте свой ход! \n'
              f'Введите координаты в виде целых чисел от 0 до 2 по вертикали '
                 f'и по горизонтали через пробел -->').split()
    if len(step) != 2 or None in step:
        print('Координаты введены некорректно. Нужно ввести 2 координаты')
        input_check(lit)
    elif int(step[0]) < 0 or int(step[0]) > 2 or int(step[1]) < 0 or int(step[1]) > 2:
        print('Вы ввели значения в недопустимом диапазоне')
        input_check(lit)
    elif step in list_of_step:
        print('Такой ход был!')
        input_check(lit)
    else:
        list_of_step.append(step)
        step_count += 1
    return step
def get_step(field, x, lit):
    field[int(x[0]) + 1][int(x[1]) + 1] = f'{lit}'
    return get_field()
def who_is_win(lit):
    global win
    if lit == "x":
        print(f'Ура у нас еть победитель!!! Победил(а) {player1}, игравший(ая) "крестиками"')
        win = 1
    elif lit == "o":
        print(f'Ура у нас еть победитель!!! Победил(а) {player2}, игравший(ая) "ноликами"')
        win = 1
def check_win(lit):
    if field_to_play[1].count(f'{lit}') == 3 or field_to_play[2].count(f'{lit}') == 3 or field_to_play[3].count(f'{lit}') == 3:
        who_is_win(lit)
    elif field_to_play[1][1] == lit and field_to_play[2][1] == lit and field_to_play[3][1] == lit:
        who_is_win(lit)
    elif field_to_play[1][2] == lit and field_to_play[2][2] == lit and field_to_play[3][2] == lit:
        who_is_win(lit)
    elif field_to_play[1][3] == lit and field_to_play[2][3] == lit and field_to_play[3][3] == lit:
        who_is_win(lit)
    elif field_to_play[1][1] == lit and field_to_play[2][2] == lit and field_to_play[3][3] == lit:
        who_is_win(lit)
    elif field_to_play[1][3] == lit and field_to_play[2][2] == lit and field_to_play[3][1] == lit:
        who_is_win(lit)
    else:
        pass

for item in range(1, 9):
    player1_step = input_check('x')
    print(f'{player1}, Вы ввели {player1_step}')
    get_step(field_to_play, player1_step, 'x')
    check_win('x')
    if win == 1:
        break
    if step_count == 9:
        print('Ничья. Для запуска новой партии перезагрузите программу')
        break
    player2_step = input_check('o')
    print(f'{player2}, Вы ввели {player2_step}')
    get_step(field_to_play, player2_step, 'o')
    check_win('o')
    if win == 1 or step_count == 9:
        break
    if step_count == 9:
        print('Ничья. Для запуска новой партии перезагрузите программу')
        break


