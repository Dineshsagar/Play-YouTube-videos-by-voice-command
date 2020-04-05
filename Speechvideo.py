import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
r4 = sr.Recognizer()

with sr.Microphone() as source:
    print("Voice Recognition Technology")
    print("Call your Assistant ")
    r3.adjust_for_ambient_noise(source,duration=1)
    audio = r3.listen(source)

if "Niharika" in r4.recognize_google(audio):
    r4 = sr.Recognizer()
    url ="https://www.youtube.com/results?search_query="
    with sr.Microphone() as source:
        print("Hey Dinesh! Your Assistant Niharika here :) Ask me anything:")
        r4.adjust_for_ambient_noise(source,duration=1)
        audio = r4.listen(source)

        try:
            get = r4.recognize_google(audio)
            print("You have asked for :",get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("Unable to recognize")
        except sr.RequestError as e:
            print("Failed".format(e))    

