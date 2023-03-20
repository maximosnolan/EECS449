import speech_recognition as sr
import pyttsx3

# import doorman from Doorman
# d = Doorman()


# Initialize speech engine
engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone()

# set the keyword to be detected
keyword = "doorman"

# define a callback function to process the detected text
def callback(recognizer, audio):
    try:
        # use the Sphinx recognizer to convert speech to text
        text = recognizer.recognize_sphinx(audio, keyword_entries=[(keyword, 0.5)])
        engine.say("How can I help you")
        engine.runAndWait()

        # listen for the next sentence
        audio = recognizer.listen(mic)
        sentence = recognizer.recognize_google(audio)

        # TODO: Still need to integrate doorman class
        # here, we will pass sentence to the doorman class, and that will return a response in the form of a string
        # response = doorman(sentence)

        # this can be commented out once the nlp class is implemented
        response = "John is at the door"

        engine.say("Sentence: " + response)
        engine.runAndWait()

        # stop listening for more input
        stop_listening(wait_for_stop=False)

    except sr.UnknownValueError:
        pass

# start listening in the background
stop_listening = r.listen_in_background(mic, callback)

# keep the main thread alive
while True:
    pass
