from tkinter import *
from tkinter import ttk


def run_manual():
    pass


def run_full_auto():
    pass


def poa_analysis_unit():
    """Запускает первичное окно с возможностью первичного просмотра баз данных, добавления, удаления, открытия"""

    start_window = Tk()
    start_window.title("Adjustment utility")

    # disables the ability to zoom the page
    start_window.minsize(800, 600)
    start_window.resizable(False, False)

    # базовые поля
    frame_for_device_buttons = LabelFrame(start_window, bg="gray90")
    frame_for_device_buttons.pack(side=LEFT, padx=1, pady=1, fill=Y)

    frame_for_units = LabelFrame(start_window, bg="gray90")
    frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

    frame_for_settings = LabelFrame(start_window, bg="gray90")
    frame_for_settings.pack(side=BOTTOM, padx=1, pady=1, fill=X)

    # левое поле
    poa_button = Button(frame_for_device_buttons, text="POA", relief=GROOVE, width=5, height=3, bg="SeaGreen1",
                        command=run_manual)
    poa_button.pack(side=TOP, padx=1, pady=1)
    sth1_button = Button(frame_for_device_buttons, text="STH-1", relief=GROOVE, width=5, height=3, bg="gray60",
                         command=run_full_auto)
    sth1_button.pack(side=TOP, padx=1, pady=1)
    sth2_button = Button(frame_for_device_buttons, text="STH-2", relief=GROOVE, width=5, height=3, bg="gray60",
                         command=run_full_auto)
    sth2_button.pack(side=TOP, padx=1, pady=1)
    sth3_button = Button(frame_for_device_buttons, text="STH-3", relief=GROOVE, width=5, height=3, bg="gray60",
                         command=run_full_auto)
    sth3_button.pack(side=TOP, padx=1, pady=1)
    as_button = Button(frame_for_device_buttons, text="AS", relief=GROOVE, width=5, height=3, bg="gray60",
                       command=run_full_auto)
    as_button.pack(side=TOP, padx=1, pady=1)
    sc_button = Button(frame_for_device_buttons, text="SC", relief=GROOVE, width=5, height=3, bg="gray60",
                       command=run_full_auto)
    sc_button.pack(side=TOP, padx=1, pady=1)
    ck_button = Button(frame_for_device_buttons, text="CK", relief=GROOVE, width=5, height=3, bg="gray60",
                       command=run_full_auto)
    ck_button.pack(side=TOP, padx=1, pady=1)

    refind_button = Button(frame_for_device_buttons, text="RR", relief=GROOVE, width=5, height=2, bg="brown1",
                           command=run_full_auto)
    refind_button.pack(side=BOTTOM, padx=1, pady=1)

    # нижнее поле
    set_button = Button(frame_for_settings, text="Set", relief=GROOVE, width=8, height=2, bg="gray60",
                        command=run_full_auto)
    set_button.pack(side=RIGHT, padx=3, pady=1)

    bytesize_list = ["8", "16", "∞"]
    bytesize_combobox = ttk.Combobox(frame_for_settings, values=bytesize_list, width=4, height=2, state="readonly")
    bytesize_combobox.pack(side=RIGHT, padx=3, pady=1)

    bytesize_label = Label(frame_for_settings, text="Bytesize:", width=8, height=2, bg="gray90")
    bytesize_label.pack(side=RIGHT, padx=3, pady=1)

    timeout_list = ["0.1", "0.3", "0.5", "1.0"]
    timeout_combobox = ttk.Combobox(frame_for_settings, values=timeout_list, width=4, height=2, state="readonly")
    timeout_combobox.pack(side=RIGHT, padx=3, pady=1)

    timeout_label = Label(frame_for_settings, text="Timeout(s):", width=8, height=2, bg="gray90")
    timeout_label.pack(side=RIGHT, padx=3, pady=1)

    baudrate_list = ["115200", "500000", "1000000"]
    port_combobox = ttk.Combobox(frame_for_settings, values=baudrate_list, width=8, height=2, state="readonly")
    port_combobox.pack(side=RIGHT, padx=3, pady=1)

    baudrate_label = Label(frame_for_settings, text="Baudrate:", width=8, height=2, bg="gray90")
    baudrate_label.pack(side=RIGHT, padx=3, pady=1)

    port_numbers = ["1", "2", "3", "4"]
    port_combobox = ttk.Combobox(frame_for_settings, values=port_numbers, width=4, height=2, state="readonly")
    port_combobox.pack(side=RIGHT, padx=3, pady=1)

    port_label = Label(frame_for_settings, text="Serial port (COM):", width=14, height=2, bg="gray90")
    port_label.pack(side=RIGHT, padx=3, pady=1)

    manual_button = Button(frame_for_settings, text="Manual", relief=GROOVE, width=8, height=2, bg="gray60",
                           command=run_full_auto)
    manual_button.pack(side=LEFT, padx=3, pady=1)

    # центральное поле (поле юнитов)
    frame_for_analytical_label = LabelFrame(frame_for_units, bg="gray95")
    frame_for_analytical_label.pack(side=TOP, padx=1, pady=1, fill=X)

    analytical_label = Label(frame_for_analytical_label, text="Analytical unit:", width=14, height=1, bg="gray95")
    analytical_label.pack(side=LEFT, padx=3, pady=1)


    # sets the size of the window and places it in the center of the screen
    start_window.update_idletasks()  # Updates information after all frames are created
    s = start_window.geometry()
    s = s.split('+')
    s = s[0].split('x')
    width_main_window = int(s[0])
    height_main_window = int(s[1])

    w = start_window.winfo_screenwidth()
    h = start_window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - width_main_window // 2
    h = h - height_main_window // 2
    start_window.geometry('+{}+{}'.format(w, h))

    start_window.mainloop()


poa_analysis_unit()
