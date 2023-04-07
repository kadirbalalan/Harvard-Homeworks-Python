import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 1:
    inp = input("Input: ")
    f = random.choice(fonts)
    figlet.setFont(font=f)
    print(figlet.renderText(inp))

elif len(sys.argv) == 2:
    sys.exit("Invalid usage")

elif len(sys.argv) == 3:
    fonts = figlet.getFonts()
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    f = sys.argv[2]
    figlet.setFont(font=f)
    inp = input("Input: ")
    print(figlet.renderText(inp))
