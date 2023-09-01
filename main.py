from turtle import (Turtle, hideturtle, 
                    bgcolor, title, getscreen, 
                    write, color, done)

from time import sleep

from maps import (map_one_func,
                  map_two_func, 
                  map_three_func)

from spawn_objects import (level_1_mob_spawn, 
                           level_2_mob_spawn,
                           level_3_mob_spawn)



''' Turtle managed object '''
class Main_character(Turtle):
    def __init__(self, x: int, y: int, shp: str, clr: str):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.color(clr)
        self.shape(shp)
        self.step = 10
        self.point = 0
    def check(self):
        for wall_item in wall_objects:
            if wall_item.is_collision(self):
                return True
        return False
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
        if self.check():
            self.goto(self.xcor(), self.ycor() - self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
        if self.check():
            self.goto(self.xcor(), self.ycor() + self.step)
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())
        if self.check():
            self.goto(self.xcor() - self.step, self.ycor())
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
        if self.check():
            self.goto(self.xcor() + self.step, self.ycor())
    def is_collide(self, player: Turtle):
        dist = self.distance(player.xcor(), player.ycor())
        if dist < (self.step * 2):
            return True
        return False

''' Evil mobile bots '''
class Evil_Bots(Turtle):
    def __init__(self, x: int, y: int, shp: str, clr: str, stp: int):
        super().__init__()
        self.penup()
        self.shape(shp)
        self.color(clr)
        self.pensize(10)
        self.goto(x, y)
        self.speed(0)
        self.step = stp
    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.setheading(self.towards(x_end, y_end))
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

''' Wall creation object '''
class Wall(Turtle):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.penup()
        self.speed(20)
        self.goto(x, y)
        self.shape('square')
        self.color('#FFEBCD')
        self.goto(x, y)
        self.width = 35
        self.height = 30
    def is_collision(self, other):
        if (self.xcor() + self.width / 2) > other.xcor() - 5 and \
            (self.xcor() - self.width / 2) < other.xcor() + 5 and \
                (self.ycor() + self.height / 2) > other.ycor() - 5 and \
                    (self.ycor() - self.height / 2) < other.ycor() + 5:
            return True
        return False

''' Game endings '''
def end(scr, health):
    sleep(1)
    scr.bgcolor('black')
    scr.reset()   
    scr.clear()
    sleep(1)
    if health == 3:
        color('#3CB371')
        sleep(1)
        write(arg=f'YOU WIN', align='center', font=('', 50, 'bold'))
    else:
        color('#DB7093')
        sleep(1)
        write(arg='YOU DIED', align='center', font=('', 50, 'bold'))
    done()


''' Main function (setting objects and combining maps) '''
def main():
    global wall_objects
    wall_objects = []

    hideturtle()
    health = 3

    scr = getscreen()
    bgcolor('black')
    title('maze')

    map_one_func(Wall, wall_objects)
    bgcolor('#708090')
    health = level_1_mob_spawn(scr, health, Main_character, Evil_Bots)
    if health == 0: end(scr, health)
    
    wall_objects = []
    
    bgcolor('black')
    scr.reset()
    scr.clearscreen()
    bgcolor('black')

    map_two_func(Wall, wall_objects)
    bgcolor('#708090')
    health = level_2_mob_spawn(scr, health, Main_character, Evil_Bots)
    if health == 0: end(scr, health)

    wall_objects = []

    bgcolor('black')
    scr.reset()
    scr.clearscreen()
    bgcolor('black')

    map_three_func(Wall, wall_objects)
    bgcolor('#708090')
    health = level_3_mob_spawn(scr, health, Main_character, Evil_Bots)
    if health == 0: end(scr, health)

    end(scr, health)
    
    
''' Start '''
if __name__ == '__main__':
    main()