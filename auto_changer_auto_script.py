from tkinter.messagebox import askyesno
import time
from tkinter import *
import auto_sampler_buttons
import random
import back_to_manual_param


def back_to_manual(gui, number_of_operations=int()):
    back_to_manual_param.back_to_manual_parameters(gui, number_of_operations)
    gui.auc_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)

    gui.stop_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.stop_base_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.version_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.info_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.status_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.status_l_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.scan_sample_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.right_engine_3_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.left_engine_3_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.right_engine_2_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.left_engine_2_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.load_engine_1_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.base_engine_1_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.read_eeprom_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.write_eeprom_button.configure(bg="gray60", state='normal', relief=GROOVE)


def status_control(gui, state):
    if state == "Stop":
        if "Moving" in gui.auto_changer_state or "Moving backward" in gui.auto_changer_state \
                or "Moving forward" in gui.auto_changer_state:
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Команда стоп не выполнена",
                              message="Двигатели продолжили вращаться после команды стоп. Перезапустите проверку, "
                                      "убедитесь в корректности ответов контроллера. Может возникать при начале "
                                      "проверки, когда двигатели каретки или лифта находятся в промежуточном положении "
                                      "между концевиками. В таком случае переместите их в крайнее положение по "
                                      "конце вику и продолжите проверку\n\n"
                                      "<Да> - для продолжения проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

    elif state == "Stop ignore":
        if "Moving backward" in gui.auto_changer_state or "Moving forward" in gui.auto_changer_state:
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Команда стоп не выполнена",
                              message="Двигатели продолжили вращаться после команды стоп. Перезапустите проверку, "
                                      "убедитесь в корректности ответов контроллера. Может возникать при начале "
                                      "проверки, когда двигатели каретки или лифта находятся в промежуточном положении "
                                      "между концевиками. В таком случае переместите их в крайнее положение по "
                                      "конце вику и продолжите проверку\n\n"
                                      "<Да> - для продолжения проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

    elif state == "Lift down":
        if "Moving" in gui.auto_changer_state or "Moving backward" in gui.auto_changer_state \
                or "Moving forward" in gui.auto_changer_state or "Lift up" in gui.auto_changer_state \
                or "Lift between" in gui.auto_changer_state:
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Лифт не опустился",
                              message="Лифт не опустился. Проверьте механические преграды на пути лифта и ток "
                                      "двигателей, после чего перезапустите проверку\n\n"
                                      "<Да> - для продолжения проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

    elif state == "Lift up":
        if "Moving" in gui.auto_changer_state or "Moving backward" in gui.auto_changer_state \
                or "Moving forward" in gui.auto_changer_state or "Lift down" in gui.auto_changer_state \
                or "Lift between" in gui.auto_changer_state:
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Лифт не поднялся",
                              message="Лифт не поднялся. Проверьте механические преграды на пути лифта и ток "
                                      "двигателей, после чего перезапустите проверку\n\n"
                                      "<Да> - для продолжения проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

    elif state == "Engine 1 base":
        if "Moving" in gui.auto_changer_state or "Moving backward" in gui.auto_changer_state \
                or "Moving forward" in gui.auto_changer_state or "Base" not in gui.auto_changer_state:
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Двигатель каретки в процессе перемещения",
                              message="Контроллер сообщает, что двигатель каретки в процессе перемещения. "
                                      "Это происходит при некорректно принятой предыдущей команде (для этого "
                                      "выполните команду Stop, либо при неисправности датчика положения\n\n"
                                      "<Да> - для продолжения проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

    elif state == "Engine 1 load":
        if "Moving" in gui.auto_changer_state or "Moving backward" in gui.auto_changer_state \
                or "Moving forward" in gui.auto_changer_state or "Load" not in gui.auto_changer_state:
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Двигатель каретки в процессе перемещения",
                              message="Контроллер сообщает, что двигатель каретки в процессе перемещения. "
                                      "Это происходит при некорректно принятой предыдущей команде (для этого "
                                      "выполните команду Stop, либо при неисправности датчика положения\n\n"
                                      "<Да> - для продолжения проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

    elif state == "Rotate left":
        if "Not moving" in gui.auto_changer_state or "Moving backward" in gui.auto_changer_state:
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Некорректное выполнение команды вращателем",
                              message="Контроллер сообщает, что двигатель вращателя не вращается, либо вращается не "
                                      "в ту сторону. Проверьте правильность подключения проводов двигателя и наличие "
                                      "на контактах соответствующего напряжения\n\n"
                                      "<Да> - для продолжения проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

    elif state == "Rotate right":
        if "Not moving" in gui.auto_changer_state or "Moving forward" in gui.auto_changer_state:
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Некорректное выполнение команды вращателем",
                              message="Контроллер сообщает, что двигатель вращателя не вращается, либо вращается не "
                                      "в ту сторону. Проверьте правильность подключения проводов двигателя и наличие "
                                      "на контактах соответствующего напряжения\n\n"
                                      "<Да> - для продолжения проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

    elif state == "Cuvette":
        if "Cuvette" not in gui.auto_changer_state:
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Сенсор не видит наличие кюветы",
                              message="Сенсор сработал некорректно и не видит наличие кюветы. Проверьте "
                                      "контакт сенсора с контроллером пробоподатчика\n\n"
                                      "<Да> - для продолжения проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

    elif state == "Not cuvette":
        if "Cuvette" in gui.auto_changer_state:
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Сенсор ошибочно видит наличие кюветы",
                              message="Сенсор сработал некорректно ошибочно видит наличие кюветы. Проверьте "
                                      "контакт сенсора с контроллером пробоподатчика. Проверьте загрязнения "
                                      "между сенсором и кюветой\n\n"
                                      "<Да> - для продолжения проверки\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False


def error_control(gui, state=str()):
    # Функция проверки ошибок из команд от автоматического скрипта

    for error in gui.auto_changer_error:

        if error == "High speed" and state != "Stop ignore":
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Ошибка скорости вращения",
                              message="Скорость вращения выше установленной, проверьте состояние датчика "
                                      "скорости, после чего продолжите проверку.\n\n"
                                      "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

        if error == "Low speed" and state != "Stop ignore":
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Ошибка скорости вращения",
                              message="Скорость вращения меньше заданной либо отсутствует. Проверьте механику "
                                      "на заклинивание двигателя и убедитесь в работоспособности датчика "
                                      "скорости.\n\n"
                                      "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

        if error == "Movement error" and state != "Stop ignore":
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Блокирование перемещения двигателя",
                              message="Убедитесь, что ничего не мешает перемещению двигателей. Может возникать "
                                      "как при механических неполадках, так и некорректно установленном токе"
                                      " шаговых двигателей.\n\n"
                                      "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False

        if error == "incorrect_answer" and state != "Stop ignore":
            auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
            result = askyesno(title="Некорректный ответ контроллера",
                              message="Происходит при неправильно выбранной частоте обмена данными, "
                                      "плохом контакте либо проблемах с разводкой на плате\n\n"
                                      "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                      "<Нет> - для выхода в ручной режим")
            if result:
                return True
            else:
                return False
    if state:
        return status_control(gui, state)


def step_1(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖▒▒▒▒▒▒▒▒▒▒ 00% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Остановка двигателей\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 7):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание остановки двигателей. Опрос № " + str(i) + "/6\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and not gui.auto_changer_error:
            return error_control(gui, state="Stop")
        else:
            continue
    return error_control(gui, state="Stop")


def step_2(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖▒▒▒▒▒▒▒▒▒▒ 00% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Базирование двигателя лифта\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine2_base_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 7):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание базирования двигателя лифта. \nОпрос № " + str(i) + "/6\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                not gui.auto_changer_error:
            if "Base" in gui.auto_changer_state or "Load" in gui.auto_changer_state:
                return error_control(gui, state="Lift down")
            else:
                continue
        else:
            continue
    return error_control(gui, state="Lift down")


def step_3(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖▒▒▒▒▒▒▒▒▒▒ 00% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Базирование двигателя каретки\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine1_base_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание базирования двигателя каретки. \nОпрос № " + str(i) + "/3\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                "Base" in gui.auto_changer_state and not gui.auto_changer_error:
            return error_control(gui, state="Engine 1 base")
        else:
            continue
    return error_control(gui, state="Engine 1 base")


def step_4(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█▒▒▒▒▒▒▒▒▒ 05% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка движения каретки\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine1_load_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nПроверка движения каретки (Загрузка). \nОпрос № " + str(i) + "/3\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                "Load" in gui.auto_changer_state and not gui.auto_changer_error:
            return error_control(gui, state="Engine 1 load")
        else:
            continue
    return error_control(gui, state="Engine 1 load")


def step_5(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██▒▒▒▒▒▒▒▒ 10% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка движения каретки\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine1_base_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nПроверка движения каретки (База). \nОпрос № " + str(i) + "/3\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                "Base" in gui.auto_changer_state and not gui.auto_changer_error:
            return error_control(gui, state="Engine 1 base")
        else:
            continue
    return error_control(gui, state="Engine 1 base")


def step_6(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███▒▒▒▒▒▒▒ 15% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка движения каретки\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine1_load_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nПроверка движения каретки (Загрузка). \nОпрос № " + str(i) + "/3\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                "Load" in gui.auto_changer_state and not gui.auto_changer_error:
            return error_control(gui, state="Engine 1 load")
        else:
            continue
    return error_control(gui, state="Engine 1 load")


def step_7(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███▒▒▒▒▒▒▒ 15% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка движения каретки\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine1_base_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nПроверка движения каретки (База). \nОпрос № " + str(i) + "/3\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                "Base" in gui.auto_changer_state and not gui.auto_changer_error:
            return error_control(gui, state="Engine 1 base")
        else:
            continue
    return error_control(gui, state="Engine 1 base")


def step_8(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 20% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Перемещение лифта вверх\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine2_scan_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 8):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание перемещения двигателя лифта вверх. \nОпрос № " + str(i) + "/7\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift up" in gui.auto_changer_state and \
                not gui.auto_changer_error:
            if "Base" in gui.auto_changer_state or "Load" in gui.auto_changer_state:
                return error_control(gui, state="Lift up")
            else:
                continue
        else:
            continue
    return error_control(gui, state="Lift up")


def step_9(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████▒▒▒▒▒ 25% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Перемещение лифта вниз\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine2_base_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 8):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание перемещения двигателя лифта вниз. \nОпрос № " + str(i) + "/7\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                not gui.auto_changer_error:
            if "Base" in gui.auto_changer_state or "Load" in gui.auto_changer_state:
                return error_control(gui, state="Lift down")
            else:
                continue
        else:
            continue
    return error_control(gui, state="Lift down")


def speed_set_right(gui, speed, state):
    gui.speed_engine_3_combobox.set(speed)
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    time.sleep(0.5)
    auto_sampler_buttons.auto_sampler_engine3_right_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание обновления датчика. Опрос № " + str(i) + "/3\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.1)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.1)
        if "Moving backward" not in gui.auto_changer_state or "Low speed" in gui.auto_changer_error \
                or "High speed" in gui.auto_changer_error:
            continue
        else:
            return error_control(gui, state)
    return error_control(gui, state)


def step_10(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████▒▒▒▒ 30% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 10\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "10", state="Rotate right")


def step_11(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███████▒▒▒ 35% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 20\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "20", state="Rotate right")


def step_12(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████████▒▒ 40% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 30\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "30", state="Rotate right")


def step_13(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████████▒ 45% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 35\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "35", state="Rotate right")


def step_14(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 50% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 40\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "40", state="Rotate right")


def step_15(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 55% █▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 45\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "45", state="Rotate right")


def step_16(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 60% ██▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 55\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "55", state="Rotate right")


def speed_set_left(gui, speed, state):
    gui.speed_engine_3_combobox.set(speed)
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    time.sleep(0.5)
    auto_sampler_buttons.auto_sampler_engine3_left_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание обновления датчика. Опрос № " + str(i) + "/3\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.1)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.1)
        if "Moving forward" not in gui.auto_changer_state or "Low speed" in gui.auto_changer_error \
                or "High speed" in gui.auto_changer_error:
            continue
        else:
            return error_control(gui, state)
    return error_control(gui, state)


def step_17(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 65% ███▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 10\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "10", state="Rotate left")


def step_18(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 70% ████▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 20\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "20", state="Rotate left")


def step_19(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 75% █████▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 30\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "30", state="Rotate left")


def step_20(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 80% ██████▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 35\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "35", state="Rotate left")


def step_21(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 85% ███████▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 40\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "40", state="Rotate left")


def step_22(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 90% ████████▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 45\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "45", state="Rotate left")


def step_23(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 90% ████████▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Остановка двигателей\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 7):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание остановки двигателей. Опрос № " + str(i) + "/6\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and not gui.auto_changer_error:
            return error_control(gui, state="Stop")
        else:
            continue
    return error_control(gui, state="Stop")


def step_24(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 90% ████████▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Перемещение каретки\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine1_load_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nПроверка движения каретки (Загрузка). \nОпрос № " + str(i) + "/3\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                "Load" in gui.auto_changer_state and not gui.auto_changer_error:
            return error_control(gui, state="Engine 1 load")
        else:
            continue
    return error_control(gui, state="Engine 1 load")


def step_25(gui):
    result = askyesno(title="Проверка сенсора кюветы",
                      message="Установите кювету в каретку для проверки сработки сенсора наличия кюветы\n\n"
                              "<Да> - для продолжения проверки\n\n"
                              "<Нет> - для выхода в ручной режим")
    if result:
        gui.info_text_box.delete('1.0', END)
        gui.frame_for_units.update_idletasks()
        gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 95% █████████▒◗\n", 'tag_green_text')
        gui.info_text_box.insert(END, "⫸ Проверка сработки датчика наличия образца\n", 'tag_black_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        for i in range(0, 4):
            gui.auto_changer_error = []
            gui.auto_changer_state = []
            gui.info_text_box.delete('3.0', END)
            gui.info_text_box.insert(END, "\nОжидание Сработки датчика образца. \nОпрос № " + str(i) + "/3\n",
                                     'tag_green_text')
            gui.info_text_box.yview(END)
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
            time.sleep(0.05)
            if "Cuvette" in gui.auto_changer_state:
                return error_control(gui, state="Cuvette")
            else:
                continue
        return error_control(gui, state="Cuvette")
    else:
        return False


def step_26(gui):
    result = askyesno(title="Проверка сенсора кюветы",
                      message="Уберите кювету из каретки для проверки сработки сенсора наличия кюветы\n\n"
                              "<Да> - для продолжения проверки\n\n"
                              "<Нет> - для выхода в ручной режим")
    if result:
        gui.info_text_box.delete('1.0', END)
        gui.frame_for_units.update_idletasks()
        gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 95% █████████▒◗\n", 'tag_green_text')
        gui.info_text_box.insert(END, "⫸ Проверка сработки датчика наличия образца\n", 'tag_black_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        for i in range(0, 4):
            gui.auto_changer_error = []
            gui.auto_changer_state = []
            gui.info_text_box.delete('3.0', END)
            gui.info_text_box.insert(END, "\nОжидание Сработки датчика образца. \nОпрос № " + str(i) + "/3\n",
                                     'tag_green_text')
            gui.info_text_box.yview(END)
            gui.frame_for_units.update_idletasks()
            time.sleep(0.5)
            auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
            time.sleep(0.05)
            if "Cuvette" not in gui.auto_changer_state:
                return error_control(gui, state="Not cuvette")
            else:
                continue
        return error_control(gui, state="Not cuvette")
    else:
        return False


def step_27(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 99% ██████████◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Базирование двигателя каретки\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine1_base_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание базирования двигателя каретки. \nОпрос № " + str(i) + "/3\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                "Base" in gui.auto_changer_state and not gui.auto_changer_error:
            return error_control(gui, state="Engine 1 base")
        else:
            continue
    return error_control(gui, state="Engine 1 base")


def stop(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Бесконечная случайная проверка...\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Остановка двигателей\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 7):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание остановки двигателей. Опрос № " + str(i) + "/6\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state:
            return error_control(gui, state="Stop ignore")
        else:
            continue
    return error_control(gui, state="Stop ignore")


def engine_1_load(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Бесконечная случайная проверка...\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Проверка движения каретки\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine1_load_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nПроверка движения каретки (Загрузка). \nОпрос № " + str(i) + "/3\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                "Load" in gui.auto_changer_state and not gui.auto_changer_error:
            return error_control(gui, state="Engine 1 load")
        else:
            continue
    return error_control(gui, state="Engine 1 load")


def engine_1_base(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Бесконечная случайная проверка...\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Базирование двигателя каретки\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine1_base_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание базирования двигателя каретки. \nОпрос № " + str(i) + "/3\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                "Base" in gui.auto_changer_state and not gui.auto_changer_error:
            return error_control(gui, state="Engine 1 base")
        else:
            continue
    return error_control(gui, state="Engine 1 base")


def lift_up(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Бесконечная случайная проверка...\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Перемещение лифта вверх\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine2_scan_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 8):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание перемещения двигателя лифта вверх. \nОпрос № " + str(i) + "/7\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift up" in gui.auto_changer_state and \
                not gui.auto_changer_error:
            if "Base" in gui.auto_changer_state or "Load" in gui.auto_changer_state:
                return error_control(gui, state="Lift up")
            else:
                continue
        else:
            continue
    return error_control(gui, state="Lift up")


def rand_speed(gui, speed):
    gui.speed_engine_3_combobox.set(speed)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Бесконечная случайная проверка...\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Перемещение лифта вверх\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine3_left_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 5):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание обновления датчика. \nОпрос № " + str(i) + "/5\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Moving forward" not in gui.auto_changer_state or "Low speed" in gui.auto_changer_error \
                or "High speed" in gui.auto_changer_error:
            continue
        else:
            return error_control(gui, state="Rotate left")
    return error_control(gui, state="Rotate left")


def lift_down(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Бесконечная случайная проверка...\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Базирование двигателя лифта\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_changer_engine2_base_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 8):
        gui.auto_changer_error = []
        gui.auto_changer_state = []
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание базирования двигателя лифта. \nОпрос № " + str(i) + "/7\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_changer_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_changer_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if "Not moving" in gui.auto_changer_state and "Lift down" in gui.auto_changer_state and \
                not gui.auto_changer_error:
            if "Base" in gui.auto_changer_state or "Load" in gui.auto_changer_state:
                return error_control(gui, state="Lift down")
            else:
                continue
        else:
            continue
    return error_control(gui, state="Lift down")


def start_check(gui):
    # Запуск скрипта автоматической проверки системы охлаждения
    number_of_ops = 0

    for function_number in range(1, 28):
        result = eval("step_" + str(function_number) + "(gui)")
        number_of_ops += 1
        while result:
            result = eval("step_" + str(function_number) + "(gui)")
        if str(result) == "False":
            back_to_manual(gui, number_of_operations=number_of_ops)
            return ()

    result = stop(gui)
    number_of_ops += 1
    if str(result) == "False":
        back_to_manual(gui, number_of_operations=number_of_ops)
        return ()
    time.sleep(0.2)

    result = askyesno(title="Проверка окончена",
                      message="Проверка успешно окончена. Включить бесконечную проверку автоматического"
                              " сменщика образцов?\n\n"
                              "<Да> - для бесконечной проверки\n\n"
                              "<Нет> - для выхода в ручной режим")
    if result:
        while True:

            result = engine_1_load(gui)
            if str(result) == "False":
                number_of_ops += 1
                back_to_manual(gui, number_of_operations=number_of_ops)
                return ()
            time.sleep(0.2)

            result = engine_1_base(gui)
            number_of_ops += 1
            if str(result) == "False":
                back_to_manual(gui, number_of_operations=number_of_ops)
                return ()
            time.sleep(0.2)

            result = lift_up(gui)
            number_of_ops += 1
            if str(result) == "False":
                back_to_manual(gui, number_of_operations=number_of_ops)
                return ()
            time.sleep(0.2)

            result = lift_up(gui)
            if str(result) == "False":
                back_to_manual(gui, number_of_operations=number_of_ops)
                return ()
            time.sleep(0.2)

            random_speed = random.choice(["10", "20", "30", "35", "40", "45", "55"])
            result = rand_speed(gui, random_speed)
            number_of_ops += 1
            if str(result) == "False":
                back_to_manual(gui, number_of_operations=number_of_ops)
                return ()
            time.sleep(2.0)

            result = stop(gui)
            number_of_ops += 1
            if str(result) == "False":
                back_to_manual(gui, number_of_operations=number_of_ops)
                return ()
            time.sleep(0.2)

            result = lift_down(gui)
            number_of_ops += 1
            if str(result) == "False":
                back_to_manual(gui, number_of_operations=number_of_ops)
                return ()
            time.sleep(0.2)

            result = lift_down(gui)
            if str(result) == "False":
                back_to_manual(gui, number_of_operations=number_of_ops)
                return ()
            time.sleep(0.2)

    else:
        back_to_manual(gui, number_of_operations=number_of_ops)
        return ()
