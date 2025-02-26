from tkinter import *
import request_response
import request_and_port_list


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

    # Status sensors - всё неактивно
    gui.temperature_label.config(text="--", bg="gray90")
    gui.humidity_label.config(text="--", bg="gray90")


def temperature_info_command(gui):
    pass


def temperature_transcription(gui, recieved_command, sensor):

    gui.temperature_humidity_auto_errors = {
        "scrap_data_error": False,
        "answered_name_error": False,
        "initialization_error": False,
        "temperature_sensor_error": False,
        "temperature_diapason_error": False,
        "humidity_diapason_error": False,
        "humidity_sensor_error": False,
        "crc_error": False,
        "package_number_error": False,
        "statuses_error": False,
    }

    if len(recieved_command) != 20:
        gui.info_text_box.insert(END, "❌ Получен обрывочный пакет данных:\n" + str(recieved_command) + "\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
        gui.temperature_humidity_auto_errors["scrap_data_error"] = True
        return

    if recieved_command:
        # проверка ответа устройства
        device_hex = recieved_command[0] + recieved_command[1]
        if sensor == 1 and device_hex == "24":
            gui.device_name_label.config(text="OK", bg="PaleGreen3")
        elif sensor == 2 and device_hex == "26":
            gui.device_name_label.config(text="OK", bg="PaleGreen3")
        elif sensor == 3 and device_hex == "28":
            gui.device_name_label.config(text="OK", bg="PaleGreen3")
        else:
            gui.device_name_label.config(text="❌", bg="salmon")
            gui.temperature_humidity_auto_errors["answered_name_error"] = True
        gui.device_name_data.config(text=device_hex.upper())

        # проверка правильности отвеченной команды
        command_hex = recieved_command[2] + recieved_command[3]
        if command_hex == "48":
            gui.stat_request_label.config(text="OK", bg="PaleGreen3")
        elif command_hex == "49":
            gui.temperature_label.config(text="🕐")
            gui.humidity_label.config(text="🕐")
            gui.info_text_box.insert(END, "Контроллер пока что не инициализировался\n"
                                          "Подождите 5-7 секунд после подключения контроллера\n"
                                          "Либо подключен устаревший датчик: "
                                          "При повторном подключении через 10 секунд даёт аналогичную ошибку\n",
                                     'tag_red_text')
            gui.info_text_box.yview(END)
            gui.temperature_humidity_auto_errors["initialization_error"] = True
            return
        else:
            gui.stat_request_label.config(text="❌", bg="salmon")
        gui.stat_request_data.config(text=command_hex.upper())

        # заполнение всех битных полей ответом от контроллера
        gui.stat_hi_data.config(text=(recieved_command[4] + recieved_command[5]).upper())
        gui.stat_low_data.config(text=(recieved_command[6] + recieved_command[7]).upper())
        gui.temp_hi_data.config(text=(recieved_command[8] + recieved_command[9]).upper())
        gui.temp_low_data.config(text=(recieved_command[10] + recieved_command[11]).upper())
        gui.humidity_hi_data.config(text=(recieved_command[12] + recieved_command[13]).upper())
        gui.humidity_low_data.config(text=(recieved_command[14] + recieved_command[15]).upper())
        gui.package_number_data.config(text=(recieved_command[16] + recieved_command[17]).upper())
        gui.crc_data.config(text=(recieved_command[18] + recieved_command[19]).upper())

        # Превращает температуру из хексов в десятеричную
        temp_hex = recieved_command[8] + recieved_command[9] + recieved_command[10] + recieved_command[11]
        temp_dec = int(temp_hex, 16)
        if temp_hex == "ffff":
            real_temperature = "FFFF"
            gui.temperature_humidity_auto_errors["temperature_sensor_error"] = True
        else:
            real_temperature = round(temp_dec * 0.04 - 40.1, 2)
        gui.temperature_label.config(text=real_temperature, bg="gray90")

        # проверка значений температуры на адекватность
        if real_temperature == "FFFF" or real_temperature <= 10 or real_temperature >= 70:
            gui.temp_hi_label.config(text="❌", bg="salmon")
            gui.temp_low_label.config(text="❌", bg="salmon")
            gui.temperature_label.config(bg="salmon")
            gui.temperature_humidity_auto_errors["temperature_diapason_error"] = True
        else:
            gui.temp_hi_label.config(text="OK", bg="PaleGreen3")
            gui.temp_low_label.config(text="OK", bg="PaleGreen3")
            gui.temperature_label.config(bg="PaleGreen3")
            gui.real_temperature_data.append(str(real_temperature))

        # превращает влажность из хексов в десятеричную
        humidity_hex = recieved_command[12] + recieved_command[13] + recieved_command[14] + recieved_command[15]
        humidity_dec = int(humidity_hex, 16)
        if humidity_hex == "ffff":
            real_humidity = "FFFF"
            gui.temperature_humidity_auto_errors["humidity_sensor_error"] = True
        else:
            real_humidity = round(-2.0468 + (0.5872 * humidity_dec) + (-0.0000015955)*humidity_dec*humidity_dec, 2)
        if real_humidity > 100:
            real_humidity = 100
        gui.humidity_label.config(text=real_humidity, bg="gray90")

        # проверка значений влажности на адекватность
        if real_humidity == "FFFF" or real_humidity <= 0:
            gui.humidity_hi_label.config(text="❌", bg="salmon")
            gui.humidity_low_label.config(text="❌", bg="salmon")
            gui.humidity_label.config(bg="salmon")
            if real_humidity <= 0:
                gui.temperature_humidity_auto_errors["humidity_diapason_error"] = True
        else:
            gui.humidity_hi_label.config(text="OK", bg="PaleGreen3")
            gui.humidity_low_label.config(text="OK", bg="PaleGreen3")
            gui.humidity_label.config(bg="PaleGreen3")
            gui.real_temperature_data.append(str(real_humidity))

        if recieved_command[16] + recieved_command[17] == "00":
            gui.package_number_label.config(text="OK", bg="PaleGreen3")
        else:
            gui.package_number_label.config(text="❌", bg="salmon")
            gui.temperature_humidity_auto_errors["package_number_error"] = True

        # Проверяет контрольную сумму
        full_dec_summ = 0
        full_hex_summ = 0
        for bit in range(0, 20):
            if bit % 2 != 0:
                hex_bit = recieved_command[bit - 1] + recieved_command[bit]
                full_dec_summ = full_dec_summ + int(hex_bit, 16)
                full_hex_summ = hex(full_dec_summ)
        if full_hex_summ[len(full_hex_summ) - 1] == "0":
            gui.crc_label.config(bg="PaleGreen3", text="OK")
        else:
            gui.crc_label.config(bg="salmon", text=str(full_hex_summ))
            gui.temperature_humidity_auto_errors["crc_error"] = True

        # проверяет статусы в ответе
        if recieved_command[4] + recieved_command[5] + recieved_command[6] + recieved_command[7] == "3d01":
            gui.stat_hi_label.config(bg="PaleGreen3", text="OK")
            gui.stat_low_label.config(bg="PaleGreen3", text="OK")
        else:
            gui.stat_hi_label.config(text="❌", bg="salmon")
            gui.stat_low_label.config(text="❌", bg="salmon")
            gui.temperature_humidity_auto_errors["statuses_error"] = True

    gui.info_text_box.insert(END, " состояние расшифровано\n", 'tag_green_text')
    gui.info_text_box.yview(END)


def temperature_status_command(gui, sensor):
    # Отправляет команду на запрос статуса системы охлаждения
    all_grey(gui)
    answer = None
    if not sensor:
        return
    elif sensor == 1:
        answer = request_response.command_sender(
            accepted_request=request_and_port_list.sth_request_dictionary["status_sth_1_package"])
    elif sensor == 2:
        answer = request_response.command_sender(
            accepted_request=request_and_port_list.sth_request_dictionary["status_sth_2_package"])
    elif sensor == 3:
        answer = request_response.command_sender(
            accepted_request=request_and_port_list.sth_request_dictionary["status_sth_3_package"])

    if answer:
        gui.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        temperature_transcription(gui, answer, sensor)
    else:
        gui.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                 'tag_red_text')
        gui.info_text_box.yview(END)
