import speech_recognition as sr
import pyttsx3
import doorman as d

# import doorman from Doorman
# d = Doorman()


# Initialize speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')#fetching different voices from the system
engine.setProperty('voice', voices[10].id)#setting voice properties
engine.setProperty('rate', 120)#sets speed of speech
driver = d.Doorman()
r = sr.Recognizer()
mic = sr.Microphone()

# set the keyword to be detected
keyword = "doorman"

#set greeting
greeting = "I am your doorman. How can I help you?"
# define a callback function to process the detected text
print("\n\n\n")
print("Welcome to the doorman AI. Please say or type in a phrase and our doorman will do their best to help you!")
print("\n\n\n")
def drive():
        # use the Sphinx recognizer to convert speech to text
        text = input("I am your doorman, how can I help you?\ninput --> ")
        print("\n\n")
        engine.say(greeting)
        engine.runAndWait()

        # listen for the next sentence
        #print("Doorman recieved msg with content: ", text)

        # here, we will pass sentence to the doorman class, and that will return a response in the form of a string
        response = driver.handleRequest(text)

        # this can be commented out once the nlp class is implemented

        engine.say(response)
        engine.runAndWait()
        print("\n\n")
        print("Doorman response:", response)
        print("\n\n")

        # stop listening for more input
        #stop_listening(wait_for_stop=False)


# start listening in the background

# keep the main thread alive
def main():
    while True:
        drive()

if __name__ == '__main__':
    main()
