import time
import auto_sampler_transcriptions
import request_response
import request_and_port_list
from tkinter import *
from tkinter.messagebox import askyesno
import tkinter as tk


def all_grey(gui):
    # Верхние поля отображения статусов
    gui.device_name_label.config(text="--", bg="gray90")
    gui.stat_request_label.config(text="--", bg="gray90")
    gui.reserve_1_label.config(text="--", bg="gray90")
    gui.state_1_label.config(text="--", bg="gray90")
    gui.rotate_low_label.config(text="--", bg="gray90")
    gui.rotate_high_label.config(text="--", bg="gray90")
    gui.errors_label.config(text="--", bg="gray90")
    gui.state_2_label.config(text="--", bg="gray90")
    gui.state_set_sample_label.config(text="--", bg="gray90")
    gui.crc_label.config(text="--", bg="gray90")

    gui.device_name_data.config(text="--", bg="gray90")
    gui.stat_request_data.config(text="--", bg="gray90")
    gui.reserve_1_data.config(text="--", bg="gray90")
    gui.state_1_data.config(text="--", bg="gray90")
    gui.rotate_low_data.config(text="--", bg="gray90")
    gui.rotate_high_data.config(text="--", bg="gray90")
    gui.errors_data.config(text="--", bg="gray90")
    gui.state_2_data.config(text="--", bg="gray90")
    gui.state_set_sample_data.config(text="--", bg="gray90")
    gui.crc_data.config(text="--", bg="gray90")

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.yview(END)

    gui.full_set_textbox.config(state="normal", bg="gray70")
    gui.full_set_textbox.delete('1.0', END)
    gui.full_set_textbox.config(state="disabled")

    gui.lift_textbox.config(state="normal", bg="gray70")
    gui.lift_textbox.delete('1.0', END)
    gui.lift_textbox.config(state="disabled")

    gui.position_textbox.config(state="normal", bg="gray70")
    gui.position_textbox.delete('1.0', END)
    gui.position_textbox.config(state="disabled")

    gui.speed_textbox.config(state="normal", bg="gray70")
    gui.speed_textbox.delete('1.0', END)
    gui.speed_textbox.config(state="disabled")

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
        gui.info_text_box.insert(END, "✔ Ответ контроллера Atmega 2560:\n", 'tag_green_text')
        gui.info_text_box.insert(END, "⫸ ASCII:  " + version_answer_ascii + "\n", 'tag_black_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера Atmega 2560\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.version_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.version_button.configure(bg="gray60")
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["version_l_sc_package"])
    if answer:
        version_answer_hex = str()
        for bit_number in range(2, 16):
            version_answer_hex = str(version_answer_hex) + str(answer[bit_number])
        version_answer_ascii = bytearray.fromhex(version_answer_hex).decode(encoding='ascii')
        gui.info_text_box.insert(END, "✔ Ответ контроллера Atmega 162:\n", 'tag_green_text')
        gui.info_text_box.insert(END, "⫸ ASCII:  " + version_answer_ascii + "\n", 'tag_black_text')
        gui.info_text_box.yview(END)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера Atmega 162\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.version_button.configure(bg="salmon")
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        gui.version_button.configure(bg="gray60")


def auto_sampler_status_command(gui, auto=False):
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Статус*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["status_sc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
        auto_sampler_transcriptions.transcript_status(gui, answer)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.status_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.status_button.configure(bg="gray60")


def auto_sampler_status_l_command(gui, auto=False):
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Статус_L*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["status_l_sc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
        auto_sampler_transcriptions.transcript_status_l(gui, answer)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.status_l_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.status_l_button.configure(bg="gray60")


def auto_sampler_stop_base_command(gui, auto=False):
    gui.auto_sampler_last_command = "stop_base"
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Стоп-База*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["stop_base_sc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.stop_base_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.stop_base_button.configure(bg="gray60")


def auto_sampler_stop_command(gui, auto=False):
    gui.auto_sampler_last_command = "stop"
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Стоп*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["stop_sc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
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
                                     "❌ Нет ответа контроллера на запрос байта LOW\n * проверьте подключение "
                                     "устройства *\n", 'tag_red_text')
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
                                     "❌ Нет ответа контроллера на запрос байта HIGH\n * проверьте подключение "
                                     "устройства *\n", 'tag_red_text')
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


def auto_sampler_engine1_command(gui, auto=False):
    gui.auto_sampler_last_command = "engine1"
    if not auto:
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
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.engine_1_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.engine_1_button.configure(bg="gray60")


def auto_sampler_engine2_up_command(gui, auto=False):
    gui.auto_sampler_last_command = "engine2_up"
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Лифт вверх*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["engine2_up_sc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.left_engine_2_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.left_engine_2_button.configure(bg="gray60")


def auto_sampler_engine2_down_command(gui, auto=False):
    gui.auto_sampler_last_command = "engine2_down"
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Лифт вниз*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["engine2_down_sc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.right_engine_2_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.right_engine_2_button.configure(bg="gray60")


def auto_sampler_engine3_left_command(gui, auto=False):
    gui.auto_sampler_last_command = "engine3_left"
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Вращение против часовой\nсо скоростью "
                                 + str(gui.speed_engine_3_combobox.get()) + " об/мин*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    speed = gui.speed_engine_3_combobox.get()
    speeds = {"10": [0x08, 0x80, 0x0C],
              "20": [0x06, 0x80, 0x0C],
              "30": [0x04, 0xEE, 0x08],
              "35": [0x04, 0xC6, 0x0A],
              "40": [0x04, 0x80, 0x0C],
              "45": [0x04, 0x96, 0x0D],
              "50": [0x04, 0xE2, 0x0E],
              "55": [0x04, 0x72, 0x10],
              "65": [0x02, 0x14, 0x0A],
              "70": [0x02, 0xC6, 0x0A],
              "75": [0x02, 0x92, 0x0B],
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
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.left_engine_3_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.left_engine_3_button.configure(bg="gray60")


def auto_sampler_engine3_right_command(gui, auto=False):
    gui.auto_sampler_last_command = "engine3_right"
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Вращение по часовой со\nскоростью "
                                 + str(gui.speed_engine_3_combobox.get()) + " об/мин*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    speed = gui.speed_engine_3_combobox.get()
    speeds = {"10": [0x08, 0x80, 0x0C],
              "20": [0x06, 0x80, 0x0C],
              "30": [0x04, 0xEE, 0x08],
              "35": [0x04, 0xC6, 0x0A],
              "40": [0x04, 0x80, 0x0C],
              "45": [0x04, 0x96, 0x0D],
              "50": [0x04, 0xE2, 0x0E],
              "55": [0x04, 0x72, 0x10],
              "65": [0x02, 0x14, 0x0A],
              "70": [0x02, 0xC6, 0x0A],
              "75": [0x02, 0x92, 0x0B],
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
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.right_engine_3_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.right_engine_3_button.configure(bg="gray60")


def auto_sampler_set_sample_command(gui, auto=False):
    auto_sampler_stop_command(gui, auto)
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Установить скорость \nвращения = "
                                 + str(gui.speed_engine_3_combobox.get()) + "*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()

    speed = gui.speed_engine_3_combobox.get()
    speeds = {"10": [0x08, 0x80, 0x0C],
              "20": [0x06, 0x80, 0x0C],
              "30": [0x04, 0xEE, 0x08],
              "35": [0x04, 0xC6, 0x0A],
              "40": [0x04, 0x80, 0x0C],
              "45": [0x04, 0x96, 0x0D],
              "50": [0x04, 0xE2, 0x0E],
              "55": [0x04, 0x72, 0x10],
              "65": [0x02, 0x14, 0x0A],
              "70": [0x02, 0xC6, 0x0A],
              "75": [0x02, 0x92, 0x0B],
              "80": [0x02, 0x80, 0x0C],
              "90": [0x02, 0x96, 0x0D],
              "100": [0x02, 0xE2, 0x0E],
              }

    # Запись low byte
    request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"][2] = \
        request_and_port_list.autosampler_eeprom_dictionary["Скорость ШД3"][0]
    request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"][4] = speeds[speed][1]
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"])
    time.sleep(0.02)
    if not answer:
        if not auto:
            gui.info_text_box.insert(END,
                                     "❌ Нет ответа контроллера на попытку установки \nскорости\n"
                                     " * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.set_sample_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.set_sample_button.configure(bg="gray60")
            return ()
    # Запись high byte
    request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"][2] = \
        request_and_port_list.autosampler_eeprom_dictionary["Скорость ШД3"][1]
    request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"][4] = speeds[speed][2]
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"])
    time.sleep(0.02)
    if not answer:
        if not auto:
            gui.info_text_box.insert(END,
                                     "❌ Нет ответа контроллера на попытку установки \nскорости\n"
                                     " * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.set_sample_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.set_sample_button.configure(bg="gray60")
            return ()
    # Запись дробления
    request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"][2] = \
        request_and_port_list.autosampler_eeprom_dictionary["Дробление ШД3"][0]
    request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"][4] = speeds[speed][0]
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["write_eeprom_sc_package"])
    time.sleep(0.02)
    if not answer:
        if not auto:
            gui.info_text_box.insert(END,
                                     "❌ Нет ответа контроллера на попытку установки \nскорости\n"
                                     " * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.set_sample_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.set_sample_button.configure(bg="gray60")
            return ()

    if not auto:
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
        gui.auto_sampler_last_command = "set_sample"
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
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


def auto_changer_engine1_base_command(gui, auto=False):
    gui.auto_sampler_last_command = "engine1_base"
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Каретка в базу*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.autochanger_request_dictionary["engine1_base_auc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.base_engine_1_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.base_engine_1_button.configure(bg="gray60")


def auto_changer_engine1_load_command(gui, auto=False):
    gui.auto_sampler_last_command = "engine1_load"
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Каретка в зону загрузки*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.autochanger_request_dictionary["engine1_load_auc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.load_engine_1_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.load_engine_1_button.configure(bg="gray60")


def auto_changer_engine2_base_command(gui, auto=False):
    gui.auto_sampler_last_command = "engine2_base"
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Лифт вниз*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.autochanger_request_dictionary["engine2_base_auc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.right_engine_2_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.right_engine_2_button.configure(bg="gray60")


def auto_changer_engine2_scan_command(gui, auto=False):
    gui.auto_sampler_last_command = "engine2_scan"
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Лифт вверх*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.autochanger_request_dictionary["engine2_scan_auc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.left_engine_2_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.left_engine_2_button.configure(bg="gray60")


def auto_changer_set_load_command(gui, auto=False):
    gui.auto_sampler_last_command = "engine2_scan"
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Сценарий перемещения в зону загрузки*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.autochanger_request_dictionary["load_sample_auc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.load_sample_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.load_sample_button.configure(bg="gray60")


def auto_changer_check_answer_command(gui, answer, auto):
    device_hex = answer[0] + answer[1]
    if device_hex != "50" and not auto:
        result = askyesno(title="Некорректный ответ контроллера",
                          message="Возникает во время перемещения двигателя каретки и по его окончанию, временами "
                                  "возникает при перемещении прочих двигателей. Для сброса состояния ошибки требуется"
                                  " выполнить команду Стоп. Выполнить команду?\n\n"
                                  "<Да> - для отправки команды Стоп и повторного запроса статуса\n\n"
                                  "<Нет> - для отмены выполнения команды Статус")
        if result:
            auto_sampler_stop_command(gui, True)
            time.sleep(0.2)
            auto_changer_status_command(gui, True)
            return False
        else:
            return False
    else:
        return True


def auto_changer_status_command(gui, auto=False):
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Статус*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["status_sc_package"])
    if answer:
        if auto_changer_check_answer_command(gui, answer, auto):
            device_hex = answer[0] + answer[1]
            if not auto:
                gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
                gui.info_text_box.yview(END)
                auto_sampler_transcriptions.transcript_status_autochanger(gui, answer)
            if auto and device_hex != "50":
                pass
            if auto and device_hex == "50":
                auto_sampler_transcriptions.transcript_status_autochanger(gui, answer)
        else:
            pass
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.status_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.status_button.configure(bg="gray60")


def auto_changer_status_l_command(gui, auto=False):
    if not auto:
        all_grey(gui)
        gui.info_text_box.insert(END, ">> Выполнение команды *Статус_L*\n")
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
    answer = request_response.command_sender(
        accepted_request=request_and_port_list.samplechanger_request_dictionary["status_l_sc_package"])
    if answer:
        if not auto:
            gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
            gui.info_text_box.yview(END)
        auto_sampler_transcriptions.transcript_status_l_autochanger(gui, answer)
    else:
        if not auto:
            gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.status_l_button.configure(bg="salmon")
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            gui.status_l_button.configure(bg="gray60")
