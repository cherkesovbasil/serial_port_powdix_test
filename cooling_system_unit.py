from tkinter import *

import poa_auto_script
import poa_buttons


def poa(gui, auto):

    gui.last_command_except_status = None

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

    stat_ctrl_name = Label(frame_for_response_name, text="⮜ Status Control ⮞", width=14, height=1, bg="gray90",
                           relief=SUNKEN)
    stat_ctrl_name.pack(side=LEFT, padx=3, pady=1)

    stat_sens_name = Label(frame_for_response_name, text="⮜ Status Sensors ⮞", width=14, height=1, bg="gray90",
                           relief=SUNKEN)
    stat_sens_name.pack(side=LEFT, padx=3, pady=1)

    t_max_name = Label(frame_for_response_name, text="t max", width=8, height=1, bg="gray90", relief=SUNKEN)
    t_max_name.pack(side=LEFT, padx=3, pady=1)

    t_min_name = Label(frame_for_response_name, text="t min", width=8, height=1, bg="gray90", relief=SUNKEN)
    t_min_name.pack(side=LEFT, padx=3, pady=1)

    flow_name = Label(frame_for_response_name, text="Поток", width=8, height=1, bg="gray90", relief=SUNKEN)
    flow_name.pack(side=LEFT, padx=3, pady=1)

    errors_name = Label(frame_for_response_name, text="Ошибки", width=8, height=1, bg="gray90", relief=SUNKEN)
    errors_name.pack(side=LEFT, padx=3, pady=1)

    pwm_1_name = Label(frame_for_response_name, text="PWM 2", width=8, height=1, bg="gray90", relief=SUNKEN)
    pwm_1_name.pack(side=LEFT, padx=3, pady=1)

    pwm_2_name = Label(frame_for_response_name, text="PWM 1", width=8, height=1, bg="gray90", relief=SUNKEN)
    pwm_2_name.pack(side=LEFT, padx=3, pady=1)

    crc_name = Label(frame_for_response_name, text="Сумм (CRC)", width=10, height=1, bg="gray90", relief=SUNKEN)
    crc_name.pack(side=LEFT, padx=3, pady=1)

    # поле отображения обработанной информации
    frame_for_response_data = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_response_data.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.device_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.device_label.pack(side=LEFT, padx=3, pady=1)

    gui.stat_ctrl_label = Label(frame_for_response_data, text="--", width=14, height=2, bg="gray95", relief=SUNKEN)
    gui.stat_ctrl_label.pack(side=LEFT, padx=3, pady=1)

    gui.stat_sens_label = Label(frame_for_response_data, text="--", width=14, height=2, bg="gray95", relief=SUNKEN)
    gui.stat_sens_label.pack(side=LEFT, padx=3, pady=1)

    gui.t_max_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
    gui.t_max_label.pack(side=LEFT, padx=3, pady=1)

    gui.t_min_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
    gui.t_min_label.pack(side=LEFT, padx=3, pady=1)

    gui.flow_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
    gui.flow_label.pack(side=LEFT, padx=3, pady=1)

    gui.errors_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
    gui.errors_label.pack(side=LEFT, padx=3, pady=1)

    gui.pwm_1_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
    gui.pwm_1_label.pack(side=LEFT, padx=3, pady=1)

    gui.pwm_2_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
    gui.pwm_2_label.pack(side=LEFT, padx=3, pady=1)

    gui.crc_label = Label(frame_for_response_data, text="--", width=10, height=2, bg="gray95", relief=SUNKEN)
    gui.crc_label.pack(side=LEFT, padx=3, pady=1)

    # поле отображения первичной информации
    frame_for_response_clear_data = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_response_clear_data.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.device_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.device_data.pack(side=LEFT, padx=3, pady=1)

    gui.stat_ctrl_data = Label(frame_for_response_clear_data, text="--", width=14, height=1, bg="gray90", relief=SUNKEN)
    gui.stat_ctrl_data.pack(side=LEFT, padx=3, pady=1)

    gui.stat_sens_data = Label(frame_for_response_clear_data, text="--", width=14, height=1, bg="gray90", relief=SUNKEN)
    gui.stat_sens_data.pack(side=LEFT, padx=3, pady=1)

    gui.t_max_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
    gui.t_max_data.pack(side=LEFT, padx=3, pady=1)

    gui.t_min_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
    gui.t_min_data.pack(side=LEFT, padx=3, pady=1)

    gui.flow_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
    gui.flow_data.pack(side=LEFT, padx=3, pady=1)

    gui.errors_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
    gui.errors_data.pack(side=LEFT, padx=3, pady=1)

    gui.pwm_1_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
    gui.pwm_1_data.pack(side=LEFT, padx=3, pady=1)

    gui.pwm_2_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
    gui.pwm_2_data.pack(side=LEFT, padx=3, pady=1)

    gui.crc_data = Label(frame_for_response_clear_data, text="--", width=10, height=1, bg="gray90", relief=SUNKEN)
    gui.crc_data.pack(side=LEFT, padx=3, pady=1)

    # фреймы для расшифровки статусов
    frame_for_statuses = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_statuses.pack(side=TOP, padx=1, pady=1, fill=X)

    frame_for_status_control = LabelFrame(frame_for_statuses, bg="gray10", text="Дешифровка ⮜ Status Control ⮞",
                                          fg="white")
    frame_for_status_control.pack(side=LEFT, padx=10, pady=3, fill=X)

    frame_for_status_sensors = LabelFrame(frame_for_statuses, bg="gray10", text="Дешифровка ⮜ Status Sensors ⮞",
                                          fg="white")
    frame_for_status_sensors.pack(side=RIGHT, padx=10, pady=3, fill=X)

    """
    Поле отображения информации Status Control
    """

    # интерфейс расшифровки команды питания вентиляторов радиатора
    frame_for_rfp = LabelFrame(frame_for_status_control, bg="gray95")
    frame_for_rfp.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.rfp_bit = Label(frame_for_rfp, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.rfp_bit.pack(side=LEFT, padx=3, pady=1)

    gui.rfp_label = Label(frame_for_rfp, text=" - Включение вентиляторов радиатора", width=43, height=1,
                          bg="gray95", relief=SUNKEN, anchor=W)
    gui.rfp_label.pack(side=LEFT, padx=3, pady=1)

    # интерфейс расшифровки команды питания помпы
    frame_for_wpp = LabelFrame(frame_for_status_control, bg="gray95")
    frame_for_wpp.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.wpp_bit = Label(frame_for_wpp, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.wpp_bit.pack(side=LEFT, padx=3, pady=1)

    gui.wpp_label = Label(frame_for_wpp, text=" - Включение питания помпы", width=43, height=1, bg="gray95",
                          relief=SUNKEN, anchor=W)
    gui.wpp_label.pack(side=LEFT, padx=3, pady=1)

    # интерфейс расшифровки команды питания вентилятора воздушного охлаждения
    frame_for_acf = LabelFrame(frame_for_status_control, bg="gray95")
    frame_for_acf.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.acf_bit = Label(frame_for_acf, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.acf_bit.pack(side=LEFT, padx=3, pady=1)

    gui.acf_label = Label(frame_for_acf, text=" - Вкл. вентилятора воздушного охлажд. (PWM)", width=43, height=1,
                          bg="gray95", relief=SUNKEN, anchor=W)
    gui.acf_label.pack(side=LEFT, padx=3, pady=1)

    # интерфейс расшифровки команды включения петли безопасности
    frame_for_srs = LabelFrame(frame_for_status_control, bg="gray95")
    frame_for_srs.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.srs_bit = Label(frame_for_srs, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.srs_bit.pack(side=LEFT, padx=3, pady=1)

    gui.srs_label = Label(frame_for_srs, text=" - Включение петли безопасности", width=43, height=1, bg="gray95",
                          relief=SUNKEN, anchor=W)
    gui.srs_label.pack(side=LEFT, padx=3, pady=1)

    # интерфейс расшифровки команды активации пищалки
    frame_for_beeper = LabelFrame(frame_for_status_control, bg="gray95")
    frame_for_beeper.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.beeper_bit = Label(frame_for_beeper, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.beeper_bit.pack(side=LEFT, padx=3, pady=1)

    gui.beeper_label = Label(frame_for_beeper, text=" - Включение звукового сигнала", width=43, height=1, bg="gray95",
                             relief=SUNKEN, anchor=W)
    gui.beeper_label.pack(side=LEFT, padx=3, pady=1)

    # интерфейс расшифровки команды активации bRadiator_Fan_En
    frame_for_rfe = LabelFrame(frame_for_status_control, bg="gray95")
    frame_for_rfe.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.rfe_bit = Label(frame_for_rfe, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.rfe_bit.pack(side=LEFT, padx=3, pady=1)

    gui.rfe_label = Label(frame_for_rfe, text=" - Вкл. вентилятора воздушного охлажд. (MAX)", width=43, height=1,
                          bg="gray95", relief=SUNKEN, anchor=W)
    gui.rfe_label.pack(side=LEFT, padx=3, pady=1)

    # резервный бит reserve_4
    frame_for_reserve_4 = LabelFrame(frame_for_status_control, bg="gray95")
    frame_for_reserve_4.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.reserve_4_bit = Label(frame_for_reserve_4, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.reserve_4_bit.pack(side=LEFT, padx=3, pady=1)

    gui.reserve_4_label = Label(frame_for_reserve_4, text=" - Резервный бит", width=43, height=1, bg="gray95",
                                relief=SUNKEN, anchor=W)
    gui.reserve_4_label.pack(side=LEFT, padx=3, pady=1)

    # резервный бит reserve_5
    frame_for_reserve_5 = LabelFrame(frame_for_status_control, bg="gray95")
    frame_for_reserve_5.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.reserve_5_bit = Label(frame_for_reserve_5, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.reserve_5_bit.pack(side=LEFT, padx=3, pady=1)

    gui.reserve_5_label = Label(frame_for_reserve_5, text=" - Резервный бит", width=43, height=1, bg="gray95",
                                relief=SUNKEN, anchor=W)
    gui.reserve_5_label.pack(side=LEFT, padx=3, pady=1)

    """
    Поле отображения информации Status Sensors
    """

    # интерфейс расшифровки статуса датчика температуры холодной воды
    frame_for_wts1 = LabelFrame(frame_for_status_sensors, bg="gray95")
    frame_for_wts1.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.wts1_bit = Label(frame_for_wts1, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.wts1_bit.pack(side=LEFT, padx=3, pady=1)

    gui.wts1_label = Label(frame_for_wts1, text=" - Сработка датчика крана горячей воды", width=43, height=1,
                           bg="gray95", relief=SUNKEN, anchor=W)
    gui.wts1_label.pack(side=LEFT, padx=3, pady=1)

    # интерфейс расшифровки статуса датчика температуры холодной воды
    frame_for_wts2 = LabelFrame(frame_for_status_sensors, bg="gray95")
    frame_for_wts2.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.wts2_bit = Label(frame_for_wts2, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.wts2_bit.pack(side=LEFT, padx=3, pady=1)

    gui.wts2_label = Label(frame_for_wts2, text=" - Сработка датчика крана холодной воды", width=43, height=1,
                           bg="gray95", relief=SUNKEN, anchor=W)
    gui.wts2_label.pack(side=LEFT, padx=3, pady=1)

    # интерфейс расшифровки статуса пароводяного клапана
    frame_for_svs = LabelFrame(frame_for_status_sensors, bg="gray95")
    frame_for_svs.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.svs_bit = Label(frame_for_svs, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.svs_bit.pack(side=LEFT, padx=3, pady=1)

    gui.svs_label = Label(frame_for_svs, text=" - Сработка пароводяного клапана", width=43, height=1, bg="gray95",
                          relief=SUNKEN, anchor=W)
    gui.svs_label.pack(side=LEFT, padx=3, pady=1)

    # интерфейс расшифровки статуса ключа системы охлаждения
    frame_for_key = LabelFrame(frame_for_status_sensors, bg="gray95")
    frame_for_key.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.key_bit = Label(frame_for_key, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.key_bit.pack(side=LEFT, padx=3, pady=1)

    gui.key_label = Label(frame_for_key, text=" - Ключ системы охлаждения (1 = Work / 0 = Dry)", width=43, height=1,
                          bg="gray95", relief=SUNKEN, anchor=W)
    gui.key_label.pack(side=LEFT, padx=3, pady=1)

    # интерфейс расшифровки статуса датчика уровня воды
    frame_for_wls = LabelFrame(frame_for_status_sensors, bg="gray95")
    frame_for_wls.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.wls_bit = Label(frame_for_wls, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.wls_bit.pack(side=LEFT, padx=3, pady=1)

    gui.wls_label = Label(frame_for_wls, text=" - Сработка датчика уровня воды (поплавок)", width=43, height=1,
                          bg="gray95", relief=SUNKEN, anchor=W)
    gui.wls_label.pack(side=LEFT, padx=3, pady=1)

    # резервный бит reserve_1
    frame_for_reserve_1 = LabelFrame(frame_for_status_sensors, bg="gray95")
    frame_for_reserve_1.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.reserve_1_bit = Label(frame_for_reserve_1, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.reserve_1_bit.pack(side=LEFT, padx=3, pady=1)

    gui.reserve_1_label = Label(frame_for_reserve_1, text=" - Резервный бит", width=43, height=1, bg="gray95",
                                relief=SUNKEN, anchor=W)
    gui.reserve_1_label.pack(side=LEFT, padx=3, pady=1)

    # резервный бит reserve_2
    frame_for_reserve_2 = LabelFrame(frame_for_status_sensors, bg="gray95")
    frame_for_reserve_2.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.reserve_2_bit = Label(frame_for_reserve_2, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.reserve_2_bit.pack(side=LEFT, padx=3, pady=1)

    gui.reserve_2_label = Label(frame_for_reserve_2, text=" - Резервный бит", width=43, height=1, bg="gray95",
                                relief=SUNKEN, anchor=W)
    gui.reserve_2_label.pack(side=LEFT, padx=3, pady=1)

    # резервный бит reserve_3
    frame_for_reserve_3 = LabelFrame(frame_for_status_sensors, bg="gray95")
    frame_for_reserve_3.pack(side=TOP, padx=1, pady=1, fill=X)

    gui.reserve_3_bit = Label(frame_for_reserve_3, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
    gui.reserve_3_bit.pack(side=LEFT, padx=3, pady=1)

    gui.reserve_3_label = Label(frame_for_reserve_3, text=" - Резервный бит", width=43, height=1, bg="gray95",
                                relief=SUNKEN, anchor=W)
    gui.reserve_3_label.pack(side=LEFT, padx=3, pady=1)

    #
    # Поле отображения командной части интерфейса
    #

    # Поле управляющего юнита

    # фрэймы поля кнопок управления системой охлаждения
    frame_for_start_stop_buttons = LabelFrame(gui.frame_for_units, bg="gray90")
    frame_for_start_stop_buttons.pack(side=RIGHT, padx=4, pady=24, fill=X)

    frame_for_dry_status_buttons = LabelFrame(gui.frame_for_units, bg="gray90")
    frame_for_dry_status_buttons.pack(side=RIGHT, padx=4, pady=24, fill=X)

    frame_for_version_info_buttons = LabelFrame(gui.frame_for_units, bg="gray90")
    frame_for_version_info_buttons.pack(side=LEFT, padx=4, pady=24, fill=X)

    # подполе мини-терминала
    gui.info_text_box = Text(gui.frame_for_units, relief=GROOVE, width=48, height=6,
                             selectbackground="grey10")
    gui.info_text_box.pack(side=RIGHT, padx=13, pady=10, fill=X)
    gui.info_text_box.tag_config('tag_red_text', foreground='red')
    gui.info_text_box.tag_config('tag_green_text', foreground='green')
    gui.info_text_box.tag_config('tag_black_text', foreground='black')

    # подполе кнопок управления
    gui.start_button = Button(frame_for_start_stop_buttons, text="Старт", relief=GROOVE, width=14, height=2,
                              bg="gray60", command=lambda: poa_buttons.poa_start_command(gui))
    gui.start_button.pack(side=TOP, pady=4, padx=4)

    gui.stop_button = Button(frame_for_start_stop_buttons, text="Стоп", relief=GROOVE, width=14, height=2,
                             bg="gray60", command=lambda: poa_buttons.poa_stop_command(gui))
    gui.stop_button.pack(side=TOP, pady=4, padx=4)

    gui.version_button = Button(frame_for_version_info_buttons, text="Версия", relief=GROOVE, width=14, height=2,
                                bg="gray60", command=lambda: poa_buttons.poa_version_command(gui))
    gui.version_button.pack(side=TOP, pady=4, padx=4)

    gui.info_button = Button(frame_for_version_info_buttons, text="Помощь", relief=GROOVE, width=14, height=2,
                             bg="gray60", command=lambda: poa_buttons.poa_info_command(gui))
    gui.info_button.pack(side=TOP, pady=4, padx=4)

    gui.dry_button = Button(frame_for_dry_status_buttons, text="Откачка", relief=GROOVE, width=14, height=2,
                            bg="gray60", command=lambda: poa_buttons.poa_dry_command(gui))
    gui.dry_button.pack(side=TOP, pady=4, padx=4)

    gui.status_button = Button(frame_for_dry_status_buttons, text="Статус", relief=GROOVE, width=14, height=2,
                               bg="gray60", command=lambda: poa_buttons.poa_status_command(gui))
    gui.status_button.pack(side=TOP, pady=4, padx=4)

    # Изменяет состояние кнопок в окне в случае автоматического режима
    if auto:
        gui.poa_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)
        gui.sth1_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.sth2_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.sth3_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.as_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.sc_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.ck_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.vs_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.start_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.stop_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.version_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.info_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.dry_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        gui.status_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        poa_auto_script.start_check(gui)
    else:
        gui.poa_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)
        gui.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.as_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)
        gui.vs_button.configure(bg="gray60", state='normal', relief=GROOVE)
