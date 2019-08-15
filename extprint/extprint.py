from .exceptions import NoSuchColorException
#from exceptions import NoSuchColorException

colors = {
    "BLACK" : "\33[30m",
    "RED" : "\33[31m",
    "GREEN" : "\33[32m",
    "YELLOW" : "\33[33m",
    "BLUE" : "\33[34m",
    "VIOLET" : "\33[35m",
    "BEIGE" : "\33[36m",
    "WHITE" : "\33[37m",
    "NONE" : ""
    }

bg_colors = {
    "BLACK" : "\33[40m",
    "RED" : "\33[41m",
    "GREEN" : "\33[42m",
    "YELLOW" : "\33[43m",
    "BLUE" : "\33[44m",
    "VIOLET" : "\33[45m",
    "BEIGE" : "\33[46m",
    "WHITE" : "\33[47m",
    "NONE" : ""
    }

style = {
    "BOLD" : "\33[1m",
    "ITALIC" : "\33[3m",

    "NONE" : "",
    "END" : "\033[0m"
    }

def set_default_print_options(start_index = 1, seperator = "-", color = "NONE", bg_color = "NONE", bold = False, italic = False):
    if(color in colors and bg_color in bg_colors):
        printcolored.__defaults__ = (color, bg_color, bold, italic)
        printlist.__defaults__ = (start_index, seperator,color, bg_color, bold, italic)
    else:
        raise NoSuchColorException()

def show_available_colors():
    print("\nAvailable Colors:")
    printlist(colors)
    

def printcolored(to_print, color = "NONE", bg_color= "NONE", bold = False, italic = False):
    """prints colored text with bold and italic options"""
    if(bold):
        bold = style["BOLD"]
    else:
        bold = style["NONE"]

    if(italic):
        italic = style["ITALIC"]
    else:
        italic = style["NONE"]

    if(color in colors and bg_color in bg_colors):
        print("{}{}{}{}{}{}".format(colors[color], bg_colors[bg_color],bold, italic, to_print, style["END"]))
    else:
        raise NoSuchColorException()

def printlist(list, start_index = 1, seperator = "-", color = "NONE", bg_color = "NONE", bold = False, italic = False):
    """prints lists and their indexes, colors may look bad in some platforms so if color is not given function uses regular print"""
    if(bold or italic or color != "NONE" or bg_color != "NONE"):
        for index, element in enumerate(list, start=start_index):
            printcolored("{} {} {}".format(index, seperator, element), color = color, bg_color = bg_color, bold = bold, italic = italic)
    else:
        for index, element in enumerate(list, start=start_index):
            print("{} {} {}".format(index, seperator, element))
