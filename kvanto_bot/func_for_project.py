from main_SQL import *
def subnet():
    n = 0
    b = 0
    text = ""
    for i in datafr("store", "products"):
        if i[3] == "service":
             n += 1
        elif i[3] == "product":
             b += 1
    text += f"товаров - {b}, услуги - {n}"
    for i in datafr("store", "products"):
        line = f"{i[0]}. {i[1]}, стоимость {i[4]}"
        text = text + "\n" + line
    return text