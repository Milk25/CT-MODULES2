import mood_responses


mood = ["happy", "sad", "excited"]

def mood_response(mood):
    mood = input("How are you feeling today? ")
    if mood == "happy":
        print("Jump for joy!")
    elif mood == "sad":
        print("Hope for the best")
    elif mood == "excited":
        print("Awesome!")


mood_response(mood)