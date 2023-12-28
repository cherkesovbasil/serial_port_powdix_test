import tkinter.font
from tkinter import *
from tkinter import ttk

import request_and_port_list
import request_response


class AdjustmentUtility:
    """Главное окно взаимодействия с девайсами"""

    def __init__(self):
        self.frame_for_full_terminal = None
        self.terminal_open = False

        self.terminal_button = None
        self.frame_for_terminal = None
        self.info_text_box = None

        self.timeout_combobox = None
        self.baudrate_combobox = None
        self.port_combobox = None
        self.bytesize_combobox = None

        self.auto_button = None
        self.sth1_button = None
        self.sth2_button = None
        self.sth3_button = None
        self.as_button = None
        self.sc_button = None
        self.ck_button = None
        self.refind_button = None
        self.set_button = None
        self.poa_button = None
        self.manual_button = None

        self.start_window = None
        self.frame_for_units = None

    def poa_unit(self):

        def all_grey():
            # Верхние поля отображения статусов
            stat_ctrl_label.config(text="-", bg="gray90")
            stat_sens_label.config(text="-", bg="gray90")
            stat_ctrl_data.config(text="-", bg="gray90")
            stat_sens_label.config(text="-", bg="gray90")

            # Status sensors - all grey
            wts1_bit.config(text="-", bg="gray90")
            wts1_label.config(bg="gray90")
            wts2_bit.config(text="-", bg="gray90")
            wts2_label.config(bg="gray90")
            svs_bit.config(text="-", bg="gray90")
            svs_label.config(bg="gray90")
            key_bit.config(text="-", bg="gray90")
            key_label.config(bg="gray90")
            wls_bit.config(text="-", bg="gray90")
            wls_label.config(bg="gray90")
            reserve_1_bit.config(text="-", bg="gray90")
            reserve_1_label.config(bg="gray90")
            reserve_2_bit.config(text="-", bg="gray90")
            reserve_2_label.config(bg="gray90")
            reserve_3_bit.config(text="-", bg="gray90")
            reserve_3_label.config(bg="gray90")

            # Status control - all grey
            rfp_bit.config(text="-", bg="gray90")
            rfp_label.config(bg="gray90")
            wpp_bit.config(text="-", bg="gray90")
            wpp_label.config(bg="gray90")
            acf_bit.config(text="-", bg="gray90")
            acf_label.config(bg="gray90")
            srs_bit.config(text="-", bg="gray90")
            srs_label.config(bg="gray90")
            beeper_bit.config(text="-", bg="gray90")
            beeper_label.config(bg="gray90")
            rfe_bit.config(text="-", bg="gray90")
            rfe_label.config(bg="gray90")
            reserve_4_bit.config(text="-", bg="gray90")
            reserve_4_label.config(bg="gray90")
            reserve_5_bit.config(text="-", bg="gray90")
            reserve_5_label.config(bg="gray90")

        def transcript_other_stuff(recieved_command=None, send_command=None):

            # Превращает из хексов в бины всю остальную команду

            # расшифровка поля Device
            def transcript_status_device():
                device_hex = recieved_command[0] + recieved_command[1]
                if device_hex == "40":
                    device_label.config(text="OK", bg="PaleGreen3")
                else:
                    device_label.config(text="❌", bg="salmon")
                device_data.config(text=device_hex.upper())

            # расшифровка поля t_max
            def transcript_status_t_max():
                t_max_hex = recieved_command[6] + recieved_command[7]
                t_max_dec = int(t_max_hex, 16)
                if 10 <= t_max_dec <= 40:
                    t_max_label.config(bg="PaleGreen3")
                else:
                    t_max_label.config(bg="salmon")
                t_max_label.config(text=str(t_max_dec).upper())
                t_max_data.config(text=t_max_hex)

            # расшифровка поля t_min
            def transcript_status_t_min():
                t_min_hex = recieved_command[8] + recieved_command[9]
                t_min_dec = int(t_min_hex, 16)
                if 10 <= t_min_dec <= 40:
                    t_min_label.config(bg="PaleGreen3")
                else:
                    t_min_label.config(bg="salmon")
                t_min_label.config(text=str(t_min_dec).upper())
                t_min_data.config(text=t_min_hex)

            # расшифровка поля flow
            def transcript_status_flow():
                flow_hex = recieved_command[10] + recieved_command[11]
                flow_dec = int(flow_hex, 16)
                flow_real = round(float(flow_dec/73), 2)
                if 2.5 <= flow_real <= 5:
                    flow_label.config(bg="PaleGreen3")
                else:
                    flow_label.config(bg="salmon")
                flow_label.config(text=str(flow_real))
                flow_data.config(text=flow_hex)

            # расшифровка поля errors
            def transcript_status_errors():
                errors_hex = recieved_command[12] + recieved_command[13]
                if errors_hex == "00":
                    errors_label.config(bg="PaleGreen3", text="OK")
                else:
                    errors_label.config(bg="salmon", text=errors_hex)
                errors_data.config(text=errors_hex)

            # расшифровка полей pwm
            def transcript_status_pwm_1_2():
                pwm_1_hex = recieved_command[14] + recieved_command[15]
                pwm_2_hex = recieved_command[16] + recieved_command[17]
                pwm_1_dec = int(pwm_1_hex, 16)
                pwm_2_dec = int(pwm_2_hex, 16)
                pwm_1_percent = int(pwm_1_dec * 100 / 254)
                pwm_2_percent = int(pwm_2_dec * 100 / 254)
                if pwm_1_percent + pwm_2_percent == 100:
                    pwm_1_label.config(bg="PaleGreen3", text=pwm_1_percent)
                    pwm_2_label.config(bg="PaleGreen3", text=pwm_2_percent)
                else:
                    pwm_1_label.config(bg="salmon", text=pwm_1_percent)
                    pwm_2_label.config(bg="salmon", text=pwm_2_percent)
                pwm_1_data.config(text=pwm_1_hex)
                pwm_2_data.config(text=pwm_2_hex)

            def check_crc():
                full_hex_summ = 0
                for bit in range(0, 17):
                    if bit != 0:
                        print("recieved_command[bit] = " + recieved_command[bit])
                        dec_command_bit = int(recieved_command[bit], 16)
                        print(dec_command_bit)
                        full_hex_summ = full_hex_summ + dec_command_bit
                print(full_hex_summ)
                full_hex_summ = hex(full_hex_summ)
                print(full_hex_summ)
                #
                #
                # Не дописано, вроде похоже на правду, что при сложении в децимале получается круглое число, но хз. чекнуть
                #
                #


            transcript_status_device()
            transcript_status_t_max()
            transcript_status_t_min()
            transcript_status_flow()
            transcript_status_errors()
            transcript_status_pwm_1_2()
            check_crc()
            pass

        def transcript_statuses(recieved_command=None, send_command=None):
            if recieved_command:
                all_grey()

                # Превращает из хексов в бины и выводит значения
                status_ctrl_hex = recieved_command[2] + recieved_command[3]
                binary_status_ctrl = "{0:08b}".format(int(status_ctrl_hex, 16))
                print(binary_status_ctrl)
                stat_ctrl_data.config(text=status_ctrl_hex.upper(), bg="gray90")

                # Превращает из хексов в бины и выводит значения
                status_sens_hex = recieved_command[4] + recieved_command[5]
                binary_status_sens = "{0:08b}".format(int(status_sens_hex, 16))
                print(binary_status_sens)
                stat_sens_data.config(text=status_sens_hex.upper(), bg="gray90")

                # Расшифровки и отображение Статуса сенсоров
                red_green_status_sens = "green"
                red_green_status_ctrl = "green"

                for bit_number in range(0, 8):
                    if bit_number == 0:
                        if int(binary_status_sens[bit_number]) == 0:
                            reserve_3_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            reserve_3_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"

                    if bit_number == 1:
                        if int(binary_status_sens[bit_number]) == 0:
                            reserve_2_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            reserve_2_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"

                    if bit_number == 2:
                        if int(binary_status_sens[bit_number]) == 0:
                            reserve_1_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            reserve_1_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"

                    if bit_number == 3:
                        if int(binary_status_sens[bit_number]) == 0:
                            wls_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            wls_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"
                            wls_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                            wls_label.config(bg="salmon")

                    if bit_number == 4:
                        if int(binary_status_sens[bit_number]) == 1:
                            if send_command == request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                                key_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                                key_label.config(bg="salmon")
                                if red_green_status_sens == "green":
                                    red_green_status_sens = "red"
                            else:
                                key_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                                key_label.config(bg="PaleGreen3")
                        else:
                            if send_command == request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                                key_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                                key_label.config(bg="PaleGreen3")
                            else:
                                key_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                                key_label.config(bg="salmon")
                                if red_green_status_sens == "green":
                                    red_green_status_sens = "red"

                    if bit_number == 5:
                        if int(binary_status_sens[bit_number]) == 0:
                            svs_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            svs_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"
                            svs_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                            svs_label.config(bg="salmon")

                    if bit_number == 6:
                        if int(binary_status_sens[bit_number]) == 0:
                            wts2_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            wts2_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"
                            wts2_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                            wts2_label.config(bg="salmon")

                    if bit_number == 7:
                        if int(binary_status_sens[bit_number]) == 0:
                            wts1_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            wts1_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"
                            wts1_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                            wts1_label.config(bg="salmon")
                            pass

                    if red_green_status_sens == "green":
                        stat_sens_label.config(text="OK", bg="PaleGreen3")
                    else:
                        stat_sens_label.config(text="❌", bg="salmon")

                #
                # Раскидка битов и статусов по Статус контроль
                #

                for bit_number in range(0, 8):
                    if bit_number == 0:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            reserve_5_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            reserve_5_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"

                    if bit_number == 1:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            reserve_4_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            reserve_4_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"

                    if bit_number == 2:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            rfe_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                            rfe_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            rfe_label.config(bg="salmon")

                    if bit_number == 3:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            beeper_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            beeper_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                            beeper_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            beeper_label.config(bg="salmon")

                    if bit_number == 4:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            srs_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                            srs_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            srs_label.config(bg="salmon")

                    if bit_number == 5:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            acf_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            acf_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                            acf_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            acf_label.config(bg="salmon")

                    if bit_number == 6:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            wpp_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                            wpp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            wpp_label.config(bg="salmon")

                    if bit_number == 7:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            rfp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            rfp_label.config(bg="PaleGreen3")
                        else:
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                            rfp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            rfp_label.config(bg="salmon")
                            pass

                    if red_green_status_ctrl == "green":
                        stat_ctrl_label.config(text="OK", bg="PaleGreen3")
                    else:
                        stat_ctrl_label.config(text="❌", bg="salmon")

                pass

        def poa_start_command():
            request_response.command_sender(accepted_request=
                                            request_and_port_list.poa_request_dictionary["stop_poa_package"])
            answer = request_response.command_sender(accepted_request=
                                                     request_and_port_list.poa_request_dictionary["start_poa_package"])
            if answer:
                transcript_statuses(answer, request_and_port_list.poa_request_dictionary["start_poa_package"])
                transcript_other_stuff(answer, request_and_port_list.poa_request_dictionary["start_poa_package"])

        def poa_stop_command():
            answer = request_response.command_sender(accepted_request=
                                                     request_and_port_list.poa_request_dictionary["stop_poa_package"])
            if answer:
                transcript_statuses(answer, request_and_port_list.poa_request_dictionary["stop_poa_package"])
                transcript_other_stuff(answer, request_and_port_list.poa_request_dictionary["stop_poa_package"])

        def poa_version_command():
            request_response.command_sender(accepted_request=request_and_port_list.
                                            poa_request_dictionary["version_poa_package"])

        def poa_status_command():
            answer = request_response.command_sender(accepted_request=
                                                     request_and_port_list.
                                                     poa_request_dictionary["status_poa_package"])
            if answer:
                transcript_statuses(answer, request_and_port_list.poa_request_dictionary["status_poa_package"])
                transcript_other_stuff(answer, request_and_port_list.poa_request_dictionary["status_poa_package"])

        def poa_dry_command():
            request_response.command_sender(accepted_request=
                                            request_and_port_list.poa_request_dictionary["stop_poa_package"])
            answer = request_response.command_sender(accepted_request=
                                                     request_and_port_list.
                                                     poa_request_dictionary["dry_poa_package"])
            if answer:
                transcript_statuses(answer, request_and_port_list.poa_request_dictionary["dry_poa_package"])
                transcript_other_stuff(answer, request_and_port_list.poa_request_dictionary["dry_poa_package"])

        def poa_info_command():
            pass

        # Прописывает с нуля интерфейсный фрейм
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        # Изменяет состояние кнопок в окне
        self.poa_button.configure(bg="green3", state='disabled', relief=RIDGE)
        self.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.as_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)

        # Заполняет настройки серийного порта
        self.bytesize_combobox.set(request_and_port_list.com_port_settings["bytesize"])
        self.timeout_combobox.set(request_and_port_list.com_port_settings["timeout"])
        self.baudrate_combobox.set(request_and_port_list.com_port_settings["baudrate"])
        self.port_combobox.set(request_and_port_list.com_port_settings["comport"])

        #
        # Информационное поле полученной и расшифрованной команды
        #

        # Поле аналитического юнита
        frame_for_analytical_label = LabelFrame(self.frame_for_units, bg="gray80")
        frame_for_analytical_label.pack(side=TOP, padx=1, pady=1, fill=X)

        analytical_label = Label(frame_for_analytical_label, text="Analytical unit:", width=14, height=1, bg="gray80")
        analytical_label.pack(side=LEFT, padx=3, pady=1)

        # поле отображения наименования полученной информации
        frame_for_response_name = LabelFrame(self.frame_for_units, bg="gray95")
        frame_for_response_name.pack(side=TOP, padx=1, pady=1, fill=X)

        device_name = Label(frame_for_response_name, text="Device", width=8, height=1, bg="gray90", relief=SUNKEN)
        device_name.pack(side=LEFT, padx=3, pady=1)

        stat_ctrl_name = Label(frame_for_response_name, text="Status control", width=12, height=1, bg="gray90",
                               relief=SUNKEN)
        stat_ctrl_name.pack(side=LEFT, padx=3, pady=1)

        stat_sens_name = Label(frame_for_response_name, text="Status Sensors", width=12, height=1, bg="gray90",
                               relief=SUNKEN)
        stat_sens_name.pack(side=LEFT, padx=3, pady=1)

        t_max_name = Label(frame_for_response_name, text="t max", width=8, height=1, bg="gray90", relief=SUNKEN)
        t_max_name.pack(side=LEFT, padx=3, pady=1)

        t_min_name = Label(frame_for_response_name, text="t min", width=8, height=1, bg="gray90", relief=SUNKEN)
        t_min_name.pack(side=LEFT, padx=3, pady=1)

        flow_name = Label(frame_for_response_name, text="Flow", width=8, height=1, bg="gray90", relief=SUNKEN)
        flow_name.pack(side=LEFT, padx=3, pady=1)

        errors_name = Label(frame_for_response_name, text="Errors", width=8, height=1, bg="gray90", relief=SUNKEN)
        errors_name.pack(side=LEFT, padx=3, pady=1)

        pwm_1_name = Label(frame_for_response_name, text="PWM 2", width=8, height=1, bg="gray90", relief=SUNKEN)
        pwm_1_name.pack(side=LEFT, padx=3, pady=1)

        pwm_2_name = Label(frame_for_response_name, text="PWM 1", width=8, height=1, bg="gray90", relief=SUNKEN)
        pwm_2_name.pack(side=LEFT, padx=3, pady=1)

        crc_name = Label(frame_for_response_name, text="CRC", width=8, height=1, bg="gray90", relief=SUNKEN)
        crc_name.pack(side=LEFT, padx=3, pady=1)

        # поле отображения обработанной информации
        frame_for_response_data = LabelFrame(self.frame_for_units, bg="gray95")
        frame_for_response_data.pack(side=TOP, padx=1, pady=1, fill=X)

        device_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
        device_label.pack(side=LEFT, padx=3, pady=1)

        stat_ctrl_label = Label(frame_for_response_data, text="--", width=12, height=2, bg="gray95", relief=SUNKEN)
        stat_ctrl_label.pack(side=LEFT, padx=3, pady=1)

        stat_sens_label = Label(frame_for_response_data, text="--", width=12, height=2, bg="gray95", relief=SUNKEN)
        stat_sens_label.pack(side=LEFT, padx=3, pady=1)

        t_max_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
        t_max_label.pack(side=LEFT, padx=3, pady=1)

        t_min_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
        t_min_label.pack(side=LEFT, padx=3, pady=1)

        flow_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
        flow_label.pack(side=LEFT, padx=3, pady=1)

        errors_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
        errors_label.pack(side=LEFT, padx=3, pady=1)

        pwm_1_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
        pwm_1_label.pack(side=LEFT, padx=3, pady=1)

        pwm_2_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
        pwm_2_label.pack(side=LEFT, padx=3, pady=1)

        crc_label = Label(frame_for_response_data, text="--", width=8, height=2, bg="gray95", relief=SUNKEN)
        crc_label.pack(side=LEFT, padx=3, pady=1)

        # поле отображения первичной информации
        frame_for_response_clear_data = LabelFrame(self.frame_for_units, bg="gray95")
        frame_for_response_clear_data.pack(side=TOP, padx=1, pady=1, fill=X)

        device_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
        device_data.pack(side=LEFT, padx=3, pady=1)

        stat_ctrl_data = Label(frame_for_response_clear_data, text="--", width=12, height=1, bg="gray90", relief=SUNKEN)
        stat_ctrl_data.pack(side=LEFT, padx=3, pady=1)

        stat_sens_data = Label(frame_for_response_clear_data, text="--", width=12, height=1, bg="gray90", relief=SUNKEN)
        stat_sens_data.pack(side=LEFT, padx=3, pady=1)

        t_max_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
        t_max_data.pack(side=LEFT, padx=3, pady=1)

        t_min_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
        t_min_data.pack(side=LEFT, padx=3, pady=1)

        flow_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
        flow_data.pack(side=LEFT, padx=3, pady=1)

        errors_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
        errors_data.pack(side=LEFT, padx=3, pady=1)

        pwm_1_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
        pwm_1_data.pack(side=LEFT, padx=3, pady=1)

        pwm_2_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
        pwm_2_data.pack(side=LEFT, padx=3, pady=1)

        crc_data = Label(frame_for_response_clear_data, text="--", width=8, height=1, bg="gray90", relief=SUNKEN)
        crc_data.pack(side=LEFT, padx=3, pady=1)

        # фреймы для расшифровки статусов
        frame_for_statuses = LabelFrame(self.frame_for_units, bg="gray95")
        frame_for_statuses.pack(side=TOP, padx=1, pady=1, fill=X)

        frame_for_status_control = LabelFrame(frame_for_statuses, bg="gray95", text="Status Control transcription")
        frame_for_status_control.pack(side=LEFT, padx=6, pady=3, fill=X)

        frame_for_status_sensors = LabelFrame(frame_for_statuses, bg="gray95", text="Status Sensors transcription")
        frame_for_status_sensors.pack(side=LEFT, padx=6, pady=3, fill=X)

        #
        # поле отображения информации Status Control
        #

        # интерфейс расшифровки команды питания вентиляторов радиатора
        frame_for_rfp = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_rfp.pack(side=TOP, padx=1, pady=1, fill=X)

        rfp_bit = Label(frame_for_rfp, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        rfp_bit.pack(side=LEFT, padx=3, pady=1)

        rfp_label = Label(frame_for_rfp, text=" - Включение вентиляторов радиатора", width=40, height=1,
                          bg="gray95", relief=SUNKEN, anchor=W)
        rfp_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки команды питания помпы
        frame_for_wpp = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_wpp.pack(side=TOP, padx=1, pady=1, fill=X)

        wpp_bit = Label(frame_for_wpp, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        wpp_bit.pack(side=LEFT, padx=3, pady=1)

        wpp_label = Label(frame_for_wpp, text=" - Включение питания помпы", width=40, height=1, bg="gray95",
                          relief=SUNKEN, anchor=W)
        wpp_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки команды питания вентилятора воздушного охлаждения
        frame_for_acf = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_acf.pack(side=TOP, padx=1, pady=1, fill=X)

        acf_bit = Label(frame_for_acf, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        acf_bit.pack(side=LEFT, padx=3, pady=1)

        acf_label = Label(frame_for_acf, text=" - Включение вентилятора воздушного охлажд.", width=40, height=1,
                          bg="gray95", relief=SUNKEN, anchor=W)
        acf_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки команды включения петли безопасности
        frame_for_srs = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_srs.pack(side=TOP, padx=1, pady=1, fill=X)

        srs_bit = Label(frame_for_srs, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        srs_bit.pack(side=LEFT, padx=3, pady=1)

        srs_label = Label(frame_for_srs, text=" - Включение петли безопасности", width=40, height=1, bg="gray95",
                          relief=SUNKEN, anchor=W)
        srs_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки команды активации пищалки
        frame_for_beeper = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_beeper.pack(side=TOP, padx=1, pady=1, fill=X)

        beeper_bit = Label(frame_for_beeper, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        beeper_bit.pack(side=LEFT, padx=3, pady=1)

        beeper_label = Label(frame_for_beeper, text=" - Включение звукового сигнала", width=40, height=1, bg="gray95",
                             relief=SUNKEN, anchor=W)
        beeper_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки команды активации bRadiator_Fan_En
        frame_for_rfe = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_rfe.pack(side=TOP, padx=1, pady=1, fill=X)

        rfe_bit = Label(frame_for_rfe, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        rfe_bit.pack(side=LEFT, padx=3, pady=1)

        rfe_label = Label(frame_for_rfe, text=" - Включение bRadiator_Fan_En???", width=40, height=1, bg="gray95",
                          relief=SUNKEN, anchor=W)
        rfe_label.pack(side=LEFT, padx=3, pady=1)

        # резервный бит reserve_4
        frame_for_reserve_4 = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_reserve_4.pack(side=TOP, padx=1, pady=1, fill=X)

        reserve_4_bit = Label(frame_for_reserve_4, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        reserve_4_bit.pack(side=LEFT, padx=3, pady=1)

        reserve_4_label = Label(frame_for_reserve_4, text=" - Reserve", width=40, height=1, bg="gray95",
                                relief=SUNKEN, anchor=W)
        reserve_4_label.pack(side=LEFT, padx=3, pady=1)

        # резервный бит reserve_5
        frame_for_reserve_5 = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_reserve_5.pack(side=TOP, padx=1, pady=1, fill=X)

        reserve_5_bit = Label(frame_for_reserve_5, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        reserve_5_bit.pack(side=LEFT, padx=3, pady=1)

        reserve_5_label = Label(frame_for_reserve_5, text=" - Reserve", width=40, height=1, bg="gray95",
                                relief=SUNKEN, anchor=W)
        reserve_5_label.pack(side=LEFT, padx=3, pady=1)

        #
        # поле отображения информации Status Sensors
        #

        # интерфейс расшифровки статуса датчика температуры холодной воды
        frame_for_wts1 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_wts1.pack(side=TOP, padx=1, pady=1, fill=X)

        wts1_bit = Label(frame_for_wts1, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        wts1_bit.pack(side=LEFT, padx=3, pady=1)

        wts1_label = Label(frame_for_wts1, text=" - Наличие датчика температуры горячей воды", width=40, height=1,
                           bg="gray95", relief=SUNKEN, anchor=W)
        wts1_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки статуса датчика температуры холодной воды
        frame_for_wts2 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_wts2.pack(side=TOP, padx=1, pady=1, fill=X)

        wts2_bit = Label(frame_for_wts2, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        wts2_bit.pack(side=LEFT, padx=3, pady=1)

        wts2_label = Label(frame_for_wts2, text=" - Наличие датчика температуры холодной воды", width=40, height=1,
                           bg="gray95", relief=SUNKEN, anchor=W)
        wts2_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки статуса пароводяного клапана
        frame_for_svs = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_svs.pack(side=TOP, padx=1, pady=1, fill=X)

        svs_bit = Label(frame_for_svs, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        svs_bit.pack(side=LEFT, padx=3, pady=1)

        svs_label = Label(frame_for_svs, text=" - Сработка пароводяного клапана", width=40, height=1, bg="gray95",
                          relief=SUNKEN, anchor=W)
        svs_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки статуса ключа системы охлаждения
        frame_for_key = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_key.pack(side=TOP, padx=1, pady=1, fill=X)

        key_bit = Label(frame_for_key, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        key_bit.pack(side=LEFT, padx=3, pady=1)

        key_label = Label(frame_for_key, text=" - Ключ системы охлаждения (1 = Work / 0 = Dry)", width=40, height=1,
                          bg="gray95", relief=SUNKEN, anchor=W)
        key_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки статуса датчика уровня воды
        frame_for_wls = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_wls.pack(side=TOP, padx=1, pady=1, fill=X)

        wls_bit = Label(frame_for_wls, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        wls_bit.pack(side=LEFT, padx=3, pady=1)

        wls_label = Label(frame_for_wls, text=" - Сработка датчика уровня воды (поплавок)", width=40, height=1,
                          bg="gray95", relief=SUNKEN, anchor=W)
        wls_label.pack(side=LEFT, padx=3, pady=1)

        # резервный бит reserve_1
        frame_for_reserve_1 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_reserve_1.pack(side=TOP, padx=1, pady=1, fill=X)

        reserve_1_bit = Label(frame_for_reserve_1, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        reserve_1_bit.pack(side=LEFT, padx=3, pady=1)

        reserve_1_label = Label(frame_for_reserve_1, text=" - Reserve", width=40, height=1, bg="gray95",
                                relief=SUNKEN, anchor=W)
        reserve_1_label.pack(side=LEFT, padx=3, pady=1)

        # резервный бит reserve_2
        frame_for_reserve_2 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_reserve_2.pack(side=TOP, padx=1, pady=1, fill=X)

        reserve_2_bit = Label(frame_for_reserve_2, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        reserve_2_bit.pack(side=LEFT, padx=3, pady=1)

        reserve_2_label = Label(frame_for_reserve_2, text=" - Reserve", width=40, height=1, bg="gray95",
                                relief=SUNKEN, anchor=W)
        reserve_2_label.pack(side=LEFT, padx=3, pady=1)

        # резервный бит reserve_3
        frame_for_reserve_3 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_reserve_3.pack(side=TOP, padx=1, pady=1, fill=X)

        reserve_3_bit = Label(frame_for_reserve_3, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        reserve_3_bit.pack(side=LEFT, padx=3, pady=1)

        reserve_3_label = Label(frame_for_reserve_3, text=" - Reserve", width=40, height=1, bg="gray95",
                                relief=SUNKEN, anchor=W)
        reserve_3_label.pack(side=LEFT, padx=3, pady=1)

        #
        # Поле отображения командной части интерфейса
        #

        # Поле управляющего юнита
        frame_for_command_label = LabelFrame(self.frame_for_units, bg="gray80")
        frame_for_command_label.pack(side=TOP, padx=1, pady=1, fill=X)

        command_label = Label(frame_for_command_label, text="Command unit:", width=14, height=1, bg="gray80")
        command_label.pack(side=LEFT, padx=3, pady=1)

        # Поле мини-терминала
        info_text_box = Listbox(self.frame_for_units, relief=GROOVE, width=55, height=6,
                                selectbackground="grey60")
        info_text_box.pack(side=LEFT, padx=10, pady=10, fill=X)

        # Поле кнопок управления системой охлаждения

        frame_for_start_stop_buttons = LabelFrame(self.frame_for_units, bg="gray80")
        frame_for_start_stop_buttons.pack(side=RIGHT, padx=4, pady=1, fill=X)

        frame_for_version_status_buttons = LabelFrame(self.frame_for_units, bg="gray80")
        frame_for_version_status_buttons.pack(side=RIGHT, padx=4, pady=1, fill=X)

        frame_for_dry_info_buttons = LabelFrame(self.frame_for_units, bg="gray80")
        frame_for_dry_info_buttons.pack(side=RIGHT, padx=4, pady=1, fill=X)

        start_button = Button(frame_for_start_stop_buttons, text="Start", relief=GROOVE, width=14, height=2,
                              bg="gray60", command=poa_start_command)
        start_button.pack(side=TOP, pady=4, padx=4)

        stop_button = Button(frame_for_start_stop_buttons, text="Stop", relief=GROOVE, width=14, height=2,
                             bg="gray60", command=poa_stop_command)
        stop_button.pack(side=TOP, pady=4, padx=4)

        version_button = Button(frame_for_version_status_buttons, text="Version", relief=GROOVE, width=14, height=2,
                                bg="gray60", command=poa_version_command)
        version_button.pack(side=TOP, pady=4, padx=4)

        status_button = Button(frame_for_version_status_buttons, text="Status", relief=GROOVE, width=14, height=2,
                               bg="gray60", command=poa_status_command)
        status_button.pack(side=TOP, pady=4, padx=4)

        dry_button = Button(frame_for_dry_info_buttons, text="Dry", relief=GROOVE, width=14, height=2,
                            bg="gray60", command=poa_dry_command)
        dry_button.pack(side=TOP, pady=4, padx=4)

        info_button = Button(frame_for_dry_info_buttons, text="Info", relief=GROOVE, width=14, height=2,
                             bg="gray60", command=poa_info_command)
        info_button.pack(side=TOP, pady=4, padx=4)

    def sth1_unit(self):
        # Прописывает с нуля интерфейсный фрейм
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        # Изменяет состояние кнопок в окне
        self.poa_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth1_button.configure(bg="green3", state='disabled', relief=RIDGE)
        self.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.as_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)

    def sth2_unit(self):
        # Прописывает с нуля интерфейсный фрейм
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        # Изменяет состояние кнопок в окне
        self.poa_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth2_button.configure(bg="green3", state='disabled', relief=RIDGE)
        self.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.as_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)

    def sth3_unit(self):
        # Прописывает с нуля интерфейсный фрейм
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        # Изменяет состояние кнопок в окне
        self.poa_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth3_button.configure(bg="green3", state='disabled', relief=RIDGE)
        self.as_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)

    def as_unit(self):
        # Прописывает с нуля интерфейсный фрейм
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        # Изменяет состояние кнопок в окне
        self.poa_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.as_button.configure(bg="green3", state='disabled', relief=RIDGE)
        self.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)

    def sc_unit(self):
        # Прописывает с нуля интерфейсный фрейм
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        # Изменяет состояние кнопок в окне
        self.poa_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.as_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sc_button.configure(bg="green3", state='disabled', relief=RIDGE)
        self.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)

    def ck_unit(self):
        # Прописывает с нуля интерфейсный фрейм
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        # Изменяет состояние кнопок в окне
        self.poa_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.as_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.ck_button.configure(bg="green3", state='disabled', relief=RIDGE)

    def refind_device(self):
        pass

    def set_parameters(self):
        pass

    def manual_parameters(self):
        self.auto_button.configure(bg="gray60", state="normal", relief=GROOVE)
        self.manual_button.configure(bg="PaleGreen3", state="disabled", relief=RIDGE)
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)
        self.poa_button.configure(state='normal', relief=GROOVE)
        self.sth1_button.configure(state='normal', relief=GROOVE)
        self.sth2_button.configure(state='normal', relief=GROOVE)
        self.sth3_button.configure(state='normal', relief=GROOVE)
        self.as_button.configure(state='normal', relief=GROOVE)
        self.sc_button.configure(state='normal', relief=GROOVE)
        self.ck_button.configure(state='normal', relief=GROOVE)
        self.set_button.configure(state='normal', relief=GROOVE)
        self.timeout_combobox.configure(state='readonly')
        self.baudrate_combobox.configure(state='readonly')
        self.port_combobox.configure(state='readonly')
        self.bytesize_combobox.configure(state='readonly')

    def auto_parameters(self):
        if self.terminal_open:
            self.terminal()
        self.manual_button.configure(bg="gray60", state="normal", relief=GROOVE)
        self.auto_button.configure(bg="PaleGreen3", state="disabled", relief=RIDGE)
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)
        self.poa_button.configure(bg="gray60", state='disabled', relief=RIDGE)
        self.sth1_button.configure(bg="gray60", state='disabled', relief=RIDGE)
        self.sth2_button.configure(bg="gray60", state='disabled', relief=RIDGE)
        self.sth3_button.configure(bg="gray60", state='disabled', relief=RIDGE)
        self.as_button.configure(bg="gray60", state='disabled', relief=RIDGE)
        self.sc_button.configure(bg="gray60", state='disabled', relief=RIDGE)
        self.ck_button.configure(bg="gray60", state='disabled', relief=RIDGE)
        self.set_button.configure(bg="gray60", state='disabled', relief=RIDGE)
        self.timeout_combobox.configure(state='disabled')
        self.timeout_combobox.set('')
        self.baudrate_combobox.configure(state='disabled')
        self.baudrate_combobox.set('')
        self.port_combobox.configure(state='disabled')
        self.port_combobox.set('')
        self.bytesize_combobox.configure(state='disabled')
        self.bytesize_combobox.set('')

    def terminal(self):
        if self.terminal_open:
            self.terminal_button.configure(text="⮞\n⮞\n⮞\n\nT\nE\nR\nM\nI\nN\nA\nL\n\n⮞\n⮞\n⮞")
            self.frame_for_full_terminal.destroy()
        else:

            def clear_left_terminal():
                left_terminal_text_box.delete(0, END)
                left_terminal_text_box.update()
                pass

            def clear_right_terminal():
                right_terminal_text_box.delete(0, END)
                right_terminal_text_box.update()
                pass

            def bit_check_crc():
                pass

            def string_check_crc():
                pass

            def send_bit_command():
                left_terminal_text_box.insert(END, "40 15 74 1C 7E 00 00 68 ⮘ crc ok")
                left_terminal_text_box.update()
                left_terminal_text_box.yview(END)
                pass

            def send_string_command():
                pass

            self.terminal_button.configure(text="⮜\n⮜\n⮜\n\nT\nE\nR\nM\nI\nN\nA\nL\n\n⮜\n⮜\n⮜")

            # Фреймы основного интерфейса терминала
            self.frame_for_full_terminal = LabelFrame(self.frame_for_terminal, bg="gray90")
            self.frame_for_full_terminal.pack(side=RIGHT, padx=1, pady=1, fill=Y)

            frame_for_terminal_windows = LabelFrame(self.frame_for_full_terminal, bg="gray90")
            frame_for_terminal_windows.pack(side=TOP, padx=1, pady=1, fill=X)

            frame_for_left_window = LabelFrame(frame_for_terminal_windows, bg="gray90", text="Отправленная команда")
            frame_for_left_window.pack(side=LEFT, padx=1, pady=1, fill=X)

            frame_for_right_window = LabelFrame(frame_for_terminal_windows, bg="gray90", text="Полученная команда")
            frame_for_right_window.pack(side=RIGHT, padx=1, pady=1, fill=X)

            frame_for_per_byte_command = LabelFrame(self.frame_for_full_terminal, bg="gray90")
            frame_for_per_byte_command.pack(side=TOP, padx=1, pady=5, fill=X)

            frame_for_text_command = LabelFrame(self.frame_for_full_terminal, bg="gray90")
            frame_for_text_command.pack(side=TOP, padx=1, pady=1, fill=X)

            # Левое поле терминала
            left_terminal_text_box = Listbox(frame_for_left_window, relief=GROOVE, width=25, height=25,
                                             selectbackground="grey60")
            left_terminal_text_box.pack(side=TOP, padx=1, pady=1, fill=X)

            left_terminal_clear_button = Button(frame_for_left_window, text="Clear", relief=GROOVE, width=25, height=1,
                                                bg="gray60", command=clear_left_terminal)
            left_terminal_clear_button.pack(side=TOP, padx=1, pady=1)

            # Правое поле терминала
            right_terminal_text_box = Listbox(frame_for_right_window, relief=GROOVE, width=25, height=25,
                                              selectbackground="grey60")
            right_terminal_text_box.pack(side=TOP, padx=1, pady=1, fill=X)

            right_terminal_clear_button = Button(frame_for_right_window, text="Clear", relief=GROOVE, width=25,
                                                 height=1, bg="gray60", command=clear_right_terminal)
            right_terminal_clear_button.pack(side=TOP, padx=1, pady=1)

            # Побитное поле для введения команды
            bit_1_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, selectbackground="grey60")
            bit_1_entry.pack(side=LEFT, padx=1, pady=1, fill=X)
            bit_2_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, selectbackground="grey60")
            bit_2_entry.pack(side=LEFT, padx=1, pady=1, fill=X)
            bit_3_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, selectbackground="grey60")
            bit_3_entry.pack(side=LEFT, padx=1, pady=1, fill=X)
            bit_4_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, selectbackground="grey60")
            bit_4_entry.pack(side=LEFT, padx=1, pady=1, fill=X)
            bit_5_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, selectbackground="grey60")
            bit_5_entry.pack(side=LEFT, padx=1, pady=1, fill=X)
            bit_6_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, selectbackground="grey60")
            bit_6_entry.pack(side=LEFT, padx=1, pady=1, fill=X)
            bit_7_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, selectbackground="grey60")
            bit_7_entry.pack(side=LEFT, padx=1, pady=1, fill=X)
            bit_8_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, selectbackground="grey60")
            bit_8_entry.pack(side=LEFT, padx=1, pady=1, fill=X)

            bit_check_crc_button = Button(frame_for_per_byte_command, text="CRC", relief=GROOVE, width=4,
                                          height=1, bg="gray60", command=bit_check_crc)
            bit_check_crc_button.pack(side=LEFT, padx=6, pady=1)

            send_bit_command_button = Button(frame_for_per_byte_command, text="Send", relief=GROOVE, width=11,
                                             height=1, bg="gray60", command=send_bit_command)
            send_bit_command_button.pack(side=RIGHT, padx=3, pady=1)

            # Построчное поле для введения команды
            string_entry = Entry(frame_for_text_command, relief=GROOVE, width=39, selectbackground="grey60")
            string_entry.pack(side=LEFT, padx=1, pady=1, fill=X)

            string_check_crc_button = Button(frame_for_text_command, text="CRC", relief=GROOVE, width=4,
                                             height=1, bg="gray60", command=string_check_crc)
            string_check_crc_button.pack(side=LEFT, padx=6, pady=1)

            send_string_command_button = Button(frame_for_text_command, text="Send", relief=GROOVE, width=11,
                                                height=1, bg="gray60", command=send_string_command)
            send_string_command_button.pack(side=RIGHT, padx=3, pady=1)

        self.terminal_open = not self.terminal_open

    def main_frame_unit(self):
        """Запускает первичное окно с возможностью первичного просмотра баз данных, добавления, удаления, открытия"""

        self.start_window = Tk()
        self.start_window.title("Adjustment utility")

        # disables the ability to zoom the page
        self.start_window.minsize(831, 600)
        self.start_window.resizable(False, False)

        # базовые поля
        frame_for_device_buttons = LabelFrame(self.start_window, bg="gray90")
        frame_for_device_buttons.pack(side=LEFT, padx=1, pady=1, fill=Y)

        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        frame_for_settings = LabelFrame(self.start_window, bg="gray90")
        frame_for_settings.pack(side=BOTTOM, padx=1, pady=1, fill=X)

        self.frame_for_terminal = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_terminal.pack(side=RIGHT, padx=1, pady=2, fill=Y)

        # левое поле
        self.poa_button = Button(frame_for_device_buttons, text="POA", relief=GROOVE, width=5, height=3, bg="gray60",
                                 command=self.poa_unit)
        self.poa_button.pack(side=TOP, padx=1, pady=1)
        self.sth1_button = Button(frame_for_device_buttons, text="STH-1", relief=GROOVE, width=5, height=3, bg="gray60",
                                  command=self.sth1_unit)
        self.sth1_button.pack(side=TOP, padx=1, pady=1)
        self.sth2_button = Button(frame_for_device_buttons, text="STH-2", relief=GROOVE, width=5, height=3, bg="gray60",
                                  command=self.sth2_unit)
        self.sth2_button.pack(side=TOP, padx=1, pady=1)
        self.sth3_button = Button(frame_for_device_buttons, text="STH-3", relief=GROOVE, width=5, height=3, bg="gray60",
                                  command=self.sth3_unit)
        self.sth3_button.pack(side=TOP, padx=1, pady=1)
        self.as_button = Button(frame_for_device_buttons, text="AS", relief=GROOVE, width=5, height=3, bg="gray60",
                                command=self.as_unit)
        self.as_button.pack(side=TOP, padx=1, pady=1)
        self.sc_button = Button(frame_for_device_buttons, text="SC", relief=GROOVE, width=5, height=3, bg="gray60",
                                command=self.sc_unit)
        self.sc_button.pack(side=TOP, padx=1, pady=1)
        self.ck_button = Button(frame_for_device_buttons, text="CK", relief=GROOVE, width=5, height=3, bg="gray60",
                                command=self.ck_unit)
        self.ck_button.pack(side=TOP, padx=1, pady=1)

        self.refind_button = Button(frame_for_device_buttons, text="⭯", relief=GROOVE, width=5, height=2, bg="brown1",
                                    command=self.refind_device)
        self.refind_button.pack(side=BOTTOM, padx=1, pady=1)

        # нижнее поле
        self.set_button = Button(frame_for_settings, text="Set", relief=GROOVE, width=8, height=2, bg="gray60",
                                 command=self.set_parameters)
        self.set_button.pack(side=RIGHT, padx=3, pady=1)

        bytesize_list = ["8", "16", "∞"]
        self.bytesize_combobox = ttk.Combobox(frame_for_settings, values=bytesize_list, width=4, height=2,
                                              state="readonly")
        self.bytesize_combobox.pack(side=RIGHT, padx=3, pady=1)

        bytesize_label = Label(frame_for_settings, text="Bytesize:", width=7, height=2, bg="gray90")
        bytesize_label.pack(side=RIGHT, padx=3, pady=1)

        timeout_list = ["0.1", "0.3", "0.5", "1.0"]
        self.timeout_combobox = ttk.Combobox(frame_for_settings, values=timeout_list, width=4, height=2,
                                             state="readonly")
        self.timeout_combobox.pack(side=RIGHT, padx=3, pady=1)

        timeout_label = Label(frame_for_settings, text="Timeout(s):", width=10, height=2, bg="gray90")
        timeout_label.pack(side=RIGHT, padx=3, pady=1)

        baudrate_list = ["115200", "500000", "1000000"]
        self.baudrate_combobox = ttk.Combobox(frame_for_settings, values=baudrate_list, width=8, height=2,
                                              state="readonly")
        self.baudrate_combobox.pack(side=RIGHT, padx=3, pady=1)

        baudrate_label = Label(frame_for_settings, text="Baudrate:", width=8, height=2, bg="gray90")
        baudrate_label.pack(side=RIGHT, padx=3, pady=1)

        port_numbers = ["COM25", "2", "3", "4"]
        self.port_combobox = ttk.Combobox(frame_for_settings, values=port_numbers, width=8, height=2, state="readonly")
        self.port_combobox.pack(side=RIGHT, padx=3, pady=1)

        port_label = Label(frame_for_settings, text="Serial port:", width=8, height=2, bg="gray90")
        port_label.pack(side=RIGHT, padx=3, pady=1)

        self.manual_button = Button(frame_for_settings, text="Manual", relief=GROOVE, width=8, height=2,
                                    bg="gray60", command=self.manual_parameters)
        self.manual_button.pack(side=LEFT, padx=3, pady=1)

        self.auto_button = Button(frame_for_settings, text="Auto", relief=GROOVE, width=8, height=2,
                                  bg="gray60", command=self.auto_parameters, state="disabled")
        self.auto_button.pack(side=LEFT, pady=1)

        # правое поле
        self.terminal_button = Button(self.frame_for_terminal, text="⮞\n⮞\n⮞\n\nT\nE\nR\nM\nI\nN\nA\nL\n\n⮞\n⮞\n⮞",
                                      relief=GROOVE, width=2, bg="gray60", command=self.terminal)
        self.terminal_button.pack(side=RIGHT, fill=Y)

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

        # не ясно, нужно ли то, что ниже
        self.manual_parameters()
        ##############################################################
        ############# УДООООЛИИИИИИ ниже, мэйнлуп оставь######
        ##############################################################
        self.poa_unit()

        self.start_window.mainloop()


AdjustmentUtility().main_frame_unit()
