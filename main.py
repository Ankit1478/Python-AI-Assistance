import openai
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()

r = sr.Recognizer()

openai.api_key = 

for i in range(10):
    text = "hi"
    with sr.Microphone() as source:
        print("Please speak something...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            continue
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            continue

    if text.lower() == "exit":
        break

    completion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": text}
        ]

    )

    # Extract the response message
    message_content = completion.choices[0].message['content']

    # Speak the response
    engine.say(message_content)
    engine.runAndWait()

    # Print the response
    print("ChatGPT: ", message_content)
