import threading
import time
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from googletrans import Translator

# Global variables
last_input_time = time.time()
is_translating = False

# Function to translate text
def translate_text():
    global is_translating
    input_text = input_box.get(1.0, END)
    selected_lang = selected_language.get()
    if input_text.strip() and selected_lang:
        is_translating = True
        translator = Translator()
        translation = translator.translate(input_text, src="auto", dest=selected_lang)
        output_text_box.delete(1.0, END)
        output_text_box.insert(1.0, translation.text)
        is_translating = False

# Function to handle key release events
def handle_key_release(event):
    global last_input_time, is_translating

    last_input_time = time.time()
    input_text = input_box.get(1.0, END).strip()

    if is_translating or not input_text:
        output_text_box.delete(1.0, END)  # Clear the output text box
        return

    def countdown():
        time.sleep(2)
        if time.time() - last_input_time >= 0.01:
            translate_text()

    threading.Thread(target=countdown).start()

# Function to translate on space key press
# def translate_on_space(event):
#     # if event.keysym == "space":
#     #     translate_text()
#     pass

# Function to clear the text boxes
def clear():
    input_box.delete(1.0, END)
    output_text_box.delete(1.0, END)

# Create the main application window
root = Tk()
root.title('Translate')
root.geometry("500x630")
root.iconbitmap(r'src\logo.ico')
root.resizable(False, False)


# Load background image
background_image = Image.open(r'src\background.png')
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0)

# Create a title label
title_label = Label(root, text="Translator", fg="#FFFFFF", bd=0, bg="#0f4c82")
title_label.config(font=("Transformers Movie", 30))
title_label.pack(pady=10)

# Create an input text box
input_box = Text(root, width=28, height=8, font=("ROBOTO", 16))
input_box.pack(pady=20, padx=20, fill="both", expand=True)
input_box.bind("<KeyRelease>", handle_key_release)
# input_box.bind("<Key>", translate_on_space)

# Language selection
languages = ['en', 'vi', 'fr', 'de', 'es', 'ja', 'ko', 'zh-CN']
selected_language = StringVar()
selected_language.set(languages[0])

def on_language_change(event):
    translate_text()

# Create a language selection combobox
language_combobox = ttk.Combobox(root, textvariable=selected_language, values=languages, state="readonly")
language_combobox.pack(pady=5)
language_combobox.bind("<<ComboboxSelected>>", on_language_change)

# Create an output text box
output_text_box = Text(root, width=28, height=8, font=("ROBOTO", 16))
output_text_box.pack(pady=50, padx=20, fill="both", expand=True)

# Start the application
root.mainloop()
