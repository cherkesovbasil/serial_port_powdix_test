from tkinter import *
from tkinter.scrolledtext import ScrolledText
import com_ports_unit


def auto(gui):

    # Очищает базовый фрейм от мусора
    for widget in gui.frame_for_units.winfo_children():
        widget.destroy()

    # Делает интерфейс активным для взаимодействия
    gui.poa_button.configure(state="disabled", bg="gray60")
    gui.sth1_button.configure(state="disabled", bg="gray60")
    gui.sth2_button.configure(state="disabled", bg="gray60")
    gui.sth3_button.configure(state="disabled", bg="gray60")
    gui.as_button.configure(state="disabled", bg="gray60")
    gui.sc_button.configure(state="disabled", bg="gray60")
    gui.ck_button.configure(state="disabled", bg="gray60")
    gui.vs_button.configure(state="disabled", bg="gray60")
    gui.refind_button.configure(state="disabled", bg="gray60")
    gui.set_button.configure(state="disabled", bg="gray60")
    gui.manual_button.configure(state="normal", bg="gray60")
    gui.auto_button.configure(state="disabled", bg="SeaGreen1")
    gui.terminal_button.configure(state="disabled", bg="gray60")

    gui.bytesize_combobox.configure(state="disabled")
    gui.timeout_combobox.configure(state="disabled")
    gui.baudrate_combobox.configure(state="disabled")
    gui.port_combobox.configure(state="disabled")

    gui.bytesize_label.configure(fg="gray60")
    gui.timeout_label.configure(fg="gray60")
    gui.baudrate_label.configure(fg="gray60")
    gui.port_label.configure(fg="gray60")

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
