import customtkinter as c

def biggest_number():
    list = [10, 2, 30, 4, 5, 6, 70, 8 , 9, 10]
    bn = list[0]
    for number in list:
        if number > bn:
            bn = number
        else:
           pass
    print(bn)

biggest_number()