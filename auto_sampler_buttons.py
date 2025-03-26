import time

import request_response
import request_and_port_list
from tkinter import *
import tkinter as tk


def all_grey(gui):
    # Верхние поля отображения статусов
    gui.device_name_label.config(text="--", bg="gray90")
    gui.stat_request_label.config(text="--", bg="gray90")
    gui.stat_hi_label.config(text="--", bg="gray90")
    gui.stat_low_label.config(text="--", bg="gray90")
    gui.temp_hi_label.config(text="--", bg="gray90")
    gui.temp_low_label.config(text="--", bg="gray90")
    gui.humidity_hi_label.config(text="--", bg="gray90")
    gui.humidity_low_label.config(text="--", bg="gray90")
    gui.package_number_label.config(text="--", bg="gray90")
    gui.crc_label.config(text="--", bg="gray90")

    gui.device_name_data.config(text="--", bg="gray90")
    gui.stat_request_data.config(text="--", bg="gray90")
    gui.stat_hi_data.config(text="--", bg="gray90")
    gui.stat_low_data.config(text="--", bg="gray90")
    gui.temp_hi_data.config(text="--", bg="gray90")
    gui.temp_low_data.config(text="--", bg="gray90")
    gui.humidity_hi_data.config(text="--", bg="gray90")
    gui.humidity_low_data.config(text="--", bg="gray90")
    gui.package_number_data.config(text="--", bg="gray90")
    gui.crc_data.config(text="--", bg="gray90")

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.yview(END)

    # Status sensors - всё неактивно
    # gui.temperature_label.config(text="--", bg="gray90")
    # gui.humidity_label.config(text="--", bg="gray90")


def auto_sampler_version_command(gui):
    # Отправляет команду на запрос версии системы охлаждения
    all_grey(gui)
    gui.info_text_box.insert(END, ">> Выполнение команды *Версия*\n")
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["version_sc_package"])
    if answer:
        version_answer_hex = str()
        for bit_number in range(2, 16):
            version_answer_hex = str(version_answer_hex) + str(answer[bit_number])
        version_answer_ascii = bytearray.fromhex(version_answer_hex).decode(encoding='ascii')
        gui.info_text_box.insert(END, "✔ Ответ контроллера:\n", 'tag_green_text')
        gui.info_text_box.insert(END, "⫸ HEX:    " + answer.upper() + "\n⫸ ASCII:  " + version_answer_ascii +
                                 "\n", 'tag_black_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.version_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.version_button.configure(bg="gray60")


def auto_sampler_status_command(gui):
    pass


def auto_sampler_status_l_command(gui):
    pass


def auto_sampler_stop_base_command(gui):
    all_grey(gui)
    gui.info_text_box.insert(END, ">> Выполнение команды *Стоп-База*\n")
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["stop_base_sc_package"])
    if answer:
        gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.stop_base_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.stop_base_button.configure(bg="gray60")


def auto_sampler_stop_command(gui):
    all_grey(gui)
    gui.info_text_box.insert(END, ">> Выполнение команды *Стоп*\n")
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["stop_sc_package"])
    if answer:
        gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.stop_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.stop_button.configure(bg="gray60")


def auto_sampler_write_eeprom_command(gui):
    all_grey(gui)
    gui.info_text_box.insert(END, ">> Выполнение команды *Запись в EEPROM*\n")
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    request_name = gui.parameter_import_combobox.get()
    if not request_name:
        gui.info_text_box.insert(END, "❌ Выберите запрос перед нажатием кнопки\n'Записать'\n", 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.write_eeprom_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.write_eeprom_button.configure(bg="gray60")
        return ()

    low_byte = gui.value_import_combobox_low.get().lower()
    if len(low_byte) != 2 and len(low_byte) != 0:
        print(low_byte)
        gui.info_text_box.insert(END, "❌ Убедитесь, что ввели корректное значение\n"
                                      "('hex' содержит только 2 значения (цифра либо \nбуква) [low byte])\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.write_eeprom_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.write_eeprom_button.configure(bg="gray60")
        return ()
    if low_byte == "--" or low_byte == "":
        hex_low_byte = None
    else:
        for letter in low_byte:
            if letter not in "abcdef0123456789":
                gui.info_text_box.insert(END, "❌ Убедитесь, что ввели корректное значение\n"
                                              "('hex' содержит только цифры 0-9 и буквы A-F)\n", 'tag_red_text')
                gui.info_text_box.yview(END)
                gui.write_eeprom_button.configure(bg="salmon")
                gui.frame_for_units.update_idletasks()
                time.sleep(0.5)
                gui.write_eeprom_button.configure(bg="gray60")
                return ()
        hex_low_byte = hex(int("0x" + str(low_byte), 16))

    high_byte = gui.value_import_combobox_high.get().lower()
    if len(high_byte) != 2 and len(high_byte) != 0:
        gui.info_text_box.insert(END, "❌ Убедитесь, что ввели корректное значение\n"
                                      "('hex' содержит только 2 значения (цифра либо \nбуква) [high byte])\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.write_eeprom_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.write_eeprom_button.configure(bg="gray60")
        return ()
    if high_byte == "--" or high_byte == "":
        hex_high_byte = None
    else:
        for letter in high_byte:
            if letter not in "abcdef0123456789":
                gui.info_text_box.insert(END, "❌ Убедитесь, что ввели корректное значение\n"
                                              "('hex' содержит только цифры 0-9 и буквы A-F)\n", 'tag_red_text')
                gui.info_text_box.yview(END)
                gui.write_eeprom_button.configure(bg="salmon")
                gui.frame_for_units.update_idletasks()
                time.sleep(0.5)
                gui.write_eeprom_button.configure(bg="gray60")
                return ()
        hex_high_byte = hex(int("0x" + str(high_byte), 16))

    # Запись low byte
    if hex_low_byte:
        # получение бита low
        request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"][2] = \
            request_and_port_list.autosampler_eeprom_dictionary[request_name][0]
        request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"][4] = int(hex_low_byte, 16)
        answer = request_response.command_sender(
            accepted_request=request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"])
        if answer:
            low_answer_hex = str()
            for bit_number in range(2, 16):
                low_answer_hex = str(low_answer_hex) + str(answer[bit_number])
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ байта LOW получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
        else:
            gui.info_text_box.insert(END,
                                     "❌ Нет ответа контроллера на запрос байта LOW\n"
                                     " * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.write_eeprom_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.write_eeprom_button.configure(bg="gray60")
            return ()
    # Запись high byte
    if hex_high_byte:
        if not request_and_port_list.autosampler_eeprom_dictionary[request_name][1]:
            gui.info_text_box.insert(END,
                                     "❌ Для данной настройки есть только байт LOW\n"
                                     " * очистите поле HIGH *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.write_eeprom_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.write_eeprom_button.configure(bg="gray60")
            return ()
        # получение бита high
        request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"][2] = \
            request_and_port_list.autosampler_eeprom_dictionary[request_name][1]
        request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"][4] = int(hex_high_byte, 16)
        answer = request_response.command_sender(
            accepted_request=request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"])
        if answer:
            high_answer_hex = str()
            for bit_number in range(2, 16):
                high_answer_hex = str(high_answer_hex) + str(answer[bit_number])
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ байта HIGH получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
        else:
            gui.info_text_box.insert(END,
                                     "❌ Нет ответа контроллера на запрос байта HIGH\n"
                                     " * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.write_eeprom_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.write_eeprom_button.configure(bg="gray60")
            return ()


def auto_sampler_read_eeprom_command(gui):
    all_grey(gui)
    gui.info_text_box.insert(END, ">> Выполнение команды *Чтение из EEPROM*\n")
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    request_name = gui.parameter_export_combobox.get()
    if not request_name:
        gui.info_text_box.insert(END, "❌ Выберите запрос перед нажатием кнопки \n'Считать'\n", 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.read_eeprom_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.read_eeprom_button.configure(bg="gray60")
        return ()
    if request_and_port_list.autosampler_eeprom_dictionary[request_name][1]:
        # получение бита low
        request_and_port_list.samplechanger_request_dictionary["read_eeprom_sc_package"][2] = \
            request_and_port_list.autosampler_eeprom_dictionary[request_name][0]
        answer = request_response.command_sender(
            accepted_request=request_and_port_list.samplechanger_request_dictionary["read_eeprom_sc_package"])
        if answer:
            low_answer_hex = str()
            for bit_number in range(2, 16):
                low_answer_hex = str(low_answer_hex) + str(answer[bit_number])
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ байта LOW получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
        else:
            gui.info_text_box.insert(END,
                                     "❌ Нет ответа контроллера на запрос байта LOW\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.read_eeprom_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.read_eeprom_button.configure(bg="gray60")
            return ()

        # получение бита high
        request_and_port_list.samplechanger_request_dictionary["read_eeprom_sc_package"][2] = \
            request_and_port_list.autosampler_eeprom_dictionary[request_name][1]
        answer = request_response.command_sender(
            accepted_request=request_and_port_list.samplechanger_request_dictionary["read_eeprom_sc_package"])
        if answer:
            high_answer_hex = str()
            for bit_number in range(2, 16):
                high_answer_hex = str(high_answer_hex) + str(answer[bit_number])
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ байта HIGH получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
        else:
            gui.info_text_box.insert(END,
                                     "❌ Нет ответа контроллера на запрос байта HIGH\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.read_eeprom_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.read_eeprom_button.configure(bg="gray60")
            return ()
    else:
        # получение бита low
        request_and_port_list.samplechanger_request_dictionary["read_eeprom_sc_package"][2] = \
            request_and_port_list.autosampler_eeprom_dictionary[request_name][0]
        answer = request_response.command_sender(
            accepted_request=request_and_port_list.samplechanger_request_dictionary["read_eeprom_sc_package"])
        if answer:
            low_answer_hex = str()
            for bit_number in range(2, 16):
                low_answer_hex = str(low_answer_hex) + str(answer[bit_number])
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
            high_answer_hex = "----------"
        else:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера на запрос\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.read_eeprom_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.read_eeprom_button.configure(bg="gray60")
            return ()

    # заполняет значения бита low
    gui.value_export_textbox_low.config(state="normal")
    gui.value_export_textbox_low.delete('1.0', END)
    gui.value_export_textbox_low.insert(tk.END, str(low_answer_hex[6]).upper() + str(low_answer_hex[7]).upper())
    gui.value_export_textbox_low.config(state="disabled")

    # заполняет значения бита high
    gui.value_export_textbox_high.config(state="normal")
    gui.value_export_textbox_high.delete('1.0', END)
    gui.value_export_textbox_high.insert(tk.END, str(high_answer_hex[6]).upper() + str(high_answer_hex[7]).upper())
    gui.value_export_textbox_high.config(state="disabled")


def auto_sampler_engine1_command(gui):
    all_grey(gui)
    gui.info_text_box.insert(END, ">> Выполнение команды *Запуск барабана на\nпозицию №" +
                             str(gui.speed_engine_1_combobox.get()) + "*\n")
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    position_number = gui.speed_engine_1_combobox.get()
    position_numbers = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
    request_and_port_list.samplechanger_request_dictionary["engine1_sc_package"][2] = position_numbers[
        int(position_number) - 1]

    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["engine1_sc_package"])
    if answer:
        gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.engine_1_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.engine_1_button.configure(bg="gray60")


def auto_sampler_engine2_up_command(gui):
    all_grey(gui)
    gui.info_text_box.insert(END, ">> Выполнение команды *Лифт вверх*\n")
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["engine2_up_sc_package"])
    if answer:
        gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.left_engine_2_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.left_engine_2_button.configure(bg="gray60")


def auto_sampler_engine2_down_command(gui):
    all_grey(gui)
    gui.info_text_box.insert(END, ">> Выполнение команды *Лифт вниз*\n")
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["engine2_down_sc_package"])
    if answer:
        gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.right_engine_2_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.right_engine_2_button.configure(bg="gray60")


def auto_sampler_engine3_left_command(gui):
    all_grey(gui)
    gui.info_text_box.insert(END, ">> Выполнение команды *Вращение против часовой\nсо скоростью "
                             + str(gui.speed_engine_3_combobox.get()) + " об/мин*\n")
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    speed = gui.speed_engine_3_combobox.get()
    speeds = {"10": [0x08, 0x80, 0x0C],
              "20": [0x06, 0x80, 0x0C],
              "30": [0x04, 0xEE, 0x08],
              "40": [0x04, 0x80, 0x0C],
              "50": [0x04, 0xE2, 0x0E],
              "60": [0x02, 0xEE, 0x08],
              "70": [0x02, 0xC6, 0x0A],
              "80": [0x02, 0x80, 0x0C],
              "90": [0x02, 0x96, 0x0D],
              "100": [0x02, 0xE2, 0x0E],
              }

    request_and_port_list.samplechanger_request_dictionary["engine3_left_sc_package"][3] = speeds[str(speed)][0]
    request_and_port_list.samplechanger_request_dictionary["engine3_left_sc_package"][7] = speeds[str(speed)][1]
    request_and_port_list.samplechanger_request_dictionary["engine3_left_sc_package"][8] = speeds[str(speed)][2]

    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["engine3_left_sc_package"])
    if answer:
        gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.left_engine_3_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.left_engine_3_button.configure(bg="gray60")


def auto_sampler_engine3_right_command(gui):
    all_grey(gui)
    gui.info_text_box.insert(END, ">> Выполнение команды *Вращение по часовой со\nскоростью "
                             + str(gui.speed_engine_3_combobox.get()) + " об/мин*\n")
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    speed = gui.speed_engine_3_combobox.get()
    speeds = {"10": [0x08, 0x80, 0x0C],
              "20": [0x06, 0x80, 0x0C],
              "30": [0x04, 0xEE, 0x08],
              "40": [0x04, 0x80, 0x0C],
              "50": [0x04, 0xE2, 0x0E],
              "60": [0x02, 0xEE, 0x08],
              "70": [0x02, 0xC6, 0x0A],
              "80": [0x02, 0x80, 0x0C],
              "90": [0x02, 0x96, 0x0D],
              "100": [0x02, 0xE2, 0x0E],
              }

    request_and_port_list.samplechanger_request_dictionary["engine3_right_sc_package"][3] = speeds[str(speed)][0]
    request_and_port_list.samplechanger_request_dictionary["engine3_right_sc_package"][7] = speeds[str(speed)][1]
    request_and_port_list.samplechanger_request_dictionary["engine3_right_sc_package"][8] = speeds[str(speed)][2]

    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["engine3_right_sc_package"])
    if answer:
        gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.right_engine_3_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.right_engine_3_button.configure(bg="gray60")


def auto_sampler_set_sample_command(gui):
    all_grey(gui)
    gui.info_text_box.insert(END, ">> Выполнение команды *Установить образец №"
                             + str(gui.speed_engine_1_combobox.get()) + "*\n")
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    position_number = gui.speed_engine_1_combobox.get()
    position_numbers = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
    request_and_port_list.samplechanger_request_dictionary["set_sample_sc_package"][2] = position_numbers[
        int(position_number) - 1]

    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["set_sample_sc_package"])
    if answer:
        gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.set_sample_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.set_sample_button.configure(bg="gray60")


def auto_sampler_info_command(gui):
    # Команда, вызывающая файл с основной информацией по подсистеме охлаждения
    auto_sampler_help_window = Tk()
    auto_sampler_help_window.title("Контроль систем дифрактометра")

    # Отключает возможность зума
    auto_sampler_help_window.minsize(831, 600)
    auto_sampler_help_window.resizable(False, False)

    # Базовые поля
    frame_for_device_buttons = LabelFrame(auto_sampler_help_window, bg="gray90")
    frame_for_device_buttons.pack(side=LEFT, padx=1, pady=2, fill=Y)

    frame_for_terminal = LabelFrame(auto_sampler_help_window, bg="gray90")
    frame_for_terminal.pack(side=RIGHT, padx=1, pady=2, fill=Y)

    frame_for_settings = LabelFrame(auto_sampler_help_window, bg="gray90")
    frame_for_settings.pack(side=BOTTOM, padx=1, pady=1, fill=X)

    frame_for_units = LabelFrame(auto_sampler_help_window, bg="gray10")
    frame_for_units.pack(side=TOP, padx=1, pady=1, fill=BOTH)

    poa_button = Button(frame_for_device_buttons, text="СИСТ. ОХЛ.", relief=GROOVE, width=11, height=2,
                        bg="gray60", state="disabled")
    poa_button.pack(side=TOP, padx=1, pady=2)

    # Устанавливает размер окна и помещает его в центр экрана
    auto_sampler_help_window.update_idletasks()  # Обновление информации после создания всех фреймов
    s = auto_sampler_help_window.geometry()
    s = s.split('+')
    s = s[0].split('x')
    width_main_window = int(s[0])
    height_main_window = int(s[1])

    w = auto_sampler_help_window.winfo_screenwidth()
    h = auto_sampler_help_window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - width_main_window // 2
    h = h - height_main_window // 2
    auto_sampler_help_window.geometry('+{}+{}'.format(w, h))
    # Первичная инициализация с вопросов выбора режима работы

    auto_sampler_help_window.mainloop()

    pass
