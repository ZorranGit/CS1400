def rate_animal(animal):
    if animal=="dog":
        return 1
    elif animal=="danger noodle":
        return 4
    elif animal=="capybara":
        return 3
    elif animal=="cat":
        return 2
    else:
        return -1
print(rate_animal("owl"))
