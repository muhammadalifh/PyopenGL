import turtle 

animal = turtle.Turtle()

turtle.screensize(canvwidth=300, canvheight=300, 
                  bg="black") 
turtle.title("Tugas 3 🐮")

def ring(col, rad): 
	animal.fillcolor(col)  
	animal.begin_fill() 
	animal.circle(rad)  
	animal.end_fill() 

def talloval(col, rad):
	animal.fillcolor(col)
	animal.begin_fill()
	animal.left(45)
	for loop in range(2):      
		animal.circle(rad,90)   
		animal.circle(rad/2,90)      
	animal.end_fill() 

def flatoval_right(col, rad):		
	animal.fillcolor(col)
	animal.begin_fill()
	animal.right(-100)
	for loop in range(2):
		animal.circle(rad,90)
		animal.circle(rad/2,90)
	animal.end_fill() 

def flatoval_left(col, rad):		
	animal.fillcolor(col)
	animal.begin_fill()
	animal.left(45)
	for loop in range(2):
		animal.circle(rad,90)
		animal.circle(rad/2,90)
	animal.end_fill()


##### Draw Body ##### 
animal.up() 
animal.setpos(-10, -208) 
animal.down()
ring("red", 180) 



##### Draw face ##### 
animal.up() 
animal.setpos(20, 0) 
animal.down() 
talloval("red", 100) 

##### Draw ears ##### 
# Draw first ear 
animal.up() 
animal.setpos(-35, 150) 
animal.down() 
flatoval_left("red", 25)

# Draw second ear 
animal.up() 
# animal.setpos(15, 165) 
animal.setpos(25, 178) 
animal.down() 
flatoval_right("red", 25)

##### Draw eyes white ##### 
# Draw first eye 
animal.up() 
animal.setpos(-45, 110) 
animal.down()
ring("white", 13) 

# Draw second eye 
animal.up() 
animal.setpos(10, 110) 
animal.down() 
ring("white", 13) 

##### Draw eyes blue ##### 
# Draw first eye 
animal.up() 
animal.setpos(-45, 100) 
animal.down() 
ring("blue", 5) 
# Draw second eye 
animal.up() 
animal.setpos(10, 100) 
animal.down() 
ring("blue", 5) 

##### Draw nose ##### 
# Draw first nose 
animal.up() 
animal.setpos(-5, 10) 
animal.down() 
ring("black", 5) 

# Draw second nose 
animal.up() 
animal.setpos(-20, 10) 
animal.down()
ring("black", 5)


##### Draw tongue ##### 
animal.up() 
animal.setpos(5, -5) 
animal.down() 
flatoval_left("pink", 15)


##### Draw first leg ##### 
animal.up()
animal.goto(70,-80)
animal.down()
animal.color("red")
animal.begin_fill()
animal.left(35)
for i in range(2):
	animal.forward(180)
	animal.left(90)
	animal.forward(10)
	animal.left(90)
animal.end_fill()

##### Draw second leg ##### 
animal.up()
animal.goto(-90,-80)
animal.down()
animal.color("red")
animal.begin_fill()
animal.left(0)
for i in range(2):
	animal.forward(180)
	animal.left(90)
	animal.forward(10)
	animal.left(90)
animal.end_fill()

##### Draw third leg ##### 
animal.up()
animal.goto(20,-80)
animal.down()
animal.color("red")
animal.begin_fill()
animal.left(0)
for i in range(2):
	animal.forward(165)
	animal.left(90)
	animal.forward(10)
	animal.left(90)
animal.end_fill()

##### Draw fourth leg ##### 
animal.up()
animal.goto(-40,-80)
animal.down()
animal.color("red")
animal.begin_fill()
animal.left(0)
for i in range(2):
	animal.forward(165)
	animal.left(90)
	animal.forward(10)
	animal.left(90)
animal.end_fill()


animal.hideturtle()  
turtle.mainloop()