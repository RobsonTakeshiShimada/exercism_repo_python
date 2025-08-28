def equilateral(sides):
    if sides == [0,0,0]:
        return False
    if sides[0] == sides[1] and sides[0] == sides[2] and sides[1] == sides[2]:
        return True
    else:
        return False

def isosceles(sides):
    if sides[0]+sides[1]<sides[2] or sides[0]+sides[2]<sides[1] or sides[1]+sides[2]<sides[0]:
        return False
    elif sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True
    else:
        return False


def scalene(sides):
    if isosceles(sides):
        return False
    elif sides[0]+sides[1]<sides[2] or sides[0]+sides[2]<sides[1] or sides[1]+sides[2]<sides[0]:
        return False
    elif sides[0] != sides[1] and sides[0] != sides[2]:
        return True
    else:
        return False
