import pyttsx3, os

outfile = input("enter_file_name.extinsion: ")
text = input("Enter your text here: ")

engine = pyttsx3.init('sapi5') # setting sapi5 as voice engine
voices = engine.getProperty('voices') # getting all voices as list
engine.setProperty('rate',140) # voice rate
engine.setProperty('voice', voices[2].id) # voice id
engine.save_to_file(text, outfile) # writing to output file
engine.runAndWait()

print("Conversion completed")

os.system(outfile) # playing audio file