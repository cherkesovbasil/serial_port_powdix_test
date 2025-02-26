from tkinter.messagebox import askyesno
import time
from tkinter import *
import temperature_buttons


def error_control(gui):
    # Функция проверки ошибок из команд от автоматического скрипта
    reset = False

    for error, status in gui.temperature_humidity_auto_errors.items():
        if status:

            if error == "scrap_data_error":

                result = askyesno(title="Получен обрывочный пакет данных",
                                  message="Ответ контроллера не полный (обрывочный пакет данных). "
                                          "Изредка происходит при случайных обстоятельствах\n"
                                          "При повторяющейся проблеме - некорректная работа приёмо-передатчика.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема разовая либо "
                                          "исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "answered_name_error":

                result = askyesno(title="Ошибка имени опрашиваемого устройства",
                                  message="Может возникать при подключении устаревшей версии датчика либо проблемах "
                                          "обмена данными (плохое соединение), некорректная прошивка и пр.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема разовая или "
                                          "исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "initialization_error":

                result = askyesno(title="Ошибка инициализации датчика температуры/влажности",
                                  message="Датчик ещё не инициализирован. Подождите 5-7 секунд прежде чем "
                                          "нажимать <Да>. При повторно возникшей проблеме есть вероятность того, что "
                                          "подключен устаревший датчик (проблема не проходит после нескольких подобных "
                                          "сообщений). Данное ПО не работает с устаревшими датчиками.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "temperature_sensor_error":

                result = askyesno(title="Ошибка сенсора температуры",
                                  message="Датчик температуры ответил FFFF - повторите опрос ещё раз, в случае "
                                          "повторного получения аналогичного ответа, перепрошейте датчик. "
                                          "Если обновление прошивки не помогает, датчик DA1 считается непригодным и "
                                          "подлежит замене (если это SHT3x).\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "temperature_diapason_error":

                result = askyesno(title="Ошибка значений сенсора температуры",
                                  message="Датчик температуры вывел некорректные показания температуры - повторите "
                                          "опрос ещё раз, в случае повторного получения аналогичного ответа, "
                                          "перепрошейте датчик. Если обновление прошивки не помогает, датчик DA1 "
                                          "считается непригодным и подлежит замене (если это SHT3x).\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "humidity_diapason_error":

                result = askyesno(title="Ошибка значений сенсора влажности",
                                  message="Датчик влажности вывел некорректные показания влажности - повторите "
                                          "опрос ещё раз, в случае повторного получения аналогичного ответа, "
                                          "перепрошейте датчик. Если обновление прошивки не помогает, датчик DA1 "
                                          "считается непригодным и подлежит замене (если это SHT3x).\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "humidity_sensor_error":

                result = askyesno(title="Ошибка сенсора влажности",
                                  message="Датчик влажности ответил FFFF - повторите опрос ещё раз, в случае "
                                          "повторного получения аналогичного ответа, перепрошейте датчик. "
                                          "Если обновление прошивки не помогает, датчик DA1 считается непригодным и "
                                          "подлежит замене (если это SHT3x).\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "package_number_error":

                result = askyesno(title="Ошибка номера отправленного пакета",
                                  message="Появляется периодически при сбоях обмена данными. В случае единичного "
                                          "возникновения проблемы, продолжите проверку. При повторном получении"
                                          "аналогичного ответа проверьте, является ли датчик DA1: SHT3x. С "
                                          "альтернативными датчиками программа не работает.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "statuses_error":

                result = askyesno(title="Ошибка ответа по статусам датчика",
                                  message="Появляется периодически при сбоях обмена данными. В случае единичного "
                                          "возникновения проблемы, продолжите проверку. При повторном получении"
                                          "аналогичного ответа проверьте, является ли датчик DA1: SHT3x. С "
                                          "альтернативными датчиками программа не работает.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "crc_error":

                result = askyesno(title="Ошибка контрольной суммы",
                                  message="Контрольная сумма ответа не совпадает расчётной. Проблема может "
                                          "быть связана с повреждением пакета информации, отправленного "
                                          "контроллером системы охлаждения. При повторяющейся ошибке "
                                          "пересбросьте питание.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

        else:
            reset = True

    if reset:
        return None


def step_1(gui, sensor):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖▒▒▒▒▒▒▒▒▒▒ 00% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка подключения датчика\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    temperature_buttons.temperature_status_command(gui, sensor)

    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1)
    return error_control(gui)


def step_2(gui, sensor):
    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██▒▒▒▒▒▒▒▒ 10% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "[общий анализ]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    temperature_buttons.temperature_status_command(gui, sensor)

    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1)
    return error_control(gui)


def step_3(gui, sensor):
    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 20% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS)"
                                  "\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████▒▒▒▒ 30% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\nОЖИДАНИЕ ОБНОВЛЕНИЯ СИСТЕМ ДАТЧИКА: 4 сек.\n",
                             'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████████▒▒ 40% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\nОЖИДАНИЕ ОБНОВЛЕНИЯ СИСТЕМ ДАТЧИКА: 3 сек.\n",
                             'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 50% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\nОЖИДАНИЕ ОБНОВЛЕНИЯ СИСТЕМ ДАТЧИКА: 2 сек.\n",
                             'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 60% ██▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\nОЖИДАНИЕ ОБНОВЛЕНИЯ СИСТЕМ ДАТЧИКА: 1 сек.\n",
                             'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 70% ████▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1)

    temperature_buttons.temperature_status_command(gui, sensor)
    return error_control(gui)


def step_4():
    result = askyesno(title="Проверка изменения параметров",
                      message="Подышите на датчик, после чего продолжите проверку\n\n"
                              "<Да> - для продолжения проверки\n\n"
                              "<Нет> - для выхода в ручной режим")
    if result:
        return True
    else:
        return False


def step_5(gui, sensor):
    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 70% ████▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка изменения параметров системы\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1.5)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 80% ██████▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\nОЖИДАНИЕ ОБНОВЛЕНИЯ СИСТЕМ ДАТЧИКА: 2 сек.\n",
                             'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1.5)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 90% ████████▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\nОЖИДАНИЕ ОБНОВЛЕНИЯ СИСТЕМ ДАТЧИКА: 1 сек.\n",
                             'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1.5)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 100% ██████████◗\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(1.5)

    temperature_buttons.temperature_status_command(gui, sensor)
    check_status = error_control(gui)
    if check_status:
        return check_status
    if not check_status:
        if float(gui.real_temperature_data[-1]) > float(gui.real_temperature_data[-3]) and \
                float(gui.real_temperature_data[-2]) > float(gui.real_temperature_data[-4]):
            return
        elif float(gui.real_temperature_data[-1]) == float(gui.real_temperature_data[-3]) and float(gui.real_temperature_data[-3]) == 100 \
                and float(gui.real_temperature_data[-2]) > float(gui.real_temperature_data[-4]):
            return
        elif float(gui.real_temperature_data[-1]) == float(gui.real_temperature_data[-3]) and \
                float(gui.real_temperature_data[-2]) == float(gui.real_temperature_data[-4]):
            result = askyesno(title="Датчик не успел обновить параметры",
                              message="Параметры датчика не обновились.\nЕсли данная проблема повториться при "
                                      "перезапуске, попробуйте подышать на него снова, выждать 5-7 секунд и "
                                      "нажать <Да>.\n\n"
                                      "<Да> - для повторной проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False
        else:
            result = askyesno(title="Обновление параметров некорректно",
                              message="Обновлённые данные ниже прежних либо некорректны.\nСтарые значения "
                                      "темпер./влажн = " + gui.real_temperature_data[-4] + " / "
                                      + gui.real_temperature_data[-3] + "\nНовые значения темпер./влажн   = " +
                                      gui.real_temperature_data[-2] + " / " + gui.real_temperature_data[-1] +
                                      "\nЕсли данная проблема повториться при перезапуске, попробуйте подышать на "
                                      "него снова, выждать 5-7 секунд и нажать <Да>.\n\n"
                                      "<Да> - для повторной проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False


def step_15():
    result = askyesno(title="Проверка работы завершена",
                      message="Проверка завершена успешно.\nПоказатели соответствуют норме.\n\n"
                              "<Да> - для повторной проверки\n\n"
                              "<Нет> - для выхода в ручной режим")
    if result:
        return True
    else:
        return False


def check_step(step_number, gui, sensor):
    out = None

    if step_number == 1:
        out = step_1(gui, sensor)
    elif step_number == 2:
        out = step_2(gui, sensor)
    elif step_number == 3:
        out = step_3(gui, sensor)
    elif step_number == 4:
        out = step_4()
    elif step_number == 5:
        out = step_5(gui, sensor)
    elif step_number == 15:
        out = step_15()

    if out:
        while out:
            if step_number == 1:
                out = step_1(gui, sensor)
            elif step_number == 2:
                out = step_2(gui, sensor)
            elif step_number == 3:
                out = step_3(gui, sensor)
            elif step_number == 5:
                out = step_5(gui, sensor)
        else:
            if out is None:
                pass
            else:
                back_to_manual(gui, sensor)
                gui.info_text_box.delete('1.0', END)
                gui.info_text_box.insert(END, "❌ АВТОМАТИЧЕСКАЯ ПРОВЕРКА ОСТАНОВЛЕНА\n", 'tag_red_text')
                gui.info_text_box.insert(END, "⫸ Программа переведена в ручной режим\n", 'tag_black_text')
                gui.info_text_box.yview(END)
                gui.frame_for_units.update_idletasks()
                return True
    elif out is None:
        pass
    else:
        back_to_manual(gui, sensor)
        gui.info_text_box.delete('1.0', END)
        gui.info_text_box.insert(END, "❌ АВТОМАТИЧЕСКАЯ ПРОВЕРКА ОСТАНОВЛЕНА\n", 'tag_red_text')
        gui.info_text_box.insert(END, "⫸ Программа переведена в ручной режим\n", 'tag_black_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        return True
    return


def back_to_manual(gui, sensor):
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

    gui.poa_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.as_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.vs_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.refind_button.configure(state="normal", bg="gray60")
    gui.set_button.configure(state="normal", bg="gray60")
    gui.manual_button.configure(state="disabled", bg="SeaGreen1")
    gui.auto_button.configure(state="normal", bg="gray60")
    gui.terminal_button.configure(state="normal", bg="gray60")

    gui.bytesize_combobox.configure(state="normal")
    gui.timeout_combobox.configure(state="normal")
    gui.baudrate_combobox.configure(state="normal")
    gui.port_combobox.configure(state="normal")

    gui.bytesize_label.configure(fg="black")
    gui.timeout_label.configure(fg="black")
    gui.baudrate_label.configure(fg="black")
    gui.port_label.configure(fg="black")

    gui.device_name_label.configure(text="--", bg="gray95")
    gui.stat_request_label.configure(text="--", bg="gray95")
    gui.stat_hi_label.configure(text="--", bg="gray95")
    gui.stat_low_label.configure(text="--", bg="gray95")
    gui.temp_hi_label.configure(text="--", bg="gray95")
    gui.temp_low_label.configure(text="--", bg="gray95")
    gui.humidity_hi_label.configure(text="--", bg="gray95")
    gui.humidity_low_label.configure(text="--", bg="gray95")
    gui.package_number_label.configure(text="--", bg="gray95")
    gui.crc_label.configure(text="--", bg="gray95")

    gui.device_name_data.configure(text="--", bg="gray90")
    gui.stat_request_data.configure(text="--", bg="gray90")
    gui.stat_hi_data.configure(text="--", bg="gray90")
    gui.stat_low_data.configure(text="--", bg="gray90")
    gui.temp_hi_data.configure(text="--", bg="gray90")
    gui.temp_low_data.configure(text="--", bg="gray90")
    gui.humidity_hi_data.configure(text="--", bg="gray90")
    gui.humidity_low_data.configure(text="--", bg="gray90")
    gui.package_number_data.configure(text="--", bg="gray90")
    gui.crc_data.configure(text="--", bg="gray90")

    # Status sensors - всё неактивно
    gui.temperature_label.configure(text="--", bg="gray90")
    gui.humidity_label.configure(text="--", bg="gray90")

    gui.check_status_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.info_button.configure(bg="gray60", state='normal', relief=GROOVE)


def start_check(gui, sensor):
    # Запуск скрипта автоматической проверки системы охлаждения
    if not check_step(1, gui, sensor):
        if not check_step(2, gui, sensor):
            if not check_step(3, gui, sensor):
                if not step_4():
                    back_to_manual(gui, sensor)
                    gui.info_text_box.delete('1.0', END)
                    gui.info_text_box.insert(END, "❌ АВТОМАТИЧЕСКАЯ ПРОВЕРКА ОСТАНОВЛЕНА\n",
                                             'tag_red_text')
                    gui.info_text_box.insert(END, "⫸ Программа переведена в ручной режим\n",
                                             'tag_black_text')
                    gui.info_text_box.yview(END)
                    gui.frame_for_units.update_idletasks()
                    return
                else:
                    if not check_step(5, gui, sensor):
                        if not step_15():
                            back_to_manual(gui, sensor)
                            gui.info_text_box.delete('1.0', END)
                            gui.info_text_box.insert(END,
                                                     "❌ АВТОМАТИЧЕСКАЯ"
                                                     " ПРОВЕРКА"
                                                     " ОСТАНОВЛЕНА\n",
                                                     'tag_red_text')
                            gui.info_text_box.insert(END,
                                                     "⫸ Программа "
                                                     "переведена в "
                                                     "ручной режим\n",
                                                     'tag_black_text')
                            gui.info_text_box.yview(END)
                            gui.frame_for_units.update_idletasks()
                            return
                        else:
                            start_check(gui, sensor)
