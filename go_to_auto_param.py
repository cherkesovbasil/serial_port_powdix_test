from tkinter import *


def go_to_auto_parameters(gui):
    try:
        gui.info_text_box.delete('1.0', END)
        gui.info_text_box.insert(END, " ⫸ Переведено в автоматический режим управления\n", 'tag_green_text')
        gui.info_text_box.yview(END)
    except:
        pass

    gui.poa_button.configure(bg="gray60", state='disabled', relief=GROOVE)
    gui.sth1_button.configure(bg="gray60", state='disabled', relief=GROOVE)
    gui.sth2_button.configure(bg="gray60", state='disabled', relief=GROOVE)
    gui.sth3_button.configure(bg="gray60", state='disabled', relief=GROOVE)
    gui.as_button.configure(bg="gray60", state='disabled', relief=GROOVE)
    gui.sc_button.configure(bg="gray60", state='disabled', relief=GROOVE)
    gui.auc_button.configure(bg="gray60", state='disabled', relief=GROOVE)
    gui.ck_button.configure(bg="gray60", state='disabled', relief=GROOVE)
    gui.vs_button.configure(bg="gray60", state='disabled', relief=GROOVE)
    gui.manual_button.configure(state="normal", bg="gray60")
    gui.auto_button.configure(state="disabled", bg="SeaGreen1")

    gui.bytesize_combobox.configure(state="disabled")
    gui.timeout_combobox.configure(state="disabled")
    gui.baudrate_combobox.configure(state="disabled")
    gui.port_combobox.configure(state="disabled")

    gui.bytesize_label.configure(fg="gray60")
    gui.timeout_label.configure(fg="gray60")
    gui.baudrate_label.configure(fg="gray60")
    gui.port_label.configure(fg="gray60")

    gui.refind_button.configure(state="disabled", bg="gray60")
    gui.set_button.configure(state="disabled", bg="gray60")
    gui.terminal_button.configure(state="disabled", bg="gray60", relief=GROOVE)
