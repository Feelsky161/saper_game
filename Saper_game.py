from config import level_map
# 0 - пусто
# 1- бомба



game_level =1 #1 - 4*4 2 - 5*5 3 - 6*6

def create_field(size):
    field = [[0 for j in range(size)] for i in range (size)]
    # for i in range(size):
    #     field.append([])
    #     for j in range (size):
    #         field[i].append(0)
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

        column = int(input("Введите номер строки: "))
        if column not in range(1, field_size + 1):
            raise Exception()

        return [row-1, column-1]

    except:

        print("некорректные данные")
        player_step()




def game():

    try:

        game_level = int(input("Введите уровень игры (1/2/3): "))
        if game_level not in [1, 2, 3]:
            raise Exception()

    except:

        print("некорректные данные")
        game()


    field_size = level_map[game_level]
    field  = create_field(level_map[game_level])
    show_field(field)
    step=player_step()
    field[step[0]][step[1]] = 1





if __name__ == '__main__':
    field = create_field(4)
    show_field(field)
    game()
