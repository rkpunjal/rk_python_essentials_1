import random

jokes = [
    "Programming is 10% writing code and 90% understanding why it’s not working."
    , "Q. What did the Java Code say to the C code?\nA.  You’ve got no class."
    , '''A programmer puts two glasses on his bedside table before going to sleep.
A full one, in case he gets thirsty,
and an empty one, in case he doesn’t.'''
    , "Q. Why do programmers prefer Dark-Mode?\nA. Because Light attracts Bugs."
    , "Q. Why do Java programmers have to wear glasses?\nA. Because they don’t C#"
    , "Programmer: An organism that turns coffee into software"
    , '''Q. How did the first program die?
A. It was executed.'''
    , '''Q. How do you explain the Inception movie to a programmer?
A. Basically, when you run a VM inside another VM, inside another VM, inside another VM…, everything runs real slow! :P'''
    , '''Q. Whats the object-oriented way to become wealthy?
A. Inheritance'''
    , '''Q. What do computers and air conditioners have in common?
A. They both become useless when you open windows.'''
    , '''Q. Why was the statement scared while the comment was not?
A. Statements are executed.'''
    , '''Q. What do you call when 8 mosquitos bit you?
A. A mosquito byte.'''
    , '''Boss. What is this [“hip”, ”hip”]?
Dev. hip hip array!'''
    , "Programmer: A person who fixed a problem that\nyou don't know you have,\nin a way you don't understand!"
    , "Algorighm: Word used by programmers when ....\nthey don't want to explain what they did."
    , "Hardware: The part of the computer that you can kick"
    , "Q. What would you all programmer from Norway?\nA. A Nerdic"
    , "Q. What's a programmer's favourite hangout place?\nA. Foo Bar"
    , "Q. 0 is False and 1 is True, right?\nA. 1"
    , "Real programmers count from 0"
    , "Software developers like to solve problems.\nIf there are no problems\nthey will create their own problems."
    , '''SQL query walked into a bar, but walked out soon ... \nBecause he couldn't find a Table!'''
    , '''Optimist : The Glass is half Full.
Pessimist: The Glass is half Empty
Programmer: The Glass is twice as large as necessary!'''
    , '''I don't see women as "Objets"
I consider each to be in a "Class" of her own'''
    , '''I'd like to make the world a better place
But they don't give me the Source-Code!'''
    , '''while(alive){
    eat();
    sleep();
    code();
    }'''
    , "Bad code can't be debugged, neither can good code!"
    , "Q. Why did the developer use a credit card to buy all the gifts?\nA. Because he had cleared all his cache."
    , "According to Programmers, 1 kilometer should be 1024 meters!"
    , "Shaw’s Principle: Build a system that even a fool can use, and only a fool will want to use it."
]


def tell_a_joke():
    joke = jokes[random.randint(0, len(jokes) - 1)]
    print(joke)
    return joke



