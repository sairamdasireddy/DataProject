import random

sampledata = {
    'hi': ["hello", "Heyyyy"],
    'what is your name': ["I am Chatbot", "I am a robot"],
    'what is db': ["DB means Database", "DB is storing some data"],
    'anything else': ['nothing', 'Nothing else']
}

def samplefunc(user_input):
    user_input = user_input.lower()  # Normalize input to lowercase
    if user_input in sampledata:
        return random.choice(sampledata[user_input])
    else:
        return 'Sorry, try again...!'

def main():
    print("Welcome to the chatbot! Type 'Bye' to exit.")
    while True:
        user_input = input('Type here: ')
        if user_input.lower() == 'bye':
            print('Okay, bye..!')
            break 
        result = samplefunc(user_input)
        print(f'Your result is: {result}')

if __name__ == "__main__":
    main()
