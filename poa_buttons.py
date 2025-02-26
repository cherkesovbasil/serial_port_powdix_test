import request_response
import request_and_port_list
import poa_transcriptions
from tkinter import *


def all_grey(gui):
    # Верхние поля отображения статусов
    gui.device_label.config(text="--", bg="gray90")
    gui.stat_ctrl_label.config(text="--", bg="gray90")
    gui.stat_sens_label.config(text="--", bg="gray90")
    gui.t_max_label.config(text="--", bg="gray90")
    gui.t_min_label.config(text="--", bg="gray90")
    gui.flow_label.config(text="--", bg="gray90")
    gui.errors_label.config(text="--", bg="gray90")
    gui.pwm_1_label.config(text="--", bg="gray90")
    gui.pwm_2_label.config(text="--", bg="gray90")
    gui.crc_label.config(text="--", bg="gray90")

    gui.device_data.config(text="--", bg="gray90")
    gui.stat_ctrl_data.config(text="--", bg="gray90")
    gui.stat_sens_data.config(text="--", bg="gray90")
    gui.t_max_data.config(text="--", bg="gray90")
    gui.t_min_data.config(text="--", bg="gray90")
    gui.flow_data.config(text="--", bg="gray90")
    gui.errors_data.config(text="--", bg="gray90")
    gui.pwm_1_data.config(text="--", bg="gray90")
    gui.pwm_2_data.config(text="--", bg="gray90")
    gui.crc_data.config(text="--", bg="gray90")

    # Status sensors - всё неактивно
    gui.wts1_bit.config(text="-", bg="gray90")
    gui.wts1_label.config(bg="gray90")
    gui.wts2_bit.config(text="-", bg="gray90")
    gui.wts2_label.config(bg="gray90")
    gui.svs_bit.config(text="-", bg="gray90")
    gui.svs_label.config(bg="gray90")
    gui.key_bit.config(text="-", bg="gray90")
    gui.key_label.config(bg="gray90")
    gui.wls_bit.config(text="-", bg="gray90")
    gui.wls_label.config(bg="gray90")
    gui.reserve_1_bit.config(text="-", bg="gray90")
    gui.reserve_1_label.config(bg="gray90")
    gui.reserve_2_bit.config(text="-", bg="gray90")
    gui.reserve_2_label.config(bg="gray90")
    gui.reserve_3_bit.config(text="-", bg="gray90")
    gui.reserve_3_label.config(bg="gray90")

    # Status control - всё неактивно
    gui.rfp_bit.config(text="-", bg="gray90")
    gui.rfp_label.config(bg="gray90")
    gui.wpp_bit.config(text="-", bg="gray90")
    gui.wpp_label.config(bg="gray90")
    gui.acf_bit.config(text="-", bg="gray90")
    gui.acf_label.config(bg="gray90")
    gui.srs_bit.config(text="-", bg="gray90")
    gui.srs_label.config(bg="gray90")
    gui.beeper_bit.config(text="-", bg="gray90")
    gui.beeper_label.config(bg="gray90")
    gui.rfe_bit.config(text="-", bg="gray90")
    gui.rfe_label.config(bg="gray90")
    gui.reserve_4_bit.config(text="-", bg="gray90")
    gui.reserve_4_label.config(bg="gray90")
    gui.reserve_5_bit.config(text="-", bg="gray90")
    gui.reserve_5_label.config(bg="gray90")


def poa_start_command(gui, manual_check=True):
    # Отправляет команду на запуск насоса системы охлаждения
    all_grey(gui)
    request_response.command_sender(
        accepted_request=request_and_port_list.poa_request_dictionary["stop_poa_package"])
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.poa_request_dictionary["start_poa_package"])
    if answer:
        if manual_check:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
        gui.last_command_except_status = request_and_port_list.poa_request_dictionary["start_poa_package"]
        poa_transcriptions.transcript_statuses(gui, answer,
                                               request_and_port_list.poa_request_dictionary["start_poa_package"])
        poa_transcriptions.transcript_other_stuff(gui, answer)
        if manual_check:
            gui.info_text_box.insert(END, " состояние расшифровано\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if manual_check:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)


def poa_stop_command(gui):
    # Отправляет команду на остановку насоса системы охлаждения
    all_grey(gui)
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.poa_request_dictionary["stop_poa_package"])
    if answer:
        gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.last_command_except_status = request_and_port_list.poa_request_dictionary["stop_poa_package"]
        poa_transcriptions.transcript_statuses(gui, answer,
                                               request_and_port_list.poa_request_dictionary["stop_poa_package"])
        poa_transcriptions.transcript_other_stuff(gui, answer)
        gui.info_text_box.insert(END, " состояние расшифровано\n", 'tag_green_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)


def poa_version_command(gui):
    # Отправляет команду на запрос версии системы охлаждения
    all_grey(gui)
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.poa_request_dictionary["version_poa_package"])
    if answer:
        version_answer_hex = str()
        for bit_number in range(2, 16):
            version_answer_hex = str(version_answer_hex) + str(answer[bit_number])
        version_answer_ascii = bytearray.fromhex(version_answer_hex).decode(encoding='ascii')
        gui.info_text_box.insert(END, "✔ Ответ от контроллера:\n", 'tag_green_text')
        gui.info_text_box.insert(END, "⫸ HEX:    " + answer.upper() + "\n⫸ ASCII:  " + version_answer_ascii +
                                 "\n", 'tag_black_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)


def poa_status_command(gui, manual_check=True):
    # Отправляет команду на запрос статуса системы охлаждения
    all_grey(gui)
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.poa_request_dictionary["status_poa_package"])
    if answer:
        if manual_check:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
        poa_transcriptions.transcript_statuses(gui, answer,
                                               request_and_port_list.poa_request_dictionary["status_poa_package"])
        poa_transcriptions.transcript_other_stuff(gui, answer)
        if manual_check:
            gui.info_text_box.insert(END, " состояние расшифровано\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if manual_check:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)


def poa_dry_command(gui):
    # Отправляет команду на откачку воды в системе охлаждения
    all_grey(gui)
    request_response.command_sender(
        accepted_request=request_and_port_list.poa_request_dictionary["stop_poa_package"])
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.poa_request_dictionary["dry_poa_package"])
    if answer:
        gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.last_command_except_status = request_and_port_list.poa_request_dictionary["dry_poa_package"]
        poa_transcriptions.transcript_statuses(gui, answer,
                                               request_and_port_list.poa_request_dictionary["dry_poa_package"])
        poa_transcriptions.transcript_other_stuff(gui, answer)
        gui.info_text_box.insert(END, " состояние расшифровано\n", 'tag_green_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)


def poa_info_command():
    # Команда, вызывающая файл с основной информацией по подсистеме охлаждения
    poa_help_window = Tk()
    poa_help_window.title("Контроль систем дифрактометра")

    # Отключает возможность зума
    poa_help_window.minsize(831, 600)
    poa_help_window.resizable(False, False)

    # Базовые поля
    frame_for_device_buttons = LabelFrame(poa_help_window, bg="gray90")
    frame_for_device_buttons.pack(side=LEFT, padx=1, pady=2, fill=Y)

    frame_for_terminal = LabelFrame(poa_help_window, bg="gray90")
    frame_for_terminal.pack(side=RIGHT, padx=1, pady=2, fill=Y)

    frame_for_settings = LabelFrame(poa_help_window, bg="gray90")
    frame_for_settings.pack(side=BOTTOM, padx=1, pady=1, fill=X)

    frame_for_units = LabelFrame(poa_help_window, bg="gray10")
    frame_for_units.pack(side=TOP, padx=1, pady=1, fill=BOTH)

    poa_button = Button(frame_for_device_buttons, text="СИСТ. ОХЛ.", relief=GROOVE, width=11, height=2,
                             bg="gray60", state="disabled")
    poa_button.pack(side=TOP, padx=1, pady=2)

    # Устанавливает размер окна и помещает его в центр экрана
    poa_help_window.update_idletasks()  # Обновление информации после создания всех фреймов
    s = poa_help_window.geometry()
    s = s.split('+')
    s = s[0].split('x')
    width_main_window = int(s[0])
    height_main_window = int(s[1])

    w = poa_help_window.winfo_screenwidth()
    h = poa_help_window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - width_main_window // 2
    h = h - height_main_window // 2
    poa_help_window.geometry('+{}+{}'.format(w, h))
    # Первичная инициализация с вопросов выбора режима работы

    poa_help_window.mainloop()

    pass
