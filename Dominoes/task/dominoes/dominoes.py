# Write your code here
import random

stock = []
comp = []
status = ''
snake = []
player = []
scores = {}
for a in range(7):
    for b in range(7):
        if [a, b] not in stock:
            stock.append([b, a])
random.shuffle(stock)


def rozdanie():
    global status, snake, comp, stock, player
    comp = stock[0:7]
    player = stock[7:14]
    stock = stock[14:]

    for a in range(6, 1, -1):
        if [a, a] in comp:
            snake = [[a, a]]
            comp.remove([a, a])
            status = "player"
            break
        if [a, a] in player:
            snake = [[a, a]]
            player.remove([a, a])
            status = "computer"
            break
    if not status:
        random.shuffle(stock)
        rozdanie()


def runda():
    global stock, status, snake, player, comp
    if status == "player":
        move = input()
        try:
            move = int(move)
        except:
            print("Invalid input. Please try again.")
            runda()
            return
        if move == 0:
            if stock:
                player.append(stock.pop())
        elif abs(move) > len(player):
            print("Invalid input. Please try again.")
            runda()
            return
        elif move > 0:
            if snake[-1][1] in player[move - 1]:
                if snake[-1][1] == player[move - 1][0]:
                    snake.append(player.pop(move - 1))
                else:
                    a = player.pop(move - 1)
                    [x, y] = a
                    snake.append([y, x])
            else:
                print("Illegal move. Please try again.")
                runda()
                return
        elif move < 0:
            if snake[0][0] in player[(0 - move) - 1]:
                if snake[0][0] == player[(0 - move) - 1][1]:
                    snake.insert(0, player.pop((0 - move) - 1))
                else:
                    a = player.pop((0 - move) - 1)
                    [x, y] = a
                    snake.insert(0, [y, x])
            else:
                print("Illegal move. Please try again.")
                runda()
                return
        status = "computer"
    else:
        input()
        which_domino()
        status = "player"


def show():
    global stock, comp, player, status
    print("=" * 70)
    print(f"Stock size: {len(stock)}\nComputer pieces: {len(comp)}\n")
    if len(snake) <= 6:
        print(*snake, sep="")
    else:
        print(*(snake[:3]), sep="", end="")
        print("...", sep="", end="")
        print(*(snake[-3:]), sep="")
    print("\nYour pieces:")
    for i, p in enumerate(player):
        print(f"{i + 1}:{p}")


def is_winner():
    global status, comp, player, end
    while True:
        if not comp:
            print("\nStatus: The game is over. The computer won!")
            end = True
            break
        elif not player:
            print("\nStatus: The game is over. You won!")
            end = True
            break
        if snake[0][0] == snake[-1][1]:
            counter = 0
            for a, b in snake:
                if a == snake[0][0]:
                    counter += 1
                if b == snake[0][0]:
                    counter += 1
            if counter == 8:
                print("Status: The game is over. It's a draw!")
                end = True
                break
            elif status == "computer":
                print("\nStatus: Computer is about to make a move. Press Enter to continue...")
            elif status == "player":
                print("\nStatus: It's your turn to make a move. Enter your command.")
            break
        elif status == "computer":
            print("\nStatus: Computer is about to make a move. Press Enter to continue...")
        elif status == "player":
            print("\nStatus: It's your turn to make a move. Enter your command.")
        break


def which_domino():
    global comp, snake, scores, stock
    scores = {}
    counter = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }
    for a in comp:
        for num in counter.keys():
            counter[num] += a.count(num)
    for a in stock:
        for num in counter.keys():
            counter[num] += a.count(num)
    for a in comp:
        x, y = a
        scores[tuple(a)] = counter[x] + counter[y]
    while scores:
        domino = list(max(scores, key=scores.get))
        if snake[-1][1] in domino:
            if snake[-1][1] == domino[0]:
                snake.append(domino)
                comp.remove(domino)
            else:
                x, y = domino
                snake.append([y, x])
                comp.remove(domino)
            break
        elif snake[0][0] in domino:
            if snake[0][0] == domino[1]:
                snake.insert(0, domino)
                comp.remove(domino)
            else:
                x, y = domino
                snake.insert(0, [y, x])
                comp.remove(domino)
            break
        else:
            del scores[tuple(domino)]
    if not scores and stock:
        comp.append(stock.pop())


if __name__ == "__main__":
    rozdanie()
    end = False
    while not end:
        show()
        is_winner()
        if end:
            break
        runda()
