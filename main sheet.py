import turtle
import functions

global mode
global occupied

# background
back_ground = turtle.Screen()
back_ground.bgcolor('white')
back_ground.title('Tic Tac Toe')

# board
wn = turtle.Screen()
wn.bgpic("TicTacToeBoard.gif")
board = turtle.Turtle()
board.speed(0)
board.width(3)
board.penup()
board.setposition(-200, -200)
board.pendown()
for i in range(4):
    board.fd(400)
    board.left(90)
board.penup()
board.setposition(-75, -200)
board.setheading(90)
board.pendown()
board.fd(400)
board.penup()
board.setposition(75, 200)
board.pendown()
board.setheading(-90)
board.fd(400)
board.penup()
board.setposition(-200, 75)
board.setheading(360)
board.pendown()
board.fd(400)
board.penup()
board.setposition(-200, -75)
board.pendown()
board.fd(400)
board.hideturtle()

# tools
winner = turtle.Turtle()
winner.hideturtle()
occupied = []
ao = 0
bo = 0
co = 0
qo = 0
wo = 0
eo = 0
doa = 0
dob = 0
winner_o = turtle.Turtle()
winner_o.hideturtle()
winner_o.width(3)
winner_o.penup()
winner_o.speed(2)
winner_o.color('red')
o_wins = 0
ax = 0
bx = 0
cx = 0
qx = 0
wx = 0
ex = 0
dxa = 0
dxb = 0
winner_x = turtle.Turtle()
winner_x.hideturtle()
winner_x.width(3)
winner_x.penup()
winner_x.speed(2)
winner_x.color('black')
x_wins = 0
Mode = '0'
Moves = 0

# main game loop
while True:
    # player inputs
    Position = input('Position: ').lower()
    if Position == 'a1' and Mode == '0' and 'A1' not in occupied:
        functions.A10()
        occupied.append('A1')
        ao += 1
        qo += 1
        doa += 1
        Mode = 'x'
        Moves += 1
    elif Position == 'a1' and 'A1' in occupied:
        print('Position Occupied')
    elif Position == 'a2' and Mode == '0' and 'A2' not in occupied:
        functions.A20()
        occupied.append('A2')
        ao += 1
        wo += 1
        Mode = 'x'
        Moves += 1
    elif Position == 'a2' and 'A2' in occupied:
        print('Position Occupied')
    elif Position == 'a3' and Mode == '0' and 'A3' not in occupied:
        functions.A30()
        occupied.append('A3')
        ao += 1
        eo += 1
        dob += 1
        Mode = 'x'
        Moves += 1
    elif Position == 'a3' and 'A3' in occupied:
        print('Position Occupied')
    elif Position == 'b1' and Mode == '0' and 'B1' not in occupied:
        functions.B10()
        occupied.append('B1')
        bo += 1
        qo += 1
        Mode = 'x'
        Moves += 1
    elif Position == 'b1' and 'B1' in occupied:
        print('Position Occupied')
    elif Position == 'b2' and Mode == '0' and 'B2' not in occupied:
        functions.B20()
        occupied.append('B2')
        bo += 1
        wo += 1
        doa += 1
        dob += 1
        Mode = 'x'
        Moves += 1
    elif Position == 'b2' and 'B2' in occupied:
        print('Position Occupied')
    elif Position == 'b3' and Mode == '0' and 'B3' not in occupied:
        functions.B30()
        occupied.append('B3')
        bo += 1
        eo += 1
        Mode = 'x'
        Moves += 1
    elif Position == 'b3' and 'B3' in occupied:
        print('Position Occupied')
    elif Position == 'c1' and Mode == '0' and 'C1' not in occupied:
        functions.C10()
        occupied.append('C1')
        co += 1
        qo += 1
        dob += 1
        Mode = 'x'
        Moves += 1
    elif Position == 'c1' and 'C1' in occupied:
        print('Position Occupied')
    elif Position == 'c2' and Mode == '0' and 'C2' not in occupied:
        functions.C20()
        occupied.append('C2')
        co += 1
        wo += 1
        Mode = 'x'
        Moves += 1
    elif Position == 'c2' and 'C2' in occupied:
        print('Position Occupied')
    elif Position == 'c3' and Mode == '0' and 'C3' not in occupied:
        functions.C30()
        occupied.append('C3')
        co += 1
        eo += 1
        doa += 1
        Mode = 'x'
        Moves += 1
    elif Position == 'c3' in occupied:
        print('Position Occupied')
    elif Position == 'a1' and Mode == 'x':
        functions.A1X()
        occupied.append('A1')
        ax += 1
        qx += 1
        dxa += 1
        Mode = '0'
        Moves += 1
    elif Position == 'a2' and Mode == 'x':
        functions.A2X()
        occupied.append('A2')
        ax += 1
        wx += 1
        Mode = '0'
        Moves += 1
    elif Position == 'a3' and Mode == 'x':
        functions.A3X()
        occupied.append('A3')
        ax += 1
        ex += 1
        dxb += 1
        Mode = '0'
        Moves += 1
    elif Position == 'b1' and Mode == 'x':
        functions.B1X()
        occupied.append('B1')
        bx += 1
        qx += 1
        Mode = '0'
        Moves += 1
    elif Position == 'b2' and Mode == 'x':
        functions.B2X()
        occupied.append('B2')
        bx += 1
        wx += 1
        dxa += 1
        dxb += 1
        Mode = '0'
        Moves += 1
    elif Position == 'b3' and Mode == 'x':
        functions.B3X()
        occupied.append('B3')
        bx += 1
        ex += 1
        Mode = '0'
        Moves += 1
    elif Position == 'c1' and Mode == 'x':
        functions.C1X()
        occupied.append('C1')
        cx += 1
        qx += 1
        dxb += 1
        Mode = '0'
        Moves += 1
    elif Position == 'c2' and Mode == 'x':
        functions.C2X()
        occupied.append('C2')
        cx += 1
        wx += 1
        Mode = '0'
        Moves += 1
    elif Position == 'c3' and Mode == 'x':
        functions.C3X()
        occupied.append('C3')
        cx += 1
        ex += 1
        dxa += 1
        Mode = '0'
        Moves += 1
    elif Position == '':
        break
    else:
        print("That's not an valid input.")
    # winning statements circles
    if 3 == ao:
        winner.write('Circle Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_o.setposition(-200, 137.5)
        winner_o.pendown()
        winner_o.fd(400)
        winner_o.penup()
        winner_o.setheading(0)
        o_wins += 1
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner.clear()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == bo:
        winner.write('Circle Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_o.setposition(-200, 0)
        winner_o.pendown()
        winner_o.fd(400)
        winner_o.penup()
        winner_o.setheading(0)
        o_wins += 1
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        Moves = 0
    elif 3 == co:
        winner.write('Circle Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_o.setposition(-200, -137.5)
        winner_o.pendown()
        winner_o.fd(400)
        winner_o.penup()
        winner_o.setheading(0)
        o_wins += 1
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == qo:
        winner.write('Circle Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_o.setposition(-137.5, 200)
        winner_o.setheading(-90)
        winner_o.pendown()
        winner_o.fd(400)
        winner_o.penup()
        winner_o.setheading(0)
        o_wins += 1
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == wo:
        winner.write('Circle Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_o.setposition(0, 200)
        winner_o.setheading(-90)
        winner_o.pendown()
        winner_o.fd(400)
        winner_o.penup()
        winner_o.setheading(0)
        o_wins += 1
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == eo:
        winner.write('Circle Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_o.setposition(137.5, 200)
        winner_o.setheading(-90)
        winner_o.pendown()
        winner_o.fd(400)
        winner_o.penup()
        winner_o.setheading(0)
        o_wins += 1
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == doa:
        winner.write('Circle Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_o.setposition(-200, 200)
        winner_o.setheading(-45)
        winner_o.pendown()
        winner_o.fd(565.68)
        winner_o.penup()
        winner_o.setheading(0)
        o_wins += 1
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == dob:
        winner.write('Circle Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_o.setposition(200, 200)
        winner_o.setheading(-135)
        winner_o.pendown()
        winner_o.fd(565.68)
        winner_o.penup()
        winner_o.setheading(0)
        o_wins += 1
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    # winning statements crosses
    elif 3 == ax:
        winner.write('Crosses Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_x.setposition(-200, 137.5)
        winner_x.pendown()
        winner_x.fd(400)
        winner_x.penup()
        x_wins += 1
        winner_x.setheading(0)
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == bx:
        winner.write('Crosses Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_x.setposition(-200, 0)
        winner_x.pendown()
        winner_x.fd(400)
        winner_x.penup()
        x_wins += 1
        winner_x.setheading(0)
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == cx:
        winner.write('Crosses Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_x.setposition(-200, -137.5)
        winner_x.pendown()
        winner_x.fd(400)
        winner_x.penup()
        x_wins += 1
        winner_x.setheading(0)
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == qx:
        winner.write('Crosses Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_x.setposition(-137.5, 200)
        winner_x.setheading(-90)
        winner_x.pendown()
        winner_x.fd(400)
        x_wins += 1
        winner_x.penup()
        winner_x.setheading(0)
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == wx:
        winner.write('Crosses Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_x.setposition(0, 200)
        winner_x.setheading(-90)
        winner_x.pendown()
        winner_x.fd(400)
        winner_x.penup()
        winner_x.setheading(0)
        x_wins += 1
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == ex:
        winner.write('Crosses Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_x.setposition(137.5, 200)
        winner_x.setheading(-90)
        winner_x.pendown()
        winner_x.fd(400)
        winner_x.setheading(0)
        x_wins += 1
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == dxa:
        winner.write('Crosses Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_x.setposition(-200, 200)
        winner_x.setheading(-45)
        winner_x.pendown()
        winner_x.fd(565.68)
        winner_x.penup()
        winner_x.setheading(0)
        x_wins += 1
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif 3 == dxb:
        winner.write('Crosses Scores', False, align='left', font=('Arial', 20, 'normal'))
        winner_x.setposition(200, 200)
        winner_x.setheading(-135)
        winner_x.pendown()
        winner_x.fd(565.68)
        winner_x.penup()
        x_wins += 1
        winner_x.setheading(0)
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0
    elif Moves >= 9:
        winner.write('Tie!', False, align='center', font=('Arial', 50, 'normal'))
        winner_x.fd(565.68)
        winner_x.setheading(0)
        occupied = []
        ao = 0
        bo = 0
        co = 0
        qo = 0
        wo = 0
        eo = 0
        doa = 0
        dob = 0
        ax = 0
        bx = 0
        cx = 0
        qx = 0
        wx = 0
        ex = 0
        dxa = 0
        dxb = 0
        functions.clear_o()
        functions.clear_x()
        winner_o.clear()
        winner_x.clear()
        winner.clear()
        Moves = 0

    # best of 3
    if o_wins >= 3:
        winner.color('red')
        winner.write('Circle Wins!', False, align='center', font=('Arial', 50, 'normal'))
        break
    elif x_wins >= 3:
        winner.write('Cross Wins!', False, align='center', font=('Arial', 50, 'normal'))
        break

# delay
delay = input('Press Enter To Finish: ')
