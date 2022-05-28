print("Привет")
field = list(range(1, 10))


def make_field():
    for i in range(3):
        print(field[0 + i * 3], field[1 + i * 3], field[2 + i * 3])


def x0_input(player):
    while True:
        player_answer = input("Куда поставить " + player)
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректно")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if field[player_answer - 1] != "X" and field[player_answer - 1] != "0":
                field[player_answer - 1] = player
                break


def check_win():
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_combinations:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def main():
    count = 0
    while True:
        make_field()
        if count % 2 == 0:
            x0_input("X")
        else:
            x0_input("0")
        count += 1
        if count > 4:
            win = check_win()
            if win:
                print("Выиграл " + ("0" if count % 2 == 0 else "X"))
                break
        if count == 9:
            print("Ничья")
    make_field()


main()
