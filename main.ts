input.onButtonPressed(Button.AB, function () {
    basic.pause(1000)
    basic.showNumber(HEARTS)
    basic.clearScreen()
    basic.pause(1000)
    basic.showNumber(CLUBS)
    basic.clearScreen()
    basic.pause(1000)
    basic.showNumber(DIAMONDS)
    basic.clearScreen()
    basic.pause(1000)
    basic.showNumber(SPADES)
    basic.clearScreen()
    basic.pause(1000)
    if (CLUBS == SPADES || DIAMONDS == HEARTS || (CLUBS == DIAMONDS || CLUBS == HEARTS) || (DIAMONDS == SPADES || HEARTS == SPADES)) {
        basic.showString("ONEPAIR")
        basic.clearScreen()
        basic.pause(1000)
    } else if (CLUBS == SPADES && DIAMONDS == HEARTS || CLUBS == DIAMONDS && HEARTS == SPADES || CLUBS == HEARTS && DIAMONDS == SPADES) {
        basic.showString("TWOPAIR")
        basic.clearScreen()
        basic.pause(1000)
    } else if (SPADES == DIAMONDS && (DIAMONDS == HEARTS && SPADES == HEARTS) || (DIAMONDS == HEARTS && (DIAMONDS == CLUBS && HEARTS == CLUBS) || (HEARTS == CLUBS && (HEARTS == SPADES && CLUBS == SPADES) || CLUBS == SPADES && (CLUBS == DIAMONDS && SPADES == DIAMONDS)))) {
        basic.showString("THREE OF KIND ")
        basic.clearScreen()
        basic.pause(1000)
    } else if (false) {
        basic.clearScreen()
    } else {
    	
    }
})
let SPADES = 0
let CLUBS = 0
let DIAMONDS = 0
let HEARTS = 0
HEARTS = randint(1, 3)
DIAMONDS = randint(1, 3)
CLUBS = randint(1, 3)
SPADES = randint(1, 3)
