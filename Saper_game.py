from config import level_map
import random
# 0 - пусто
# 1 - бомба
game_level = 1  # 1 - 4*4, 2 - 5*5, 3 - 6*6


def create_field(size):
    field = [[0 for j in range(size)] for i in range(size)]

    # Расставляем бомбы с вероятностью 20%
    bomb_count = int(size * size * 0.2)  # Рассчитываем количество бомб

    for _ in range(bomb_count):
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if field[row][col] != 1:  # Проверяем, чтобы бомба не ставилась дважды
            field[row][col] = 1

    return field


def show_field(field):
    for i in field:
        for j in i:
            print(j, end=" ")
        print()


def player_step():
    try:
        field_size = level_map[game_level]
        row = int(input("Введите номер строки: "))
        if row not in range(1, field_size + 1):
            raise Exception()
        column = int(input("Введите номер столбца: "))
        if column not in range(1, field_size + 1):
            raise Exception()

        return [row - 1, column - 1]
    except:
        print("Некорректные данные")
        player_step()


def game():
    global game_level
    try:
        game_level = int(input("Введите уровень игры (1/2/3): "))
        if game_level not in [1, 2, 3]:
            raise Exception()
    except:
        print("Некорректные данные")
        game()

    field_size = level_map[game_level]
    field = create_field(field_size)
    show_field(field)
    step = player_step()
    field[step[0]][step[1]] = 1  # Отмечаем шаг игрока
    show_field(field)  # Показываем обновленное поле




if __name__ == '__main__':
    game()
