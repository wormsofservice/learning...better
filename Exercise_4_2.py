# Construct a function with an argument


def greeting(language):
    if language == "English":
        print("Hello")
    elif language == "Espanol":
        print("Hola")
    else:
        print("Sorry, I don't speak that!")

#language = input("What language do you speak? ")
#greeting(language)

greeting(input("What language do you speak? "))