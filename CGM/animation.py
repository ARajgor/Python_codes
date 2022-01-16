import turtle

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("grey12")
#wn.bgpic("e.jpg")
#wn.addshape("e.gif")
wn.setup(width=800, height=600)  # screen_size
wn.tracer(0)

# score
score_a = 0
score_b = 0


# Bar A
bar_a = turtle.Turtle()
bar_a.speed(0)  # speed_of_animation
bar_a.shape("square")
bar_a.color("white")
bar_a.shapesize(stretch_wid=5, stretch_len=0.5)
bar_a.penup()
bar_a.goto(-385, 0)

# Bar B
bar_b = turtle.Turtle()
bar_b.speed(0)  # speed_of_animation
bar_b.shape("square")
bar_b.color("white")
bar_b.shapesize(stretch_wid=5, stretch_len=0.5)
bar_b.penup()
bar_b.goto(380, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed_of_animation
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.080
ball.dy = 0.08

# pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 20, "normal"))

# pen1

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(260, 280)
pen1.write("5 Point to Win", align="left", font=("Arial", 10, "normal"))

# function

def bar_a_up():
    y = bar_a.ycor()  # getting_y_coordinate
    y = y + 20
    bar_a.sety(y)  # new_position


def bar_a_down():
    y = bar_a.ycor()  # getting_y_coordinate
    y = y - 20
    bar_a.sety(y)  # new_position


def bar_b_up():
    y = bar_b.ycor()  # getting_y_coordinate
    y = y + 20
    bar_b.sety(y)  # new_position


def bar_b_down():
    y = bar_b.ycor()  # getting_y_coordinate
    y = y - 20
    bar_b.sety(y)  # new_position


# Keyboard_binding
wn.listen()  # listen_for_input
wn.onkeypress(bar_a_up, "w")  # When_w_press_call_bar_a_up_function
wn.onkeypress(bar_a_down, "s")  # When_s_press_call_bar_a_down_function

wn.onkeypress(bar_b_up, "Up")  # When_Up_press_call_bar_b_up_function
wn.onkeypress(bar_b_down, "Down")  # When_Down_press_call_bar_b_down_function

# main game loop
while True:
    wn.update()

    # move_the_ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border_checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1  # Reverse_the_direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1  # Reverse_the_direction

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1    # score_when_ball_go_off_screen
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Arial", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1    # score_when_ball_go_off_screen
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Arial", 20, "normal"))

    # bar_and_ball_collisions
    if (370 < ball.xcor() < 380) and (ball.ycor() < bar_b.ycor() + 40 and ball.ycor() > bar_b.ycor() - 40):
        ball.setx(370)
        ball.dx = ball.dx * -1

    if (-370 > ball.xcor() > -380) and (ball.ycor() < bar_a.ycor() + 40 and ball.ycor() > bar_a.ycor() - 40):
        ball.setx(-370)
        ball.dx = ball.dx * -1

    if score_a == 5 or score_b == 5:
        wn.bye()