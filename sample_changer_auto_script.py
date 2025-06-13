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


def back_to_manual(gui):
    back_to_manual_param.back_to_manual_parameters(gui)
    gui.sc_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)

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


def step_2(gui):
    reset_errors(gui)
    gui.ignore = True
    gui.ignore_speed = True
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█▒▒▒▒▒▒▒▒▒ 05% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
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


def step_3(gui):
    reset_errors(gui)
    gui.ignore = True
    gui.ignore_speed = True
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██▒▒▒▒▒▒▒▒ 10% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
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


def step_4(gui):
    reset_errors(gui)
    gui.ignore = True
    gui.ignore_speed = True
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██▒▒▒▒▒▒▒▒ 10% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
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


def step_5(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███▒▒▒▒▒▒▒ 15% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 10\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "10")


def step_6(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███▒▒▒▒▒▒▒ 15% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 20\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "20")


def step_7(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 20% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 30\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "30")


def step_8(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 20% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 35\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "35")


def step_9(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████▒▒▒▒▒ 25% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 40\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "40")


def step_10(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████▒▒▒▒ 30% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 45\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "45")


def step_11(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████▒▒▒▒ 30% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 50\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "50")


def step_12(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███████▒▒▒ 35% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 55\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "55")


def step_13(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖███████▒▒▒ 35% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 60\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "65")


def step_14(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████████▒▒ 40% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 70\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "70")


def step_15(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████████▒ 45% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 75\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "75")


def step_16(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖█████████▒ 45% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 80\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "80")


def step_17(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 50% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 90\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_right(gui, "90")


def step_18(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 50% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
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


def step_19(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 55% █▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 10\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "10")


def step_20(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 60% ██▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 20\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "20")


def step_21(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 60% ██▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 30\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "30")


def step_22(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 65% ███▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 35\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "35")


def step_23(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 65% ███▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 40\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "40")


def step_24(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 70% ████▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 45\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "45")


def step_25(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 75% █████▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 50\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "50")


def step_26(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 75% █████▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 55\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "55")


def step_27(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 80% ███████▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 60\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "65")


def step_28(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 80% ██████▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 70\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "70")


def step_29(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 85% ███████▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 75\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "75")


def step_30(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 90% ████████▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 80\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "80")


def step_31(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 90% ████████▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 90\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "90")


def step_32(gui):
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 95% █████████▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 100\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    return speed_set_left(gui, "100")


def step_33(gui):
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


def lift_up(gui):
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    reset_errors(gui)
    gui.ignore = True
    gui.ignore_speed = True
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Бесконечная случайная проверка...\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Подъём лифта в верхнее положение...\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    auto_sampler_buttons.auto_sampler_engine2_up_command(gui, auto=True)
    gui.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
    for i in range(0, 8):
        gui.info_text_box.delete('3.0', END)
        gui.info_text_box.insert(END, "\nОжидание подъёма лифта. Опрос № " + str(i) + "/7\n", 'tag_green_text')
        gui.info_text_box.yview(END)
        gui.frame_for_units.update_idletasks()
        time.sleep(0.5)
        auto_sampler_buttons.auto_sampler_status_command(gui, auto=True)
        time.sleep(0.05)
        auto_sampler_buttons.auto_sampler_status_l_command(gui, auto=True)
        time.sleep(0.05)
        if gui.auto_sampler_real_state["lift_status"] != "Up" or gui.auto_sampler_real_state["engine3_state"]:
            continue
        else:
            gui.ignore = False
            return error_control(gui)
    return error_control(gui)


def start_check(gui):
    # Запуск скрипта автоматической проверки системы охлаждения

    for function_number in range(1, 34):
        result = eval("step_" + str(function_number) + "(gui)")
        while result:
            result = eval("step_" + str(function_number) + "(gui)")
        if str(result) == "False":
            back_to_manual(gui)
            return ()

    result = askyesno(title="Проверка окончена",
                      message="Проверка успешно окончена. Включить бесконечную проверку автоматического"
                              " сменщика образцов?\n\n"
                              "<Да> - для бесконечной проверки\n\n"
                              "<Нет> - для выхода в ручной режим")
    if result:
        while True:
            random_speed = random.choice(["10", "20", "30", "35", "40", "45", "50", "55", "65", "70",
                                          "75", "80", "90", "100"])
            result = random_speed_left(gui, random_speed)
            if str(result) == "False":
                back_to_manual(gui)
                return ()
            time.sleep(0.2)
            result = lift_down(gui)
            if str(result) == "False":
                back_to_manual(gui)
                return ()
            time.sleep(0.2)
            result = random_speed_left(gui, random_speed)
            if str(result) == "False":
                back_to_manual(gui)
                return ()
            time.sleep(0.2)
            result = lift_up(gui)
            if str(result) == "False":
                back_to_manual(gui)
                return ()
            time.sleep(0.2)
    else:
        back_to_manual(gui)
        return ()
