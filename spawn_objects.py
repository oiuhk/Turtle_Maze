''' Spawn of objects of the First level '''
def level_1_mob_spawn(scr, health: int, Main_character: object, Evil_Bots: object):
    player = Main_character(240, 180, 'turtle', '#DB7093')
    winner = Main_character(220, -220, 'turtle', '#3CB371')

    bot1 = Evil_Bots(60, -140, 'arrow', '#DC143C', 10)
    bot1.set_move(60, -140, 60, -260)

    bot2 = Evil_Bots(-260, 180, 'arrow', '#DC143C', 10)
    bot2.set_move(-260, 180, -80, 180)

    bot3 = Evil_Bots(80, 180, 'arrow', '#DC143C', 10)
    bot3.set_move(80, 180, 80, 80)

    bot4 = Evil_Bots(-60, -120, 'arrow', '#DC143C', 10)
    bot4.set_move(-60, -120, -260, -120)
    
    scr.onkey(player.move_up, 'Up')
    scr.onkey(player.move_left, 'Left')
    scr.onkey(player.move_right, 'Right')
    scr.onkey(player.move_down, 'Down')
    scr.listen()
    
    while health != 0:
        bot1.make_step()
        bot2.make_step()
        bot3.make_step()
        bot4.make_step()

        if player.is_collide(bot1):
            health -= 1; player.goto(240, 180)
        if player.is_collide(bot2):
            health -= 1; player.goto(240, 180)
        if player.is_collide(bot3):
            health -= 1; player.goto(240, 180)
        if player.is_collide(bot4):
            health -= 1; player.goto(240, 180)
        if player.is_collide(winner):
            break
    return health


''' Spawn objects of the Second level '''
def level_2_mob_spawn(scr, health: int, Main_character: object, Evil_Bots: object):
    player = Main_character(-180, -240, 'turtle', '#DB7093')
    winner = Main_character(220, -260, 'turtle', '#3CB371')

    bot1 = Evil_Bots(-40, -160, 'arrow', '#DC143C', 10)
    bot1.set_move(-40, -160, -260, -160)

    bot2 = Evil_Bots(-40, 160, 'arrow', '#DC143C', 10)
    bot2.set_move(-40, 160, -40, 260)

    bot3 = Evil_Bots(-160, 20, 'arrow', '#DC143C', 10)
    bot3.set_move(-160, 20, 260, 20)

    bot4 = Evil_Bots(260, -160, 'arrow', '#DC143C', 10)
    bot4.set_move(260, -160, 40, -160)
    
    scr.onkey(player.move_up, 'Up')
    scr.onkey(player.move_left, 'Left')
    scr.onkey(player.move_right, 'Right')
    scr.onkey(player.move_down, 'Down')
    scr.listen()
    
    while health != 0:
        bot1.make_step()
        bot2.make_step()
        bot3.make_step()
        bot4.make_step()

        if player.is_collide(bot1):
            health -= 1; player.goto(-180, -240)
        if player.is_collide(bot2):
            health -= 1; player.goto(-180, -240)
        if player.is_collide(bot3):
            health -= 1; player.goto(-180, -240)
        if player.is_collide(bot4):
            health -= 1; player.goto(-180, -240)
        if player.is_collide(winner):
            break
    return health


''' Spawn of objects of the Third level '''
def level_3_mob_spawn(scr, health: int, Main_character: object, Evil_Bots: object):
    player = Main_character(-260, 260, 'turtle', '#DB7093')
    winner = Main_character(260, -240, 'turtle', '#3CB371')

    bot1 = Evil_Bots(-260, -60, 'arrow', '#DC143C', 10)
    bot1.set_move(-260, -60, -140, -60)

    bot2 = Evil_Bots(240, 180, 'arrow', '#DC143C', 10)
    bot2.set_move(240, 180, 240, 260)

    bot3 = Evil_Bots(140, 60, 'arrow', '#DC143C', 10)
    bot3.set_move(140, 60, 260, 60)

    bot4 = Evil_Bots(-80, -160, 'arrow', '#DC143C', 10)
    bot4.set_move(-80, -160, -80, -260)
    
    scr.onkey(player.move_up, 'Up')
    scr.onkey(player.move_left, 'Left')
    scr.onkey(player.move_right, 'Right')
    scr.onkey(player.move_down, 'Down')
    scr.listen()
    
    while health != 0:
        bot1.make_step()
        bot2.make_step()
        bot3.make_step()
        bot4.make_step()
        if player.is_collide(bot1):
            health -= 1; player.goto(-260, 260)
        if player.is_collide(bot2):
            health -= 1; player.goto(-260, 260)
        if player.is_collide(bot3):
            health -= 1; player.goto(-260, 260)
        if player.is_collide(bot4):
            health -= 1; player.goto(-260, 260)
        if player.is_collide(winner):
            break
    return health