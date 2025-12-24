from tkinter.messagebox import askyesno
import time
from tkinter import *
import auto_sampler_buttons
import random
import back_to_manual_param

def reset_errors(gui):
    gui.auto_sampler_real_state = {
        "engine3_state": False,
        "lift_state": False,
        "lift_status": False,
        "engine2_state": False,
        "set_sample_state": False,
        "wait_state": False,
        "incorrect_answer": False,
        "movement_errors": False,
        "engine1_state": False
    }
    gui.wait_status = False
    gui.ignore = False
    gui.ignore_speed = False


def back_to_manual(gui, number_of_operations=int()):
    back_to_manual_param.back_to_manual_parameters(gui, number_of_operations)
    gui.as_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)

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


def error_control(gui):
    # Функция проверки ошибок из команд от автоматического скрипта
    reset = False
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)

    if gui.wait_status:
        return None

    for error, status in gui.auto_sampler_real_state.items():
        if status:

            if error == "engine3_state" and not gui.ignore_speed:

                if gui.auto_sampler_real_state["engine3_state"][0] < gui.auto_sampler_real_state["engine3_state"][1]:
                    result = askyesno(title="Ошибка скорости вращения",
                                      message="Скорость вращения выше установленной, проверьте состояние датчика "
                                              "скорости, после чего продолжите проверку.\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                else:
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

            if error == "movement_errors":

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

            if error == "engine1_state" and not gui.ignore:
                if gui.auto_sampler_real_state["engine1_state"] == "Fault":
                    result = askyesno(title="Ошибка определения позиции",
                                      message="Барабан остановился в некорректной позиции образца. Требуется проверить "
                                              "сработку датчиков положения барабана.\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                    if result:
                        return True
                    else:
                        return False
                if gui.auto_sampler_real_state["engine1_state"] == "Wait":
                    result = askyesno(title="Ошибка определения позиции",
                                      message="Барабан остановился в промежуточной позиции либо ему не хватило времени"
                                              " на перемещение. Требуется проверить сработку датчиков положения "
                                              "барабана и скорость/дробление шагового двигателя. А так же отсутствие"
                                              " закусываний платформы mini-standa, механических повреждений, "
                                              "/ посторонних предметов, мешающих перемещению барабана.\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                    if result:
                        return True
                    else:
                        return False

            if gui.ignore:
                result = askyesno(title="Ошибка лифта",
                                  message="Лифт не переместился в заданное положение. Проверьте ток шагового двигателя "
                                          "лифта, работоспособность двигателя и наличие посторонних предметов, "
                                          "мешающих перемещению лифта.\n\n"
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


def error_control_set_sample(gui):
    # Функция проверки ошибок из команд от автоматического скрипта
    reset = False
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    for error, status in gui.auto_sampler_real_state.items():
        if status:
            if error == "set_sample_state":
                if gui.auto_sampler_real_state["set_sample_state"] == "lift_fault":
                    result = askyesno(title="Ошибка установки образца",
                                      message="Лифт не отозвался на команду. Возможно заклинивание либо "
                                              "некорректная установка тока шагового двигателя.\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                elif gui.auto_sampler_real_state["set_sample_state"] == "engine1":
                    result = askyesno(title="Ошибка установки образца",
                                      message="Барабан не переместил образец на установленную позицию. Проверьте "
                                              "сработку датчиков положения барабана, ток шагового двигателя барабана, "
                                              "отсутствие закусываний платформы mini-standa и наличие механических "
                                              "повреждений / посторонних предметов, мешающих перемещению барабана.\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                elif gui.auto_sampler_real_state["set_sample_state"] == "lift_up":
                    result = askyesno(title="Ошибка установки образца",
                                      message="Лифт не вышел в верхнюю позицию. Проверьте ток шагового двигателя "
                                              "лифта, работоспособность двигателя и наличие посторонних предметов, "
                                              "мешающих перемещению лифта.\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                elif gui.auto_sampler_real_state["set_sample_state"] == "lift_down":
                    result = askyesno(title="Ошибка установки образца",
                                      message="Лифт не вышел в нижнюю позицию. Проверьте ток шагового двигателя "
                                              "лифта, работоспособность двигателя и наличие посторонних предметов, "
                                              "мешающих перемещению лифта.\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                else:
                    result = askyesno(title="Ошибка установки образца",
                                      message="Неизвестная ошибка установки образца.\n\n"
                                              "<Да> - для продолжения проверки\n (если проблема исправлена)\n\n"
                                              "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if gui.wait_status:
                result = askyesno(title="Ошибка времени ожидания образца",
                                  message="Команда перемещения образца не выполнена за отведённое время. Повторить "
                                          "запрос?\n\n"
                                          "<Да> - для продолжения проверки\n\n"
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
    reset_errors(gui)
    gui.ignore = True
    gui.ignore_speed = True
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖▒▒▒▒▒▒▒▒▒▒ 00% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Возвращение в базовое положение\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_stop_base_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 6):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание возвращения, Опрос № " + str(i) + "/5\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["lift_status"] != "Down":
            continue
        else:
            gui.ignore = False
            return error_control(gui)
    return error_control(gui)


def find_samples(gui, position):
    reset_errors(gui)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    if position < 6:
        gui.info_text_box.insert(END, "⫸ Прогресс ◖▒▒▒▒▒▒▒▒▒▒ 0" + str(position) + "% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    else:
        gui.info_text_box.insert(END, "⫸ Прогресс ◖█▒▒▒▒▒▒▒▒▒ 0" + str(position) + "% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Определение позиций образцов\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine1_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    timer = 11
    if position != 1:
        timer = 4
    for i in range(0, timer):
        gui.info_text_box.delete('3.0', END)
        if position == 1:
            gui.info_text_box.insert(END, "\nОжидание позиции №" + str(position) + ". Опрос № " + str(i) + "/10\n",
                                     'tag_green_text')
        else:
            gui.info_text_box.insert(END, "\nОжидание позиции №" + str(position) + ". Опрос № " + str(i) + "/3\n",
                                     'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine1_state"] != "Done":
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def step_2(gui):
    gui.speed_engine_1_combobox.set("1")
    return find_samples(gui, 1)


def step_3(gui):
    gui.speed_engine_1_combobox.set("2")
    return find_samples(gui, 2)


def step_4(gui):
    gui.speed_engine_1_combobox.set("3")
    return find_samples(gui, 3)


def step_5(gui):
    gui.speed_engine_1_combobox.set("4")
    return find_samples(gui, 4)


def step_6(gui):
    gui.speed_engine_1_combobox.set("5")
    return find_samples(gui, 5)


def step_7(gui):
    gui.speed_engine_1_combobox.set("6")
    return find_samples(gui, 6)


def step_8(gui):
    gui.speed_engine_1_combobox.set("7")
    return find_samples(gui, 7)


def step_9(gui):
    gui.speed_engine_1_combobox.set("8")
    return find_samples(gui, 8)


def step_10(gui):
    gui.speed_engine_1_combobox.set("4")
    reset_errors(gui)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█▒▒▒▒▒▒▒▒▒ 09% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Поворот на половину оборота колеса\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine1_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 8):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание позиции №4. Опрос № " + str(i) + "/7\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine1_state"] != "Done":
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def step_11(gui):
    gui.speed_engine_1_combobox.set("8")
    reset_errors(gui)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██▒▒▒▒▒▒▒▒ 10% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Поворот на половину оборота колеса\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine1_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 8):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание позиции №8. Опрос № " + str(i) + "/7\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine1_state"] != "Done":
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def step_12(gui):
    gui.speed_engine_1_combobox.set("6")
    reset_errors(gui)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██▒▒▒▒▒▒▒▒ 11% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Поворот на 2/3 оборота колеса\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine1_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 10):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание позиции №6. Опрос № " + str(i) + "/9\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine1_state"] != "Done":
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def step_13(gui):
    gui.speed_engine_1_combobox.set("4")
    reset_errors(gui)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██▒▒▒▒▒▒▒▒ 12% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Поворот на 2/3 оборота колеса\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine1_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 10):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание позиции №4. Опрос № " + str(i) + "/9\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine1_state"] != "Done":
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def step_14(gui):
    gui.speed_engine_1_combobox.set("3")
    reset_errors(gui)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██▒▒▒▒▒▒▒▒ 13% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Поворот на полный оборота колеса\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine1_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 11):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание позиции №3. Опрос № " + str(i) + "/10\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine1_state"] != "Done":
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def step_15(gui):
    gui.speed_engine_1_combobox.set("2")
    reset_errors(gui)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██▒▒▒▒▒▒▒▒ 14% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Поворот на полный оборота колеса\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine1_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 11):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание позиции №2. Опрос № " + str(i) + "/10\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine1_state"] != "Done":
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def step_16(gui):
    gui.speed_engine_1_combobox.set("1")
    reset_errors(gui)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███▒▒▒▒▒▒▒ 15% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Поворот на полный оборота колеса\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine1_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 11):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание позиции №1. Опрос № " + str(i) + "/10\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine1_state"] != "Done":
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def step_17(gui):
    reset_errors(gui)
    gui.ignore = True
    gui.ignore_speed = True
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███▒▒▒▒▒▒▒ 16% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Подъём лифта\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine2_up_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание подъёма лифта. Опрос № " + str(i) + "/3\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["lift_status"] != "Up":
            continue
        else:
            gui.ignore = False
            return error_control(gui)
    return error_control(gui)


def step_18(gui):
    reset_errors(gui)
    gui.ignore = True
    gui.ignore_speed = True
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███▒▒▒▒▒▒▒ 17% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Спуск лифта\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine2_down_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание спуска лифта. Опрос № " + str(i) + "/3\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["lift_status"] != "Down":
            continue
        else:
            gui.ignore = False
            return error_control(gui)
    return error_control(gui)


def step_19(gui):
    reset_errors(gui)
    gui.ignore = True
    gui.ignore_speed = True
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███▒▒▒▒▒▒▒ 18% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Подъём лифта\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine2_up_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание подъёма лифта. Опрос № " + str(i) + "/3\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["lift_status"] != "Up":
            continue
        else:
            gui.ignore = False
            return error_control(gui)
    return error_control(gui)


def step_20(gui):
    reset_errors(gui)
    gui.ignore = True
    gui.ignore_speed = True
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███▒▒▒▒▒▒▒ 19% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Спуск лифта\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine2_down_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 4):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание спуска лифта. Опрос № " + str(i) + "/3\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["lift_status"] != "Down":
            continue
        else:
            gui.ignore = False
            return error_control(gui)
    return error_control(gui)


def speed_set_right(gui, speed):
    gui.speed_engine_3_combobox.set(speed)
    reset_errors(gui)
    auto_sampler_buttons.auto_sampler_engine3_right_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 5):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание обновления датчика. Опрос № " + str(i) + "/5\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine3_state"]:
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def step_21(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 22% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 10\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "10")


def step_22(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 23% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 20\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "20")


def step_23(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 24% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 30\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "30")


def step_24(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████▒▒▒▒▒ 25% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 35\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "35")


def step_25(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████▒▒▒▒▒ 26% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 40\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "40")


def step_26(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████▒▒▒▒▒ 27% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 45\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "45")


def step_27(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████▒▒▒▒▒ 28% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 50\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "50")


def step_28(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████▒▒▒▒▒ 29% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 55\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "55")


def step_29(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████▒▒▒▒ 30% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 60\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "65")


def step_30(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████▒▒▒▒ 31% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 70\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "70")


def step_31(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████▒▒▒▒ 32% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 75\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "75")


def step_32(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████▒▒▒▒ 33% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 80\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "80")


def step_33(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████▒▒▒▒ 34% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 90\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "90")


def step_34(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███████▒▒▒ 35% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 100\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "100")


def speed_set_left(gui, speed):
    gui.speed_engine_3_combobox.set(speed)
    reset_errors(gui)
    auto_sampler_buttons.auto_sampler_engine3_left_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 5):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание обновления датчика. Опрос № " + str(i) + "/5\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine3_state"]:
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def step_35(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███████▒▒▒ 36% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 10\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "10")


def step_36(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███████▒▒▒ 37% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 20\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "20")


def step_37(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███████▒▒▒ 38% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 30\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "30")


def step_38(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███████▒▒▒ 39% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 35\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "35")


def step_39(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████████▒▒ 40% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 40\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "40")


def step_40(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████████▒▒ 41% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 45\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "45")


def step_41(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████████▒▒ 42% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 50\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "50")


def step_42(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████████▒▒ 43% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 55\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "55")


def step_43(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████████▒▒ 44% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 60\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "65")


def step_44(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████████▒ 45% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 70\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "70")


def step_45(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████████▒ 46% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 75\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "75")


def step_46(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████████▒ 47% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 80\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "80")


def step_47(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████████▒ 48% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 90\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "90")


def step_48(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████████▒ 49% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 100\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "100")


def set_sample_auto(gui, sample):
    reset_errors(gui)
    gui.speed_engine_1_combobox.set(sample)
    auto_sampler_buttons.auto_sampler_set_sample_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 13):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание установки образца. Опрос № " + str(i) + "/12\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["set_sample_state"] or gui.wait_status:
            continue
        else:
            return error_control_set_sample(gui)
    return error_control_set_sample(gui)


def step_49(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 50% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка образца №1\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return set_sample_auto(gui, 1)


def step_50(gui):
    time.sleep(0.5)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 56% █▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка образца №2\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return set_sample_auto(gui, 2)


def step_51(gui):
    time.sleep(0.5)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 62% ██▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка образца №3\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return set_sample_auto(gui, 3)


def step_52(gui):
    time.sleep(0.5)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 68% ███▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка образца №4\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return set_sample_auto(gui, 4)


def step_53(gui):
    time.sleep(0.5)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 74% ████▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка образца №5\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return set_sample_auto(gui, 5)


def step_54(gui):
    time.sleep(0.5)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 80% ██████▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка образца №6\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return set_sample_auto(gui, 6)


def step_55(gui):
    time.sleep(0.5)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 86% ███████▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка образца №7\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return set_sample_auto(gui, 7)


def step_56(gui):
    time.sleep(0.5)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 92% ████████▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка образца №8\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return set_sample_auto(gui, 8)


def step_57(gui):
    time.sleep(0.5)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 98% █████████▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка образца №1\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return set_sample_auto(gui, 1)


def step_58(gui):
    reset_errors(gui)
    gui.ignore = True
    gui.ignore_speed = True
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 100% ██████████◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Возвращение в базовое положение\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_stop_base_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 26):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание возвращения, Опрос № " + str(i) + "/25\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["lift_status"] != "Down":
            continue
        else:
            gui.ignore = False
            return error_control(gui)
    return error_control(gui)


def random_sample_auto(gui, sample):
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    time.sleep(0.5)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Бесконечная случайная проверка...\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка случайного образца...\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    reset_errors(gui)
    gui.speed_engine_1_combobox.set(sample)
    auto_sampler_buttons.auto_sampler_set_sample_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 31):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание установки образца. Опрос № " + str(i) + "/30\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["set_sample_state"] or gui.wait_status:
            continue
        else:
            return error_control_set_sample(gui)
    return error_control_set_sample(gui)


def random_speed_left(gui, speed):
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Бесконечная случайная проверка...\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка случайной скорости вращения...\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    gui.speed_engine_3_combobox.set(speed)
    reset_errors(gui)
    auto_sampler_buttons.auto_sampler_engine3_left_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 8):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание обновления датчика. Опрос № " + str(i) + "/7\n",
                                 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(3)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine3_state"]:
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def lift_down(gui):
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    reset_errors(gui)
    gui.ignore = True
    gui.ignore_speed = True
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Бесконечная случайная проверка...\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Спуск лифта в базовое положение...\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine2_down_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 8):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание спуска лифта. Опрос № " + str(i) + "/7\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["lift_status"] != "Down" or gui.auto_sampler_real_state["engine3_state"]:
            continue
        else:
            gui.ignore = False
            return error_control(gui)
    return error_control(gui)


def random_position(gui, position):
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    gui.speed_engine_1_combobox.set(str(position))
    reset_errors(gui)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Бесконечная случайная проверка...\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Установка случайного положения...\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine1_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 26):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nПоиск положения. Опрос № " + str(i) + "/25\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["engine1_state"] != "Done":
            continue
        else:
            return error_control(gui)
    return error_control(gui)


def start_check(gui):
    # Запуск скрипта автоматической проверки системы охлаждения
    number_of_ops = 0
    for function_number in range(1, 59):
        result = eval("step_" + str(function_number) + "(gui)")
        number_of_ops += 1
        while result:
            result = eval("step_" + str(function_number) + "(gui)")
        if str(result) == "False":
            back_to_manual(gui, number_of_operations=number_of_ops)
            return ()

    result = askyesno(title="Проверка окончена",
                      message="Проверка успешно окончена. Включить бесконечную проверку автоматического"
                              " сменщика образцов?\n\n"
                              "<Да> - для бесконечной проверки\n\n"
                              "<Нет> - для выхода в ручной режим")
    if result:
        while True:
            random_sample = random.randint(1, 8)
            result = random_sample_auto(gui, random_sample)
            number_of_ops += 1
            if str(result) == "False":
                back_to_manual(gui, number_of_operations=number_of_ops)
                return ()
            time.sleep(0.2)
            random_speed = random.choice(["10", "20", "30", "35", "40", "45", "50", "55", "65", "70",
                                          "75", "80", "90", "100"])
            result = random_speed_left(gui, random_speed)
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
            position = random.randint(1, 8)
            result = random_position(gui, position)
            number_of_ops += 1
            if str(result) == "False":
                back_to_manual(gui, number_of_operations=number_of_ops)
                return ()
            time.sleep(0.2)
    else:
        back_to_manual(gui, number_of_operations=number_of_ops)
        return ()
