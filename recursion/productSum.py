
def productSum(array,multiplayer = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element,multiplayer+1)
        else:
            sum += element
    return sum*multiplayer


