

def debug(text,color=1):
    colors = {
        '*purple*':'\033[95m',
        '*blue*':'\033[94m',
        '*green*':'\033[92m',
        '*yellow*':'\033[93m',
        '*red*':'\033[91m',
        '*end*':'\033[0m',
        }
    if color:
        for color in colors:
            text = text.replace(color,colors[color])
    print(text)
