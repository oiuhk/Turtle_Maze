''' first map '''
def map_one_func(Wall: object, wall_objects: list):
    # map borders
    for item in range(-300, 300, 20):
        wall_objects.append(Wall(-300, item))
    for item in range(-300, 300, 20):
        wall_objects.append(Wall(item, 300))
    for item in range(300, -300, -20):
        wall_objects.append(Wall(300, item))
    for item in range(300, -300, -20):
        wall_objects.append(Wall(item, -300))

    # walls
    for item in range(-220, -80, 20):
        wall_objects.append(Wall(item, 220))
    for item in range(220, 300, 20):
        wall_objects.append(Wall(-180, item))
    for item in range(-20, 200, 20):
        wall_objects.append(Wall(item, 220))
    for item in range(140, 220, 20):
        wall_objects.append(Wall(-20, item))
    for item in range(-140, -20, 20):
        wall_objects.append(Wall(item, 140))
    for item in range(120, 220, 20):
        wall_objects.append(Wall(180, item))
    for item in range(180, 300, 20):
        wall_objects.append(Wall(item, 120))
    for item in range(100, 160, 20):
        wall_objects.append(Wall(-140, item))
    for item in range(20, 160, 20):
        wall_objects.append(Wall(-220, item))
    for item in range(-220, -160, 20):
        wall_objects.append(Wall(item, 20))
    for item in range(-60, 20, 20):
        wall_objects.append(Wall(-180, item))
    for item in range(-300, -180, 20):
        wall_objects.append(Wall(item, -60))
    for item in range(-100, -40, 20):
        wall_objects.append(Wall(item, 20))
    for item in range(20, 60, 20):
        wall_objects.append(Wall(-40, item))
    for item in range(-40, 60, 20):
        wall_objects.append(Wall(item, 60))
    for item in range(20, 60, 20):
        wall_objects.append(Wall(40, item))
    for item in range(40, 200, 20):
        wall_objects.append(Wall(item, 20))
    for item in range(0, 300, 20):
        wall_objects.append(Wall(item, -100))
    for item in range(-180, -80, 20):
        wall_objects.append(Wall(0, item))
    for item in range(-180, 0, 20):
        wall_objects.append(Wall(item, -180))
    for item in range(-280, -160, 20):
        wall_objects.append(Wall(140, item))


''' second map '''
def map_two_func(Wall: object, wall_objects: list):
    # map borders
    for item in range(-300, 300, 20):
        wall_objects.append(Wall(-300, item))
    for item in range(-300, 300, 20):
        wall_objects.append(Wall(item, 300))
    for item in range(300, -300, -20):
        wall_objects.append(Wall(300, item))
    for item in range(300, -300, -20):
        wall_objects.append(Wall(item, -300))

    # walls
    for item in range(-200, -100, 20):
        wall_objects.append(Wall(item, 200))
    for item in range(200, -100, -20):
        wall_objects.append(Wall(-200, item))
    for item in range(-200, 0, 20):
        wall_objects.append(Wall(item, -100))
    for item in range(-100, -200, -20):
        wall_objects.append(Wall(0 ,item))
    for item in range(-280, -200, -20):
        wall_objects.append(Wall(-200 ,item))
    for item in range(-60, 120, 20):
        wall_objects.append(Wall(item, -200))
    for item in range(-140, -220, -20):
        wall_objects.append(Wall(item, -200))
    for item in range(-200, -300, -20):
        wall_objects.append(Wall(-220, item))
    for item in range(-240, -200, 20):
        wall_objects.append(Wall(-140, item))
    for item in range(-280, -200, 20):
        wall_objects.append(Wall(100, item))
    for item in range(-120, -60, 20):
        wall_objects.append(Wall(item, 120))
    for item in range(120, 60, -20):
        wall_objects.append(Wall(-60, item))
    for item in range(-60, -200, -20):
        wall_objects.append(Wall(item, 60))
    for item in range(60, 300, 20):
        wall_objects.append(Wall(40, item))
    for item in range(40, 200, 20):
        wall_objects.append(Wall(item, 60))
    for item in range(60, 240, 20):
        wall_objects.append(Wall(200, item))
    for item in range(120, 200, 20):
        wall_objects.append(Wall(item, 220))
    for item in range(140, 220, 20):
        wall_objects.append(Wall(120, item))
    for item in range(-120, 300, 20):
        wall_objects.append(Wall(item, -20))
    for item in range(80, 300, 20):
        wall_objects.append(Wall(item, -120))
    for item in range(180, 300, 20):
        wall_objects.append(Wall(item, -200))


''' third map '''
def map_three_func(Wall: object, wall_objects: list):
    # map borders
    for item in range(-300, 300, 20):
        wall_objects.append(Wall(-300, item))
    for item in range(-300, 300, 20):
        wall_objects.append(Wall(item, 300))
    for item in range(300, -300, -20):
        wall_objects.append(Wall(300, item))
    for item in range(300, -300, -20):
        wall_objects.append(Wall(item, -300))

    # walls
    for item in range(0, 300, 20):
        wall_objects.append(Wall(-200, item))
    for item in range(-280, -100, 20):
        wall_objects.append(Wall(-200, item))
    for item in range(-180, -100, 20):
        wall_objects.append(Wall(item, -120))
    for item in range(-120, 220, 20):
        wall_objects.append(Wall(-100, item))
    for item in range(-100, 200, 20):
        wall_objects.append(Wall(item, 220))
    for item in range(0, 300, 20):
        wall_objects.append(Wall(item, 140))
    for item in range(-80, 120, 20):
        wall_objects.append(Wall(item, 60))
    for item in range(-60, 60, 20):
        wall_objects.append(Wall(60, item))
    for item in range(-20, 60, 20):
        wall_objects.append(Wall(item, -60))
    for item in range(-60, 0, 20):
        wall_objects.append(Wall(-20, item))
    for item in range(140, 300, 20):
        wall_objects.append(Wall(item, 0))
    for item in range(-180, 0, 20):
        wall_objects.append(Wall(140, item))
    for item in range(-20, 140, 20):
        wall_objects.append(Wall(item, -180))
    for item in range(-280, -60, 20):
        wall_objects.append(Wall(220, item))