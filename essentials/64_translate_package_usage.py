
# using 'translate' package

# pip install translate

from translate import Translator

translator = Translator(to_lang = "no")

while True:
    print("print 'q' to Exit Translator")
    print("Source Language: 'English', Destion Language: 'Norwegian'")
    print("-----------------------------------------------------------")
    msg = input("Type your message: ")

    if (msg.lower() in ["q", "quit", "exit", "stop"]):
        print("Exiting Translation ....")
        break

    translation = translator.translate(msg)
    print("Norwegian : ", translation)
    print("-----------------------------------------------------------")

