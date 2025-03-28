from tkinter.messagebox import askyesno
import time
from tkinter import *
import auto_sampler_buttons


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


def back_to_manual(gui):
    gui.poa_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.as_button.configure(bg="SeaGreen1", state='disabled', relief=RIDGE)
    gui.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)
    gui.vs_button.configure(bg="gray60", state='normal', relief=GROOVE)
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
    gui.manual_button.configure(state="disabled", bg="SeaGreen1")
    gui.auto_button.configure(state="normal", bg="gray60")


def error_control(gui):
    # Функция проверки ошибок из команд от автоматического скрипта
    reset = False
    auto_sampler_buttons.auto_sampler_stop_command(gui, auto=True)
    for error, status in gui.auto_sampler_real_state.items():
        if status:

            if error == "incorrect_answer":

                result = askyesno(title="Некорректный ответ контроллера",
                                  message="Если случай единичный, можно продолжать проверку без дополнительных "
                                          "действий. В случае повторного получения данной ошибки стоит проверить"
                                          " линию связи с контроллером и наличие помех.\n\n"
                                          "<Да> - для продолжения проверки\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            if error == "engine3_state" and not gui.ignore:

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


def step_1(gui):
    reset_errors(gui)
    gui.ignore = True
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


def step_21(gui):
    gui.speed_engine_3_combobox.set("10")
    reset_errors(gui)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 20% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 10\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
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


def step_22(gui):
    gui.speed_engine_3_combobox.set("10")
    reset_errors(gui)
    gui.info_text_box.delete('1.0', END)
    gui.frame_for_units.update_idletasks()
    gui.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 21% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
    gui.info_text_box.insert(END, "⫸ Запуск вращателя на скорости: 10\n", 'tag_black_text')
    gui.info_text_box.yview(END)
    gui.frame_for_units.update_idletasks()
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


def start_check(gui):
    # Запуск скрипта автоматической проверки системы охлаждения

    for function_number in range(1, 23):
        result = eval("step_" + str(function_number) + "(gui)")
        while result:
            result = eval("step_" + str(function_number) + "(gui)")
        if str(result) == "False":
            back_to_manual(gui)
            return ()
