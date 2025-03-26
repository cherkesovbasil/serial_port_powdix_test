import serial
from tkinter import *
from tkinter import ttk
import request_and_port_list
import request_response
import time
import cooling_system_unit
import temperature_humidity_unit
import auto_sampler_unit
import sample_changer_unit
import knife_unit
import variable_slit_unit


def com_ports(gui):
    # Функция работы с COM-портами

    def update_info(port_number, message):

        # Обновляю поле отчёта о поиске портов
        gui.report_box.insert(END, message)
        gui.report_box.update()
        gui.report_box.yview(END)

        # обновляю шкалу загрузки
        gui.process_progressbar["value"] = port_number * 2
        gui.process_progressbar.update()

    def find_device():

        def check_green():
            # Выделяет зелёным порт, на котором висит устройство

            gui.box_for_com_ports.delete('1.0', END)
            for x in range(0, len(open_ports)):
                frame_1 = Frame()
                if x == actual_port_number - 1:
                    label_1 = Label(frame_1, text=f"COM-порт {open_ports[x]}", width=33, background="SeaGreen1",
                                    relief=GROOVE)
                else:
                    label_1 = Label(frame_1, text=f"COM-порт {open_ports[x]}", width=33, background="gray60",
                                    relief=GROOVE)
                label_1.pack(side=LEFT)
                gui.box_for_com_ports.window_create(END, window=frame_1)
                gui.box_for_com_ports.insert(END, '\n')
                gui.box_for_com_ports.update()

        def if_answer(response, request_id):
            gui.report_box.insert(END, " -  Запрос   : " +
                                  str(request_and_port_list.identification_dictionary[request_id]))
            gui.report_box.insert(END, " -  Ответ     : " + str(response))
            gui.report_box.insert(END, " -  Порт      : " + str(extracted_port))
            gui.report_box.insert(END, " -  Частота  : " +
                                  str(request_and_port_list.com_port_settings["baudrate"]))
            check_green()
            gui.report_box.update()
            time.sleep(1)
            gui.report_box.delete(0, END)

            gui.bytesize_combobox.set(request_and_port_list.com_port_settings["bytesize"])
            gui.timeout_combobox.set(request_and_port_list.com_port_settings["timeout"])
            gui.baudrate_combobox.set(request_and_port_list.com_port_settings["baudrate"])
            gui.port_combobox.set(extracted_port)

            gui.report_box.insert(END, "                                          "
                                       "⮜⮜⮜ ИНИЦИАЛИЗАЦИЯ СКРИПТА ⮞⮞⮞")
            gui.report_box.insert(END, "                                                        ▒▒▒▒▒▒▒▒▒▒ [00%]")
            gui.report_box.update()
            time.sleep(0.1)
            gui.report_box.delete(0, END)
            gui.report_box.insert(END, "                                          "
                                       "⮜⮜⮜ ИНИЦИАЛИЗАЦИЯ СКРИПТА ⮞⮞⮞")
            gui.report_box.insert(END, "                                                        ██▒▒▒▒▒▒▒▒ [20%]")
            gui.report_box.update()
            time.sleep(0.1)
            gui.report_box.delete(0, END)
            gui.report_box.insert(END, "                                          "
                                       "⮜⮜⮜ ИНИЦИАЛИЗАЦИЯ СКРИПТА ⮞⮞⮞")
            gui.report_box.insert(END, "                                                        ████▒▒▒▒▒▒ [40%]")
            gui.report_box.update()
            time.sleep(0.1)
            gui.report_box.delete(0, END)
            gui.report_box.insert(END, "                                          "
                                       "⮜⮜⮜ ИНИЦИАЛИЗАЦИЯ СКРИПТА ⮞⮞⮞")
            gui.report_box.insert(END, "                                                        ██████▒▒▒▒ [60%]")
            gui.report_box.update()
            time.sleep(0.1)
            gui.report_box.delete(0, END)
            gui.report_box.insert(END, "                                          "
                                       "⮜⮜⮜ ИНИЦИАЛИЗАЦИЯ СКРИПТА ⮞⮞⮞")
            gui.report_box.insert(END, "                                                        ████████▒▒ [80%]")
            gui.report_box.update()
            time.sleep(0.1)
            gui.report_box.delete(0, END)
            gui.report_box.insert(END, "                                          "
                                       "⮜⮜⮜ ИНИЦИАЛИЗАЦИЯ СКРИПТА ⮞⮞⮞")
            gui.report_box.insert(END, "                                                        ██████████ [100%]")
            gui.report_box.update()
            time.sleep(0.1)

            for widgets in gui.frame_for_units.winfo_children():
                widgets.destroy()

        actual_port_number = 0
        answer = None

        for extracted_port in open_ports:

            # Обновляет поле отчёта о поиске портов
            gui.report_box.delete(0, END)
            gui.report_box.insert(END, "                                   ⮜⮜⮜ ОПРАШИВАЮ ПОРТ " + str(extracted_port)
                                  + " ⮞⮞⮞")
            gui.report_box.update()

            request_and_port_list.com_port_settings["comport"] = extracted_port
            if answer:
                break

            # Выделяет синим задействованный на данный момент порт
            actual_port_number += 1
            gui.box_for_com_ports.delete('1.0', END)
            for i in range(0, len(open_ports)):
                frame = Frame()
                if i == actual_port_number - 1:
                    label = Label(frame, text=f"COM-порт {open_ports[i]}", width=33, background="deep sky blue",
                                  relief=GROOVE)
                else:
                    label = Label(frame, text=f"COM-порт {open_ports[i]}", width=33, background="gray60",
                                  relief=GROOVE)
                label.pack(side=LEFT)
                gui.box_for_com_ports.window_create(END, window=frame)
                gui.box_for_com_ports.insert(END, '\n')

            # Ищет, какое устройство подключено к данному порту
            for request_name, request in request_and_port_list.identification_dictionary.items():

                if request_name == "poa_request":
                    gui.report_box.insert(END, " -  Опрос подсистемы охлаждения анода")
                    gui.report_box.update()
                    gui.poa_button.config(background="deep sky blue")
                    gui.poa_button.update()
                    request_and_port_list.com_port_settings["baudrate"] = 115200
                    answer = request_response.command_sender(accepted_request=request)

                    if answer:
                        gui.report_box.delete(0, END)
                        gui.report_box.insert(END, "                             "
                                                   "⮜⮜⮜ ПОДКЛЮЧЕНО К ПОДСИСТЕМЕ ОХЛАЖДЕНИЯ АНОДА ⮞⮞⮞")
                        gui.poa_button.config(background="SeaGreen1")
                        gui.poa_button.update()
                        if_answer(answer, request_name)
                        cooling_system_unit.poa(gui, auto=True)
                        return answer
                    else:
                        gui.report_box.insert(END, " -  Ответ отсутствует")
                        gui.poa_button.config(background="gray60")
                        gui.poa_button.update()

                elif request_name == "sth_1_request":
                    gui.report_box.insert(END, " -  Опрос датчика температуры/влажности №1")
                    gui.sth1_button.config(background="deep sky blue")
                    gui.sth1_button.update()
                    request_and_port_list.com_port_settings["baudrate"] = 115200
                    answer = request_response.command_sender(accepted_request=request)
                    if answer:
                        gui.report_box.delete(0, END)
                        gui.report_box.insert(END, "                                   "
                                                   "⮜⮜⮜ ПОДКЛЮЧЕНО К ДАТЧИКУ ТЕМПЕРАТУРЫ/ВЛАЖНОСТИ №1 ⮞⮞⮞")
                        gui.sth1_button.config(background="SeaGreen1")
                        gui.sth1_button.update()
                        if_answer(answer, request_name)
                        temperature_humidity_unit.sth(gui, sensor=1, auto=True)
                        return answer
                    else:
                        gui.report_box.insert(END, " -  Ответ отсутствует")
                        gui.sth1_button.config(background="gray60")
                        gui.sth1_button.update()

                elif request_name == "sth_2_request":
                    gui.report_box.insert(END, " -  Опрос датчика температуры/влажности №2")
                    gui.sth2_button.config(background="deep sky blue")
                    gui.sth2_button.update()
                    request_and_port_list.com_port_settings["baudrate"] = 115200
                    answer = request_response.command_sender(accepted_request=request)
                    if answer:
                        gui.report_box.delete(0, END)
                        gui.report_box.insert(END, "                                   "
                                                   "⮜⮜⮜ ПОДКЛЮЧЕНО К ДАТЧИКУ ТЕМПЕРАТУРЫ/ВЛАЖНОСТИ №2 ⮞⮞⮞")
                        gui.sth2_button.config(background="SeaGreen1")
                        gui.sth2_button.update()
                        if_answer(answer, request_name)
                        temperature_humidity_unit.sth(gui, sensor=2, auto=True)
                        return answer
                    else:
                        gui.report_box.insert(END, " -  Ответ отсутствует")
                        gui.sth2_button.config(background="gray60")
                        gui.sth2_button.update()

                elif request_name == "sth_3_request":
                    gui.report_box.insert(END, " -  Опрос датчика температуры/влажности №3")
                    gui.sth3_button.config(background="deep sky blue")
                    gui.sth3_button.update()
                    request_and_port_list.com_port_settings["baudrate"] = 115200
                    answer = request_response.command_sender(accepted_request=request)
                    if answer:
                        gui.report_box.delete(0, END)
                        gui.report_box.insert(END, "                                   "
                                                   "⮜⮜⮜ ПОДКЛЮЧЕНО К ДАТЧИКУ ТЕМПЕРАТУРЫ/ВЛАЖНОСТИ №3 ⮞⮞⮞")
                        gui.sth3_button.config(background="SeaGreen1")
                        gui.sth3_button.update()
                        if_answer(answer, request_name)
                        temperature_humidity_unit.sth(gui, sensor=3, auto=True)
                        return answer
                    else:
                        gui.report_box.insert(END, " -  Ответ отсутствует")
                        gui.sth3_button.config(background="gray60")
                        gui.sth3_button.update()

                elif request_name == "as_request":
                    gui.report_box.insert(END, " -  Опрос автоматического сменщика образца")
                    gui.as_button.config(background="deep sky blue")
                    gui.as_button.update()
                    request_and_port_list.com_port_settings["baudrate"] = 1000000
                    answer = request_response.command_sender(accepted_request=request)
                    if answer:
                        gui.report_box.delete(0, END)
                        gui.report_box.insert(END, "                                   "
                                                   "⮜⮜⮜ ПОДКЛЮЧЕНО К АВТОМАТИЧЕСКОМУ СМЕНЩИКУ ОБРАЗЦОВ ⮞⮞⮞")
                        gui.as_button.config(background="SeaGreen1")
                        gui.as_button.update()
                        if_answer(answer, request_name)
                        auto_sampler_unit.aus(gui)
                        return answer
                    else:
                        gui.report_box.insert(END, " -  Ответ отсутствует")
                        gui.as_button.config(background="gray60")
                        gui.as_button.update()

                elif request_name == "sc_request":
                    gui.report_box.insert(END, " -  Опрос вращателя образца")
                    gui.sc_button.config(background="deep sky blue")
                    gui.sc_button.update()
                    request_and_port_list.com_port_settings["baudrate"] = 1000000
                    answer = request_response.command_sender(accepted_request=request)
                    if answer:
                        gui.report_box.delete(0, END)
                        gui.report_box.insert(END, "                                   "
                                                   "⮜⮜⮜ ПОДКЛЮЧЕНО К ВРАЩАТЕЛЮ ОБРАЗЦА ⮞⮞⮞")
                        gui.sc_button.config(background="SeaGreen1")
                        gui.sc_button.update()
                        if_answer(answer, request_name)
                        sample_changer_unit.sc(gui)
                        return answer
                    else:
                        gui.report_box.insert(END, " -  Ответ отсутствует")
                        gui.sc_button.config(background="gray60")
                        gui.sc_button.update()

                elif request_name == "ck_request":
                    gui.report_box.insert(END, " -  Опрос автоматического коллиматора-ножа")
                    gui.ck_button.config(background="deep sky blue")
                    gui.ck_button.update()
                    request_and_port_list.com_port_settings["baudrate"] = 500000
                    answer = request_response.command_sender(accepted_request=request)
                    if answer:
                        gui.report_box.delete(0, END)
                        gui.report_box.insert(END, "                                   "
                                                   "⮜⮜⮜ ПОДКЛЮЧЕНО К АВТОМАТИЧЕСКОМУ КОЛЛИМАТОРУ-НОЖУ ⮞⮞⮞")
                        gui.ck_button.config(background="SeaGreen1")
                        gui.ck_button.update()
                        if_answer(answer, request_name)
                        knife_unit.knife(gui)
                        return answer
                    else:
                        gui.report_box.insert(END, " -  Ответ отсутствует")
                        gui.ck_button.config(background="gray60")
                        gui.ck_button.update()

                elif request_name == "vs_request":
                    gui.report_box.insert(END, " -  Опрос автоматизированной варьируемой щели")
                    gui.vs_button.config(background="deep sky blue")
                    gui.vs_button.update()
                    request_and_port_list.com_port_settings["baudrate"] = 115200
                    answer = request_response.command_sender(accepted_request=request)
                    if answer:
                        gui.report_box.delete(0, END)
                        gui.report_box.insert(END, "                                   "
                                                   "⮜⮜⮜ ПОДКЛЮЧЕНО К АВТОМАТИЗИРОВАННОЙ ВАРЬИРУЕМОЙ ЩЕЛИ ⮞⮞⮞")
                        gui.vs_button.config(background="SeaGreen1")
                        gui.vs_button.update()
                        if_answer(answer, request_name)
                        variable_slit_unit.vs(gui)
                        return answer
                    else:
                        gui.report_box.insert(END, " -  Ответ отсутствует")
                        gui.vs_button.config(background="gray60")
                        gui.vs_button.update()

    if gui.again_button:
        gui.again_button.destroy()

    gui.progress_label = Label(gui.frame_for_progress_bar, text="Поиск доступных COM-портов:", fg="white", bg="gray10")
    gui.progress_label.pack(side=TOP, fill=X)

    gui.process_progressbar = ttk.Progressbar(gui.frame_for_progress_bar, orient="horizontal")
    gui.process_progressbar.pack(side=TOP, fill=X)

    # Проверяет доступные порты и создаёт из них список
    open_ports = []
    found = False
    for com_counter in range(1, 51):
        step = " -  Проверяю COM-порт: " + str(com_counter)
        update_info(com_counter, step)
        try:
            port = "COM" + str(com_counter)
            ser = serial.Serial(port)
            ser.close()
            step = " -  Ответ от COM-порта: " + str(port) + " получен"
            update_info(com_counter, step)
            open_ports.append(port)
            found = True
        except serial.serialutil.SerialException:
            pass

    if not found:
        step = "Доступных COM-портов не обнаружено"
        update_info(0, step)
        return []

    # Обновляю поле отчёта о поиске портов
    gui.report_box.delete(0, END)
    gui.report_box.insert(END, "                                   ⮜⮜⮜ ОТРИСОВЫВАЮ ИНТЕРФЕЙС ПОРТОВ ⮞⮞⮞")
    gui.report_box.update()
    gui.report_box.yview(END)

    for widget in gui.frame_for_progress_bar.winfo_children():
        widget.destroy()

    device_answer = find_device()
    no_signature(gui, device_answer)


def no_signature(gui, device_answer):

    # Исключение - ничего не нашло
    if not device_answer:

        for widget in gui.frame_for_progress_bar.winfo_children():
            widget.destroy()

        gui.bytesize_combobox.set("")
        gui.timeout_combobox.set("")
        gui.baudrate_combobox.set("")
        gui.port_combobox.set("")

        gui.report_box.delete(0, END)
        gui.report_box.insert(END, "                                          "
                                   "⮜⮜⮜ ДОСТУПНЫХ УСТРОЙСТВ НЕ НАЙДЕНО ⮞⮞⮞")
        gui.report_box.insert(END, " -  Проверьте подключение устройства и нажмите кнопку ⮜Повторный поиск устройства⮞"
                                   " на нижней панели ")
        gui.report_box.insert(END, " -  Либо перейдите в ⮜Ручной⮞ режим")
        gui.report_box.update()
        gui.box_for_com_ports.delete('1.0', END)
        gui.box_for_com_ports.update()

        gui.again_button = Button(gui.frame_for_progress_bar, text="Повторный поиск устройства", relief=GROOVE,
                                  width=40, height=2, bg="firebrick4", foreground="white",
                                  command=lambda: com_ports(gui))
        gui.again_button.pack(side=TOP, padx=40, pady=3)
