import turtle
hoang = turtle.Turtle()
hoang.shape("turtle")
hoang.color("red")

# Hình vuông:
for i in range(4):
    hoang.forward(100)
    hoang.left(90)
    
hoang.penup()
hoang.goto(150,200)
hoang.pendown()   
    
# Hình tam giác:
for i in range(3):
    hoang.forward(100)
    hoang.left(120)
    
# Hình tròn: 
hoang.circle(100)

# Hình lục giác:
for i in range(6):
    hoang.forward(100)
    hoang.left(60)