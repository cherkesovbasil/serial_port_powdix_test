from tkinter import *


def back_to_manual_parameters(gui, number_of_operations=int()):
    try:
        gui.info_text_box.delete('1.0', END)
        gui.info_text_box.insert(END, " ⫸ Ручной режим управления\n", 'tag_red_text')
        gui.info_text_box.yview(END)
        if number_of_operations:
            gui.info_text_box.insert(END,
                                     "Количество успешно выполненных операций = " + str(number_of_operations) + "\n",
                                     'tag_green_text')
    except:
        pass

    gui.poa_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.as_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.auc_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.vs_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.manual_button.configure(state="disabled", bg="SeaGreen1")
    gui.auto_button.configure(state="normal", bg="gray60")

    gui.bytesize_combobox.configure(state="normal")
    gui.timeout_combobox.configure(state="normal")
    gui.baudrate_combobox.configure(state="normal")
    gui.port_combobox.configure(state="normal")

    gui.bytesize_label.configure(fg="black")
    gui.timeout_label.configure(fg="black")
    gui.baudrate_label.configure(fg="black")
    gui.port_label.configure(fg="black")

    gui.refind_button.configure(state="normal", bg="gray60")
    gui.set_button.configure(state="normal", bg="gray60")
    gui.terminal_button.configure(state="normal", bg="gray60", relief=GROOVE)
