from tkinter import *
from tkinter import ttk
import tkinter as tk

import auto_sampler_auto_script
import request_and_port_list
import auto_sampler_buttons


def aus(gui, auto=False):
    gui.auto_sampler_last_command = None
    gui.auto_sampler_real_state = {}

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

    gui.device_name = Label(frame_for_response_name, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.device_name.pack(side=LEFT, padx=3, pady=1)

    gui.stat_request = Label(frame_for_response_name, text="--", width=8, height=1, bg="gray90",
                             relief=SUNKEN)
    gui.stat_request.pack(side=LEFT, padx=3, pady=1)

    gui.reserve_1 = Label(frame_for_response_name, text="--", width=10, height=1, bg="gray90",
                          relief=SUNKEN)
    gui.reserve_1.pack(side=LEFT, padx=3, pady=1)

    gui.state_1 = Label(frame_for_response_name, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.state_1.pack(side=LEFT, padx=3, pady=1)

    gui.rotate_low = Label(frame_for_response_name, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.rotate_low.pack(side=LEFT, padx=3, pady=1)

    gui.rotate_high = Label(frame_for_response_name, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.rotate_high.pack(side=LEFT, padx=3, pady=1)

    gui.errors = Label(frame_for_response_name, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.errors.pack(side=LEFT, padx=3, pady=1)

    gui.state_2 = Label(frame_for_response_name, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.state_2.pack(side=LEFT, padx=3, pady=1)

    gui.state_set_sample = Label(frame_for_response_name, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
    gui.state_set_sample.pack(side=LEFT, padx=3, pady=1)

    gui.crc_name = Label(frame_for_response_name, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.crc_name.pack(side=LEFT, padx=3, pady=1)

    # поле отображения обработанной информации
    frame_for_response_data = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_response_data.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.device_name_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.device_name_label.pack(side=LEFT, padx=3, pady=1)

    gui.stat_request_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
    gui.stat_request_label.pack(side=LEFT, padx=3, pady=1)

    gui.reserve_1_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.reserve_1_label.pack(side=LEFT, padx=3, pady=1)

    gui.state_1_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.state_1_label.pack(side=LEFT, padx=3, pady=1)

    gui.rotate_low_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.rotate_low_label.pack(side=LEFT, padx=3, pady=1)

    gui.rotate_high_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.rotate_high_label.pack(side=LEFT, padx=3, pady=1)

    gui.errors_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.errors_label.pack(side=LEFT, padx=3, pady=1)

    gui.state_2_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.state_2_label.pack(side=LEFT, padx=3, pady=1)

    gui.state_set_sample_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95",
                                       relief=SUNKEN)
    gui.state_set_sample_label.pack(side=LEFT, padx=3, pady=1)

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

    gui.reserve_1_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.reserve_1_data.pack(side=LEFT, padx=3, pady=1)

    gui.state_1_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.state_1_data.pack(side=LEFT, padx=3, pady=1)

    gui.rotate_low_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90",
                                relief=SUNKEN)
    gui.rotate_low_data.pack(side=LEFT, padx=3, pady=1)

    gui.rotate_high_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90",
                                 relief=SUNKEN)
    gui.rotate_high_data.pack(side=LEFT, padx=3, pady=1)

    gui.errors_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90",
                            relief=SUNKEN)
    gui.errors_data.pack(side=LEFT, padx=3, pady=1)

    gui.state_2_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90",
                             relief=SUNKEN)
    gui.state_2_data.pack(side=LEFT, padx=3, pady=1)

    gui.state_set_sample_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90",
                                      relief=SUNKEN)
    gui.state_set_sample_data.pack(side=LEFT, padx=3, pady=1)

    gui.crc_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.crc_data.pack(side=LEFT, padx=3, pady=1)

    # фреймы для EEPROM и индикации
    frame_for_eeprom_indication = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_eeprom_indication.pack(side=TOP, padx=1, pady=1, fill=X)

    frame_for_eeprom = LabelFrame(frame_for_eeprom_indication, bg="gray10")
    frame_for_eeprom.pack(side=LEFT, padx=1, pady=1, fill=X)

    frame_for_indication = LabelFrame(frame_for_eeprom_indication, bg="gray10")
    frame_for_indication.pack(side=LEFT, padx=18, pady=1, fill=X)

    frame_for_import_eeprom = LabelFrame(frame_for_eeprom, bg="gray10", text="Записать в EEPROM", fg="white")
    frame_for_import_eeprom.pack(side=LEFT, padx=10, pady=20, fill=X)

    frame_for_export_eeprom = LabelFrame(frame_for_eeprom, bg="gray10", text="Считать из EEPROM", fg="white")
    frame_for_export_eeprom.pack(side=LEFT, padx=10, pady=15, fill=X)

    frame_for_parameter_import = LabelFrame(frame_for_import_eeprom, bg="gray10")
    frame_for_parameter_import.pack(side=TOP, padx=1, pady=1, fill=X)

    frame_for_value_import = LabelFrame(frame_for_import_eeprom, bg="gray10")
    frame_for_value_import.pack(side=TOP, padx=1, pady=1, fill=X)

    frame_for_button_import = LabelFrame(frame_for_import_eeprom, bg="gray10")
    frame_for_button_import.pack(side=TOP, padx=1, pady=1, fill=X)

    parameter_import_label = Label(frame_for_parameter_import, text="Параметр", width=8, height=1, bg="gray10",
                                   fg="white")
    parameter_import_label.pack(side=LEFT, padx=3, pady=1)

    def parameters_init():
        parameters = []
        for request in request_and_port_list.autosampler_request_dictionary.keys():
            parameters.append(request)
        return parameters

    def value_init(*args):
        parameter_selection = gui.parameter_import_combobox.get()
        if parameter_selection:
            values_low = []
            values_high = []
            for value in request_and_port_list.autosampler_request_dictionary[parameter_selection][0]:
                values_high.append(value)
            for value in request_and_port_list.autosampler_request_dictionary[parameter_selection][1]:
                values_low.append(value)
            gui.value_import_combobox_low["values"] = values_low
            gui.value_import_combobox_low.current(0)
            gui.value_import_combobox_high["values"] = values_high
            gui.value_import_combobox_high.current(0)
            gui.parameter_export_combobox.set(parameter_selection)

            # очищает значения бита low
            gui.value_export_textbox_low.config(state="normal")
            gui.value_export_textbox_low.delete('1.0', END)
            gui.value_export_textbox_low.config(state="disabled")
            # очищает значения бита high
            gui.value_export_textbox_high.config(state="normal")
            gui.value_export_textbox_high.delete('1.0', END)
            gui.value_export_textbox_high.config(state="disabled")

    gui.parameter_import_combobox = ttk.Combobox(frame_for_parameter_import, width=17, height=50, state="readonly",
                                                 values=parameters_init())
    gui.parameter_import_combobox.pack(side=RIGHT, padx=3, pady=1)

    gui.parameter_import_combobox.bind("<<ComboboxSelected>>", value_init)

    value_import_label = Label(frame_for_value_import, text="High / Low", width=8, height=1, bg="gray10",
                               fg="white")
    value_import_label.pack(side=LEFT, padx=3, pady=1)

    var_h = tk.StringVar()
    var_h.trace('w', value_init)

    gui.value_import_combobox_low = ttk.Combobox(frame_for_value_import, width=6, height=50,
                                                 state="normal", textvariable=var_h)
    gui.value_import_combobox_low.pack(side=RIGHT, padx=3, pady=1)

    var_l = tk.StringVar()
    var_l.trace('w', value_init)

    gui.value_import_combobox_high = ttk.Combobox(frame_for_value_import, width=6, height=50,
                                                  state="normal", textvariable=var_l)
    gui.value_import_combobox_high.pack(side=RIGHT, padx=3, pady=1)

    gui.write_eeprom_button = Button(frame_for_button_import, text="Записать", relief=GROOVE, width=27, height=1,
                                     bg="gray60", state="normal",
                                     command=lambda: auto_sampler_buttons.auto_sampler_write_eeprom_command(gui))
    gui.write_eeprom_button.pack(side=LEFT, pady=1)

    frame_for_parameter_export = LabelFrame(frame_for_export_eeprom, bg="gray10")
    frame_for_parameter_export.pack(side=TOP, padx=1, pady=1, fill=X)

    frame_for_value_export = LabelFrame(frame_for_export_eeprom, bg="gray10")
    frame_for_value_export.pack(side=TOP, padx=1, pady=1, fill=X)

    frame_for_button_export = LabelFrame(frame_for_export_eeprom, bg="gray10")
    frame_for_button_export.pack(side=TOP, padx=1, pady=1, fill=X)

    parameter_export_label = Label(frame_for_parameter_export, text="Параметр", width=8, height=1, bg="gray10",
                                   fg="white")
    parameter_export_label.pack(side=LEFT, padx=3, pady=1)

    def clear_high_low(*args):
        # очищает значения бита low
        gui.value_export_textbox_low.config(state="normal")
        gui.value_export_textbox_low.delete('1.0', END)
        gui.value_export_textbox_low.config(state="disabled")
        # очищает значения бита high
        gui.value_export_textbox_high.config(state="normal")
        gui.value_export_textbox_high.delete('1.0', END)
        gui.value_export_textbox_high.config(state="disabled")

    gui.parameter_export_combobox = ttk.Combobox(frame_for_parameter_export, values=parameters_init(), width=17,
                                                 height=50,
                                                 state="readonly")
    gui.parameter_export_combobox.pack(side=RIGHT, padx=3, pady=1)

    gui.parameter_export_combobox.bind("<<ComboboxSelected>>", clear_high_low)

    value_export_label = Label(frame_for_value_export, text="High / Low", width=8, height=1, bg="gray10",
                               fg="white")
    value_export_label.pack(side=LEFT, padx=3, pady=1)

    gui.value_export_textbox_low = Text(frame_for_value_export, width=7, height=1, state="disabled", bg="gray70")
    gui.value_export_textbox_low.pack(side=RIGHT, padx=3, pady=1)

    gui.value_export_textbox_high = Text(frame_for_value_export, width=7, height=1, state="disabled", bg="gray70")
    gui.value_export_textbox_high.pack(side=RIGHT, padx=3, pady=1)

    gui.read_eeprom_button = Button(frame_for_button_export, text="Считать", relief=GROOVE, width=27, height=1,
                                    bg="gray60", state="normal",
                                    command=lambda: auto_sampler_buttons.auto_sampler_read_eeprom_command(gui))
    gui.read_eeprom_button.pack(side=LEFT, pady=1)

    # Индикация статусов и ошибок
    frame_for_speed = LabelFrame(frame_for_indication, bg="gray10")
    frame_for_speed.pack(side=TOP, padx=1, pady=1, fill=X)
    frame_for_set_indication = LabelFrame(frame_for_indication, bg="gray10", fg="white")
    frame_for_set_indication.pack(side=TOP, padx=1, pady=1, fill=X)

    frame_for_speed_1 = LabelFrame(frame_for_speed, bg="gray10")
    frame_for_speed_1.pack(side=TOP, padx=1, pady=1, fill=X)
    speed_label = Label(frame_for_speed_1, text="Скорость вращения", width=17, height=1, bg="gray10",
                        fg="white")
    speed_label.pack(side=LEFT, padx=1, pady=1)
    gui.speed_textbox = Text(frame_for_speed_1, width=17, height=1, state="disabled", bg="gray70")
    gui.speed_textbox.pack(side=TOP, padx=1, pady=1)

    frame_for_set = LabelFrame(frame_for_set_indication, bg="gray10")
    frame_for_set.pack(side=TOP, padx=1, pady=1, fill=X)
    full_set_label = Label(frame_for_set, text="Установка образца", width=17, height=1, bg="gray10",
                           fg="white")
    full_set_label.pack(side=LEFT, padx=1, pady=1)
    gui.full_set_textbox = Text(frame_for_set, width=17, height=1, state="disabled", bg="gray70")
    gui.full_set_textbox.pack(side=LEFT, padx=1, pady=1)

    frame_for_lift = LabelFrame(frame_for_set_indication, bg="gray10")
    frame_for_lift.pack(side=TOP, padx=1, pady=1, fill=X)
    lift_label = Label(frame_for_lift, text="Лифт", width=17, height=1, bg="gray10",
                       fg="white")
    lift_label.pack(side=LEFT, padx=1, pady=1)
    gui.lift_textbox = Text(frame_for_lift, width=17, height=1, state="disabled", bg="gray70")
    gui.lift_textbox.pack(side=LEFT, padx=1, pady=1)

    frame_for_position = LabelFrame(frame_for_set_indication, bg="gray10")
    frame_for_position.pack(side=TOP, padx=1, pady=1, fill=X)
    position_label = Label(frame_for_position, text="Барабан", width=17, height=1, bg="gray10",
                           fg="white")
    position_label.pack(side=LEFT, padx=1, pady=1)
    gui.position_textbox = Text(frame_for_position, width=17, height=1, state="disabled", bg="gray70")
    gui.position_textbox.pack(side=LEFT, padx=1, pady=1)

    # фреймы для ЗАПУСКА ДВИГАТЕЛЕЙ И УСТАНОВКИ ОБРАЗЦА
    frame_for_engines = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_engines.pack(side=TOP, padx=1, pady=1, fill=X)

    frame_for_engine_1 = LabelFrame(frame_for_engines, bg="gray10", text="Двигатель №1 | барабан |", fg="white")
    frame_for_engine_1.pack(side=LEFT, padx=15, pady=12, fill=X)

    frame_for_engine_2 = LabelFrame(frame_for_engines, bg="gray10", text="Двигатель №2 | лифт |", fg="white")
    frame_for_engine_2.pack(side=LEFT, padx=15, pady=12, fill=X)

    frame_for_engine_3 = LabelFrame(frame_for_engines, bg="gray10", text="Двигатель №3 | вращатель |", fg="white")
    frame_for_engine_3.pack(side=LEFT, padx=15, pady=12, fill=X)

    frame_for_set_sample = LabelFrame(frame_for_engines, bg="gray10", text="Установить образец", fg="white")
    frame_for_set_sample.pack(side=LEFT, padx=15, pady=12, fill=X)

    speed = ["10", "20", "30", "35", "40", "45", "50", "55", "65", "70", "75", "80", "90", "100"]
    position = ["1", "2", "3", "4", "5", "6", "7", "8"]

    # Двигатель №1
    frame_for_speed_engine_1 = LabelFrame(frame_for_engine_1, bg="gray10")
    frame_for_speed_engine_1.pack(side=TOP, padx=1, pady=1, fill=X)

    speed_engine_1_label = Label(frame_for_speed_engine_1, text="Позиция:     ", width=10, height=1, bg="gray10",
                                 fg="white")
    speed_engine_1_label.pack(side=LEFT, padx=3, pady=1)

    gui.speed_engine_1_combobox = ttk.Combobox(frame_for_speed_engine_1, width=5, height=50, state="readonly",
                                               values=position)
    gui.speed_engine_1_combobox.pack(side=RIGHT, padx=3, pady=1)

    gui.speed_engine_1_combobox.set("1")

    frame_for_buttons_engine_1 = LabelFrame(frame_for_engine_1, bg="gray10")
    frame_for_buttons_engine_1.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.engine_1_button = Button(frame_for_buttons_engine_1, text="Запуск", relief=GROOVE, width=20, height=1,
                                 bg="gray60", state="normal",
                                 command=lambda: auto_sampler_buttons.auto_sampler_engine1_command(gui))
    gui.engine_1_button.pack(side=LEFT, pady=1)

    # Двигатель №2
    frame_for_speed_engine_2 = LabelFrame(frame_for_engine_2, bg="gray10")
    frame_for_speed_engine_2.pack(side=TOP, padx=1, pady=1, fill=X)

    lift_engine_2_label = Label(frame_for_speed_engine_2, text="---", width=10, height=1, bg="gray10",
                                fg="white")
    lift_engine_2_label.pack(side=TOP, padx=3, pady=1)

    frame_for_buttons_engine_2 = LabelFrame(frame_for_engine_2, bg="gray10")
    frame_for_buttons_engine_2.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.left_engine_2_button = Button(frame_for_buttons_engine_2, text="⮝⮝⮝", relief=GROOVE, width=10, height=1,
                                      bg="gray60", state="normal",
                                      command=lambda: auto_sampler_buttons.auto_sampler_engine2_up_command(gui))
    gui.left_engine_2_button.pack(side=LEFT, pady=1)

    gui.right_engine_2_button = Button(frame_for_buttons_engine_2, text="⮟⮟⮟", relief=GROOVE, width=10, height=1,
                                       bg="gray60", state="normal",
                                       command=lambda: auto_sampler_buttons.auto_sampler_engine2_down_command(gui))
    gui.right_engine_2_button.pack(side=LEFT, pady=1)

    # Двигатель №3
    frame_for_speed_engine_3 = LabelFrame(frame_for_engine_3, bg="gray10")
    frame_for_speed_engine_3.pack(side=TOP, padx=1, pady=1, fill=X)

    speed_engine_3_label = Label(frame_for_speed_engine_3, text="Скорость:     ", width=10, height=1, bg="gray10",
                                 fg="white")
    speed_engine_3_label.pack(side=LEFT, padx=3, pady=1)

    gui.speed_engine_3_combobox = ttk.Combobox(frame_for_speed_engine_3, width=5, height=50, state="readonly",
                                               values=speed)
    gui.speed_engine_3_combobox.pack(side=RIGHT, padx=3, pady=1)

    gui.speed_engine_3_combobox.set("50")

    frame_for_buttons_engine_3 = LabelFrame(frame_for_engine_3, bg="gray10")
    frame_for_buttons_engine_3.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.left_engine_3_button = Button(frame_for_buttons_engine_3, text="⮜⮜⮜", relief=GROOVE, width=10, height=1,
                                      bg="gray60", state="normal",
                                      command=lambda: auto_sampler_buttons.auto_sampler_engine3_left_command(gui))
    gui.left_engine_3_button.pack(side=LEFT, pady=1)

    gui.right_engine_3_button = Button(frame_for_buttons_engine_3, text="⮞⮞⮞", relief=GROOVE, width=10, height=1,
                                       bg="gray60", state="normal",
                                       command=lambda: auto_sampler_buttons.auto_sampler_engine3_right_command(gui))
    gui.right_engine_3_button.pack(side=LEFT, pady=1)

    # Установить образец
    frame_for_rotate_set = LabelFrame(frame_for_set_sample, bg="gray10")
    frame_for_rotate_set.pack(side=TOP, padx=1, pady=1, fill=X)

    rotate_engine_3_label = Label(frame_for_rotate_set, text="---", width=10, height=1, bg="gray10",
                                  fg="white")
    rotate_engine_3_label.pack(side=TOP, padx=3, pady=1)

    frame_for_button_set_sample = LabelFrame(frame_for_set_sample, bg="gray10")
    frame_for_button_set_sample.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.set_sample_button = Button(frame_for_button_set_sample, text="Установить", relief=GROOVE, width=20, height=1,
                                   bg="gray60", state="normal",
                                   command=lambda: auto_sampler_buttons.auto_sampler_set_sample_command(gui))
    gui.set_sample_button.pack(side=LEFT, pady=1)

    #
    # Поле отображения командной части интерфейса
    #

    # Поле управляющего юнита

    # фрэймы поля кнопок управления автосменщиком

    frame_for_stop_base_buttons = LabelFrame(gui.frame_for_units, bg="gray90")
    frame_for_stop_base_buttons.pack(side=RIGHT, padx=4, pady=19, fill=X)

    frame_for_version_info_buttons = LabelFrame(gui.frame_for_units, bg="gray90")
    frame_for_version_info_buttons.pack(side=LEFT, padx=4, pady=19, fill=X)

    frame_for_status_l_buttons = LabelFrame(gui.frame_for_units, bg="gray90")
    frame_for_status_l_buttons.pack(side=LEFT, padx=4, pady=19, fill=X)

    # подполе мини-терминала
    gui.info_text_box = Text(gui.frame_for_units, relief=GROOVE, width=48, height=6,
                             selectbackground="grey10")
    gui.info_text_box.pack(side=RIGHT, padx=13, pady=10, fill=X)
    gui.info_text_box.tag_config('tag_red_text', foreground='red')
    gui.info_text_box.tag_config('tag_green_text', foreground='green')
    gui.info_text_box.tag_config('tag_black_text', foreground='black')

    # подполе кнопок управления
    gui.version_button = Button(frame_for_version_info_buttons, text="Версия", relief=GROOVE, width=14, height=2,
                                bg="gray60", command=lambda: auto_sampler_buttons.auto_sampler_version_command(gui))
    gui.version_button.pack(side=TOP, pady=4, padx=4)

    gui.info_button = Button(frame_for_version_info_buttons, text="Помощь", relief=GROOVE, width=14, height=2,
                             bg="gray60", command=lambda: auto_sampler_buttons.auto_sampler_info_command(gui))
    gui.info_button.pack(side=TOP, pady=4, padx=4)

    gui.status_button = Button(frame_for_status_l_buttons, text="Статус", relief=GROOVE, width=14, height=2,
                               bg="gray60", command=lambda: auto_sampler_buttons.auto_sampler_status_command(gui))
    gui.status_button.pack(side=TOP, pady=4, padx=4)

    gui.status_l_button = Button(frame_for_status_l_buttons, text="Статус_L", relief=GROOVE, width=14, height=2,
                                 bg="gray60", command=lambda: auto_sampler_buttons.auto_sampler_status_l_command(gui))
    gui.status_l_button.pack(side=TOP, pady=4, padx=4)

    gui.stop_base_button = Button(frame_for_stop_base_buttons, text="Стоп-База", relief=GROOVE, width=14, height=2,
                                  bg="gray60", command=lambda: auto_sampler_buttons.auto_sampler_stop_base_command(gui))
    gui.stop_base_button.pack(side=TOP, pady=4, padx=4)

    gui.stop_button = Button(frame_for_stop_base_buttons, text="Стоп", relief=GROOVE, width=14, height=2,
                             bg="gray60", command=lambda: auto_sampler_buttons.auto_sampler_stop_command(gui))
    gui.stop_button.pack(side=TOP, pady=4, padx=4)

    # Изменяет состояние кнопок в окне в случае автоматического режима
    if auto:
        gui.poa_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.sth1_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.sth2_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.sth3_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.as_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)
        gui.sc_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.ck_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.vs_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.stop_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.stop_base_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.version_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.info_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.status_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.status_l_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.set_sample_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.right_engine_3_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.left_engine_3_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.right_engine_2_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.left_engine_2_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.engine_1_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.read_eeprom_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.write_eeprom_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.manual_button.configure(state="normal", bg="gray60")
        gui.auto_button.configure(state="disabled", bg="SeaGreen1")
        auto_sampler_auto_script.start_check(gui)
    else:
        gui.poa_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.as_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)
        gui.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.vs_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.stop_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.stop_base_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.version_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.info_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.status_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.status_l_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.set_sample_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.right_engine_3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.left_engine_3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.right_engine_2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.left_engine_2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.engine_1_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.read_eeprom_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.write_eeprom_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.manual_button.configure(state="disabled", bg="SeaGreen1")
        gui.auto_button.configure(state="normal", bg="gray60")
