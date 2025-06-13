from tkinter import *
from tkinter.scrolledtext import ScrolledText
import com_ports_unit
import go_to_auto_param


def auto(gui):

    # Очищает базовый фрейм от мусора
    for widget in gui.frame_for_units.winfo_children():
        widget.destroy()

    # Делает интерфейс неактивным для взаимодействия
    go_to_auto_param.go_to_auto_parameters(gui)

    # Создание графической оболочки для отображения поиска и подключения к устройству
    upper_frame = LabelFrame(gui.frame_for_units, bg="gray10")
    upper_frame.pack(side=TOP, padx=1, pady=2, fill=BOTH)

    bottom_frame = LabelFrame(gui.frame_for_units, bg="gray10")
    bottom_frame.pack(side=TOP, padx=1, pady=2, fill=BOTH)

    frame_for_com_ports = LabelFrame(upper_frame, bg="gray10")
    frame_for_com_ports.pack(side=LEFT, padx=1, pady=2, fill=BOTH)

    frame_for_report = LabelFrame(upper_frame, bg="gray10")
    frame_for_report.pack(side=RIGHT, padx=1, pady=2, fill=BOTH)

    gui.frame_for_progress_bar = LabelFrame(bottom_frame, bg="gray10")
    gui.frame_for_progress_bar.pack(side=BOTTOM, pady=2, fill=BOTH)

    gui.box_for_com_ports = ScrolledText(frame_for_com_ports, width=30, height=28, bg="gray10", fg="white")
    gui.box_for_com_ports.pack(padx=1, pady=2, fill=BOTH)

    gui.report_box = Listbox(frame_for_report, relief=GROOVE, width=85, height=28, bg="gray10", fg="white")
    gui.report_box.pack(side=TOP, padx=1, pady=2)

    gui.report_box.insert(END, "                                   ⮜⮜⮜ СТАРТ ПОИСКА ДОСТУПНЫХ COM-портов ⮞⮞⮞")
    gui.report_box.insert(END, "                                              (процедура может занять некоторое время)")
    gui.report_box.update()
    gui.report_box.yview(END)
    gui.again_button = False
    com_ports_unit.com_ports(gui)
