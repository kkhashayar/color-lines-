import turtle, random, math, time
from pygame import mixer

screen = turtle.Screen()
screen.setup(700,700,0)
screen.bgcolor("black")

mixer.init()
dropping = mixer.Sound("dropping.wav")
cleaning = mixer.Sound("Decline.wav")
player = mixer.Sound("jumpland.wav")
p2 = turtle.Turtle()
p2.hideturtle()
p2.penup()
p2.color("yellow")
p2.speed(0)
p2.setpos(0, -240)
p2.shape("classic")



class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.distance = 40
        self.space = 5
        self.row = 9
        self.col = 9
        self.board = []
        self.empty_positions = []
        self.taken_positions = []
        self.elements =[1,3,5,9]
        self.element = 0 # for picking 
        #self.element = True 
        self.computer_switch = True
        self.count = 0
        self.count_reset = 0 
        #-- Class internal attribs
        self.penup()
        self.speed(0)
        self.pencolor("yellow")
        self.shape("square")
        self.shapesize(self.distance/20)
        self.fillcolor("black")
        self.setpos(-280, 280)
        # For storing temporary information on picking the color
        self.temp_pos = []
        self.temp_board = []
        # For on screen texts
        self.score = 0 

    def reset_pick(self):
        turtle.onscreenclick(self.pick)
    def reset_drop(self):
        turtle.onscreenclick(self.drop)

    def build_board(self):
        for r in range(self.row):
            self.board.append([])
            for c in range(self.col):
                self.board[r].append(0)

    def print_board(self):
        print("************************")
        for r in range(self.row):
            print(self.board[r], end = "")
            print()

    def show_board(self):
        screen.tracer(False)
        for r in range(self.row):
            for c in range(self.col):
                self.stamp()
                self.empty_positions.append(self.pos())
                self.forward(self.distance)
            self.back(self.distance * self.row)
            self.right(90)
            self.forward(self.distance)
            self.left(90)
            self.hideturtle()
        #print("lenght of empty positions: ", len(self.empty_positions))
    # i try to convert the x,y  position to row,col
    # which is working but i think its very primitive way of doing it :(

    def delete_x_y(self, r,c):
        if r == 0:
            y = 280
        if r == 1:
            y = 240
        if r == 2:
            y = 200
        if r == 3:
            y = 160
        if r == 4:
            y = 120
        if r == 5:
            y = 80
        if r == 6:
            y = 40
        if r == 7:
            y = 0
        if r == 8:
            y = -40
        #--
        if c == 0:
            x = -280
        if c == 1:
            x = -240
        if c == 2:
            x = -200
        if c == 3:
            x = -160
        if c == 4:
            x = -120
        if c == 5:
            x = -80
        if c == 6:
            x = -40
        if c == 7:
            x = 0
        if c == 8:
            x = 40
##        print("values to be deleted: ")
##        print(x,y)
        self.hideturtle()
        self.speed(3)
        self.pencolor("black")
        self.fillcolor("black")
        self.goto(x,y)
        self.stamp()
        self.taken_positions.remove((x,y))

    def get_row_col(self, x,y):
        if y == 280:
            row = 0
        if y == 240:
            row = 1
        if y == 200:
            row = 2
        if y == 160:
            row = 3
        if y == 120:
            row = 4
        if y == 80:
            row = 5
        if y == 40:
            row = 6
        if y == 0:
            row = 7
        if y == -40:
            row = 8
        #--
        if x == -280:
            col = 0
        if x == -240:
            col = 1
        if x == -200:
            col = 2
        if x == -160:
            col = 3
        if x == -120:
            col = 4
        if x == -80:
            col = 5
        if x == -40:
            col = 6
        if x == 0:
            col = 7
        if x == 40:
            col = 8
        global row, col
        return row
        return col
                
    def computer_move(self):
        for i in range(3):
            if self.computer_switch is True:
                screen.tracer(True)
                self.speed(10)
                
                element = random.choice(self.elements)
                self.shape("circle")
                self.shapesize((self.distance/20) - 0.50)
                self.setpos(250, 200)
                self.speed(3)
                self.showturtle()

                if element == 1:
                    self.color("lightblue")
                    self.fillcolor("blue")
                elif element == 3:
                    self.color("lightblue")
                    self.fillcolor("red")
                elif element == 5:
                    self.color("lightblue")
                    self.fillcolor("green")
                elif element == 9:
                    self.color("lightblue")
                    self.fillcolor("orange")
                #--
                row = random.randrange(0,9)
                col = random.randrange(0,9)

                if row == 0:
                    y = 280
                if row == 1:
                    y = 240
                if row == 2:
                    y = 200
                if row == 3:
                    y = 160
                if row == 4:
                    y = 120
                if row == 5:
                    y = 80
                if row == 6:
                    y = 40
                if row == 7:
                    y = 0
                if row == 8:
                    y = -40
                #--
                if col == 0:
                    x = -280
                if col == 1:
                    x = -240
                if col == 2:
                    x = -200
                if col == 3:
                    x = -160
                if col == 4:
                    x = -120
                if col == 5:
                    x = -80
                if col == 6:
                    x = -40
                if col == 7:
                    x = 0
                if col == 8:
                    x = 40
        
                if self.board[row][col] == 0:
                    self.count +=1
                    self.board[row][col] = element
                    dropping.play()
                    self.goto(x,y)
                    self.stamp()
                    self.hideturtle()
                    self.taken_positions.append((x,y))
                    if self.count == 3:
                        self.computer_switch = False
                        self.count = self.count_reset
                        self.check_win(element)
                if self.board[row][col] != 0:
                    self.computer_move()
                    
##        self.print_board()
##        print("*")
##        print("lenght of empty positions: ", len(self.empty_positions))
##        print("lenght of taken positions: ", len(self.taken_positions))
        #self.reset_pick()

        
    def check_win(self, element):
    
        # check horizontal
        for c in range(self.col -3):
            for r in range(self.row):
                if self.board[r][c] == element and self.board[r][c+1]== element and self.board[r][c+2]== element and self.board[r][c+3]== element:
                    #print("horizontal .......")
                    self.board[r][c] = 0
                    self.delete_x_y(r,c)
                    self.board[r][c+1]= 0
                    self.delete_x_y(r,c+1)
                    self.board[r][c+2]= 0
                    self.delete_x_y(r,c+2)
                    self.board[r][c+3]= 0
                    self.delete_x_y(r,c+3)
                    cleaning.play()
                    self.score += 10
                    p2.clear()
                    p2.write(game.score, font = font_normal)
                    self.reset_pick()
                    
        # check vertical
        for c in range(self.col):
            for r in range(self.row - 3):
                if self.board[r][c] == element and self.board [r+1][c]== element and self.board[r+2][c] == element and self.board [r+3][c]== element:
                    #print("vertical .........")
                    self.board[r][c] = 0
                    self.delete_x_y(r,c)
                    self.board[r+1][c] = 0
                    self.delete_x_y(r+1,c)
                    self.board[r+2][c] = 0
                    self.delete_x_y(r+2,c)
                    self.board[r+3][c] = 0
                    self.delete_x_y(r+3,c)
                    cleaning.play()
                    self.score += 10
                    p2.clear()
                    p2.write(game.score, font = font_normal)
                    self.reset_pick()
               # Check positive Diagonal
        for c in range(self.col - 3):
            for r in range(self.row - 3):
                if self.board[r][c] == element and self.board [r+1][c+1]== element  and self.board[r+2][c+2] == element and self.board [r+3][c+3]==element:
                    #print ("positive diagonal.....")
                    self.board[r][c] =0
                    self.delete_x_y(r,c)
                    self.board[r+1][c+1] = 0
                    self.delete_x_y(r+1,c+1)
                    self.board[r+2][c+2] = 0
                    self.delete_x_y(r+2,c+2)
                    self.board[r+3][c+3] = 0
                    self.delete_x_y(r+3,c+3)
                    cleaning.play()
                    self.score += 10
                    p2.clear()
                    p2.write(game.score, font = font_normal)
                    self.reset_pick()
                    
        # Check negative Diagonal
        for c in range(self.col -3):
            for r in range(3, self.row):
                if self.board[r][c] == element and self.board [r-1][c+1]== element and self.board[r-2][c+2] == element and self.board [r-3][c+3]==element:
                    #print("negative diagonal........")
                    self.board[r][c] =0
                    self.delete_x_y(r,c)
                    self.board[r-1][c+1] = 0
                    self.delete_x_y(r-1,c+1)
                    self.board[r-2][c+2] = 0
                    self.delete_x_y(r-2,c+2)
                    self.board[r-3][c+3] = 0
                    self.delete_x_y(r-3,c+3)
                    cleaning.play()
                    self.score += 10
                    p2.clear()
                    p2.write(game.score, font = font_normal)
                    self.reset_pick()
                    
        if self.computer_switch == False:
            self.reset_pick()
                  
    def pick(self, x,y):
        # choosing the spot and picking the color 
##        print("**********")
##        print("picking method")
        x = int(self.distance * round(x/self.distance))
        y = int(self.distance * round(y/self.distance))
        #print("position on Gboard: ",x,y)
        if y == 280:
            row = 0
        if y == 240:
            row = 1
        if y == 200:
            row = 2
        if y == 160:
            row = 3
        if y == 120:
            row = 4
        if y == 80:
            row = 5
        if y == 40:
            row = 6
        if y == 0:
            row = 7
        if y == -40:
            row = 8
        #--
        if x == -280:
            col = 0
        if x == -240:
            col = 1
        if x == -200:
            col = 2
        if x == -160:
            col = 3
        if x == -120:
            col = 4
        if x == -80:
            col = 5
        if x == -40:
            col = 6
        if x == 0:
            col = 7
        if x == 40:
            col = 8
        self.element = (self.board[row][col])
        # if you choose an empty spot , it will redirect you here 
        if self.element == 0:
            self.color("black")
            self.fillcolor("black")
            #print("Value in 2D array: ",self.element)
            self.reset_pick()
        # matching the choosen color to its numeric value 
        elif self.element != 0:
            if self.element == 1:
                self.color("lightblue")
                self.fillcolor("blue")
            elif self.element == 3:
                self.color("lightblue")
                self.fillcolor("red")
            elif self.element == 5:
                self.color("lightblue")
                self.fillcolor("green")
            elif self.element == 9:
                self.color("lightblue")
                self.fillcolor("orange")
            elif self.element ==0:
                self.color("black")
                self.fillcolor("back")
            #show the picked color
            self.hideturtle()
            self.speed(0)
            self.setpos(30,-90)
            self.showturtle()
            # show the value of the spot
            #print("Value in 2D array: ",self.element)
            # storing the position on gboard
            self.temp_pos.append(x)
            self.temp_pos.append(y)
            # storing the position on 2
            self.temp_board.append(row)
            self.temp_board.append(col)
            self.reset_drop()

    
    def reset_pick(self):
        turtle.onscreenclick(self.pick)
    def reset_drop(self):
        turtle.onscreenclick(self.drop)
               
    def drop(self, xd,yd):
##        print("***********")
##        print("dropping  method")
        xd = int(self.distance * round(xd/self.distance))
        yd = int(self.distance * round(yd/self.distance))
        #print("position on Gboard: ",xd,yd)
        if yd == 280:
            row = 0
        if yd == 240:
            row = 1
        if yd == 200:
            row = 2
        if yd == 160:
            row = 3
        if yd == 120:
            row = 4
        if yd == 80:
            row = 5
        if yd == 40:
            row = 6
        if yd == 0:
            row = 7
        if yd == -40:
            row = 8
        #-
        if xd == -280:
            col = 0
        if xd == -240:
            col = 1
        if xd == -200:
            col = 2
        if xd == -160:
            col = 3
        if xd == -120:
            col = 4
        if xd == -80:
            col = 5
        if xd == -40:
            col = 6
        if xd == 0:
            col = 7
        if xd == 40:
            col = 8
        if self.board[row][col] != 0:
            # if you drop your selected color on its picked place, or on another color
            # you will redirected to picking method 
            #print("spot is taken")
            # Remove the selected color indicator 
            self.hideturtle()
            self.speed(0)
            self.setpos(30,-90)
            self.pencolor("black")
            self.fillcolor("black")
            self.stamp()
            # Remove Gboard pick temporary info 
            self.temp_board = []
            # Remove 2D arraye pick temporary info
            self.temp_pos = []
            self.reset_pick()
        # so now i have check win problem and path finding problem,
        # path finding problem
        if self.board[row][col] == 0:
            self.board[row][col] = self.element
            self.board[self.temp_board[0]][self.temp_board[1]] = 0
            self.temp_board = []
            self.taken_positions.append((xd,yd))
            self.goto(xd,yd)
            self.stamp()
            player.play()
            self.goto(self.temp_pos[0], self.temp_pos[1])
            self.pencolor("black")
            self.fillcolor("black")
            self.stamp()
            self.temp_pos = []
            self.computer_switch = True
            element = self.element
            self.check_win(element)
            self.computer_move()

font_bold = ("arial", "18", "bold")
font_normal = ("arial", "14", "bold")
def static_text():
    p1 = turtle.Turtle()
    p1.hideturtle()
    p1.penup()
    p1.color("lightgreen")
    p1.speed(0)
    p1.setpos(0, -200)
    p1.shape("classic")
    p1.write("score", font = font_bold)

##def dinamic_text(game):
##    p2 = turtle.Turtle()
##    p2.hideturtle()
##    p2.penup()
##    p2.color("yellow")
##    p2.speed(0)
##    p2.setpos(0, -240)
##    p2.shape("classic")
##    p2.clear()
##    p2.write(game.score, font = font_normal)

game = Game()
game.build_board()
game.show_board()
game.computer_move()
static_text()




    


        
        
        
