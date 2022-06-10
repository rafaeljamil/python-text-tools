# Rotating letters using ASCII values

def go_round(start, end, rot):
    result = rot

    while (result > end):
        excess = result - end
        result = start + (excess - 1)
    
    return result

def rotate(letter, rotation):
    rotation = int(rotation)
    val = 0
    ch = ord(letter)

    if (ch >= 65 and ch <= 90):
        rot = ch + rotation
        val = go_round(65, 90, rot)
    elif (ch >= 97 and ch <= 122):
        rot = ch + rotation
        val = go_round(97, 122, rot)
    else:
        val = ch
    
    return chr(val)