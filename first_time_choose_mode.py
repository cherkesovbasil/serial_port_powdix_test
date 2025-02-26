from tkinter import *
import manual_parameters
import auto_parameters
import icon
from base64 import b64decode
from PIL import Image, ImageTk
from tkinter import Label


def choose_mode(gui):
    """При первом запуске добавляет возможность выбора режима работы (ручной/автоматический)"""

    frame_for_choose_mode = LabelFrame(gui.frame_for_units, bg="gray90")
    frame_for_choose_mode.pack(side=TOP, padx=1, pady=165, fill=BOTH)

    frame_for_choose_text = LabelFrame(frame_for_choose_mode, bg="gray90")
    frame_for_choose_text.pack(side=TOP, padx=1, pady=1, fill=X)

    choose_text_label_1 = Label(frame_for_choose_text, text="ВЫБЕРИТЕ РЕЖИМ РАБОТЫ:\n", height=2, fg="black",
                                bg="gray90")
    choose_text_label_1.pack(side=TOP, padx=3, pady=1)

    choose_text_label_2 = Label(frame_for_choose_text,
                                text="⮞ В ручном режиме разблокирована возможность работы с терминалом и нет "
                                     "возможности генерации отчётов ⮜\n",
                                height=2, fg="gray40", bg="gray90")
    choose_text_label_2.pack(side=TOP, padx=3, pady=1)

    choose_text_label_3 = Label(frame_for_choose_text,
                                text="⮞ В автоматическом режиме по умолчанию установлена работа скриптов. "
                                     "Просто выполняйте предлагаемые сценарием действия ⮜\n",
                                height=2, fg="SeaGreen4", bg="gray90")
    choose_text_label_3.pack(side=TOP, padx=3, pady=1)

    frame_for_manual_auto_buttons = LabelFrame(frame_for_choose_mode, bg="gray90")
    frame_for_manual_auto_buttons.pack(side=TOP, padx=1, pady=1, fill=X)

    frame_for_manual_button = LabelFrame(frame_for_manual_auto_buttons, bg="gray90")
    frame_for_manual_button.pack(side=LEFT, padx=10, pady=10, fill=X)

    frame_for_auto_button = LabelFrame(frame_for_manual_auto_buttons, bg="gray90")
    frame_for_auto_button.pack(side=RIGHT, padx=10, pady=10, fill=X)

    initial_manual_button = Button(frame_for_manual_button, text="Ручной", relief=GROOVE, width=40, height=2,
                                   bg="gray60", command=lambda: manual_parameters.manual(gui))
    initial_manual_button.pack(side=LEFT, padx=40, pady=6)

    initial_full_auto_button = Button(frame_for_auto_button, text="Автоматический", relief=GROOVE, width=40,
                                      height=2, bg="SeaGreen1", command=lambda: auto_parameters.auto(gui))
    initial_full_auto_button.pack(side=LEFT, padx=40, pady=6)

    """ Превращает BASE64 код иконки в строку """
    pic_bytes = b64decode(icon.main_icon.encode())  # trasform into bytes with Base64
    image_2 = ImageTk.BytesIO(pic_bytes)  # create a pillow ImageTk from bytes

    """ Открытие иконки (закомментированный для открытия изображений в лэйблах) """
    pil_photo = Image.open(image_2)  # get the image with PIL Image
    tk_photo = ImageTk.PhotoImage(pil_photo)  # convert to an image Tkinter can handle
    # label = Label(self.start_window, image=tk_photo).pack()  # display the image into tkinter interface
    gui.start_window.tk.call('wm', 'iconphoto', gui.start_window, tk_photo)

    gui.start_window.deiconify()
