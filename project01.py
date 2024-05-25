from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator
from tkinter import ttk

def clear():
    box2.config(state="normal")
    box1.delete(1.0, END)
    box2.delete(1.0, END)
    box2.config(state="disabled")

def translate():
    dst_lang = lang_codes[dest_lang.get()]
    INPUT = box1.get(1.0, END)
    try:
        t = Translator()
        a = t.translate(text=INPUT, src="auto", dest=dst_lang)
        b = a.text
    except Exception as e:
        if(str(e)=="list index out of range"):
            error_message = "Translation error: none character"
        if(str(e)=="[Errno 11001] getaddrinfo failed"):
            error_message = "Translation error: no internet"
        if(str(e)=="the JSON object must be str, bytes or bytearray, not NoneType"):
            error_message = "Translation error: The limit is 4,999 characters"
        else:
            pass
        b = error_message  # Gán thông báo lỗi vào biến kết quả
    box2.config(state="normal")
    box2.delete(1.0, END)
    box2.insert(1.0, b)
    box2.config(state="disabled")

root = Tk()
root.title('Translate')
root.geometry("500x600")
root.iconbitmap(r'src\logo.ico')
root.resizable(False, False)
load = Image.open(r'src\background.png')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

#Tên app
name = Label(root, text="Translator", fg="#FFFFFF", bd=0, bg="#0f4c82")
name.config(font=(".VnCooper", 30))
name.pack(pady=10)

#Tạo box input
box1 = LabelFrame(root, text="Input")
box1.place(x=40, y=70)
box1 = Text(box1, width=50, height=10, font=("arial", 12))
box1.pack()

# Tạo khoảng cách giữa box1 và box2
spacer = Frame(root, height=20)
spacer.pack()

#Tạo box output
box2 = LabelFrame(root, text="Output")
box2.place(x=40, y=250)
box2 = Text(box2, width=50, height=10, font=("arial", 12))
box2.pack()
#khóa box output
box2.config(state="disabled")

#Tạo box option ngôn ngữ
box_option = LabelFrame(root, text="Option")
box_option.place(x=40, y=450)


#tạo list chọn ngôn ngữ
lang_codes = {
    "English": "en",
    "Vietnamese": "vi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    # thêm ngôn ngữ ở đây
}

#Tạo combobox
dest_lang_label = Label(box_option, text="Destination Language:")
dest_lang_label.pack()
dest_lang = ttk.Combobox(box_option, values=list(lang_codes.keys()))
dest_lang.set("Vietnamese")
dest_lang.pack()

trans_button = Button(root, text="Translate", width=15, command=translate)
trans_button.place(x=340, y=456)
clear_button = Button(root, text="Clear text", width=15, command=clear)
clear_button.place(x=340, y=483)

root.mainloop()