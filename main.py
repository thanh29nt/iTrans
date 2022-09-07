import googletrans
from googletrans import Translator
t = Translator()
from tkinter import  *
from PIL import Image, ImageTk
from time import strftime

root = Tk()
root.title("iTrans")
root.geometry("960x541")
root.iconbitmap("Moon.ico")

load = Image.open("FullMoon.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x = 0, y = 0)

name = Label(root, text = "This is iTrans", fg = "#FFFFFF", bd = 0.5, bg = "#03152F")
name.config(font=("Transformers Movie", 15))
name.pack(pady = 10)

boxSrc = Text(root, width = 15, height = 1, font = ("ROBOTO", 12))
boxSrc.place(x = 8, y = 10)

boxDest = Text(root, width = 15, height = 1, font = ("ROBOTO", 12))
boxDest.place(x = 8, y = 40)

box = Text(root, width = 35, height = 5, font = ("ROBOTO", 16))
box.pack(pady = 15)

box1 = Text(root, width = 35, height = 5, font = ("ROBOTO", 16))
box1.pack(pady = 50)

box2 = Label(root, font = ("Digital-7", 16), bg = "#03152F", fg = "#ffffff")
box2.pack(pady = 60)
box2.place(x = 410, y = 210)

button_frame = Frame(root).pack(side = BOTTOM)

def clear() :
    box.delete(1.0, END)
    box1.delete(1.0, END)
def trans() :
    INPUT = box.get('1.0', 'end-1c')
    INPUTsrc = boxSrc.get('1.0', 'end-1c')
    INPUTdst = boxDest.get('1.0', 'end-1c')
    t = Translator()
    a = t.translate(INPUT, src = INPUTsrc, dest = INPUTdst)
    b = a.text
    box1.insert(END, b)

def clock() :
    string = strftime('%H : %M : %S : %p')
    box2.config(text = string)
    box2.after(1000, clock)


clear_btn = Button(button_frame, text = "Clear text", font = (("Arial"), 10, 'bold'), bg = "#303030", fg = "#FFFFFF", command = clear)
clear_btn.place(x = 600, y = 210)
trans_btn = Button(button_frame, text = "Translate", font = (("Arial"), 10, 'bold'), bg = "#303030", fg = "#FFFFFF", command = trans)
trans_btn.place(x = 285, y = 210)
clock()

root.mainloop()


# List languages available
#{'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 
# 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 
# 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 
# 'da': 'danish', 'nl': 'dutch', 
# 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 
# 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 
# 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 
# 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 
# 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 
# 'ja': 'japanese', 'jw': 'javanese', 
# 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 
# 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 
# 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 
# 'ne': 'nepali', 'no': 'norwegian', 
# 'or': 'odia', 
# 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 
# 'ro': 'romanian', 'ru': 'russian', '
# sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 
# 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 
# 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 
# 'vi': 'vietnamese', 
# 'cy': 'welsh',
# 'xh': 'xhosa', 
# 'yi': 'yiddish', 'yo': 'yoruba', 
# 'zu': 'zulu'}
