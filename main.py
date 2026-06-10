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
    if CLUBS == SPADES or DIAMONDS == HEARTS or (CLUBS == DIAMONDS or CLUBS == HEARTS) or (DIAMONDS == SPADES or HEARTS == SPADES):
        basic.show_string("ONEPAIR")
        basic.clear_screen()
        basic.pause(1000)
    elif CLUBS == SPADES and DIAMONDS == HEARTS or CLUBS == DIAMONDS and HEARTS == SPADES or CLUBS == HEARTS and DIAMONDS == SPADES:
        basic.show_string("TWOPAIR")
        basic.clear_screen()
        basic.pause(1000)
    elif SPADES == DIAMONDS and (DIAMONDS == HEARTS and SPADES == HEARTS) or (DIAMONDS == HEARTS and (DIAMONDS == CLUBS and HEARTS == CLUBS) or (HEARTS == CLUBS and (HEARTS == SPADES and CLUBS == SPADES) or CLUBS == SPADES and (CLUBS == DIAMONDS and SPADES == DIAMONDS))):
        basic.show_string("THREE OF KIND ")
        basic.clear_screen()
        basic.pause(1000)
    elif False:
        basic.clear_screen()
    else:
        pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

SPADES = 0
CLUBS = 0
DIAMONDS = 0
HEARTS = 0
HEARTS = randint(1, 3)
DIAMONDS = randint(1, 3)
CLUBS = randint(1, 3)
SPADES = randint(1, 3)