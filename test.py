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
    # scr_lang = lang_codes[source_lang.get()]
    dst_lang = lang_codes[dest_lang.get()]
    
    INPUT = box1.get(1.0, END)
    try:
        t = Translator()
        a = t.translate(text=INPUT, src="auto", dest=dst_lang)
        b = a.text
    except Exception as e:
        error_message = "Translation error: " + str(e)
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

#title
name = Label(root, text="Translator", fg="#FFFFFF", bd=0, bg="#0f4c82")
name.config(font=("Transformers Movie", 30))
name.pack(pady=10)

#Tạo box input
box1 = LabelFrame(root, text="Input")
box1.place(x=40, y=70)
box1 = Text(box1, width=35, height=6, font=("arial", 16))
box1.pack()

# Tạo khoảng cách giữa box1 và box2
spacer = Frame(root, height=20)
spacer.pack()

#Tạo box output
box2 = LabelFrame(root, text="Output")
box2.place(x=40, y=250)
box2 = Text(box2, width=35, height=6, font=("arial", 16))
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

# source_lang_label = Label(box_option, text="Source Language:")
# source_lang_label.pack()
# source_lang = ttk.Combobox(box_option, values=list(lang_codes.keys()))
# source_lang.set("English")
# source_lang.pack()

dest_lang_label = Label(box_option, text="Destination Language:")
dest_lang_label.pack()
dest_lang = ttk.Combobox(box_option, values=list(lang_codes.keys()))
dest_lang.set("English")
dest_lang.pack()

trans_button = Button(root, text="Translate", width=15, command=translate)
trans_button.place(x=340, y=456)
clear_button = Button(root, text="Clear text", width=15, command=clear)
clear_button.place(x=340, y=483)

root.mainloop()



#--------------------------------------------------------------------------------------


#from tkinter import *
# from PIL import Image, ImageTk
# # import googletrans
# from googletrans import Translator

# root=Tk()
# root.title('Translate')
# root.geometry("500x600")
# root.iconbitmap(r'src\logo.ico')
# root.resizable(False, False)
# load=Image.open(r'src\background.png')
# render=ImageTk.PhotoImage(load)
# img=Label(root,image=render)
# img.place(x=0,y=0)

# name=Label(root,text="Translator",fg="#FFFFFF", bd=0, bg="#0f4c82")
# name.config(font=("Transformers Movie",30))
# name.pack(pady=10)

# def clear():
#     box1.delete(1.0, END)
#     box2.delete(1.0, END)
# def translate():
#     scr_lang= 'en'
#     dest_lang= 'vi'
#     if (x.get()) == 0:
#         scr_lang= 'en'
#         dest_lang= 'vi'
#     elif(x.get()) == 1:
#         scr_lang= 'vi'
#         dest_lang= 'en'
#     else:
#         pass
#     INPUT = box1.get(1.0, END)
#     t=Translator()
#     a=t.translate(text= INPUT, src= scr_lang, dest= dest_lang)
#     b=a.text
#     box2.delete(1.0, END)
#     box2.insert(1.0, b)

# #Tạo box input
# box1= LabelFrame(root, text="Input")
# box1.place(x=40, y=70)

# box1= Text(box1, width=35, height=6, font=("arial",16))
# box1.pack()

# # Tạo khoảng cách giữa box1 và box2
# spacer = Frame(root, height=20)
# spacer.pack()

# box2= LabelFrame(root, text="Output")
# box2.place(x=40, y=250)

# #Tạo box output
# box2= Text(box2, width=35, height=6, font=("arial",16))
# box2.pack()

# #Tạo box option ngôn ngữ
# box_option = LabelFrame(root, text = "Option")
# box_option.place(x=40, y=450)

# lang = ["English to Vietnamese", "Vietnamese to English"] # 0 là dịch TA-TV, 1 là dịch TV-TA
# x= IntVar()
# x.set("0")

# for index in range(len(lang)):
#     radiobutton = Radiobutton(box_option, text= lang[index], variable=x, value=index, font='arial 10')
#     radiobutton.pack(anchor= W)

# #Tạo box chức năng
# trans_button=Button(root, text="Translate", width=15, command=translate)
# trans_button.place(x=340, y=456)
# clear_button=Button(root, text="Clear text", width=15, command=clear)
# clear_button.place(x=340, y=493)



# root.mainloop()




#---------------------------------------------------------------------------------



# from tkinter import *
# from PIL import Image, ImageTk
# # import googletrans
# from googletrans import Translator

# # Tạo Tk window
# root=Tk()
# root.title('Translate')
# root.geometry("500x630")
# root.iconbitmap('logo.ico')
# root.resizable(False, False)
# load=Image.open('background.png')
# render=ImageTk.PhotoImage(load)
# img=Label(root,image=render)
# img.place(x=0,y=0)

# name=Label(root,text="Translator",fg="#FFFFFF", bd=0, bg="#0f4c82")
# name.config(font=("Transformers Movie",30))
# name.pack(pady=10)

# box1=Text(root, width=28, height=8, font=("ROBOTO",16))
# box1.pack(pady=20)

# Button_frame=Frame(root).pack(side=BOTTOM)

# def clear():
#     box1.delete(1.0, END)
#     box2.delete(1.0, END)
# def translate():
#     INPUT = box1.get(1.0, END)
#     print(INPUT)
#     t=Translator()
#     a=t.translate(INPUT, src="vi", dest="en")
#     b=a.text
#     box2.delete(1.0, END)
#     box2.insert(1.0, b)
# clear_button=Button(Button_frame, text="Clear text", font=(("Arial"), 10, 'bold'), bg='#303030', fg='#ffffff', command=clear)
# clear_button.place(x=150, y=310)
# trans_button=Button(Button_frame, text="Translate", font=(("Arial"), 10, 'bold'), bg='#303030', fg='#ffffff', command=translate)
# trans_button.place(x=290, y=310)

# box2=Text(root, width=28, height=8, font=("ROBOTO",16))
# box2.pack(pady=50)

# root.mainloop()

# # Nguồn: https://pypi.org/project/googletrans-py/
# # mục tiêu: app phiên dịch từ tiếng việt sang tiếng anh 
# # chức năng: phiên dịch



