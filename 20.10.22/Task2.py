"""
Напишите программу добавляющую в рецепт бутерброда ингридиенты "Салат" и "Ананасы" с помощью декораторов.
"""

def recept(burger):
    def wrapper():
        print("Что еще нужно добавить?")
        burger()
        print("Состав вашего бургера: булочки, котлета, помидор, сыр")
    return wrapper

@recept
def func_to_decor():
    print("Салат и Ананасы")

func_to_decor()