

# import tkinter as tk
# from tkinter import messagebox
# import pyttsx3
# import speech_recognition as sr
# import json

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)  
# engine.setProperty('rate', 150)  #ch

# # Define global variables
# questions = []
# responses = []

# def load_questions_from_json():
#     global questions
#     try:
#         with open('questions.json', 'r') as f:
#             data = json.load(f)
#             questions = data.get('questions', [])
#             if not questions:
#                 raise ValueError("No questions found in the JSON file.")
#     except Exception as e:
#         speak(f"Error loading questions: {e}")
#         questions = ["Tell me about yourself."]  # Default question

# # Function to speak text
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Function to listen to user responses
# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening...")
#         print("Listening...")  # Debug statement
#         audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
#     try:
#         response = recognizer.recognize_google(audio)
#         print(f"Recognized: {response}")  # Debug statement
#         return response
#     except sr.UnknownValueError:
#         speak("Sorry, I did not catch that. Could you please repeat Or if you dont know the answer lets move to the next question?")
#         return None
#     except sr.RequestError as e:
#         speak(f"Sorry, there was an issue with the speech recognition service: {e}")
#         return None


# def start_interview():
#     global responses
#     responses = []
#     for question in questions:
#         speak(question)
#         response = listen()
#         if response:
#             responses.append({"question": question, "response": response})
#             canvas2.create_text(10, len(responses) * 30 + 50, anchor=tk.NW, text=f"Q: {question}\nA: {response}", font=('Arial', 12), fill="black", width=470)
#             root.update()
#     save_responses()

# # Function to save responses to a JSON file
# def save_responses():
#     with open('interview_responses.json', 'w') as f:
#         json.dump(responses, f, indent=4)
#     speak("Interview completed. Responses saved.")

# # Function to handle button clicks
# def on_button_click():
#     start_interview()

# # Function to close the application
# def close_application():
#     root.destroy()

# def display_welcome_message():
#     welcome_text = "Welcome to the Ai Assitant bot !\nPlease click 'Start Interview' to begin."
#     canvas2.create_text(10, 10, anchor=tk.NW, text=welcome_text, font=('Arial', 16), fill="black", width=760)
#     speak("Welcome to the Interview Round . Please click Start Interview to begin.")

# # Create and configure the main window
# root = tk.Tk()
# root.title("Interview Bot")
# root.geometry('800x600')
# root.configure(bg='white')

# canvas2 = tk.Canvas(root, bg='white', width=780, height=500)
# canvas2.pack(pady=10)

# # Add a button to start the interview
# start_button = tk.Button(root, text="Start Interview", command=on_button_click, font=('Arial', 14))
# start_button.pack(pady=20)

# # Add a button to close the application
# close_button = tk.Button(root, text="Exit", command=close_application, font=('Arial', 14))
# close_button.pack(pady=10)

# # Load questions from the JSON file
# load_questions_from_json()

# # Run the main loop
# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import pyttsx3
# import speech_recognition as sr
# import json
# import cv2
# import threading

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)  
# engine.setProperty('rate', 150)

# # Define global variables
# questions = []
# responses = []
# face_detected = False
# detection_active = True

# def load_questions_from_json():
#     global questions
#     try:
#         with open('questions.json', 'r') as f:
#             data = json.load(f)
#             questions = data.get('questions', [])
#             if not questions:
#                 raise ValueError("No questions found in the JSON file.")
#     except Exception as e:
#         speak(f"Error loading questions: {e}")
#         questions = ["Tell me about yourself."]  # Default question

# # Function to speak text
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Function to listen to user responses
# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening...")
#         print("Listening...")  # Debug statement
#         audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
#     try:
#         response = recognizer.recognize_google(audio)
#         print(f"Recognized: {response}")  # Debug statement
#         return response
#     except sr.UnknownValueError:
#         speak("Sorry, I did not catch that. Could you please repeat or if you don't know the answer let's move to the next question?")
#         return None
#     except sr.RequestError as e:
#         speak(f"Sorry, there was an issue with the speech recognition service: {e}")
#         return None

# def start_interview():
#     global responses
#     responses = []
#     for question in questions:
#         speak(question)
#         response = listen()
#         if response:
#             responses.append({"question": question, "response": response})
#             canvas2.create_text(10, len(responses) * 30 + 50, anchor=tk.NW, text=f"Q: {question}\nA: {response}", font=('Arial', 12), fill="black", width=470)
#             root.update()
#     save_responses()

# # Function to save responses to a JSON file
# def save_responses():
#     with open('interview_responses.json', 'w') as f:
#         json.dump(responses, f, indent=4)
#     speak("Interview completed. Responses saved.")

# # Function to handle button clicks
# def on_button_click():
#     global face_detected
#     # Ensure face detection is active before starting the interview
#     if not face_detected:
#         speak("Please ensure your face is detected before starting the interview.")
#         return
#     start_interview()

# # Function to close the application
# def close_application():
#     global detection_active
#     detection_active = False
#     root.destroy()

# def display_welcome_message():
#     welcome_text = "Welcome to the AI Assistant bot!\nPlease click 'Start Interview' to begin."
#     canvas2.create_text(10, 10, anchor=tk.NW, text=welcome_text, font=('Arial', 16), fill="black", width=760)
#     speak("Welcome to the Interview Round. Please click Start Interview to begin.")

# def detect_faces():
#     global face_detected
#     global detection_active
#     # Load pre-trained face detection model
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
#     # Initialize video capture
#     cap = cv2.VideoCapture(0)
    
#     while detection_active:
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
#         if len(faces) > 0:
#             face_detected = True
#         else:
#             face_detected = False
    
#     cap.release()
#     cv2.destroyAllWindows()


# root = tk.Tk()
# root.title("Interview Bot")
# root.geometry('800x600')
# root.configure(bg='white')

# canvas2 = tk.Canvas(root, bg='white', width=780, height=500)
# canvas2.pack(pady=10)

# # Add a button to start the interview
# start_button = tk.Button(root, text="Start Interview", command=on_button_click, font=('Arial', 14))
# start_button.pack(pady=20)

# # Add a button to close the application
# close_button = tk.Button(root, text="Exit", command=close_application, font=('Arial', 14))
# close_button.pack(pady=10)


# display_welcome_message()

# load_questions_from_json()


# face_thread = threading.Thread(target=detect_faces)
# face_thread.start()

# # Run the main loop
# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# import pyttsx3
# import speech_recognition as sr
# import json
# import cv2
# import threading

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)  
# engine.setProperty('rate', 150)

# # Define global variables
# questions = []
# responses = []
# face_detected = False
# detection_active = True

# def load_questions_from_json():
#     global questions
#     try:
#         with open('questions.json', 'r') as f:
#             data = json.load(f)
#             questions = data.get('questions', [])
#             if not questions:
#                 raise ValueError("No questions found in the JSON file.")
#     except Exception as e:
#         speak(f"Error loading questions: {e}")
#         questions = ["Tell me about yourself."]  # Default question

# # Function to speak text
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Function to listen to user responses
# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening...")
#         print("Listening...")  # Debug statement
#         audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
#     try:
#         response = recognizer.recognize_google(audio)
#         print(f"Recognized: {response}")  # Debug statement
#         return response
#     except sr.UnknownValueError:
#         speak("Sorry, I did not catch that. Could you please repeat or if you don't know the answer let's move to the next question?")
#         return None
#     except sr.RequestError as e:
#         speak(f"Sorry, there was an issue with the speech recognition service: {e}")
#         return None

# def start_interview():
#     global responses
#     responses = []
#     for question in questions:
#         speak(question)
#         response = listen()
#         if response:
#             responses.append({"question": question, "response": response})
#             canvas2.create_text(10, len(responses) * 30 + 50, anchor=tk.NW, text=f"Q: {question}\nA: {response}", font=('Arial', 12), fill="black", width=470)
#             root.update()
#     save_responses()

# # Function to save responses to a JSON file
# def save_responses():
#     with open('interview_responses.json', 'w') as f:
#         json.dump(responses, f, indent=4)
#     speak("Interview completed. Responses saved.")

# # Function to handle button clicks
# def on_button_click():
#     global face_detected
#     # Ensure face detection is active before starting the interview
#     if not face_detected:
#         speak("Please ensure your face is detected before starting the interview.")
#         return
#     start_interview()

# # Function to close the application
# def close_application():
#     global detection_active
#     detection_active = False
#     root.destroy()

# def display_welcome_message():
#     welcome_text = "Welcome to the AI Assistant bot!\nPlease click 'Start Interview' to begin."
#     canvas2.create_text(10, 10, anchor=tk.NW, text=welcome_text, font=('Arial', 16), fill="black", width=760)
#     speak("Welcome to the Interview Round. Please click Start Interview to begin.")

# def detect_faces():
#     global face_detected
#     global detection_active
    
#     # Load pre-trained face detection model
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
#     # Initialize video capture
#     cap = cv2.VideoCapture(0)
    
#     while detection_active:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture image.")  # Debug statement
#             break
        
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
#         if len(faces) > 0:
#             face_detected = True
#             # Draw rectangle around the faces
#             for (x, y, w, h) in faces:
#                 cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#         else:
#             face_detected = False

#         # Display the resulting frame
#         cv2.imshow('Face Detection', frame)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     cap.release()
#     cv2.destroyAllWindows()

# # Create and configure the main window
# root = tk.Tk()
# root.title("Interview Bot")
# root.geometry('800x600')
# root.configure(bg='white')

# canvas2 = tk.Canvas(root, bg='white', width=780, height=500)
# canvas2.pack(pady=10)

# # Add a button to start the interview
# start_button = tk.Button(root, text="Start Interview", command=on_button_click, font=('Arial', 14))
# start_button.pack(pady=20)

# # Add a button to close the application
# close_button = tk.Button(root, text="Exit", command=close_application, font=('Arial', 14))
# close_button.pack(pady=10)

# # Display welcome message
# display_welcome_message()

# # Load questions from the JSON file
# load_questions_from_json()

# # Start the face detection in a separate thread
# face_thread = threading.Thread(target=detect_faces)
# face_thread.start()

# # Run the main loop
# root.mainloop()




# import tkinter as tk
# import pyttsx3
# import speech_recognition as sr
# import json
# import cv2
# import threading

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)  
# engine.setProperty('rate', 150)

# # Define global variables
# questions = []
# responses = []
# face_detected = False
# detection_active = True

# video_filename = 'recorded_video.mp4'

# def load_questions_from_json():
#     global questions
#     try:
#         with open('questions.json', 'r') as f:
#             data = json.load(f)
#             questions = data.get('questions', [])
#             if not questions:
#                 raise ValueError("No questions found in the JSON file.")
#     except Exception as e:
#         speak(f"Error loading questions: {e}")

# # Function to speak text
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Function to listen to user responses
# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening...")
#         print("Listening...")  # Debug statement
#         audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
#     try:
#         response = recognizer.recognize_google(audio)
#         print(f"Recognized: {response}")  # Debug statement
#         return response
#     except sr.UnknownValueError:
#         speak("Sorry, I did not catch that. Could you please repeat or if you don't know the answer let's move to the next question?")
#         return None
#     except sr.RequestError as e:
#         speak(f"Sorry, there was an issue with the speech recognition service: {e}")
#         return None

# def start_interview():
#     global responses
#     responses = []
#     for question in questions:
#         speak(question)
#         response = listen()
#         if response:
#             responses.append({"question": question, "response": response})
#             canvas2.create_text(10, len(responses) * 30 + 50, anchor=tk.NW, text=f"Q: {question}\nA: {response}", font=('Arial', 12), fill="black", width=470)
#             root.update()
#     save_responses()

# # Function to save responses to a JSON file
# def save_responses():
#     with open('interview_responses.json', 'w') as f:
#         json.dump(responses, f, indent=4)
#     speak("Interview completed. Responses saved.")

# # Function to handle button clicks
# def on_button_click():
#     global face_detected
#     # Ensure face detection is active before starting the interview
#     if not face_detected:
#         speak("Please ensure your face is detected before starting the interview.")
#         return
#     start_interview()

# # Function to close the application
# def close_application():
#     global detection_active
#     detection_active = False
#     root.destroy()

# def display_welcome_message():
#     welcome_text = "Welcome to the AI Assistant bot!\nPlease click 'Start Interview' to begin."
#     canvas2.create_text(10, 10, anchor=tk.NW, text=welcome_text, font=('Arial', 16), fill="black", width=760)
#     speak("Welcome to the Interview Round. Please click Start Interview to begin.")

# def record_video():
#     global detection_active

#     # Load pre-trained face detection model
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
#     # Initialize video capture
#     cap = cv2.VideoCapture(0)
    
#     # Set up video writer to save the recorded video
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 codec
#     out = cv2.VideoWriter(video_filename, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
    
#     while detection_active:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture image.")  # Debug statement
#             break
        
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
#         if len(faces) > 0:
#             global face_detected
#             face_detected = True
#             # Draw rectangle around the faces
#             for (x, y, w, h) in faces:
#                 cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#         else:
#             face_detected = False

#         # Display the resulting frame
#         cv2.imshow('Face Detection', frame)
        
#         # Write the frame to the video file
#         out.write(frame)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()


# root = tk.Tk()
# root.title("Interview Bot")
# root.geometry('800x600')
# root.configure(bg='white')

# canvas2 = tk.Canvas(root, bg='white', width=780, height=500)
# canvas2.pack(pady=10)

# # Add a button to start the interview
# start_button = tk.Button(root, text="Start Interview", command=on_button_click, font=('Arial', 14))
# start_button.pack(pady=20)


# close_button = tk.Button(root, text="Exit", command=close_application, font=('Arial', 14))
# close_button.pack(pady=10)

# display_welcome_message()
# q

# load_questions_from_json()


# video_thread = threading.Thread(target=record_video)
# video_thread.start()

# root.mainloop()





# WITH TEXT BLOP
# import tkinter as tk
# import pyttsx3
# import speech_recognition as sr
# import json
# import cv2
# import threading
# from textblob import TextBlob
# import time 

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('voice', engine.getProperty('voices')[0].id)
# engine.setProperty('rate', 150)

# # Define global variables
# questions = []
# responses = []
# face_detected = False
# detection_active = True
# video_filename = 'recorded_video.mp4'

# def load_questions_from_json():
#     global questions
#     try:
#         with open('questions.json', 'r') as f:
#             data = json.load(f)
#             questions = data.get('questions', [])
#             if not questions:
#                 raise ValueError("No questions found in the JSON file.")
#     except Exception as e:
#         speak(f"Error loading questions: {e}")
#         questions = ["Tell me about yourself."]

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def analyze_sentiment(response):
#     blob = TextBlob(response)
#     return blob.sentiment.polarity

# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening...")
#         audio = recognizer.listen(source, timeout=15, phrase_time_limit=60)
#     try:
#         response = recognizer.recognize_google(audio)
#         sentiment = analyze_sentiment(response)
#         return response, sentiment
#     except sr.UnknownValueError:
#         speak("Sorry, I did not catch that. Could you please repeat?")
#         return None, None
#     except sr.RequestError as e:
#         speak(f"Error with the speech recognition service: {e}")
#         return None, None

# def start_interview():
#     global responses
#     responses = []
#     for question in questions:
#         speak(question)
        
#         # Record the start time
#         start_time = time.time()
        
#         response, sentiment = listen()

#         end_time = time.time()
        
#         duration = end_time - start_time
        
#         if response:
#             responses.append({
#                 "question": question,
#                 "response": response,
#                 "sentiment": sentiment,
#                 "response_time_seconds": duration  
#             })
#             # Update canvas safely from the main thread
#             def update_canvas():
#                 canvas2.create_text(10, len(responses) * 30 + 50, anchor=tk.NW, 
#                                     text=f"Q: {question}\nA: {response} (Sentiment: {sentiment:.2f})\nTime: {duration:.2f} seconds",
#                                     font=('Arial', 12), fill="black", width=470)
#                 root.update()
#             root.after(0, update_canvas)
#     save_responses()

# def save_responses():
#     try:
#         with open('interview_responses.json', 'w') as f:
#             json.dump(responses, f, indent=4)
#         speak("Interview completed. Thanks you for the time .")
#     except Exception as e:
#         speak(f"Error saving responses: {e}")

# def on_button_click():
#     if not face_detected:
#         speak("Please ensure your face is detected in the box before starting the interview.")
#         return
#     start_interview()

# def close_application():
#     global detection_active
#     detection_active = False
#     root.destroy()

# def display_welcome_message():
#     welcome_text = "Welcome to the AI Assistant bot!\nif you are ready please click 'Start Interview' to begin."
#     canvas2.create_text(10, 10, anchor=tk.NW, text=welcome_text, font=('Arial', 16), fill="black", width=760)
#     speak("Dear Candidate Welcome to the Interview Round. Make sure your face is detected s. Please click Start Interview to begin.")

# def record_video():
#     global detection_active, face_detected
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     cap = cv2.VideoCapture(0)
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(video_filename, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
#     while detection_active:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture image.")
#             break
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#         face_detected = len(faces) > 0
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#         cv2.imshow('Face Detection', frame)
#         out.write(frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()

# # Create and configure the main window
# root = tk.Tk()
# root.title("Interview Bot")
# root.geometry('800x600')
# root.configure(bg='white')

# canvas2 = tk.Canvas(root, bg='white', width=780, height=500)
# canvas2.pack(pady=10)

# # Add a button to start the interview
# start_button = tk.Button(root, text="Start Interview", command=on_button_click, font=('Arial', 14))
# start_button.pack(pady=20)


# close_button = tk.Button(root, text="Exit", command=close_application, font=('Arial', 14))
# close_button.pack(pady=10)


# display_welcome_message()

# load_questions_from_json()

# video_thread = threading.Thread(target=record_video, daemon=True)
# video_thread.start()

# root.mainloop()




# ACTUAL CODE 
# import tkinter as tk
# import pyttsx3
# import speech_recognition as sr
# import json
# import cv2
# import threading
# from textblob import TextBlob
# import time
# import pyaudio
# import wave
# import subprocess  

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('voice', engine.getProperty('voices')[0].id)
# engine.setProperty('rate', 150)

# # Define global variables
# questions = []
# responses = []
# face_detected = False
# detection_active = True
# video_filename = 'recorded_video.mp4'

# def load_questions_from_json():
#     global questions
#     try:
#         with open('questions.json', 'r') as f:
#             data = json.load(f)
#             questions = data.get('questions', [])
#             if not questions:
#                 raise ValueError("No questions found in the JSON file.")
#     except Exception as e:
#         speak(f"Error loading questions: {e}")
#         questions = ["Tell me about yourself."]

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def analyze_sentiment(response):
#     blob = TextBlob(response)
#     return blob.sentiment.polarity

# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening...")
#         audio = recognizer.listen(source, timeout=15, phrase_time_limit=60)
#     try:
#         response = recognizer.recognize_google(audio)
#         sentiment = analyze_sentiment(response)
#         return response, sentiment
#     except sr.UnknownValueError:
#         speak("Sorry, I did not catch that. Could you please repeat?")
#         return None, None
#     except sr.RequestError as e:
#         speak(f"Error with the speech recognition service: {e}")
#         return None, None

# def start_interview():
#     global responses
#     responses = []
#     for question in questions:
#         speak(question)
        
#         # Record the start time
#         start_time = time.time()
        
#         response, sentiment = listen()

#         end_time = time.time()
        
#         duration = end_time - start_time
        
#         if response:
#             responses.append({
#                 "question": question,
#                 "response": response,
#                 "sentiment": sentiment,
#                 "response_time_seconds": duration  
#             })
#             # Update canvas safely from the main thread
#             def update_canvas():
#                 canvas2.create_text(10, len(responses) * 30 + 50, anchor=tk.NW, 
#                                     text=f"Q: {question}\nA: {response} (Sentiment: {sentiment:.2f})\nTime: {duration:.2f} seconds",
#                                     font=('Arial', 12), fill="black", width=470)
#                 root.update()
#             root.after(0, update_canvas)
#     save_responses()

# def save_responses():
#     try:
#         with open('interview_responses.json', 'w') as f:
#             json.dump(responses, f, indent=4)
#         speak("Interview completed. Thanks you for the time.")
#     except Exception as e:
#         speak(f"Error saving responses: {e}")

# def on_button_click():
#     if not face_detected:
#         speak("Please ensure your face is detected in the box before starting the interview.")
#         return
#     start_interview()

# def close_application():
#     global detection_active
#     detection_active = False
#     root.destroy()

# def display_welcome_message():
#     welcome_text = "Welcome to the AI Assistant bot!\nIf you are ready please click 'Start Interview' to begin."
#     canvas2.create_text(10, 10, anchor=tk.NW, text=welcome_text, font=('Arial', 16), fill="black", width=760)
#     speak("Dear Candidate Welcome to the Interview Round. Make sure your face is detected. Please click Start Interview to begin.")

# def record_video_and_audio():
#     global detection_active, face_detected
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     cap = cv2.VideoCapture(0)
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(video_filename, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

#     # Audio recording setup
#     audio_format = pyaudio.paInt16
#     audio_channels = 1
#     audio_rate = 44100
#     audio_chunk = 1024
#     audio_recording = pyaudio.PyAudio()
#     audio_stream = audio_recording.open(format=audio_format, channels=audio_channels,
#                                         rate=audio_rate, input=True, frames_per_buffer=audio_chunk)
#     audio_frames = []
    
#     while detection_active:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture image.")
#             break
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#         face_detected = len(faces) > 0
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#         cv2.imshow('Face Detection', frame)
#         out.write(frame)
        
#         # Capture audio
#         audio_data = audio_stream.read(audio_chunk)
#         audio_frames.append(audio_data)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     # Release resources
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()
#     audio_stream.stop_stream()
#     audio_stream.close()
#     audio_recording.terminate()

#     # Save audio file
#     with wave.open(video_filename, 'wb') as wf:
#         wf.setnchannels(audio_channels)
#         wf.setsampwidth(audio_recording.get_sample_size(audio_format))
#         wf.setframerate(audio_rate)
#         wf.writeframes(b''.join(audio_frames))

#     # Combine audio and video files
#     merge_audio_video(video_filename, video_filename, final_filename)

# def merge_audio_video(video_filename, audio_filename, final_filename):
#     command = [
#         'ffmpeg', '-i', video_filename, '-i', audio_filename, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', final_filename
#     ]
#     subprocess.run(command)

# # Create and configure the main window
# root = tk.Tk()
# root.title("Interview Bot")
# root.geometry('800x600')
# root.configure(bg='white')

# canvas2 = tk.Canvas(root, bg='white', width=780, height=500)
# canvas2.pack(pady=10)

# # Add a button to start the interview
# start_button = tk.Button(root, text="Start Interview", command=on_button_click, font=('Arial', 14))
# start_button.pack(pady=20)

# close_button = tk.Button(root, text="Exit", command=close_application, font=('Arial', 14))
# close_button.pack(pady=10)

# display_welcome_message()

# load_questions_from_json()

# video_thread = threading.Thread(target=record_video_and_audio, daemon=True)
# video_thread.start()

# root.mainloop()




# import tkinter as tk
# import pyttsx3
# import speech_recognition as sr
# import json
# import cv2
# import threading
# from textblob import TextBlob
# import time
# import pyaudio
# import wave
# import subprocess  

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('voice', engine.getProperty('voices')[0].id)
# engine.setProperty('rate', 150)

# # Define global variables
# questions = []
# responses = []
# face_detected = False
# detection_active = True
# video_filename = 'recorded_video.mp4'
# audio_filename = 'recorded_audio.wav'
# final_filename = 'final_output.mp4'
# interview_stop_flag = threading.Event()  # Flag to stop the interview

# def load_questions_from_json():
#     global questions
#     try:
#         with open('questions.json', 'r') as f:
#             data = json.load(f)
#             questions = data.get('questions', [])
#             if not questions:
#                 raise ValueError("No questions found in the JSON file.")
#     except Exception as e:
#         speak(f"Error loading questions: {e}")
# 

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def analyze_sentiment(response):
#     blob = TextBlob(response)
#     return blob.sentiment.polarity

# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening...")
#         audio = recognizer.listen(source, timeout=15, phrase_time_limit=60)
#     try:
#         response = recognizer.recognize_google(audio)
#         sentiment = analyze_sentiment(response)
#         return response, sentiment
#     except sr.UnknownValueError:
#         speak("Sorry, I did not catch that. Could you please repeat?")
#         return None, None
#     except sr.RequestError as e:
#         speak(f"Error with the speech recognition service: {e}")
#         return None, None

# def start_interview():
#     global responses
#     responses = []
#     for question in questions:
#         if interview_stop_flag.is_set():
#             speak("Interview stopped due to multiple face detections.")
#             break

#         speak(question)
        
#         # Record the start time
#         start_time = time.time()
        
#         response, sentiment = listen()

#         end_time = time.time()
        
#         duration = end_time - start_time
        
#         if response:
#             responses.append({
#                 "question": question,
#                 "response": response,
#                 "sentiment": sentiment,
#                 "response_time_seconds": duration  
#             })
#             # Update canvas safely from the main thread
#             def update_canvas():
#                 canvas2.create_text(10, len(responses) * 30 + 50, anchor=tk.NW, 
#                                     text=f"Q: {question}\nA: {response} (Sentiment: {sentiment:.2f})\nTime: {duration:.2f} seconds",
#                                     font=('Arial', 12), fill="black", width=470)
#                 root.update()
#             root.after(0, update_canvas)
#     save_responses()

# def save_responses():
#     try:
#         with open('interview_responses.json', 'w') as f:
#             json.dump(responses, f, indent=4)
#         speak("Interview completed. Thank you for the time.")
#     except Exception as e:
#         speak(f"Error saving responses: {e}")

# def on_button_click():
#     if not face_detected:
#         speak("Please ensure your face is detected in the box before starting the interview.")
#         return
#     start_interview()

# def close_application():
#     global detection_active
#     detection_active = False
#     interview_stop_flag.set()  # Signal to stop the interview if running
#     root.destroy()

# def display_welcome_message():
#     welcome_text = "Welcome to the AI Assistant bot!\nIf you are ready please click 'Start Interview' to begin."
#     canvas2.create_text(10, 10, anchor=tk.NW, text=welcome_text, font=('Arial', 16), fill="black", width=760)
#     speak("Dear Candidate, Welcome to the Interview Round. Make sure your face is detected. Please click Start Interview to begin.")

# def record_video_and_audio():
#     global detection_active, face_detected
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     cap = cv2.VideoCapture(0)
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(video_filename, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

#     # Audio recording setup
#     audio_format = pyaudio.paInt16
#     audio_channels = 1
#     audio_rate = 44100
#     audio_chunk = 1024
#     audio_recording = pyaudio.PyAudio()
#     audio_stream = audio_recording.open(format=audio_format, channels=audio_channels,
#                                         rate=audio_rate, input=True, frames_per_buffer=audio_chunk)
#     audio_frames = []
    
#     while detection_active:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture image.")
#             break
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
#         if len(faces) >= 2:
#             interview_stop_flag.set()  
#             speak("Two faces detected. Stopping the interview.")
#             break
        
#         face_detected = len(faces) > 0
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#         cv2.imshow('Face Detection', frame)
#         out.write(frame)
        
#         # Capture audio
#         audio_data = audio_stream.read(audio_chunk)
#         audio_frames.append(audio_data)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     # Release resources
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()
#     audio_stream.stop_stream()
#     audio_stream.close()
#     audio_recording.terminate()

#     # Save audio file
#     with wave.open(audio_filename, 'wb') as wf:
#         wf.setnchannels(audio_channels)
#         wf.setsampwidth(audio_recording.get_sample_size(audio_format))
#         wf.setframerate(audio_rate)
#         wf.writeframes(b''.join(audio_frames))

#     # Combine audio and video files
#     merge_audio_video(video_filename, audio_filename, final_filename)








# import tkinter as tk
# import pyttsx3
# import speech_recognition as sr
# import json
# import cv2
# import threading
# import time
# from textblob import TextBlob
# import pyaudio
# import wave
# import subprocess

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('voice', engine.getProperty('voices')[0].id)
# engine.setProperty('rate', 150)

# # Define global variables
# questions = {}
# responses = []
# face_detected = False
# detection_active = True
# video_filename = 'recorded_video.mp4'
# audio_filename = 'recorded_audio.wav'
# final_filename = 'final_output.mp4'
# interview_stop_flag = threading.Event() 
# selected_role = None  

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def load_questions_from_json():
#     global questions
#     try:
#         with open('questions.json', 'r') as f:
#             data = json.load(f)
#             questions = {role: [q['question'] for q in qs] for item in data['questions'] for role, qs in item.items()}
#             if not questions:
#                 raise ValueError("No questions found in the JSON file.")
#     except Exception as e:
#         speak(f"Error loading questions: {e}")

# def display_role_selection():
#     role_selection = tk.Toplevel(root)
#     role_selection.title("Select Role")
    
#     def set_role(role):
#         global selected_role
#         selected_role = role
#         role_selection.destroy()
#         start_interview()  # Start interview immediately after selection
    
#     tk.Label(role_selection, text="Please select the position you are applying for:", font=('Arial', 14)).pack(pady=10)
#     tk.Button(role_selection, text="Web Developer", command=lambda: set_role("Web Developer"), font=('Arial', 12)).pack(pady=5)
#     tk.Button(role_selection, text="Data Scientist", command=lambda: set_role("Data Scientist"), font=('Arial', 12)).pack(pady=5)
    
# def analyze_sentiment(response):
#     blob = TextBlob(response)
#     return blob.sentiment.polarity

# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening...")
#         audio = recognizer.listen(source, timeout=15, phrase_time_limit=60)
#     try:
#         response = recognizer.recognize_google(audio)
#         sentiment = analyze_sentiment(response)
#         return response, sentiment
#     except sr.UnknownValueError:
#         speak("Sorry, I did not catch that. Could you please repeat?")
#         return None, None
#     except sr.RequestError as e:
#         speak(f"Error with the speech recognition service: {e}")
#         return None, None
    
# def start_interview():
#     global responses
#     responses = []
    
#     if selected_role is None or selected_role not in questions:
#         speak("No questions available for the selected role.")
#         return
    
#     for question in questions[selected_role]:
#         if interview_stop_flag.is_set():
#             speak("Interview stopped due to multiple face detections.")
#             break

#         speak(question)

#         start_time = time.time()  # Start timer
#         response, sentiment = listen()  # Get user response
#         duration = time.time() - start_time  # Calculate duration

#         if response:
#             responses.append({
#                 "question": question,
#                 "response": response,
#                 "sentiment": sentiment,
#                 "response_time_seconds": duration  
#             })

#             # Update canvas safely from the main thread
#             def update_canvas():
#                 canvas2.create_text(10, len(responses) * 30 + 50, anchor=tk.NW, 
#                                     text=f"Q: {question}\nA: {response}\nSentiment: {sentiment:.2f}\nTime: {duration:.2f} seconds",
#                                     font=('Arial', 12), fill="black", width=470)
#                 root.update()
#             root.after(0, update_canvas)
    
#     save_responses()

# def save_responses():
#     try:
#         with open('interview_responses.json', 'w') as f:
#             json.dump(responses, f, indent=4)
#         speak("Interview completed. Thank you for your time.")
#     except Exception as e:
#         speak(f"Error saving responses: {e}")

# def close_application():
#     global detection_active
#     detection_active = False
#     interview_stop_flag.set()  # Signal to stop the interview if running
#     root.destroy()

# def display_welcome_message():
#     welcome_text = "Welcome to the AI Assistant bot!\nIf you are ready please click on  'Start Interview' button to begin."
#     canvas2.create_text(10, 10, anchor=tk.NW, text=welcome_text, font=('Arial', 16), fill="black", width=760)
#     speak("Dear Candidate, Welcome to the Interview Round. Please select your role to proceed  further with the interview.")

# def record_video_and_audio():
#     global detection_active, face_detected
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     cap = cv2.VideoCapture(0)
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(video_filename, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

#     # Audio recording setup
#     audio_format = pyaudio.paInt16
#     audio_channels = 1
#     audio_rate = 44100
#     audio_chunk = 1024
#     audio_recording = pyaudio.PyAudio()
#     audio_stream = audio_recording.open(format=audio_format, channels=audio_channels,
#                                         rate=audio_rate, input=True, frames_per_buffer=audio_chunk)
#     audio_frames = []
    
#     face_count = 0
#     stable_face_count = 0
#     stable_face_threshold = 5  

#     while detection_active:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture image.")
#             break
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
#         # Filter out very small detections
#         filtered_faces = [face for face in faces if face[2] > 50 and face[3] > 50]  
        
#         current_face_count = len(filtered_faces)
        
#         # If the face count is stable over a number of frames, consider it stable
#         if current_face_count >= 2.5:
#             stable_face_count += 1
#         else:
#             stable_face_count = 0
        
#         if stable_face_count >= stable_face_threshold:
#             interview_stop_flag.set()  
#             speak("Two or more faces detected consistently. Stopping the interview.")
#             break
        
#         face_detected = current_face_count == 1
#         for (x, y, w, h) in filtered_faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
#         cv2.imshow('Face Detection', frame)
#         out.write(frame)
        
#         # Capture audio
#         audio_data = audio_stream.read(audio_chunk)
#         audio_frames.append(audio_data)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     # Release resources
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()
#     audio_stream.stop_stream()
#     audio_stream.close()
#     audio_recording.terminate()

#     # Save audio file
#     with wave.open(audio_filename, 'wb') as wf:
#         wf.setnchannels(audio_channels)
#         wf.setsampwidth(audio_recording.get_sample_size(audio_format))
#         wf.setframerate(audio_rate)
#         wf.writeframes(b''.join(audio_frames))

#     # Combine audio and video files
#     merge_audio_video(video_filename, audio_filename, final_filename)

# def merge_audio_video(video_filename, audio_filename, final_filename):
#     # Use raw string to avoid issues with backslashes
#     ffmpeg_path = r'C:\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe'
#     command = [
#         ffmpeg_path, '-i', video_filename, '-i', audio_filename,
#         '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', final_filename
#     ]
#     print(f"Running command: {' '.join(command)}")

#     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout_output = result.stdout.decode()
#     stderr_output = result.stderr.decode()

#     print(f"ffmpeg output:\n{stdout_output}")
#     if result.returncode != 0:
#         print(f"ffmpeg error:\n{stderr_output}")
#     else:
#         print("Audio and video successfully merged.")

# root = tk.Tk()
# root.title("Interview Bot")
# root.geometry('800x600')
# root.configure(bg='white')

# canvas2 = tk.Canvas(root, bg='white', width=780, height=500)
# canvas2.pack(pady=10)

# start_button = tk.Button(root, text="Start Interview", command=display_role_selection, font=('Arial', 14))
# start_button.pack(pady=20)

# close_button = tk.Button(root, text="Exit", command=close_application, font=('Arial', 14))
# close_button.pack(pady=10)

# display_welcome_message()

# load_questions_from_json()

# video_thread = threading.Thread(target=record_video_and_audio, daemon=True)
# video_thread.start()

# root.mainloop()










# import tkinter as tk
# from tkinter import Canvas
# import pyttsx3
# import speech_recognition as sr
# import json
# import cv2
# import threading
# import time
# from textblob import TextBlob
# from PIL import Image, ImageTk
# import pyaudio
# import wave
# import subprocess

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('voice', engine.getProperty('voices')[0].id)
# engine.setProperty('rate', 150)

# # Define global variables
# questions = {}
# responses = []
# face_detected = False
# detection_active = True
# video_filename = 'recorded_video.mp4'
# audio_filename = 'recorded_audio.wav'
# final_filename = 'final_output.mp4'
# interview_stop_flag = threading.Event()
# selected_role = None

# # Initialize OpenCV variables
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# video_capture = cv2.VideoCapture(0)


# def speak(text):
#     engine.say(text)
#     engine.runAndWait()


# def load_questions_from_json():
#     global questions
#     try:
#         with open('questions.json', 'r') as f:
#             data = json.load(f)
#             questions = {role: [q['question'] for q in qs] for item in data['questions'] for role, qs in item.items()}
#             if not questions:
#                 raise ValueError("No questions found in the JSON file.")
#     except Exception as e:
#         speak(f"Error loading questions: {e}")


# def display_role_selection():
#     role_selection = tk.Toplevel(root)
#     role_selection.title("Select Role")

#     def set_role(role):
#         global selected_role
#         selected_role = role
#         role_selection.destroy()
#         start_interview()  # Start interview immediately after selection

#     tk.Label(role_selection, text="Please select the position you are applying for:", font=('Arial', 14)).pack(pady=10)
#     tk.Button(role_selection, text="Web Developer", command=lambda: set_role("Web Developer"), font=('Arial', 12)).pack(
#         pady=5)
#     tk.Button(role_selection, text="Data Scientist", command=lambda: set_role("Data Scientist"), font=('Arial', 12)).pack(
#         pady=5)


# def analyze_sentiment(response):
#     blob = TextBlob(response)
#     return blob.sentiment.polarity


# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening...")
#         audio = recognizer.listen(source, timeout=15, phrase_time_limit=60)
#     try:
#         response = recognizer.recognize_google(audio)
#         sentiment = analyze_sentiment(response)
#         return response, sentiment
#     except sr.UnknownValueError:
#         speak("Sorry, I did not catch that. Could you please repeat?")
#         return None, None
#     except sr.RequestError as e:
#         speak(f"Error with the speech recognition service: {e}")
#         return None, None


# def start_interview():
#     global responses
#     responses = []

#     if selected_role is None or selected_role not in questions:
#         speak("No questions available for the selected role.")
#         return

#     for question in questions[selected_role]:
#         if interview_stop_flag.is_set():
#             speak("Interview stopped due to multiple face detections.")
#             break

#         speak(question)

#         start_time = time.time()  # Start timer
#         response, sentiment = listen()  # Get user response
#         duration = time.time() - start_time  # Calculate duration

#         if response:
#             responses.append({
#                 "question": question,
#                 "response": response,
#                 "sentiment": sentiment,
#                 "response_time_seconds": duration
#             })

#             def update_canvas():
#                 canvas2.create_text(10, len(responses) * 30 + 50, anchor=tk.NW,
#                                     text=f"Q: {question}\nA: {response}\nSentiment: {sentiment:.2f}\nTime: {duration:.2f} seconds",
#                                     font=('Arial', 12), fill="black", width=470)
#                 root.update()

#             root.after(0, update_canvas)

#     save_responses()


# def save_responses():
#     try:
#         with open('interview_responses.json', 'w') as f:
#             json.dump(responses, f, indent=4)
#         speak("Interview completed. Thank you for your time.")
#     except Exception as e:
#         speak(f"Error saving responses: {e}")


# def close_application():
#     global detection_active
#     detection_active = False
#     interview_stop_flag.set()  # Signal to stop the interview if running
#     root.destroy()


# def display_welcome_message():
#     welcome_text = "Welcome to the AI Assistant bot!\nIf you are ready please click on  'Start Interview' button to begin."
#     canvas2.create_text(10, 10, anchor=tk.NW, text=welcome_text, font=('Arial', 16), fill="black", width=760)
#     speak("Dear Candidate, Welcome to the Interview Round. Please select your role to proceed  further with the interview.")


# def update_video_feed():
#     global face_detected
#     ret, frame = video_capture.read()
#     if ret:
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#         face_detected = len(faces) == 1

#         # Convert frame to an image for Tkinter
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(frame)
#         imgtk = ImageTk.PhotoImage(image=img)

#         # Update the canvas
#         video_canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
#         video_canvas.imgtk = imgtk  # Store reference to avoid garbage collection

#     root.after(10, update_video_feed)  # Refresh every 10ms


# # Tkinter GUI setup
# root = tk.Tk()
# root.title("Interview Bot")
# root.geometry('800x600')
# root.configure(bg='white')

# canvas2 = tk.Canvas(root, bg='white', width=780, height=150)
# canvas2.pack(pady=10)

# # Add a canvas for the video feed
# video_canvas = Canvas(root, width=640, height=360, bg="black")
# video_canvas.pack(pady=10)

# start_button = tk.Button(root, text="Start Interview", command=display_role_selection, font=('Arial', 14))
# start_button.pack(pady=20)

# close_button = tk.Button(root, text="Exit", command=close_application, font=('Arial', 14))
# close_button.pack(pady=10)

# display_welcome_message()
# load_questions_from_json()
# update_video_feed()

# root.mainloop()


# UPDATED INTERFACE
# import tkinter as tk
# from tkinter import ttk, messagebox
# import pyttsx3
# import cv2
# from PIL import Image, ImageTk
# import threading
# import pyaudio
# import wave
# import subprocess
# import json
# from textblob import TextBlob
# import time
# import speech_recognition as sr

# # Initialize global variables
# video_filename = "recorded_video.mp4"
# audio_filename = "recorded_audio.wav"
# final_filename = "final_output.mp4"
# questions = {}
# responses = []
# selected_role = None
# recording = False
# interview_stop_flag = threading.Event()

# # Initialize Text-to-Speech engine
# engine = pyttsx3.init()
# engine.setProperty("rate", 150)

# # Initialize OpenCV variables
# video_capture = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# def speak(text):
#     """Speak the given text."""
#     engine.say(text)
#     engine.runAndWait()

# def load_questions():
#     """Load questions from a JSON file."""
#     global questions
#     try:
#         with open("questions.json", "r") as f:
#             data = json.load(f)
#             questions = {role: [q["question"] for q in qs] for item in data["questions"] for role, qs in item.items()}
#     except Exception as e:
#         speak("Error loading questions. Please check the JSON file.")
#         messagebox.showerror("Error", f"Failed to load questions: {e}")

# def start_recording():
#     """Start video and audio recording in a separate thread."""
#     global recording
#     recording = True
#     threading.Thread(target=record_video_and_audio, daemon=True).start()

# def stop_recording():
#     """Stop recording."""
#     global recording
#     recording = False

# def record_video_and_audio():
#     """Record video and audio and save to disk."""
#     fourcc = cv2.VideoWriter_fourcc(*"mp4v")
#     out = cv2.VideoWriter(video_filename, fourcc, 20.0, (640, 480))

#     # Initialize audio recording
#     audio = pyaudio.PyAudio()
#     stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
#     frames = []

#     face_not_detected_count = 0  # Counter for tracking continuous face absence

#     while recording:
#         # Capture video frame
#         ret, frame = video_capture.read()
#         if not ret:
#             break

#         # Detect faces
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#         if len(faces) == 0:
#             # No face detected, increment counter
#             face_not_detected_count += 1
#             if face_not_detected_count > 50:  
#                 speak("Error: No face detected for too long.")
#                 messagebox.showerror("Error", "No face detected for too long. Please ensure your face is visible.")
#                 stop_recording()
#                 break
#         else:
#             # Reset counter if a face is detected
#             face_not_detected_count = 0

#         # If more than two faces are detected, stop the recording process
#         if len(faces) > 1:
#             speak("Error: Multiple  faces detected.")
#             messagebox.showerror("Error", "Seems like multiple faces is dected by FRS system. The interview will be stopped.")
#             stop_recording()
#             break

#         # If exactly two faces are detected, stop the interview
#         if len(faces) > 1 :
#             speak("Error: Two faces detected. The interview will be stopped.")
#             messagebox.showerror("Error", "Two faces detected. The interview process can not be continued .")
#             stop_recording()
#             break

#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#         out.write(frame)
#         show_frame(frame)

#         # Record audio data
#         audio_data = stream.read(1024)
#         frames.append(audio_data)

#     out.release()
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()

#     with wave.open(audio_filename, "wb") as wf:
#         wf.setnchannels(1)
#         wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
#         wf.setframerate(44100)
#         wf.writeframes(b"".join(frames))

#     if recording:
#         merge_audio_video()


        
        

# def merge_audio_video():
#     """Combine audio and video into a single file."""
#     ffmpeg_path = "ffmpeg"  # Ensure ffmpeg is installed and added to PATH
#     command = [
#         ffmpeg_path,
#         "-i",
#         video_filename,
#         "-i",
#         audio_filename,
#         "-c:v",
#         "libx264",
#         "-c:a",
#         "aac",
#         "-strict",
#         "experimental",
#         final_filename,
#     ]
#     subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     speak("Recording saved successfully.")

# def show_frame(frame):
#     """Display the current video frame in the Tkinter GUI."""
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     img = Image.fromarray(frame)
#     imgtk = ImageTk.PhotoImage(image=img)
#     video_label.imgtk = imgtk
#     video_label.configure(image=imgtk)

# def update_video_feed():
#     """Continuously update the video feed."""
#     ret, frame = video_capture.read()
#     if ret:
#         show_frame(frame)
#     if recording:
#         root.after(30, update_video_feed)  # Schedule the next update
#         root.update()

# def display_welcome_message():
#     """Display a welcome message in the Tkinter GUI."""
#     welcome_text = """Welcome to the AI Assistant bot! Kindly follow the instructions below before starting:
# 1. Ensure your camera is turned on and functioning properly.
# 2. Make sure your face is visible and focused on the camera for a better interview experience.
# 3. Once you are ready, click on the 'Start Interview' button to begin.
# 4. If system detect more then 2 face then process will terminate"""
    
#     canvas2.create_text(10, 10, anchor=tk.NW, text=welcome_text, font=('Arial', 16), fill="black", width=760)
#     speak("Dear Candidate, Welcome to the Interview Round. Please select your role to proceed further with the interview.")

# def display_role_selection():
#     """Display role selection window."""
#     role_selection = tk.Toplevel(root)
#     role_selection.title("Select Role")
    
#     def set_role(role):
#         global selected_role
#         selected_role = role
#         role_selection.destroy()
#         start_recording()  
#         threading.Thread(target=start_interview, daemon=True).start()  
    
#     tk.Label(role_selection, text="Please select the position you are applying for:", font=('Arial', 14)).pack(pady=10)
#     tk.Button(role_selection, text="Web Developer", command=lambda: set_role("Web Developer"), font=('Arial', 12)).pack(pady=5)
#     tk.Button(role_selection, text="Data Scientist", command=lambda: set_role("Data Scientist"), font=('Arial', 12)).pack(pady=5)

# def listen():
#     """Listen for the user's speech and return the response and sentiment."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         speak("Listening...")
#         audio = recognizer.listen(source, timeout=15, phrase_time_limit=60)
#     try:
#         response = recognizer.recognize_google(audio)
#         sentiment = analyze_sentiment(response)
#         return response, sentiment
#     except sr.UnknownValueError:
#         speak("Sorry, I did not catch that. Could you please repeat?")
#         return None, None
#     except sr.RequestError as e:
#         speak(f"Error with the speech recognition service: {e}")
#         return None, None

# def analyze_sentiment(text):
#     """Analyze sentiment of the text using TextBlob."""
#     if text:
#         sentiment = TextBlob(text).sentiment.polarity
#         return sentiment
#     return 0

# def start_interview():
#     global responses
#     responses = []

#     if selected_role is None or selected_role not in questions:
#         speak("No questions available for the selected role.")
#         return

#     for question in questions[selected_role]:
#         if interview_stop_flag.is_set():
#             speak("Interview stopped due to multiple face detections.")
#             break

#         speak(question)

#         start_time = time.time()  # Start timer
#         response, sentiment = listen()  # Get user response
#         duration = time.time() - start_time  # Calculate duration

#         if response:
#             responses.append({
#                 "question": question,
#                 "response": response,
#                 "sentiment": sentiment,
#                 "response_time_seconds":  round(duration, 2)
#             })

#             # def update_canvas():
            
#             #     text=f"Q: {question}\nA: {response}\nSentiment: {sentiment:.2f}\nTime: {duration:.2f} seconds",
#             #     font= (('Arial', 12), fill="black", width=470)
#             #     root.update()

#             # root.after(0, update_canvas)

#     save_responses()

# def save_responses():
#     """Save interview responses to a JSON file."""
#     try:
#         with open('interview_responses.json', 'w') as f:
#             json.dump(responses, f, indent=4)
#         speak("Interview completed. Thank you for your time.")
#     except Exception as e:
#         speak(f"Error saving responses: {e}")
#         messagebox.showerror("Error", f"Error saving responses: {e}")

# def close_application():
#     """Close the application and release resources."""
#     global recording
#     recording = False
#     video_capture.release()
#     cv2.destroyAllWindows()
#     root.destroy()

# # Tkinter GUI setup
# root = tk.Tk()
# root.title("AI Assistant Bot")
# root.geometry("900x700")
# root.configure(bg="white")

# # Frames
# video_frame = tk.Frame(root, bg="white")
# video_frame.pack(pady=10)

# controls_frame = tk.Frame(root, bg="white")
# controls_frame.pack(pady=10)

# status_frame = tk.Frame(root, bg="white")
# status_frame.pack(pady=10)

# # Canvas for displaying text
# canvas2 = tk.Canvas(root, width=800, height=200, bg="white")
# canvas2.pack()

# # Video feed
# video_label = tk.Label(video_frame, bg="black", width=640, height=480)
# video_label.pack()

# # Buttons
# start_interview_button = ttk.Button(controls_frame, text="Start Interview", command=display_role_selection)
# start_interview_button.grid(row=0, column=0, padx=10, pady=10)

# exit_button = ttk.Button(controls_frame, text="Exit", command=close_application)
# exit_button.grid(row=0, column=1, padx=10, pady=10)

# # Start video feed
# update_video_feed()

# # Load questions
# load_questions()

# display_welcome_message()

# root.mainloop()



import tkinter as tk
from tkinter import ttk, messagebox
import pyttsx3
import cv2
from PIL import Image, ImageTk
import threading
import pyaudio
import wave
import subprocess
import json
from textblob import TextBlob
import time
import speech_recognition as sr

# Initialize global variables
video_filename = "recorded_video.mp4"
audio_filename = "recorded_audio.wav"
final_filename = "final_output.mp4"
questions = {}
responses = []
selected_role = None
recording = False
interview_stop_flag = threading.Event()

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# Initialize OpenCV variables
video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Thread-safe variables for face detection
face_detection_lock = threading.Lock()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def load_questions():
    """Load questions from a JSON file."""
    global questions
    try:
        with open("questions.json", "r") as f:
            data = json.load(f)
            questions = {role: [q["question"] for q in qs] for item in data["questions"] for role, qs in item.items()}
    except Exception as e:
        speak("Error loading questions. Please check the JSON file.")
        messagebox.showerror("Error", f"Failed to load questions: {e}")

def start_recording():
    """Start video and audio recording in a separate thread."""
    global recording
    recording = True
    threading.Thread(target=record_video_and_audio, daemon=True).start()

def stop_recording():
    """Stop recording."""
    global recording
    recording = False
    
def merge_audio_video():
    """Combine audio and video into a single file."""
    ffmpeg_path = "ffmpeg"  # Ensure ffmpeg is installed and added to PATH
    command = [
        ffmpeg_path,
        "-i",
        video_filename,
        "-i",
        audio_filename,
        "-c:v",
        "libx264",
        "-c:a",
        "aac",
        "-strict",
        "experimental",
        final_filename,
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    speak("Recording saved successfully.")
def record_video_and_audio():
    """Record video and audio and save to disk."""
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(video_filename, fourcc, 20.0, (640, 480))

    # Initialize audio recording
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []

    face_not_detected_count = 0  # Counter for tracking continuous face absence

    while recording:
        # Capture video frame
        ret, frame = video_capture.read()
        if not ret:
            break

        # Detect faces in a separate thread to prevent lag
        threading.Thread(target=detect_faces, args=(frame,), daemon=True).start()

        # Record audio data
        audio_data = stream.read(1024)
        frames.append(audio_data)

    out.release()
    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(audio_filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b"".join(frames))

    if recording:
        merge_audio_video()

def detect_faces(frame):
    """Detect faces and handle logic like stopping the interview if two faces are detected."""
    global face_not_detected_count

    with face_detection_lock:
        # Convert to grayscale and detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) == 0:
            # No face detected, increment counter
            face_not_detected_count += 1
            if face_not_detected_count > 50:  
                speak("Error: No face detected for too long.")
                messagebox.showerror("Error", "No face detected for too long. Please ensure your face is visible.")
                stop_recording()
        elif len(faces) >= 2:
           
            speak("Error: Multiple faces detected. Interview is stopping.")
            messagebox.showerror("Error", "Multiple faces detected. The interview will be stopped.")
            stop_recording()
        else:
            # Reset counter if face detected
            face_not_detected_count = 0

        if len(faces) > 1:
            # Handle the case when exactly two faces are detected
            speak("Error: Two faces detected. The interview process cannot continue.")
            messagebox.showerror("Error", "Two faces detected. The interview will be stopped.")
            stop_recording()

        # Draw rectangles around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        show_frame(frame)

def show_frame(frame):
    """Display the current video frame in the Tkinter GUI."""
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)

def update_video_feed():
    """Continuously update the video feed."""
    ret, frame = video_capture.read()
    if ret:
        show_frame(frame)
    if recording:
        root.after(30, update_video_feed)  # Schedule the next update

def display_welcome_message():
    """Display a welcome message in the Tkinter GUI."""
    welcome_text = """Welcome to the AI Assistant bot! Kindly follow the instructions below before starting:
1. Ensure your camera is turned on and functioning properly.
2. Make sure your face is visible and focused on the camera for a better interview experience.
3. Once you are ready, click on the 'Start button to begin.
4. If system detects more than 2 faces, the process will terminate."""
    
    canvas2.create_text(10, 10, anchor=tk.NW, text=welcome_text, font=('Arial', 16), fill="black", width=760)
    speak("Dear Candidate, Welcome to the Interview Round. Please select your role to proceed further with the interview process.")

def display_role_selection():
    """Display role selection window."""
    role_selection = tk.Toplevel(root)
    role_selection.title("Select Role")
    
    def set_role(role):
        global selected_role
        selected_role = role
        role_selection.destroy()
        start_recording()  
        threading.Thread(target=start_interview, daemon=True).start()  
    
    tk.Label(role_selection, text="Please select the position you are applying for:", font=('Arial', 14)).pack(pady=10)
    tk.Button(role_selection, text="Web Developer", command=lambda: set_role("Web Developer"), font=('Arial', 12)).pack(pady=5)
    tk.Button(role_selection, text="Data Scientist", command=lambda: set_role("Data Scientist"), font=('Arial', 12)).pack(pady=5)

def listen():
    """Listen for the user's speech and return the response and sentiment."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = recognizer.listen(source, timeout=15, phrase_time_limit=60)
    try:
        response = recognizer.recognize_google(audio)
        sentiment = analyze_sentiment(response)
        return response, sentiment
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that. Could you please repeat?")
        return None, None
    except sr.RequestError as e:
        speak(f"Error with the speech recognition service: {e}")
        return None, None


def analyze_sentiment(text):
    """Analyze sentiment of the text using TextBlob."""
    if text:
        sentiment = TextBlob(text).sentiment.polarity
        return sentiment
    return 0

def start_interview():
    global responses
    responses = []

    if selected_role is None or selected_role not in questions:
        speak("No questions available for the selected role.")
        return

    for question in questions[selected_role]:
        if interview_stop_flag.is_set():
            speak("Interview stopped due to multiple face detections.")
            break

        speak(question)

        start_time = time.time()  # Start timer
        response, sentiment = listen()  
        duration = time.time() - start_time 

        if response:
            responses.append({
                "question": question,
                "response": response,
                "sentiment": sentiment,
                "response_time_seconds":  round(duration, 2)
            })

    save_responses()

def save_responses():
    """Save interview responses to a JSON file."""
    try:
        with open('interview_responses.json', 'w') as f:
            json.dump(responses, f, indent=4)
        speak("Interview completed. Thank you for your time.")
    except Exception as e:
        speak(f"Error saving responses: {e}")
        messagebox.showerror("Error", f"Error saving responses: {e}")

def close_application():
    """Close the application and release resources."""
    global recording
    recording = False
    video_capture.release()
    cv2.destroyAllWindows()
    root.destroy()

# Tkinter GUI setup
root = tk.Tk()
root.title("AI Assistant Bot")
root.geometry("900x700")
root.configure(bg="white")

# Frames
video_frame = tk.Frame(root, bg="white")
video_frame.pack(pady=10)

controls_frame = tk.Frame(root, bg="white")
controls_frame.pack(pady=10)

status_frame = tk.Frame(root, bg="white")
status_frame.pack(pady=10)

# Canvas for displaying text
canvas2 = tk.Canvas(root, width=800, height=200, bg="white")
canvas2.pack()

# Video feed
video_label = tk.Label(video_frame, bg="black", width=640, height=480)
video_label.pack()

# Buttons
start_interview_button = ttk.Button(controls_frame, text="Start Interview", command=display_role_selection)
start_interview_button.grid(row=0, column=0, padx=10, pady=10)

exit_button = ttk.Button(controls_frame, text="Exit", command=close_application)
exit_button.grid(row=0, column=1, padx=10, pady=10)

# Start video feed
update_video_feed()

# Load questions
load_questions()

display_welcome_message()

root.mainloop()







