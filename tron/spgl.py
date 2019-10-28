# Simple Python Game Library Version 0.8.5.5 by /u/wynand1004 AKA @TokyoEdTech
# Documentation on Github: https://wynand1004.github.io/SPGL
# Python 2.x and 3.x Compatible

import os
import turtle
import time
import random
import math
import pickle
import platform

# Import message box
# This code is necessary for Python 2.x and 3.x compatibility
try:
    import tkMessageBox as messagebox
except:
    from tkinter import messagebox

# Import filedialog
try:
	from tkinter import filedialog
except:
	import tkFileDialog as filedialog


# If on Windows, import winsound or, better yet, switch to Linux!
if platform.system() == "Windows":
    try:
        import winsound
    except:
        print ("Winsound module not available.")


# Use for Keyboard Bindings
KEY_UP = "Up"
KEY_DOWN = "Down"
KEY_LEFT = "Left"
KEY_RIGHT = "Right"
KEY_SPACE = "space"
KEY_ESCAPE = "Escape"
KEY_ENTER = "Return"
KEY_RETURN = "Return"
KEY_SHIFT_LEFT = "Shift_L"
KEY_SHIFT_RIGHT = "Shift_R"
KEY_CONTROL_LEFT = "Control_L"
KEY_CONTROL_RIGHT = "Control_R"
KEY_ALT_LEFT = "Alt_L"
KEY_ALT_RIGHT = "Alt_R"
KEY_CAPS_LOCK = "Caps_Lock"
KEY_F1 = "F1"
KEY_F2 = "F2"
KEY_F3 = "F3"
KEY_F4 = "F4"
KEY_F5 = "F5"
KEY_F6 = "F6"
KEY_F7 = "F7"
KEY_F8 = "F8"
KEY_F9 = "F9"
KEY_F10 = "F10"
KEY_F11 = "F11"
KEY_F12 = "F12"

# Game Class
class Game(object):

    # Keep List of Sprites
    sprites = []

    # Keep List of Labels
    labels = []

    # Keep List of Buttons
    buttons = []

    # Logs
    logs = []

    def __init__(
                self,
                screen_width = 800,
                screen_height = 600,
                background_color = "black",
                title = "Simple Game Library by /u/wynand1004 AKA @TokyoEdTech",
                splash_time = 3):

        # Setup using Turtle module methods
        turtle.setup(width=screen_width, height=screen_height)
        turtle.bgcolor(background_color)
        turtle.title(title)
        turtle.tracer(0) # Stop automatic screen refresh
        turtle.listen() # Listen for keyboard input
        turtle.hideturtle() # Hides default turtle
        turtle.penup() # Puts pen up for defaut turtle
        turtle.setundobuffer(0) # Do not keep turtle history in memory
        turtle.onscreenclick(self.click)

        # Game Attributes
        self.FPS = 30.0 # Lower this on slower computers or with large number of sprites
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.DATAFILE = "game.dat"
        self.SPLASHFILE = "splash.gif" # Must be in the same folder as game file

        self.title = title
        self.gravity = 0
        self.state = "showsplash"
        self.splash_time = splash_time

        self.time = time.time()

        # Clear the terminal and print the game title
        self.clear_terminal_screen()
        print (self.title)

        # Show splash
        self.show_splash(self.splash_time)

    # Pop ups
    def ask_yes_no(self, title, message):
        return messagebox.askyesno(title, message)

    def show_info(self, title, message):
        return messagebox.showinfo(title, message)

    def show_warning(self, title, message):
        return messagebox.showwarning(title, message)

    def show_error(self, title, message):
        return messagebox.showerror(title, message)

    def ask_question(self, title, message):
        return messagebox.askquestion(title, message)

    def ask_ok_cancel(self, title, message):
        return messagebox.askokcancel(title, message)

    def ask_retry_cancel(self, title, message):
        return messagebox.askretrycancel(title, message)

    def ask_open_filename(self):
        return filedialog.askopenfilename()

    def print_error_logs(self):
        print ("Error Logs:")

        if len(Game.logs) == 0:
            print ("No errors")
        else:
            for error in Game.logs:
                print (error)


        print ("")

    def tick(self):
        # Check the game state
        # showsplash, running, gameover, paused

        if self.state == "showsplash":
            self.show_splash(self.splash_time)

        elif self.state == "paused":
            pass

        elif self.state == "gameover":
            pass

        else:
            # Iterate through all sprites and call their tick method
            for sprite in Game.sprites:
                if sprite.state:
                    sprite.tick()

            # Iterate through all labels and call their update method
            for label in Game.labels:
                if label.text != "":
                    label.tick()

        # Update the screen
        self.update_screen()

    def click(self, x, y):
        print ("The window was clicked at ({},{})".format(x, y))

    def show_splash(self, seconds):
        # Show splash screen
        # To be implemented

        try:
            # Load self.SPLASHFILE
            turtle.bgpic(self.SPLASHFILE)

            self.update_screen()

            # Pause
            self.time = time.time()
            while time.time() < self.time + (self.splash_time):
                pass

            # Hide Splash
            turtle.bgpic("")

        except:
            Game.logs.append("Warning: {} missing from disk.".format(self.SPLASHFILE))

        # Change state to running
        self.state = "running"

    def destroy_all_sprites(self):
        for sprite in Game.sprites:
            if sprite.state:
                sprite.destroy()

    def save_data(self, key, value):
        # Load DATAFILE
        try:
            data = pickle.load(open(self.DATAFILE, "rb"))
        except:
            data = {}
            Game.logs.append("Warning: Creating new {} file on disk.".format(self.DATAFILE))

        data[key] = value

        #Save DATAFILE
        pickle.dump(data, open(self.DATAFILE, "wb"))

    def load_data(self, key):
        # Load DATAFILE
        try:
            data = pickle.load(open(self.DATAFILE, "rb"))
        except:
            data = {}
            Game.logs.append("Warning: {} missing from disk.".format(self.DATAFILE))

        if key in data:
            return data[key]
        else:
            return None

    def set_title(self, title):
        turtle.title(title)
        self.title = title

    def set_keyboard_binding(self, key, function):
        # Allow any order of arguments as this is reversed from Tkinter
        # Check if key is a string. If not, reverse the arguments
        if type(key) is not str:
            temp = key
            key = function
            function = temp

        # Python 3
        try:
            turtle.onkeypress(function, key)
        # Python 2
        except:
            turtle.onkey(function, key)

    def update_screen(self):
        while time.time() < self.time + (1.0 / self.FPS):
            pass
        turtle.update()
        self.time = time.time()

    def play_sound(self, sound_file, time = 0):
        # Windows
        if platform.system() == 'Windows':
            winsound.PlaySound(sound_file, winsound.SND_ASYNC)
        # Linux
        elif platform.system() == "Linux":
            os.system("aplay -q {}&".format(sound_file))
        # Mac
        else:
            os.system("afplay {}&".format(sound_file))

        if time > 0:
	        turtle.ontimer(lambda: self.play_sound(sound_file, time), t=int(time * 1000))

    def stop_all_sounds(self):
        # Windows
        if platform.system() == 'Windows':
            Game.logs.append("Warning: .stop_all_sounds not implemened on Windows yet.")
        # Linux
        elif platform.system() == "Linux":
            os.system("killall aplay")
        # Mac
        else:
            os.system("killall afplay")

    def clear_terminal_screen(self):
        # Windows
    	if platform.system() == 'Windows':
    		os.system("cls")
        # Linux and Mac
    	else:
    		os.system("clear")

    def print_game_info(self):
        print (self.title)
        print ("")
        print ("Window Dimensions: {}x{}".format(self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        print ("")

        # Calcuate number of active sprites
        active_sprites = 0
        for sprite in Game.sprites:
            if sprite.state:
                active_sprites += 1

        print ("Number of Sprites (Active / Total): {} / {}".format(active_sprites, len(Game.sprites)))

        print ("Number of Labels: {}".format(len(Game.labels)))
        print ("Number of Buttons: {}".format(len(Game.buttons)))
        print ("")
        print ("Frames Per Second (Target): {}".format(self.FPS))
        print ("")
        self.print_error_logs()

    def is_collision(self, sprite_1, sprite_2):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(sprite_1.xcor() - sprite_2.xcor()) * 2) < (sprite_1.width + sprite_2.width)
        y_collision = (math.fabs(sprite_1.ycor() - sprite_2.ycor()) * 2) < (sprite_1.height + sprite_2.height)
        return (x_collision and y_collision)

    def is_circle_collision(self, sprite_1, sprite_2, radius):
        # Collision based on distance
    	a=sprite_1.xcor()-sprite_2.xcor()
    	b=sprite_1.ycor()-sprite_2.ycor()
    	distance = math.sqrt((a**2) + (b**2))

    	if distance < radius:
    		return True
    	else:
    		return False

    def show_game_over(self):
        self.state = "gameover"
        self.hide_all_sprites()
        print ("Game Over!")
        self.state = "paused"

    def set_background(self, image):
        if image.endswith(".gif"):
            turtle.bgpic(image)
        else:
            Game.logs.append("Warning: Background image {} must be a gif.".format(image))

    def exit(self):
        self.stop_all_sounds()
        os._exit(0)

# Sprite Class
class Sprite(turtle.Turtle):
    def __init__(self,
                shape,
                color,
                x = 0,
                y = 0,
                width = 20,
                height = 20):

        turtle.Turtle.__init__(self)
        self.speed(0) # Animation Speed
        # Register shape if it is a .gif file
        if shape.endswith(".gif"):
            try:
                turtle.register_shape(shape)
            except:
                Game.logs.append("Warning: {} file missing from disk.".format(shape))

                # Set placeholder shape
                shape = "square"
                width = 20 # This is the default for turtle module primitives
                height = 20 # This is the default for turtle module primitives

        self.shape(shape)
        self.color(color)
        self.penup()
        self.goto(x, y)

        # Attributes
        self.width = width
        self.height = width

        self.speed = 0.0 # Speed of motion
        self.dx = 0.0
        self.dy = 0.0
        self.acceleration = 0.0
        self.friction = 0.0

        self.state = "active"
        self.solid = True

        #Set click binding
        self.onclick(self.click)

        # Append to master sprite list
        Game.sprites.append(self)

    def tick(self):
        # This is the function that is called each frame of the game
        # For most sprites, you'll want to call the move method here
        # self.move()
        pass

    def move(self):
        self.fd(self.speed)

    def destroy(self):
        # When a sprite is destoyed move it off screen, hide it, and set state to None
        # This is a workaround as there is no way to delete a sprite from memory in the turtle module.
        self.hideturtle()
        self.goto(10000, 10000)
        self.state = None

    def set_image(self, image, width, height):
        # Allows the use of custom images (must be .gif) due to turtle/tkinter limitation
        # Register shape if it is a .gif file
        if image.endswith(".gif"):
            try:
                turtle.register_shape(image)
            except:
                Game.logs.append("Warning: {} file missing from disk.".format(image))

                # Set placeholder shape
                image = "square"
                width = 20 # This is the default for turtle module primitives
                height = 20 # This is the default for turtle module primitives

        self.shape(image)
        self.width = width
        self.height = height

        # Click binding needs to be set again after image change
        self.onclick(self.click)

    def set_bounding_box(self, width, height):
        self.width = width
        self.height = height

    def click(self, x, y):
        print ("The sprite was clicked at ({},{})".format(x, y))

    def rotate_left(self, degrees):
        self.lt(degrees)
		
    def rotate_right(self, degrees):
        self.rt(degrees)
		
    def go_forward(self, distance):
        self.fd(distance)
		
    def go_backward(self, distance):
        self.fd(-distance)
		

#Label Class
class Label(turtle.Turtle):
    def __init__(self,
                text,
                color,
                x = 0,
                y = 0,
                font_name = "Arial",
                font_size = 12,
                font_type = "normal",
                align = "left"):

        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.color(color)
        self.font_name = font_name
        self.font_size = font_size
        self.font_type = font_type
        self.font = (font_name, font_size, font_type)
        self.align = align

        # Attributes
        self.text = text

        # Append to master label list
        Game.labels.append(self)

    def tick(self):
        self.clear()
        self.write(self.text, False, align =self.align, font = self.font)

    def update(self, text):
        self.text = text
        self.tick()
        
    def set_font_name(self, font_name):
        self.font_name = font_name
        self.font = (self.font_name, self.font_size, self.font_type)

    def set_font_size(self, font_size):
        self.font_size = font_size
        self.font = (self.font_name, self.font_size, self.font_type)
        
    def set_font_type(self, font_type):
        self.font_type = font_type
        self.font = (self.font_name, self.font_size, self.font_type)
    


#Button Class
class Button(turtle.Turtle):
    def __init__(self,
                shape,
                color,
                x = 0,
                y = 0):

        turtle.Turtle.__init__(self)
        # self.hideturtle()
        self.penup()
        # Register shape if it is a .gif file
        if shape.endswith(".gif"):
            try:
                turtle.register_shape(shape)
            except:
                Game.logs.append("Warning: {} file missing from disk.".format(shape))

                # Set placeholder shape
                shape = "square"

        self.shape(shape)
        self.color(color)
        self.goto(x, y)

        #Set click binding
        self.onclick(self.click)

        # Append to master button list
        Game.buttons.append(self)

    def set_image(self, image):
        # Register shape if it is a .gif file
        if shape.endswith(".gif"):
            try:
                turtle.register_shape(shape)
            except:
                Game.logs.append("Warning: {} file missing from disk.".format(shape))

                # Set placeholder shape
                shape = "square"

        # Allows the use of custom images (must be .gif) due to turtle/tkinter limitation
        self.shape(image)

        # Click binding needs to be set again after image change
        self.onclick(self.click)

    def click(self, x, y):
        print ("The button was clicked at ({},{})".format(x, y))
