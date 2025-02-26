from tkinter.messagebox import askyesno
import time
from tkinter import *
import poa_buttons


def error_control(gui, exception='None'):
    # Функция проверки ошибок из команд от автоматического скрипта
    reset = False

    if exception == "key_exception":
        gui.poa_auto_errors["key_error"] = False

    for error, status in gui.poa_auto_errors.items():
        if status:

            if error == "wls_error":

                result = askyesno(title="Сработка датчика уровня воды",
                                  message="Проверьте достаточен ли уровень воды и работоспособность "
                                          "поплавка. При повторяющейся ошибке пересбросьте питание.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "key_error":

                result = askyesno(title="Ошибка ключа режима работы",
                                  message="Проверьте положение ключа или правильность подключения "
                                          "проводов ключа к плате системы охлаждения. При повторяющейся "
                                          "ошибке пересбросьте питание.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "svs_error":

                result = askyesno(title="Сработка датчика пароводяного клапана",
                                  message="Проверьте расположение датчика пароводяного клапана, его "
                                          "подключение и адекватность работы. При повторяющейся ошибке "
                                          "пересбросьте питание.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "wts2_error":

                result = askyesno(title="Сработка датчика крана холодной воды",
                                  message="Проверьте наличие перемычки на контакте X6. "
                                          "В случае наличия датчика крана, проверьте корректность его"
                                          "подключения и работы. При повторяющейся ошибке пересбросьте "
                                          "питание.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "wts1_error":

                result = askyesno(title="Сработка датчика крана горячей воды",
                                  message="Проверьте наличие перемычки на контакте X7. "
                                          "В случае наличия датчика крана, проверьте корректность его"
                                          "подключения и работы. При повторяющейся ошибке пересбросьте "
                                          "питание.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "t_min_error":
                if status == 255:
                    result = askyesno(title="Ошибка данных датчика температуры холодной воды",
                                      message="Датчик температуры холодной воды не подключён либо "
                                              "неисправен (t min). Замените датчик (разъём X2), после "
                                              "чего сбросьте питание системы охлаждения и подайте "
                                              "заново\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема "
                                              "исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                    if result:
                        return True
                    else:
                        return False
                else:
                    result = askyesno(title="Ошибка данных датчика температуры холодной воды",
                                      message="Датчик температуры холодной воды даёт некорректные "
                                              "показания (t min). Замените датчик (разъём X2), после "
                                              "чего сбросьте питание системы охлаждения и подайте "
                                              "заново\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема "
                                              "исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                    if result:
                        return True
                    else:
                        return False

            if error == "t_max_error":
                if status == 255:
                    result = askyesno(title="Ошибка данных датчика температуры горячей воды",
                                      message="Датчик температуры горячей воды не подключён либо "
                                              "неисправен (t max). Замените датчик (разъём X1), после "
                                              "чего сбросьте питание системы охлаждения и подайте "
                                              "заново\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема "
                                              "исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                    if result:
                        return True
                    else:
                        return False
                else:
                    result = askyesno(title="Ошибка данных датчика температуры горячей воды",
                                      message="Датчик температуры горячей воды даёт некорректные "
                                              "показания (t max). Замените датчик (разъём X1), после "
                                              "чего сбросьте питание системы охлаждения и подайте "
                                              "заново\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема "
                                              "исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                    if result:
                        return True
                    else:
                        return False

            if error == "flow_error":

                result = askyesno(title="Ошибка данных датчика потока воды",
                                  message="Проверьте:\n"
                                          "1) достаточность подаваемого тока на плату "
                                          "системы охлаждения (~3А) - разъём X9\n"
                                          "2) правильность подключения шлангов, либо корректность "
                                          "подключения датчика потока воды и корректность отображаемых "
                                          "датчиком данных\n"
                                          "3) Корректность работы микросхемы DA5 (выход/вход)\n"
                                          "При повторяющейся ошибке пересбросьте питание.\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "pwm_1_2_error":

                result = askyesno(title="Ошибка данных питания вентиляторов радиатора",
                                  message="Некорректные данные питания вентиляторов радиатора. "
                                          "Сбросьте питание с контроллера системы охлаждения, после чего "
                                          "подайте его заново и продолжите проверку\n\n"
                                          "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "errors_error":

                result = askyesno(title="Внутренние ошибки контроллера",
                                  message="В контроллере найдено исключение. Если сбой единичный, сбросьте "
                                          "питание контроллера системы охлаждения, подайте его заново, "
                                          "после чего продолжите проверку\n\n"
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


def step_1(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖▒▒▒▒▒▒▒▒▒▒ 00% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения команды START\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_start_command(gui, False)

    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(2)
    poa_buttons.poa_status_command(gui, False)
    return error_control(gui)


def step_2(gui):
    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██▒▒▒▒▒▒▒▒ 10% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "[общий анализ]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)

    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.5)
    return error_control(gui)


def step_3(gui):
    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 20% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "запрос [1]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 22% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "запрос [2]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████▒▒▒▒▒ 25% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "запрос [3]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████▒▒▒▒▒ 27% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "запрос [4]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████▒▒▒▒ 30% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "запрос [5]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)
    return error_control(gui)


def step_4(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████████▒▒ 40% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения команды STOP\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)
    poa_buttons.poa_stop_command(gui)

    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(2)
    poa_buttons.poa_status_command(gui, False)
    return error_control(gui)


def step_5(gui):
    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 50% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "[общий анализ]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)

    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.5)
    return error_control(gui)


def step_6(gui):
    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 60% ██▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "запрос [1]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 62% ██▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "запрос [2]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 65% ███▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "запрос [3]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 67% ███▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "запрос [4]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)

    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 70% ████▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "запрос [5]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)
    return error_control(gui)


def step_7():
    result = askyesno(title="Проверка режима откачки",
                      message="Поверните ключ в положение <ОТКАЧКА>\n\n"
                              "<Да> - для продолжения проверки\n\n"
                              "<Нет> - для выхода в ручной режим")
    if result:
        return True
    else:
        return False


def step_8(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 75% █████▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения команды DRY\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)
    poa_buttons.poa_dry_command(gui)

    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(2)
    poa_buttons.poa_status_command(gui, False)
    return error_control(gui)


def step_9(gui):
    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 80% ██████▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "[общий анализ]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)

    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.5)
    return error_control(gui)


def step_10():
    result = askyesno(title="Проверка работы после откачки",
                      message="Дождитесь окончания работы сигнализации, после чего "
                              "поверните ключ в положение <РАБОТА>\n\n"
                              "<Да> - для продолжения проверки\n\n"
                              "<Нет> - для выхода в ручной режим")
    if result:
        return True
    else:
        return False


def step_11(gui):
    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 85% ███████▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "[общий анализ]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)
    poa_buttons.poa_status_command(gui, False)

    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)
    return error_control(gui, "key_exception")


def step_12(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 90% ████████▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения команды START\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.1)
    poa_buttons.poa_start_command(gui)

    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(2)
    poa_buttons.poa_status_command(gui, False)
    return error_control(gui)


def step_13(gui):
    gui.info_text_box.delete('1.0', END)
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 95% █████████▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                  "[общий анализ]\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)

    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    time.sleep(0.5)
    return error_control(gui)


def step_14(gui):
    time.sleep(0.1)
    poa_buttons.poa_stop_command(gui)
    time.sleep(2)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████████ 100% ██████████◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Остановка работы системы\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    poa_buttons.poa_status_command(gui, False)
    time.sleep(0.1)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return error_control(gui)


def step_15():
    result = askyesno(title="Проверка работы завершена",
                      message="Проверка завершена успешно.\nПоказатели соответствуют норме.\n\n"
                              "<Да> - для повторной проверки\n\n"
                              "<Нет> - для выхода в ручной режим")
    if result:
        return True
    else:
        return False


def check_step(step_number, gui):
    out = None

    if step_number == 1:
        out = step_1(gui)
    elif step_number == 2:
        out = step_2(gui)
    elif step_number == 3:
        out = step_3(gui)
    elif step_number == 4:
        out = step_4(gui)
    elif step_number == 5:
        out = step_5(gui)
    elif step_number == 6:
        out = step_6(gui)
    elif step_number == 8:
        out = step_8(gui)
    elif step_number == 9:
        out = step_9(gui)
    elif step_number == 10:
        out = step_10()
    elif step_number == 11:
        out = step_11(gui)
    elif step_number == 12:
        out = step_12(gui)
    elif step_number == 13:
        out = step_13(gui)
    elif step_number == 14:
        out = step_14(gui)
    elif step_number == 15:
        out = step_15()

    if gui.poa_auto_errors["beeper_error"]:
        while gui.poa_auto_errors["beeper_error"]:
            time.sleep(1)
            poa_buttons.poa_status_command(gui, False)
    if out:
        while out:
            if step_number != 1:
                if step_number == 1 or step_number == 2 or step_number == 3 or step_number == 12 or \
                        step_number == 13:
                    poa_buttons.poa_stop_command(gui)
                    poa_buttons.poa_start_command(gui, False)
                if step_number == 4 or step_number == 5 or step_number == 6 or step_number == 9 or \
                        step_number == 11 or step_number == 14:
                    poa_buttons.poa_stop_command(gui)
                if step_number == 8:
                    poa_buttons.poa_dry_command(gui)
            if step_number == 1:
                out = step_1(gui)
            elif step_number == 2:
                out = step_2(gui)
            elif step_number == 3:
                out = step_3(gui)
            elif step_number == 4:
                out = step_4(gui)
            elif step_number == 5:
                out = step_5(gui)
            elif step_number == 6:
                out = step_6(gui)
            elif step_number == 8:
                out = step_8(gui)
            elif step_number == 9:
                out = step_9(gui)
            elif step_number == 11:
                out = step_11(gui)
            elif step_number == 12:
                out = step_12(gui)
            elif step_number == 13:
                out = step_13(gui)
            elif step_number == 14:
                out = step_14(gui)
        else:
            if out is None:
                pass
            else:
                back_to_manual(gui)
                gui.info_text_box.delete('1.0', END)
                gui.info_text_box.insert(END, "❌ АВТОМАТИЧЕСКАЯ ПРОВЕРКА ОСТАНОВЛЕНА\n", 'tag_red_text')
                gui.info_text_box.insert(END, "⫸ Программа переведена в ручной режим\n", 'tag_black_text')
                gui.info_text_box.yview(END)
                gui.frame_for_units.update_idletasks()
                return True
    elif out is None:
        pass
    else:
        back_to_manual(gui)
        gui.info_text_box.delete('1.0', END)
        gui.info_text_box.insert(END, "❌ АВТОМАТИЧЕСКАЯ ПРОВЕРКА ОСТАНОВЛЕНА\n", 'tag_red_text')
        gui.info_text_box.insert(END, "⫸ Программа переведена в ручной режим\n", 'tag_black_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        return True
    return


def back_to_manual(gui):
    gui.poa_button.configure(state="normal", bg="gray60")
    gui.sth1_button.configure(state="normal", bg="gray60")
    gui.sth2_button.configure(state="normal", bg="gray60")
    gui.sth3_button.configure(state="normal", bg="gray60")
    gui.as_button.configure(state="normal", bg="gray60")
    gui.sc_button.configure(state="normal", bg="gray60")
    gui.ck_button.configure(state="normal", bg="gray60")
    gui.vs_button.configure(state="normal", bg="gray60")
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

    gui.device_label.configure(text="--", bg="gray95")
    gui.stat_ctrl_label.configure(text="--", bg="gray95")
    gui.stat_sens_label.configure(text="--", bg="gray95")
    gui.t_max_label.configure(text="--", bg="gray95")
    gui.t_min_label.configure(text="--", bg="gray95")
    gui.flow_label.configure(text="--", bg="gray95")
    gui.errors_label.configure(text="--", bg="gray95")
    gui.pwm_1_label.configure(text="--", bg="gray95")
    gui.pwm_2_label.configure(text="--", bg="gray95")
    gui.crc_label.configure(text="--", bg="gray95")

    gui.device_data.configure(text="--", bg="gray90")
    gui.stat_ctrl_data.configure(text="--", bg="gray90")
    gui.stat_sens_data.configure(text="--", bg="gray90")
    gui.t_max_data.configure(text="--", bg="gray90")
    gui.t_min_data.configure(text="--", bg="gray90")
    gui.flow_data.configure(text="--", bg="gray90")
    gui.errors_data.configure(text="--", bg="gray90")
    gui.pwm_1_data.configure(text="--", bg="gray90")
    gui.pwm_2_data.configure(text="--", bg="gray90")
    gui.crc_data.configure(text="--", bg="gray90")

    # Status sensors - всё неактивно
    gui.wts1_bit.configure(text="--", bg="gray90")
    gui.wts1_label.configure(bg="gray90")
    gui.wts2_bit.configure(text="--", bg="gray90")
    gui.wts2_label.configure(bg="gray90")
    gui.svs_bit.configure(text="--", bg="gray90")
    gui.svs_label.configure(bg="gray90")
    gui.key_bit.configure(text="--", bg="gray90")
    gui.key_label.configure(bg="gray90")
    gui.wls_bit.configure(text="--", bg="gray90")
    gui.wls_label.configure(bg="gray90")
    gui.reserve_1_bit.configure(text="--", bg="gray90")
    gui.reserve_1_label.configure(bg="gray90")
    gui.reserve_2_bit.configure(text="--", bg="gray90")
    gui.reserve_2_label.configure(bg="gray90")
    gui.reserve_3_bit.configure(text="--", bg="gray90")
    gui.reserve_3_label.configure(bg="gray90")

    # Status control - всё неактивно
    gui.rfp_bit.configure(text="--", bg="gray90")
    gui.rfp_label.configure(bg="gray90")
    gui.wpp_bit.configure(text="--", bg="gray90")
    gui.wpp_label.configure(bg="gray90")
    gui.acf_bit.configure(text="--", bg="gray90")
    gui.acf_label.configure(bg="gray90")
    gui.srs_bit.configure(text="--", bg="gray90")
    gui.srs_label.configure(bg="gray90")
    gui.beeper_bit.configure(text="--", bg="gray90")
    gui.beeper_label.configure(bg="gray90")
    gui.rfe_bit.configure(text="--", bg="gray90")
    gui.rfe_label.configure(bg="gray90")
    gui.reserve_4_bit.configure(text="--", bg="gray90")
    gui.reserve_4_label.configure(bg="gray90")
    gui.reserve_5_bit.configure(text="--", bg="gray90")
    gui.reserve_5_label.configure(bg="gray90")

    gui.start_button.configure(state='normal')
    gui.stop_button.configure(state='normal')
    gui.version_button.configure(state='normal')
    gui.info_button.configure(state='normal')
    gui.dry_button.configure(state='normal')
    gui.status_button.configure(state='normal')


def start_check(gui):
    # Запуск скрипта автоматической проверки системы охлаждения
    if not check_step(1, gui):
        if not check_step(2, gui):
            if not check_step(3, gui):
                if not check_step(4, gui):
                    if not check_step(5, gui):
                        if not check_step(6, gui):
                            if not step_7():
                                back_to_manual(gui)
                                gui.info_text_box.delete('1.0', END)
                                gui.info_text_box.insert(END, "❌ АВТОМАТИЧЕСКАЯ ПРОВЕРКА ОСТАНОВЛЕНА\n",
                                                         'tag_red_text')
                                gui.info_text_box.insert(END, "⫸ Программа переведена в ручной режим\n",
                                                         'tag_black_text')
                                gui.info_text_box.yview(END)
                                gui.frame_for_units.update_idletasks()
                                return
                            else:
                                if not check_step(8, gui):
                                    if not check_step(9, gui):
                                        if not step_10():
                                            back_to_manual(gui)
                                            gui.info_text_box.delete('1.0', END)
                                            gui.info_text_box.insert(END,
                                                                     "❌ АВТОМАТИЧЕСКАЯ ПРОВЕРКА "
                                                                     "ОСТАНОВЛЕНА\n", 'tag_red_text')
                                            gui.info_text_box.insert(END,
                                                                     "⫸ Программа переведена в ручной "
                                                                     "режим\n", 'tag_black_text')
                                            gui.info_text_box.yview(END)
                                            gui.frame_for_units.update_idletasks()
                                            return
                                        else:
                                            if not check_step(11, gui):
                                                if not check_step(12, gui):
                                                    if not check_step(13, gui):
                                                        if not check_step(14, gui):
                                                            if not step_15():
                                                                back_to_manual(gui)
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
                                                                start_check(gui)
