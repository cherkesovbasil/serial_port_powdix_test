from tkinter import *

import back_to_manual_param
import go_to_auto_param
import temperature_buttons
import temperature_humidity_auto_script


def sth(gui, sensor=None, auto=False):
    if sensor is None:
        return

    gui.real_temperature_data = []

    # Прописывает с нуля интерфейсный фрейм
    for widgets in gui.frame_for_units.winfo_children():
        widgets.destroy()

    """
    Информационное поле полученной и расшифрованной команды
    """

    # Поле аналитического юнита
    frame_for_analytical_label = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_analytical_label.pack(side=TOP, padx=1, pady=1, fill=X)

    analytical_label = Label(frame_for_analytical_label, text="Дешифратор принятых команд:", width=30, height=1,
                             bg="gray10", fg="white")
    analytical_label.pack(side=LEFT, padx=3, pady=1)

    # поле отображения наименования полученной информации
    frame_for_response_name = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_response_name.pack(side=TOP, padx=1, pady=1, fill=X)

    device_name = Label(frame_for_response_name, text="Устройство", width=10, height=1, bg="gray90", relief=SUNKEN)
    device_name.pack(side=LEFT, padx=3, pady=1)

    stat_request = Label(frame_for_response_name, text="Команда", width=8, height=1, bg="gray90",
                         relief=SUNKEN)
    stat_request.pack(side=LEFT, padx=3, pady=1)

    stat_hi = Label(frame_for_response_name, text="Статус Hi", width=10, height=1, bg="gray90",
                    relief=SUNKEN)
    stat_hi.pack(side=LEFT, padx=3, pady=1)

    stat_low = Label(frame_for_response_name, text="Статус Low", width=10, height=1, bg="gray90", relief=SUNKEN)
    stat_low.pack(side=LEFT, padx=3, pady=1)

    temp_hi = Label(frame_for_response_name, text="Темп Hi", width=10, height=1, bg="gray90", relief=SUNKEN)
    temp_hi.pack(side=LEFT, padx=3, pady=1)

    temp_low = Label(frame_for_response_name, text="Темп Low", width=10, height=1, bg="gray90", relief=SUNKEN)
    temp_low.pack(side=LEFT, padx=3, pady=1)

    humidity_hi = Label(frame_for_response_name, text="Влажн Hi", width=10, height=1, bg="gray90", relief=SUNKEN)
    humidity_hi.pack(side=LEFT, padx=3, pady=1)

    humidity_low = Label(frame_for_response_name, text="Влажн Low", width=10, height=1, bg="gray90", relief=SUNKEN)
    humidity_low.pack(side=LEFT, padx=3, pady=1)

    package_number = Label(frame_for_response_name, text="№ Пакета", width=8, height=1, bg="gray90", relief=SUNKEN)
    package_number.pack(side=LEFT, padx=3, pady=1)

    crc_name = Label(frame_for_response_name, text="Сумм (CRC)", width=10, height=1, bg="gray90", relief=SUNKEN)
    crc_name.pack(side=LEFT, padx=3, pady=1)

    # поле отображения обработанной информации
    frame_for_response_data = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_response_data.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.device_name_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.device_name_label.pack(side=LEFT, padx=3, pady=1)

    gui.stat_request_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
    gui.stat_request_label.pack(side=LEFT, padx=3, pady=1)

    gui.stat_hi_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.stat_hi_label.pack(side=LEFT, padx=3, pady=1)

    gui.stat_low_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.stat_low_label.pack(side=LEFT, padx=3, pady=1)

    gui.temp_hi_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.temp_hi_label.pack(side=LEFT, padx=3, pady=1)

    gui.temp_low_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.temp_low_label.pack(side=LEFT, padx=3, pady=1)

    gui.humidity_hi_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.humidity_hi_label.pack(side=LEFT, padx=3, pady=1)

    gui.humidity_low_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.humidity_low_label.pack(side=LEFT, padx=3, pady=1)

    gui.package_number_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
    gui.package_number_label.pack(side=LEFT, padx=3, pady=1)

    gui.crc_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.crc_label.pack(side=LEFT, padx=3, pady=1)

    # поле отображения первичной информации
    frame_for_response_clear_data = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_response_clear_data.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.device_name_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90",
                                 relief=SUNKEN)
    gui.device_name_data.pack(side=LEFT, padx=3, pady=1)

    gui.stat_request_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90",
                                  relief=SUNKEN)
    gui.stat_request_data.pack(side=LEFT, padx=3, pady=1)

    gui.stat_hi_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.stat_hi_data.pack(side=LEFT, padx=3, pady=1)

    gui.stat_low_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.stat_low_data.pack(side=LEFT, padx=3, pady=1)

    gui.temp_hi_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.temp_hi_data.pack(side=LEFT, padx=3, pady=1)

    gui.temp_low_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.temp_low_data.pack(side=LEFT, padx=3, pady=1)

    gui.humidity_hi_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90",
                                 relief=SUNKEN)
    gui.humidity_hi_data.pack(side=LEFT, padx=3, pady=1)

    gui.humidity_low_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90",
                                  relief=SUNKEN)
    gui.humidity_low_data.pack(side=LEFT, padx=3, pady=1)

    gui.package_number_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90",
                                    relief=SUNKEN)
    gui.package_number_data.pack(side=LEFT, padx=3, pady=1)

    gui.crc_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.crc_data.pack(side=LEFT, padx=3, pady=1)

    # фреймы для расшифровки статусов
    frame_for_result = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_result.pack(side=TOP, padx=1, pady=1, fill=X)

    frame_for_status_control = LabelFrame(frame_for_result, bg="gray10", text="Дешифрованное представление "
                                                                              "показателей", fg="white")
    frame_for_status_control.pack(side=TOP, padx=10, pady=3, fill=X)

    frame_for_frame = LabelFrame(frame_for_status_control, bg="gray10", fg="white")
    frame_for_frame.pack(side=TOP, padx=5, pady=43, fill=Y)

    frame_for_temperature = LabelFrame(frame_for_frame, bg="gray10", fg="white", text="Температура, °C")
    frame_for_temperature.pack(side=LEFT, padx=15, pady=10, fill=X)

    frame_for_humidity = LabelFrame(frame_for_frame, bg="gray10", fg="white", text="Влажность, %")
    frame_for_humidity.pack(side=LEFT, padx=15, pady=10, fill=X)

    gui.temperature_label = Label(frame_for_temperature, text="--", width=15, height=3, bg="gray90", relief=SUNKEN,
                                  font='Times 20')
    gui.temperature_label.pack(side=LEFT, padx=1, pady=1)

    gui.humidity_label = Label(frame_for_humidity, text="--", width=15, height=3, bg="gray90", relief=SUNKEN,
                               font='Times 20')
    gui.humidity_label.pack(side=LEFT, padx=1, pady=1)

    # Поле отображения командной части интерфейса
    #

    # Поле управляющего юнита

    # фрэймы поля кнопок управления
    frame_for_check_status_button = LabelFrame(gui.frame_for_units, bg="gray90")
    frame_for_check_status_button.pack(side=RIGHT, padx=4, pady=24, fill=X)

    frame_for_info_button = LabelFrame(gui.frame_for_units, bg="gray90")
    frame_for_info_button.pack(side=LEFT, padx=4, pady=24, fill=X)

    # подполе мини-терминала
    gui.info_text_box = Text(gui.frame_for_units, relief=GROOVE, width=53, height=6,
                             selectbackground="grey10")
    gui.info_text_box.pack(side=RIGHT, padx=13, pady=27, fill=X)
    gui.info_text_box.tag_config('tag_red_text', foreground='red')
    gui.info_text_box.tag_config('tag_green_text', foreground='green')
    gui.info_text_box.tag_config('tag_black_text', foreground='black')

    # подполе кнопок управления
    gui.check_status_button = Button(frame_for_check_status_button, text="Обновить статус", relief=GROOVE, width=20,
                                     height=2, bg="gray60",
                                     command=lambda: temperature_buttons.temperature_status_command(gui, sensor))
    gui.check_status_button.pack(side=TOP, pady=4, padx=4)

    gui.info_button = Button(frame_for_info_button, text="Помощь", relief=GROOVE, width=20, height=2,
                             bg="gray60", command=lambda: temperature_buttons.temperature_info_command(gui))
    gui.info_button.pack(side=TOP, pady=4, padx=4)

    # Изменяет состояние кнопок в окне в случае автоматического режима
    if auto:
        gui.sth1_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.sth2_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.sth3_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        if sensor == 1:
            gui.sth1_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)
        elif sensor == 2:
            gui.sth2_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)
        elif sensor == 3:
            gui.sth3_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)
        else:
            return

        go_to_auto_param.go_to_auto_parameters(gui)
        gui.info_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.check_status_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        temperature_humidity_auto_script.start_check(gui, sensor)
    else:
        gui.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        if sensor == 1:
            gui.sth1_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)
        elif sensor == 2:
            gui.sth2_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)
        elif sensor == 3:
            gui.sth3_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)
        else:
            return

        back_to_manual_param.back_to_manual_parameters(gui)
        gui.check_status_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.info_button.configure(bg="gray60", state='normal', relief=GROOVE)
