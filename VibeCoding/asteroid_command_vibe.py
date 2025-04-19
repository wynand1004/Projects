import turtle
import random
import time
import math

# --- Setup ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WORLD_WIDTH = 2000
WORLD_HEIGHT = 2000

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
turtle.bgcolor("black")
turtle.title("Space Block Blaster")
turtle.tracer(0)

# --- Colors ---
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# --- Player ---
player = turtle.Turtle()
player.shape("triangle")
player.penup()
player.speed(0)
player.setheading(90)
player.shapesize(stretch_wid=0.3, stretch_len=2.0)
player_color = random.choice(colors)
player.color(player_color)
player.showturtle()

player_pos = [0, 0]
player_velocity = [0, 0]
player_speed = 0.3
player_health = 100

# --- Flame (Boost Effect) ---
flame = turtle.Turtle()
flame.shape("triangle")
flame.color("orange")
flame.shapesize(stretch_wid=0.2, stretch_len=0.5)
flame.penup()
flame.speed(0)
flame.hideturtle()

# --- Score ---
score = 0

# Score Display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-SCREEN_WIDTH//2 + 20, SCREEN_HEIGHT//2 - 40)

def update_score_display():
    score_display.clear()
    score_display.write(f"Score: {score}   HP: {player_health}   Color: {player_color.upper()}", font=("Arial", 16, "normal"))

update_score_display()

# --- Missiles ---
missiles = []

# --- Blocks ---
blocks = []

# --- Stars (background) ---
stars = []
for _ in range(200):
    star = turtle.Turtle()
    star.shape("circle")
    star.color("white")
    star.shapesize(stretch_wid=0.05, stretch_len=0.05)
    star.penup()
    star.speed(0)
    x = random.randint(-WORLD_WIDTH//2, WORLD_WIDTH//2)
    y = random.randint(-WORLD_HEIGHT//2, WORLD_HEIGHT//2)
    stars.append({"turtle": star, "x": x, "y": y})

# --- Powerups (hearts) ---
powerups = []
for _ in range(10):
    pu = turtle.Turtle()
    pu.shape("circle")
    pu.color("pink")
    pu.shapesize(stretch_wid=0.5, stretch_len=0.5)
    pu.penup()
    pu.speed(0)
    x = random.randint(-WORLD_WIDTH//2, WORLD_WIDTH//2)
    y = random.randint(-WORLD_HEIGHT//2, WORLD_HEIGHT//2)
    powerups.append({"turtle": pu, "x": x, "y": y})

# --- Generate Irregular Clusters ---
def generate_irregular_cluster(center_x, center_y, size, color_choice):
    cluster_positions = []

    for dx in range(-size//2, size//2 + 1):
        for dy in range(-size//2, size//2 + 1):
            if random.random() < 0.7:
                x = center_x + dx * 25
                y = center_y + dy * 25
                cluster_positions.append((x, y))

    for x, y in cluster_positions:
        block = turtle.Turtle()
        block.shape("square")
        block.color(color_choice)
        block.penup()
        block.speed(0)
        blocks.append({"turtle": block, "x": x, "y": y, "color": color_choice, "true_color": color_choice})

# Create clusters
for _ in range(25):
    center_x = random.randint(-WORLD_WIDTH//2, WORLD_WIDTH//2)
    center_y = random.randint(-WORLD_HEIGHT//2, WORLD_HEIGHT//2)
    cluster_size = random.choice([3, 5, 7])
    color_choice = random.choice(colors)
    generate_irregular_cluster(center_x, center_y, cluster_size, color_choice)

# --- Grey inside blocks ---
block_lookup = {}
for block in blocks:
    pos = (block["x"], block["y"])
    block_lookup[pos] = block

for block in blocks:
    x, y = block["x"], block["y"]
    neighbors = [(x+25, y), (x-25, y), (x, y+25), (x, y-25)]
    if all(n in block_lookup for n in neighbors):
        block["turtle"].color("grey")
        block["color"] = "grey"  # Current color shown
    # true_color remains the original color

# --- Controls ---
keys = {"left": False, "right": False, "up": False}

def left():
    keys["left"] = True
def right():
    keys["right"] = True
def up():
    keys["up"] = True
def stop_left():
    keys["left"] = False
def stop_right():
    keys["right"] = False
def stop_up():
    keys["up"] = False

def fire_missile():
    missile = turtle.Turtle()
    missile.shape("triangle")
    missile.color("white")
    missile.shapesize(stretch_wid=0.2, stretch_len=0.8)
    missile.penup()
    missile.speed(0)
    missile.setheading(player.heading())
    missile.goto(player_pos[0], player_pos[1])
    missiles.append({"turtle": missile, "x": player_pos[0], "y": player_pos[1]})

turtle.listen()
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(up, "Up")
turtle.onkeyrelease(stop_left, "Left")
turtle.onkeyrelease(stop_right, "Right")
turtle.onkeyrelease(stop_up, "Up")
turtle.onkeypress(fire_missile, "space")

# --- Game Loop ---
last_time = time.time()

def move():
    global last_time, score, player_health
    now = time.time()
    delta = now - last_time
    last_time = now

    if player_health <= 0:
        turtle.bye()
        print("Game Over!")
        return

    # --- Player Movement ---
    if keys["left"]:
        player.left(200 * delta)
    if keys["right"]:
        player.right(200 * delta)
    if keys["up"]:
        angle = math.radians(player.heading())
        player_velocity[0] += math.cos(angle) * player_speed * delta
        player_velocity[1] += math.sin(angle) * player_speed * delta

    player_pos[0] += player_velocity[0] * 100
    player_pos[1] += player_velocity[1] * 100

    camera_x = player_pos[0]
    camera_y = player_pos[1]

    # --- Move Missiles ---
    for missile_data in missiles:
        missile = missile_data["turtle"]
        angle = math.radians(missile.heading())
        missile_data["x"] += math.cos(angle) * 500 * delta
        missile_data["y"] += math.sin(angle) * 500 * delta

    # --- Draw Stars ---
    for star_data in stars:
        star = star_data["turtle"]
        star.goto(star_data["x"] - camera_x, star_data["y"] - camera_y)

    # --- Collision Detection (Missile vs Block) ---
    missiles_to_remove = []
    blocks_to_remove = []
    for missile_data in missiles:
        mx, my = missile_data["x"], missile_data["y"]
        for block_data in blocks:
            bx, by = block_data["x"], block_data["y"]
            distance = math.hypot(mx - bx, my - by)
            if distance < 20:
                block_color = block_data["color"]
                if block_color == player_color:
                    score += 10
                else:
                    score -= 5
                update_score_display()

                # Explosion flash
                explosion = turtle.Turtle()
                explosion.shape("circle")
                explosion.color("yellow")
                explosion.shapesize(stretch_wid=0.3, stretch_len=0.3)
                explosion.penup()
                explosion.goto(bx - camera_x, by - camera_y)
                turtle.update()
                explosion.hideturtle()

                missiles_to_remove.append(missile_data)
                blocks_to_remove.append(block_data)
                break

    for missile_data in missiles_to_remove:
        missile_data["turtle"].hideturtle()
        missiles.remove(missile_data)
    for block_data in blocks_to_remove:
        pos = (block_data["x"], block_data["y"])
        if pos in block_lookup:
            del block_lookup[pos]
        block_data["turtle"].hideturtle()
        blocks.remove(block_data)

    # After removing blocks, check grey blocks if they are exposed
    for block in blocks:
        if block["color"] == "grey":
            x, y = block["x"], block["y"]
            neighbors = [(x+25, y), (x-25, y), (x, y+25), (x, y-25)]
            if not all(n in block_lookup for n in neighbors):
                block["turtle"].color(block["true_color"])
                block["color"] = block["true_color"]

    # --- Collision Detection (Player vs Block) ---
    for block_data in blocks:
        bx, by = block_data["x"], block_data["y"]
        distance = math.hypot(player_pos[0] - bx, player_pos[1] - by)
        if distance < 20:
            player_velocity[0] = 0
            player_velocity[1] = 0
            player_health -= 10
            update_score_display()
            break

    # --- Collision Detection (Player vs Powerups) ---
    for pu_data in powerups[:]:
        px, py = pu_data["x"], pu_data["y"]
        distance = math.hypot(player_pos[0] - px, player_pos[1] - py)
        if distance < 20:
            pu_data["turtle"].hideturtle()
            powerups.remove(pu_data)
            player_health = min(player_health + 20, 100)
            update_score_display()

    # --- Draw Powerups ---
    for pu_data in powerups:
        pu = pu_data["turtle"]
        pu.goto(pu_data["x"] - camera_x, pu_data["y"] - camera_y)

    # --- Draw Blocks ---
    for block_data in blocks:
        block = block_data["turtle"]
        block.goto(block_data["x"] - camera_x, block_data["y"] - camera_y)

    # --- Draw Missiles ---
    for missile_data in missiles:
        missile = missile_data["turtle"]
        missile.goto(missile_data["x"] - camera_x, missile_data["y"] - camera_y)

    # --- Draw Player ---
    player.goto(0, 0)

    # --- Draw Flame ---
    if keys["up"]:
        flame.showturtle()
        flame.setheading(player.heading())
        angle = math.radians(player.heading())
        flame.goto(-math.cos(angle) * 15, -math.sin(angle) * 15)
    else:
        flame.hideturtle()

    turtle.update()
    turtle.ontimer(move, 10)

move()
turtle.done()
