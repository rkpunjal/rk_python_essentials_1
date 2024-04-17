
# rk personal research

class bcolors:

    RED = '\033[91m'
    ORANGE = '\033[31m'

    GREEN = '\033[92m'
    LIGHT_GREEN = '\033[32m'

    YELLOW = '\033[93m'
    LIGHT_YELLOW = '\033[33m'

    BLUE = '\033[94m'
    LIGHT_BLUE = '\033[34m'

    PINK = '\033[95m'
    PURPLE = '\033[35m'

    CYAN = '\033[96m'
    LIGHT_GREY = '\033[37m'

    DARK_GREY = '\033[90m'
    BLACK = '\033[98m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSE = '\033[07m'
    STRIKE_THROUGH = '\033[09m'

    RESET = '\033[0m'


print(f"{bcolors.CYAN}{bcolors.BOLD}This is COLORED Text {bcolors.RESET} : This should be normal text")


class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    italics = '\033[03m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


print(colors.fg.red, "Something more advanced", colors.bg.green, colors.fg.black, "With Background color", colors.reset)
print("normal text")
print("what about this", colors.italics, "ITALICS TEXT", colors.reset, "NORMAL", "\x1B[3m ITALICS \x1B[0m", "NORMAL")

# print("\x1B[3mThis text\x1B[0m is \x1B[3mitalicized!\x1B[0m")
