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
    if (CLUBS == SPADES && SPADES == DIAMONDS || CLUBS == SPADES && SPADES == HEARTS || CLUBS == DIAMONDS && DIAMONDS == HEARTS || SPADES == DIAMONDS && DIAMONDS == HEARTS) {
        basic.showString("THREE OF A KIND")
        basic.clearScreen()
        basic.pause(1000)
    } else if (CLUBS == SPADES && DIAMONDS == HEARTS || CLUBS == DIAMONDS && HEARTS == SPADES || CLUBS == HEARTS && DIAMONDS == SPADES) {
        basic.showString("TWOPAIR")
        basic.clearScreen()
        basic.pause(1000)
    } else if (CLUBS == SPADES || DIAMONDS == HEARTS || CLUBS == DIAMONDS || CLUBS == HEARTS || DIAMONDS == SPADES || HEARTS == SPADES) {
        basic.showString("ONEPAIR")
        basic.clearScreen()
        basic.pause(1000)
    } else {
        basic.showString("NO PAIR")
        basic.clearScreen()
    }
})
let SPADES = 0
let DIAMONDS = 0
let CLUBS = 0
let HEARTS = 0
HEARTS = randint(1, 12)
CLUBS = randint(1, 12)
DIAMONDS = randint(2, 12)
SPADES = randint(2, 12)
