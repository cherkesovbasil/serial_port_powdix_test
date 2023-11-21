from tkinter import *
from tkinter import ttk
import serial
import time
import request_response
import request_and_port_list


class Gui:
    """Графический интерфейс"""

    def __init__(self):
        self.restart_button = None
        self.frame_for_find_device = None
        self.device_signature = None
        self.status_text_box = None
        self.text = None
        self.label = None
        self.start_window = None
        self.manual_button = None
        self.full_auto_init_window = None
        self.full_auto_button = None

    def run_manual(self):
        self.manual_button['state'] = DISABLED
        self.full_auto_button['state'] = DISABLED

        return

    def run_full_auto(self):
        """Запускает стартовое окно с запросом на генерацию баз данных"""
        self.manual_button['state'] = DISABLED
        self.full_auto_button['state'] = DISABLED

        def on_closing():
            self.full_auto_init_window.destroy()
            self.full_auto_button['state'] = NORMAL
            self.manual_button['state'] = NORMAL

        def com_ports():

            def update_info(port_number, message):

                # Обновляю поле отчёта о поиске портов
                self.status_text_box.insert(END, message)
                self.status_text_box.update()
                self.status_text_box.yview(END)

                # обновляю шкалу загрузки
                process_progressbar["value"] = port_number * 2
                process_progressbar.update()

            # noinspection PyGlobalUndefined
            def find_device():
                global answer

                self.frame_for_find_device = LabelFrame(self.full_auto_init_window)
                self.frame_for_find_device.pack(side=BOTTOM, fill=X)

                frame_for_comport = LabelFrame(self.frame_for_find_device, background="SeaGreen1")
                frame_for_comport.pack(side=LEFT)

                frame_for_requests = LabelFrame(self.frame_for_find_device)
                frame_for_requests.pack(side=RIGHT)

                com_port_label = Label(frame_for_comport, text="COM1", background="SeaGreen1")
                com_port_label.pack(side=LEFT, fill=X, padx=27)

                poa_label = Label(frame_for_requests, text="подсистема охлаждения", relief=GROOVE,
                                  background="gray90")
                poa_label.pack(side=TOP, fill=X, padx=10)

                sth1_label = Label(frame_for_requests, text="датчик температуры-влажности 1", relief=GROOVE,
                                   background="gray90")
                sth1_label.pack(side=TOP, fill=X, padx=10)

                sth2_label = Label(frame_for_requests, text="датчик температуры-влажности 2", relief=GROOVE,
                                   background="gray90")
                sth2_label.pack(side=TOP, fill=X, padx=10)

                sth3_label = Label(frame_for_requests, text="датчик температуры-влажности 3", relief=GROOVE,
                                   background="gray90")
                sth3_label.pack(side=TOP, fill=X, padx=10)

                sc_label = Label(frame_for_requests, text="автосменщик образцов/вращатель", relief=GROOVE,
                                 background="gray90")
                sc_label.pack(side=TOP, fill=X, padx=10)

                ck_label = Label(frame_for_requests, text="автоматический коллиматор-нож", relief=GROOVE,
                                 background="gray90")
                ck_label.pack(side=TOP, fill=X, padx=10)

                frame_for_status_full_auto.update()

                answer = None
                for extracted_port in open_ports:
                    if answer:
                        break


                    com_port_label.config(text="...........")
                    com_port_label.update()
                    time.sleep(0.1)
                    com_port_label.config(text=extracted_port)
                    com_port_label.update()
                    for request_name, request in request_and_port_list.identification_dictionary.items():

                        if request_name == "poa_request":
                            poa_label.config(background="deep sky blue")
                            poa_label.update()
                            answer = request_response.poa_version(comport=extracted_port,
                                                                  accepted_request=request)
                            if answer:
                                poa_label.config(background="SeaGreen1")
                                poa_label.update()
                                answer = request_name
                                return answer
                            else:
                                poa_label.config(background="gray90")
                                poa_label.update()

                        elif request_name == "sth_1_request":
                            sth1_label.config(background="deep sky blue")
                            sth1_label.update()
                            answer = request_response.poa_version(comport=extracted_port,
                                                                  accepted_request=request)
                            if answer:
                                sth1_label.config(background="SeaGreen1")
                                sth1_label.update()
                                answer = request_name
                                return answer
                            else:
                                sth1_label.config(background="gray90")
                                sth1_label.update()

                        elif request_name == "sth_2_request":
                            sth2_label.config(background="deep sky blue")
                            sth2_label.update()
                            answer = request_response.poa_version(comport=extracted_port,
                                                                  accepted_request=request)
                            if answer:
                                sth2_label.config(background="SeaGreen1")
                                sth2_label.update()
                                answer = request_name
                                return answer
                            else:
                                sth2_label.config(background="gray90")
                                sth2_label.update()

                        elif request_name == "sth_3_request":
                            sth3_label.config(background="deep sky blue")
                            sth3_label.update()
                            answer = request_response.poa_version(comport=extracted_port,
                                                                  accepted_request=request)
                            if answer:
                                sth3_label.config(background="SeaGreen1")
                                sth3_label.update()
                                answer = request_name
                                return answer
                            else:
                                sth3_label.config(background="gray90")
                                sth3_label.update()

                        elif request_name == "sc_request":
                            sc_label.config(background="deep sky blue")
                            sc_label.update()
                            answer = request_response.poa_version(comport=extracted_port,
                                                                  accepted_request=request)
                            if answer:
                                sc_label.config(background="SeaGreen1")
                                sc_label.update()
                                answer = request_name
                                return answer
                            else:
                                sc_label.config(background="gray90")
                                sc_label.update()

            open_ports = []
            found = False
            for com_counter in range(1, 51):
                step = "Checking COM-Port: " + str(com_counter)
                update_info(com_counter, step)
                try:
                    port = "COM" + str(com_counter)
                    ser = serial.Serial(port)
                    ser.close()
                    step = "Found the serial port: " + str(port)
                    update_info(com_counter, step)
                    open_ports.append(port)
                    found = True
                except serial.serialutil.SerialException:
                    pass

            if not found:
                step = "No serial ports detected"
                update_info(0, step)
                return []

            device_answer = find_device()

            return device_answer

        self.full_auto_init_window = Tk()
        self.full_auto_init_window.title("Searching for available ports")
        # команда при закрытии окна
        self.full_auto_init_window.protocol("WM_DELETE_WINDOW", on_closing)

        # disables the ability to zoom the page
        self.full_auto_init_window.resizable(False, False)

        # frame for the interface
        frame_for_status_full_auto = LabelFrame(self.full_auto_init_window)
        frame_for_status_full_auto.pack(side=TOP)

        progress_label = Label(frame_for_status_full_auto, text="Progress (checking ports):")
        progress_label.pack(side=TOP, fill=X, padx=10)

        process_progressbar = ttk.Progressbar(frame_for_status_full_auto, orient="horizontal")
        process_progressbar.pack(side=TOP, fill=X, padx=10)

        # outputs the information about the absolute error in the GUI
        self.status_text_box = Listbox(frame_for_status_full_auto, relief=GROOVE, width=50, height=4,
                                       selectbackground="grey60")
        self.status_text_box.pack(side=TOP, padx=10, pady=10)

        # sets the size of the window and places it in the center of the screen
        self.full_auto_init_window.update_idletasks()  # Updates information after all frames are created
        s = self.full_auto_init_window.geometry()
        s = s.split('+')
        s = s[0].split('x')
        width_window = int(s[0])
        height_window = int(s[1])

        w = self.full_auto_init_window.winfo_screenwidth()
        h = self.full_auto_init_window.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - width_window // 2 + 400
        h = h - height_window // 2
        self.full_auto_init_window.geometry('+{}+{}'.format(w, h))

        self.device_signature = com_ports()

        def start():
            self.status_text_box.delete(0, END)
            self.restart_button.destroy()
            self.frame_for_find_device.destroy()
            self.device_signature = com_ports()
            no_signature()
            return

        def no_signature():
            if not self.device_signature:
                self.status_text_box.delete(0, END)
                self.status_text_box.insert(END, "Не удаётся найти устройство. Проверьте")
                self.status_text_box.insert(END, "правильность подключения устройства и")
                self.status_text_box.insert(END, "перезапустите поиск")
                self.status_text_box.update()
                self.restart_button = Button(frame_for_status_full_auto, text="RESTART PROCESS", relief=GROOVE,
                                             background="brown1", command=start)
                self.restart_button.pack(side=TOP, fill=X)

        no_signature()

        return self.device_signature
    # ВОЗВРАЩАЕТ СИГНАТУРУ В ФОРМАТЕ "poa_request"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def init_start_window(self):
        """Запускает первичное окно с возможностью первичного просмотра баз данных, добавления, удаления, открытия"""

        self.start_window = Tk()
        self.start_window.title("Adjustment utility")

        # disables the ability to zoom the page
        self.start_window.minsize(40, 100)
        self.start_window.resizable(False, False)

        # frame for the main interface
        frame_for_buttons_start_window = LabelFrame(self.start_window, bg="grey90")
        frame_for_buttons_start_window.pack(side=LEFT, padx=1, pady=1)

        # outputs the information about the absolute error in the GUI
        self.manual_button = Button(frame_for_buttons_start_window, text="Manual", relief=GROOVE, width=20, height=2,
                                    bg="gray60", command=self.run_manual)
        self.manual_button.pack(side=LEFT, padx=10, pady=10)
        self.full_auto_button = Button(frame_for_buttons_start_window, text="Full-Auto", relief=GROOVE, width=20,
                                       height=2, bg="SeaGreen1", command=self.run_full_auto)
        self.full_auto_button.pack(side=LEFT, padx=10, pady=10)

        # sets the size of the window and places it in the center of the screen
        self.start_window.update_idletasks()  # Updates information after all frames are created
        s = self.start_window.geometry()
        s = s.split('+')
        s = s[0].split('x')
        width_main_window = int(s[0])
        height_main_window = int(s[1])

        w = self.start_window.winfo_screenwidth()
        h = self.start_window.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - width_main_window // 2
        h = h - height_main_window // 2
        self.start_window.geometry('+{}+{}'.format(w, h))

        self.start_window.mainloop()


init_check = Gui()
init_check.init_start_window()
