import pyttsx3


def main():
    print("Code is running...")
    # -----------------------------

    book_text = open(r"Book.txt")
    engine = pyttsx3.init()
    for i in book_text:
        engine.say(i)
        engine.runAndWait()

    # -----------------------------
    print("Code ended.")


if __name__ == '__main__':
    main()
