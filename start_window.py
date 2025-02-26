from tkinter import *
from tkinter import ttk


import set_parameters
import cooling_system_unit
import temperature_humidity_unit
import auto_sampler_unit
import sample_changer_unit
import knife_unit
import find_active_device
import manual_parameters
import auto_parameters
import terminal
import first_time_choose_mode
import variable_slit_unit


class Main_frame_unit:
    """Запускает первичное окно с основным функционалом, в которое потом интегрируются модули каждой из систем"""

    def __init__(self):
        self.start_window = Tk()
        self.start_window.title("Контроль систем дифрактометра")

        # СКРЫВАЕТ ОКНО ДО ПОЛНОЙ ГЕНЕРАЦИИ ИНТЕРФЕЙСА (ОТКРЫВАЕТ В first_time_choose_mode)
        self.start_window.withdraw()

        # Отключает возможность зума
        self.start_window.minsize(831, 600)
        self.start_window.resizable(False, False)

        # Базовые поля
        frame_for_device_buttons = LabelFrame(self.start_window, bg="gray90")
        frame_for_device_buttons.pack(side=LEFT, padx=1, pady=2, fill=Y)

        frame_for_terminal = LabelFrame(self.start_window, bg="gray90")
        frame_for_terminal.pack(side=RIGHT, padx=1, pady=2, fill=Y)

        frame_for_settings = LabelFrame(self.start_window, bg="gray90")
        frame_for_settings.pack(side=BOTTOM, padx=1, pady=1, fill=X)

        self.frame_for_units = LabelFrame(self.start_window, bg="gray10")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=BOTH)

        # Левое поле
        self.poa_button = Button(frame_for_device_buttons, text="СИСТ. ОХЛ.", relief=GROOVE, width=11, height=2,
                                 bg="gray60", command=lambda: cooling_system_unit.poa(self, auto=False),
                                 state="disabled")
        self.poa_button.pack(side=TOP, padx=1, pady=2)
        self.sth1_button = Button(frame_for_device_buttons, text="ДАТЧИК Т/В 1", relief=GROOVE, width=11, height=2,
                                  bg="gray60", command=lambda: temperature_humidity_unit.sth(self, sensor=1),
                                  state="disabled")
        self.sth1_button.pack(side=TOP, padx=1, pady=2)
        self.sth2_button = Button(frame_for_device_buttons, text="ДАТЧИК Т/В 2", relief=GROOVE, width=11, height=2,
                                  bg="gray60", command=lambda: temperature_humidity_unit.sth(self, sensor=2),
                                  state="disabled")
        self.sth2_button.pack(side=TOP, padx=1, pady=2)
        self.sth3_button = Button(frame_for_device_buttons, text="ДАТЧИК Т/В 3", relief=GROOVE, width=11, height=2,
                                  bg="gray60", command=lambda: temperature_humidity_unit.sth(self, sensor=3),
                                  state="disabled")
        self.sth3_button.pack(side=TOP, padx=1, pady=2)
        self.as_button = Button(frame_for_device_buttons, text="АВТОСМЕНЩ.", relief=GROOVE, width=11, height=2,
                                bg="gray60", command=lambda: auto_sampler_unit.aus(self), state="disabled")
        self.as_button.pack(side=TOP, padx=1, pady=2)
        self.sc_button = Button(frame_for_device_buttons, text="ВРАЩАТЕЛЬ", relief=GROOVE, width=11, height=2,
                                bg="gray60", command=lambda: sample_changer_unit.sc(self), state="disabled")
        self.sc_button.pack(side=TOP, padx=1, pady=2)
        self.ck_button = Button(frame_for_device_buttons, text="КОЛЛИМАТОР", relief=GROOVE, width=11, height=2,
                                bg="gray60", command=lambda: knife_unit.knife(self), state="disabled")
        self.ck_button.pack(side=TOP, padx=1, pady=2)
        self.vs_button = Button(frame_for_device_buttons, text="ВАР. ЩЕЛЬ", relief=GROOVE, width=11, height=2,
                                bg="gray60", command=lambda: variable_slit_unit.vs(self), state="disabled")
        self.vs_button.pack(side=TOP, padx=1, pady=2)

        self.refind_button = Button(frame_for_device_buttons, text="⭯", relief=GROOVE, width=11, height=2,
                                    bg="gray60", command=lambda: find_active_device.find(self), state="disabled")
        self.refind_button.pack(side=BOTTOM, padx=1, pady=1)

        # Нижнее поле
        self.set_button = Button(frame_for_settings, text="Установить", relief=GROOVE, width=11, height=2,
                                 bg="gray60", command=lambda: set_parameters.set_par(self), state="disabled")
        self.set_button.pack(side=RIGHT, padx=3, pady=1)

        bytesize_list = ["8", "16", "∞"]
        self.bytesize_combobox = ttk.Combobox(frame_for_settings, values=bytesize_list, width=4, height=2,
                                              state="disabled")
        self.bytesize_combobox.pack(side=RIGHT, padx=3, pady=1)

        self.bytesize_label = Label(frame_for_settings, text="Разрядность:", width=11, height=2, bg="gray90",
                                    fg="gray60")
        self.bytesize_label.pack(side=RIGHT, padx=3, pady=1)

        timeout_list = ["0.1", "0.3", "0.5", "1.0"]
        self.timeout_combobox = ttk.Combobox(frame_for_settings, values=timeout_list, width=4, height=2,
                                             state="disabled")
        self.timeout_combobox.pack(side=RIGHT, padx=3, pady=1)

        self.timeout_label = Label(frame_for_settings, text="Таймаут(с):", width=10, height=2, bg="gray90",
                                   fg="gray60")
        self.timeout_label.pack(side=RIGHT, padx=3, pady=1)

        baudrate_list = ["115200", "500000", "1000000"]
        self.baudrate_combobox = ttk.Combobox(frame_for_settings, values=baudrate_list, width=8, height=2,
                                              state="disabled")
        self.baudrate_combobox.pack(side=RIGHT, padx=3, pady=1)

        self.baudrate_label = Label(frame_for_settings, text="Частота:", width=8, height=2, bg="gray90",
                                    fg="gray60")
        self.baudrate_label.pack(side=RIGHT, padx=3, pady=1)

        port_numbers = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10", "COM11",
                        "COM12", "COM13", "COM14", "COM15", "COM16", "COM17", "COM18", "COM19", "COM20"]
        self.port_combobox = ttk.Combobox(frame_for_settings, values=port_numbers, width=8, height=5, state="disabled")
        self.port_combobox.pack(side=RIGHT, padx=3, pady=1)

        self.port_label = Label(frame_for_settings, text="Порт:", width=8, height=2, bg="gray90", fg="gray60")
        self.port_label.pack(side=RIGHT, padx=3, pady=1)

        self.manual_button = Button(frame_for_settings, text="Ручной", relief=GROOVE, width=8, height=2,
                                    bg="gray60", command=lambda: manual_parameters.manual(self), state="disabled")
        self.manual_button.pack(side=LEFT, padx=3, pady=1)

        self.auto_button = Button(frame_for_settings, text="Авто", relief=GROOVE, width=8, height=2,
                                  bg="gray60", command=lambda: auto_parameters.auto(self), state="disabled")
        self.auto_button.pack(side=LEFT, pady=1)

        # правое поле
        self.terminal_button = Button(frame_for_terminal, text="⮞\n⮞\n⮞\n\nТ\nЕ\nР\nМ\nИ\nН\nА\nЛ\n\n⮞\n⮞\n⮞",
                                      relief=GROOVE, width=2, bg="gray60", command=terminal.term, state="disabled")
        self.terminal_button.pack(side=RIGHT, fill=Y)

        # Устанавливает размер окна и помещает его в центр экрана
        self.start_window.update_idletasks()  # Обновление информации после создания всех фреймов
        s = self.start_window.geometry()
        s = s.split('+')
        s = s[0].split('x')
        width_main_window = int(s[0])
        height_main_window = int(s[1])

        w = self.start_window.winfo_screenwidth()
        h = self.start_window.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - width_main_window // 2
        h = h - height_main_window // 2
        self.start_window.geometry('+{}+{}'.format(w, h))
        # Первичная инициализация с вопросов выбора режима работы
        first_time_choose_mode.choose_mode(self)

        self.start_window.mainloop()


Main_frame_unit()
