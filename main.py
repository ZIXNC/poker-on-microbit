def on_button_pressed_ab():
    basic.pause(1000)
    basic.show_number(HEARTS)
    basic.clear_screen()
    basic.pause(1000)
    basic.show_number(CLUBS)
    basic.clear_screen()
    basic.pause(1000)
    basic.show_number(DIAMONDS)
    basic.clear_screen()
    basic.pause(1000)
    basic.show_number(SPADES)
    basic.clear_screen()
    basic.pause(1000)
    
    if (CLUBS == SPADES and SPADES == DIAMONDS) or (CLUBS == SPADES and SPADES == HEARTS) or (CLUBS == DIAMONDS and DIAMONDS == HEARTS) or (SPADES == DIAMONDS and DIAMONDS == HEARTS):
        basic.show_string("THREE OF A KIND")
        basic.clear_screen()
        basic.pause(1000)
    elif (CLUBS == SPADES and DIAMONDS == HEARTS) or (CLUBS == DIAMONDS and HEARTS == SPADES) or (CLUBS == HEARTS and DIAMONDS == SPADES):
        basic.show_string("TWOPAIR")
        basic.clear_screen()
        basic.pause(1000)
    elif CLUBS == SPADES or DIAMONDS == HEARTS or CLUBS == DIAMONDS or CLUBS == HEARTS or DIAMONDS == SPADES or HEARTS == SPADES:
        basic.show_string("ONEPAIR")
        basic.clear_screen()
        basic.pause(1000)
    else:
        basic.show_string("NO PAIR")
        basic.clear_screen()

input.on_button_pressed(Button.AB, on_button_pressed_ab)

SPADES = 0
CLUBS = 0
DIAMONDS = 0
HEARTS = 0
HEARTS = randint(1, 5)
DIAMONDS = randint(1, 5)
CLUBS = randint(1, 5)
SPADES = randint(1, 5)