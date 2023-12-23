dic = {}


def draw_game(dic: dict, m=False):
    print()
    for i in range(9):
        res = ' ' * 5 if not dic.get(i) else dic[i].center(5, ' ')
        print(*res if not m else [str(i).center(5, ' ')], '|' if (i + 1) % 3 else '', end='', sep='')
        if not (i + 1) % 3 and i + 1 != 9:
            print(f'\n{"-" * 17}')
    print('\n\n')


lst_wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def check_win(dic: dict):
    x = sorted([x[0] for x in dic.items() if x[1] == 'X'])
    o = sorted([x[0] for x in dic.items() if x[1] == '0'])
    for i in lst_wins:
        if set(i) & set(x) == set(i):
            return '"X" WIN !\nGAME OVER!'
        if set(i) & set(o) == set(i):
            return '"O" WINS !\nGAME OVER!'


def get_x(x):
    try:
        x = int(x)
    except:
        x = -1
        print('\nBye bye!')
    if x not in range(9):
        x = -1
    return x


def get_o(o):
    try:
        o = int(o)
    except:
        o = -1
        print('\nBye bye!')
    if o not in range(9):
        o = -1
    return o


def play():
    print(
        'See game map below!\nTo make your move, please enter cell number!\nTo exit enter any symbol!\n\nGAME STARTED\n')
    draw_game(dic, True)

    # while True:
    #     x = get_x()
    #     while x in dic:
    #         print('Position occupied')
    #         x = get_x()
    #     if x == -1:
    #         break
    #     dic[x] = 'X'
    #     draw_game(dic)
    #     res = check_win(dic)
    #     if res:
    #         print(res)
    #         break
    #     o = get_o()
    #     while o in dic:
    #         print('Position occupied')
    #         o = get_o()
    #     if o == -1:
    #         break
    #     dic[o] = '0'
    #
    #
    #     draw_game(dic)
    #     res = check_win(dic)
    #     if res:
    #         print(res)
    #         break


if __name__ == '__main__':
    play()
