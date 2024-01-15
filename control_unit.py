import time
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
from math import ceil
import serial
import re

import request_and_port_list
import request_response

global poa_auto_errors


class AdjustmentUtility:
    """
    Основное окно взаимодействия с девайсами и основное тело программы
    Доступные аксессуары на данный момент:
    - Система охлаждения
    """

    def __init__(self):
        # Инициализация первичных переменных для класса

        self.status_text_box = None
        self.full_auto_init_window = None
        self.device_signature = None
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

        self.last_command_except_status = None

    def poa_unit(self, auto=False):
        """Функция управления системой охлаждения"""

        def all_grey():
            # Верхние поля отображения статусов

            device_label.config(text="-", bg="gray90")
            stat_ctrl_label.config(text="-", bg="gray90")
            stat_sens_label.config(text="-", bg="gray90")
            t_max_label.config(text="-", bg="gray90")
            t_min_label.config(text="-", bg="gray90")
            flow_label.config(text="-", bg="gray90")
            errors_label.config(text="-", bg="gray90")
            pwm_1_label.config(text="-", bg="gray90")
            pwm_2_label.config(text="-", bg="gray90")
            crc_label.config(text="-", bg="gray90")

            device_data.config(text="-", bg="gray90")
            stat_ctrl_data.config(text="-", bg="gray90")
            stat_sens_data.config(text="-", bg="gray90")
            t_max_data.config(text="-", bg="gray90")
            t_min_data.config(text="-", bg="gray90")
            flow_data.config(text="-", bg="gray90")
            errors_data.config(text="-", bg="gray90")
            pwm_1_data.config(text="-", bg="gray90")
            pwm_2_data.config(text="-", bg="gray90")
            crc_data.config(text="-", bg="gray90")

            # Status sensors - всё неактивно
            wts1_bit.config(text="--", bg="gray90")
            wts1_label.config(bg="gray90")
            wts2_bit.config(text="--", bg="gray90")
            wts2_label.config(bg="gray90")
            svs_bit.config(text="--", bg="gray90")
            svs_label.config(bg="gray90")
            key_bit.config(text="--", bg="gray90")
            key_label.config(bg="gray90")
            wls_bit.config(text="--", bg="gray90")
            wls_label.config(bg="gray90")
            reserve_1_bit.config(text="--", bg="gray90")
            reserve_1_label.config(bg="gray90")
            reserve_2_bit.config(text="--", bg="gray90")
            reserve_2_label.config(bg="gray90")
            reserve_3_bit.config(text="--", bg="gray90")
            reserve_3_label.config(bg="gray90")

            # Status control - всё неактивно
            rfp_bit.config(text="--", bg="gray90")
            rfp_label.config(bg="gray90")
            wpp_bit.config(text="--", bg="gray90")
            wpp_label.config(bg="gray90")
            acf_bit.config(text="--", bg="gray90")
            acf_label.config(bg="gray90")
            srs_bit.config(text="--", bg="gray90")
            srs_label.config(bg="gray90")
            beeper_bit.config(text="--", bg="gray90")
            beeper_label.config(bg="gray90")
            rfe_bit.config(text="--", bg="gray90")
            rfe_label.config(bg="gray90")
            reserve_4_bit.config(text="--", bg="gray90")
            reserve_4_label.config(bg="gray90")
            reserve_5_bit.config(text="--", bg="gray90")
            reserve_5_label.config(bg="gray90")

        def transcript_other_stuff(recieved_command=None):
            # Расшифровка прочих параметров из полученной команды

            def transcript_status_device():
                # расшифровка поля Device

                device_hex = recieved_command[0] + recieved_command[1]
                if device_hex == "40":
                    device_label.config(text="OK", bg="PaleGreen3")
                else:
                    device_label.config(text="❌", bg="salmon")
                device_data.config(text=device_hex.upper())

            def transcript_status_t_max():
                # расшифровка поля t_max

                t_max_hex = recieved_command[6] + recieved_command[7]
                t_max_dec = int(t_max_hex, 16)
                if 10 <= t_max_dec <= 45:
                    t_max_label.config(bg="PaleGreen3")
                    poa_auto_errors["t_max_error"] = False
                else:
                    poa_auto_errors["t_max_error"] = True
                    if t_max_dec == 255:
                        poa_auto_errors["t_max_error"] = 255
                    t_max_label.config(bg="salmon")
                t_max_label.config(text=str(t_max_dec).upper())
                t_max_data.config(text=t_max_hex.upper())

            def transcript_status_t_min():
                # расшифровка поля t_min

                t_min_hex = recieved_command[8] + recieved_command[9]
                t_min_dec = int(t_min_hex, 16)
                if 10 <= t_min_dec <= 45:
                    t_min_label.config(bg="PaleGreen3")
                    poa_auto_errors["t_min_error"] = False
                else:
                    poa_auto_errors["t_min_error"] = True
                    if t_min_dec == 255:
                        poa_auto_errors["t_min_error"] = 255
                    t_min_label.config(bg="salmon")
                t_min_label.config(text=str(t_min_dec).upper())
                t_min_data.config(text=t_min_hex.upper())

            def transcript_status_flow():
                # расшифровка поля flow

                flow_hex = recieved_command[10] + recieved_command[11]
                flow_dec = int(flow_hex, 16)
                flow_real = round(float(flow_dec / 73), 2)
                if self.last_command_except_status == request_and_port_list.poa_request_dictionary["dry_poa_package"] \
                        or self.last_command_except_status == \
                        request_and_port_list.poa_request_dictionary["stop_poa_package"]:
                    if flow_real < 1:
                        flow_label.config(bg="PaleGreen3")
                        poa_auto_errors["flow_error"] = False
                    else:
                        flow_label.config(bg="salmon")
                        poa_auto_errors["flow_error"] = True
                else:
                    if 2.5 <= flow_real <= 5:
                        flow_label.config(bg="PaleGreen3")
                        poa_auto_errors["flow_error"] = False
                    else:
                        flow_label.config(bg="salmon")
                        poa_auto_errors["flow_error"] = True
                flow_label.config(text=str(flow_real))
                flow_data.config(text=flow_hex.upper())

            def transcript_status_errors():
                # расшифровка поля errors
                errors_hex = recieved_command[12] + recieved_command[13]
                if errors_hex == "00" or errors_hex == "10":
                    errors_label.config(bg="PaleGreen3", text="OK")
                    poa_auto_errors["errors_error"] = False
                else:
                    errors_label.config(bg="salmon", text=errors_hex)
                    poa_auto_errors["errors_error"] = True
                errors_data.config(text=errors_hex.upper())

            def transcript_status_pwm_1_2():
                # расшифровка полей pwm

                pwm_1_hex = recieved_command[14] + recieved_command[15]
                pwm_2_hex = recieved_command[16] + recieved_command[17]
                pwm_1_dec = int(pwm_1_hex, 16)
                pwm_2_dec = int(pwm_2_hex, 16)
                pwm_1_percent = int(pwm_1_dec * 100 / 254)
                pwm_2_percent = int(pwm_2_dec * 100 / 254)
                if self.last_command_except_status == request_and_port_list.poa_request_dictionary["dry_poa_package"] \
                        or self.last_command_except_status == \
                        request_and_port_list.poa_request_dictionary["stop_poa_package"]:
                    if pwm_1_percent < 10:
                        pwm_1_label.config(bg="PaleGreen3", text=str(pwm_1_percent) + "%")
                        poa_auto_errors["pwm_1_2_error"] = False
                    else:
                        pwm_1_label.config(bg="salmon", text=str(pwm_1_percent) + "%")
                        poa_auto_errors["pwm_1_2_error"] = True
                    if pwm_2_percent < 10:
                        pwm_2_label.config(bg="PaleGreen3", text=str(pwm_2_percent) + "%")
                        poa_auto_errors["pwm_1_2_error"] = False
                    else:
                        pwm_2_label.config(bg="salmon", text=str(pwm_2_percent) + "%")
                        poa_auto_errors["pwm_1_2_error"] = True
                else:
                    if pwm_1_percent + pwm_2_percent == 100:
                        pwm_1_label.config(bg="PaleGreen3", text=str(pwm_1_percent) + "%")
                        pwm_2_label.config(bg="PaleGreen3", text=str(pwm_2_percent) + "%")
                        poa_auto_errors["pwm_1_2_error"] = False
                    else:
                        pwm_1_label.config(bg="salmon", text=str(pwm_1_percent) + "%")
                        pwm_2_label.config(bg="salmon", text=str(pwm_2_percent) + "%")
                        poa_auto_errors["pwm_1_2_error"] = True
                pwm_1_data.config(text=pwm_1_hex.upper())
                pwm_2_data.config(text=pwm_2_hex.upper())

            def check_crc():
                # Проверяет контрольную сумму

                full_dec_summ = 0
                full_hex_summ = 0
                for bit in range(0, 20):
                    if bit % 2 != 0:
                        hex_bit = recieved_command[bit - 1] + recieved_command[bit]
                        full_dec_summ = full_dec_summ + int(hex_bit, 16)
                        full_hex_summ = hex(full_dec_summ)
                if full_hex_summ[len(full_hex_summ) - 1] == "0":
                    crc_label.config(bg="PaleGreen3", text="OK")
                    poa_auto_errors["crc_error"] = False
                else:
                    crc_label.config(bg="salmon", text=str(full_hex_summ))
                    poa_auto_errors["crc_error"] = True
                crc_data.config(text=recieved_command[18].upper() + recieved_command[19].upper())

            transcript_status_device()
            transcript_status_t_max()
            transcript_status_t_min()
            transcript_status_flow()
            transcript_status_errors()
            transcript_status_pwm_1_2()
            check_crc()

        def transcript_statuses(recieved_command=None, send_command=None):
            # Расшифровывает статусы из полученных ответов от контроллера

            global poa_auto_errors

            poa_auto_errors = {
                "wls_error": False,
                "key_error": False,
                "svs_error": False,
                "wts2_error": False,
                "beeper_error": False,
                "t_min_error": False,
                "t_max_error": False,
                "pwm_1_2_error": False,
                "errors_error": False,
                "flow_error": False,
                "crc_error": False
            }

            if self.last_command_except_status is None:
                self.last_command_except_status = request_and_port_list.poa_request_dictionary["start_poa_package"]

            if recieved_command:

                # Превращает из хексов в бины и выводит значения
                status_ctrl_hex = recieved_command[2] + recieved_command[3]
                binary_status_ctrl = "{0:08b}".format(int(status_ctrl_hex, 16))
                stat_ctrl_data.config(text=status_ctrl_hex.upper(), bg="gray90")

                # Превращает из хексов в бины и выводит значения
                status_sens_hex = recieved_command[4] + recieved_command[5]
                binary_status_sens = "{0:08b}".format(int(status_sens_hex, 16))
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
                            reserve_3_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                            reserve_3_label.config(bg="salmon")
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"

                    if bit_number == 1:
                        if int(binary_status_sens[bit_number]) == 0:
                            reserve_2_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            reserve_2_label.config(bg="PaleGreen3")
                        else:
                            reserve_2_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                            reserve_2_label.config(bg="salmon")
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"

                    if bit_number == 2:
                        if int(binary_status_sens[bit_number]) == 0:
                            reserve_1_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            reserve_1_label.config(bg="PaleGreen3")
                        else:
                            reserve_1_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                            reserve_1_label.config(bg="salmon")
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"

                    if bit_number == 3:
                        if int(binary_status_sens[bit_number]) == 0:
                            wls_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            wls_label.config(bg="PaleGreen3")
                            poa_auto_errors["wls_error"] = False
                        else:
                            wls_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                            wls_label.config(bg="salmon")
                            poa_auto_errors["wls_error"] = True
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"

                    if bit_number == 4:
                        if self.last_command_except_status == \
                                request_and_port_list.poa_request_dictionary["stop_poa_package"]:
                            key_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            key_label.config(bg="PaleGreen3")
                            poa_auto_errors["key_error"] = False
                        elif self.last_command_except_status == \
                                request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                            if int(binary_status_sens[bit_number]) == 1:
                                key_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                                key_label.config(bg="salmon")
                                poa_auto_errors["key_error"] = True
                                if red_green_status_sens == "green":
                                    red_green_status_sens = "red"
                            else:
                                key_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                                key_label.config(bg="PaleGreen3")
                                poa_auto_errors["key_error"] = False
                        elif self.last_command_except_status == \
                                request_and_port_list.poa_request_dictionary["start_poa_package"] or \
                                self.last_command_except_status is None:
                            if int(binary_status_sens[bit_number]) == 0:
                                key_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                                key_label.config(bg="salmon")
                                poa_auto_errors["key_error"] = True
                                if red_green_status_sens == "green":
                                    red_green_status_sens = "red"
                            else:
                                key_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                                key_label.config(bg="PaleGreen3")
                                poa_auto_errors["key_error"] = False

                    if bit_number == 5:
                        if int(binary_status_sens[bit_number]) == 0:
                            svs_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            svs_label.config(bg="PaleGreen3")
                            poa_auto_errors["svs_error"] = False
                        else:
                            svs_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                            svs_label.config(bg="salmon")
                            poa_auto_errors["svs_error"] = True
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"

                    if bit_number == 6:
                        if int(binary_status_sens[bit_number]) == 0:
                            wts2_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            wts2_label.config(bg="PaleGreen3")
                            poa_auto_errors["wts2_error"] = False
                        else:
                            wts2_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                            wts2_label.config(bg="salmon")
                            poa_auto_errors["wts2_error"] = True
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"

                    if bit_number == 7:
                        if int(binary_status_sens[bit_number]) == 0:
                            wts1_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                            wts1_label.config(bg="PaleGreen3")
                            poa_auto_errors["wts1_error"] = False
                        else:
                            wts1_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                            wts1_label.config(bg="salmon")
                            poa_auto_errors["wts1_error"] = True
                            if red_green_status_sens == "green":
                                red_green_status_sens = "red"

                    if red_green_status_sens == "green":
                        stat_sens_label.config(text="OK", bg="PaleGreen3")
                    else:
                        stat_sens_label.config(text="❌", bg="salmon")

                """
                Раскидка битов и статусов по Статус контроль
                """

                for bit_number in range(0, 8):

                    if bit_number == 0:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            reserve_5_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            reserve_5_label.config(bg="PaleGreen3")
                        else:
                            reserve_5_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            reserve_5_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"

                    if bit_number == 1:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            reserve_4_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            reserve_4_label.config(bg="PaleGreen3")
                        else:
                            reserve_4_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            reserve_4_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"

                    if send_command == request_and_port_list.poa_request_dictionary["status_poa_package"]:

                        if bit_number == 2:
                            if self.last_command_except_status == \
                                    request_and_port_list.poa_request_dictionary["start_poa_package"] \
                                    or self.last_command_except_status is None:
                                if int(binary_status_ctrl[bit_number]) == 1:
                                    rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    rfe_label.config(bg="PaleGreen3")
                                else:
                                    rfe_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                    rfe_label.config(bg="salmon")
                                    if red_green_status_ctrl == "green":
                                        red_green_status_ctrl = "red"
                            elif self.last_command_except_status == \
                                    request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                                if int(binary_status_ctrl[bit_number]) == 0:
                                    rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    rfe_label.config(bg="PaleGreen3")
                                else:
                                    rfe_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                                    rfe_label.config(bg="RoyalBlue1")
                            else:
                                if int(binary_status_ctrl[bit_number]) == 0:
                                    rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    rfe_label.config(bg="PaleGreen3")
                                else:
                                    rfe_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                    rfe_label.config(bg="salmon")
                                    if red_green_status_ctrl == "green":
                                        red_green_status_ctrl = "red"

                        if bit_number == 3:
                            if self.last_command_except_status == \
                                    request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                                if int(binary_status_ctrl[bit_number]) == 0:
                                    beeper_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    beeper_label.config(bg="PaleGreen3")
                                    poa_auto_errors["beeper_error"] = False
                                else:
                                    beeper_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                                    beeper_label.config(bg="RoyalBlue1")
                                    poa_auto_errors["beeper_error"] = False
                            else:
                                if int(binary_status_ctrl[bit_number]) == 0:
                                    beeper_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    beeper_label.config(bg="PaleGreen3")
                                    poa_auto_errors["beeper_error"] = False
                                else:
                                    beeper_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                    beeper_label.config(bg="salmon")
                                    poa_auto_errors["beeper_error"] = True
                                    if red_green_status_ctrl == "green":
                                        red_green_status_ctrl = "red"

                        if bit_number == 4:
                            if self.last_command_except_status == \
                                    request_and_port_list.poa_request_dictionary["start_poa_package"] \
                                    or self.last_command_except_status is None:
                                if int(binary_status_ctrl[bit_number]) == 1:
                                    srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    srs_label.config(bg="PaleGreen3")
                                else:
                                    srs_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                    srs_label.config(bg="salmon")
                                    if red_green_status_ctrl == "green":
                                        red_green_status_ctrl = "red"
                            elif self.last_command_except_status == \
                                    request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                                if int(binary_status_ctrl[bit_number]) == 0:
                                    srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    srs_label.config(bg="PaleGreen3")
                                else:
                                    srs_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                                    srs_label.config(bg="RoyalBlue1")
                            else:
                                if int(binary_status_ctrl[bit_number]) == 0:
                                    srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    srs_label.config(bg="PaleGreen3")
                                else:
                                    srs_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                    srs_label.config(bg="salmon")
                                    if red_green_status_ctrl == "green":
                                        red_green_status_ctrl = "red"

                        if bit_number == 5:
                            if self.last_command_except_status == \
                                    request_and_port_list.poa_request_dictionary["start_poa_package"] \
                                    or self.last_command_except_status is None:
                                if int(binary_status_ctrl[bit_number]) == 1:
                                    acf_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    acf_label.config(bg="PaleGreen3")
                                else:
                                    acf_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                    acf_label.config(bg="salmon")
                                    if red_green_status_ctrl == "green":
                                        red_green_status_ctrl = "red"
                            else:
                                if int(binary_status_ctrl[bit_number]) == 0:
                                    acf_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    acf_label.config(bg="PaleGreen3")
                                else:
                                    acf_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                    acf_label.config(bg="salmon")
                                    if red_green_status_ctrl == "green":
                                        red_green_status_ctrl = "red"

                        if bit_number == 6:
                            if self.last_command_except_status == \
                                    request_and_port_list.poa_request_dictionary["start_poa_package"] \
                                    or self.last_command_except_status is None:
                                if int(binary_status_ctrl[bit_number]) == 1:
                                    wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    wpp_label.config(bg="PaleGreen3")
                                else:
                                    wpp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                    wpp_label.config(bg="salmon")
                                    if red_green_status_ctrl == "green":
                                        red_green_status_ctrl = "red"
                            elif self.last_command_except_status == \
                                    request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                                if int(binary_status_ctrl[bit_number]) == 0:
                                    wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    wpp_label.config(bg="PaleGreen3")
                                else:
                                    wpp_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                                    wpp_label.config(bg="RoyalBlue1")
                            else:
                                if int(binary_status_ctrl[bit_number]) == 0:
                                    wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    wpp_label.config(bg="PaleGreen3")
                                else:
                                    wpp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                    wpp_label.config(bg="salmon")
                                    if red_green_status_ctrl == "green":
                                        red_green_status_ctrl = "red"

                    if send_command == request_and_port_list.poa_request_dictionary["start_poa_package"]:

                        if bit_number == 2:
                            if int(binary_status_ctrl[bit_number]) == 0:
                                rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                rfe_label.config(bg="PaleGreen3")
                            else:
                                rfe_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                rfe_label.config(bg="salmon")
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if bit_number == 3:
                            if int(binary_status_ctrl[bit_number]) == 0:
                                beeper_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                beeper_label.config(bg="PaleGreen3")
                                poa_auto_errors["beeper_error"] = False
                            else:
                                beeper_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                beeper_label.config(bg="salmon")
                                poa_auto_errors["beeper_error"] = True
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if bit_number == 4:
                            if int(binary_status_ctrl[bit_number]) == 1:
                                srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                srs_label.config(bg="PaleGreen3")
                            else:
                                srs_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                srs_label.config(bg="salmon")
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if bit_number == 5:
                            if int(binary_status_ctrl[bit_number]) == 1:
                                acf_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                acf_label.config(bg="PaleGreen3")
                            else:
                                acf_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                acf_label.config(bg="salmon")
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if bit_number == 6:
                            if int(binary_status_ctrl[bit_number]) == 0:
                                wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                wpp_label.config(bg="PaleGreen3")
                            else:
                                wpp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                wpp_label.config(bg="salmon")
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                    if send_command == request_and_port_list.poa_request_dictionary["stop_poa_package"]:

                        if bit_number == 2:
                            if int(binary_status_ctrl[bit_number]) == 1:
                                rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                rfe_label.config(bg="PaleGreen3")
                            else:
                                rfe_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                                rfe_label.config(bg="RoyalBlue1")

                        if bit_number == 3:
                            if int(binary_status_ctrl[bit_number]) == 0:
                                beeper_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                beeper_label.config(bg="PaleGreen3")
                                poa_auto_errors["beeper_error"] = False
                            else:
                                beeper_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                beeper_label.config(bg="salmon")
                                poa_auto_errors["beeper_error"] = True
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if bit_number == 4:
                            if int(binary_status_ctrl[bit_number]) == 1:
                                srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                srs_label.config(bg="PaleGreen3")
                            else:
                                srs_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                srs_label.config(bg="salmon")
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if bit_number == 5:
                            if int(binary_status_ctrl[bit_number]) == 0:
                                acf_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                acf_label.config(bg="PaleGreen3")
                            else:
                                acf_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                acf_label.config(bg="salmon")
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if bit_number == 6:
                            if int(binary_status_ctrl[bit_number]) == 1:
                                wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                wpp_label.config(bg="PaleGreen3")
                            else:
                                wpp_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                                wpp_label.config(bg="RoyalBlue1")

                    if send_command == request_and_port_list.poa_request_dictionary["dry_poa_package"]:

                        if bit_number == 2:
                            if int(binary_status_ctrl[bit_number]) == 0:
                                rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                rfe_label.config(bg="PaleGreen3")
                            else:
                                rfe_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                rfe_label.config(bg="salmon")
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if bit_number == 3:
                            if int(binary_status_ctrl[bit_number]) == 0:
                                beeper_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                beeper_label.config(bg="PaleGreen3")
                                poa_auto_errors["beeper_error"] = False
                            else:
                                beeper_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                beeper_label.config(bg="salmon")
                                poa_auto_errors["beeper_error"] = True
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if bit_number == 4:
                            if int(binary_status_ctrl[bit_number]) == 1:
                                srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                srs_label.config(bg="PaleGreen3")
                            else:
                                srs_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                srs_label.config(bg="salmon")
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if bit_number == 5:
                            if int(binary_status_ctrl[bit_number]) == 0:
                                acf_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                acf_label.config(bg="PaleGreen3")
                            else:
                                acf_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                acf_label.config(bg="salmon")
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if bit_number == 6:
                            if int(binary_status_ctrl[bit_number]) == 0:
                                wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                wpp_label.config(bg="PaleGreen3")
                            else:
                                wpp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                wpp_label.config(bg="salmon")
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                    if bit_number == 7:
                        t_min_hex = recieved_command[8] + recieved_command[9]
                        t_min_dec = int(t_min_hex, 16)
                        t_max_hex = recieved_command[6] + recieved_command[7]
                        t_max_dec = int(t_max_hex, 16)

                        if send_command == request_and_port_list.poa_request_dictionary["status_poa_package"]:
                            if t_max_dec > 31 and self.last_command_except_status == \
                                    request_and_port_list.poa_request_dictionary["start_poa_package"] or \
                                    t_min_dec > 31 and self.last_command_except_status == \
                                    request_and_port_list.poa_request_dictionary["start_poa_package"]:
                                if int(binary_status_ctrl[bit_number]) == 1:
                                    rfp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    rfp_label.config(bg="PaleGreen3")
                                else:
                                    rfp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                    rfp_label.config(bg="salmon")
                                    if red_green_status_ctrl == "green":
                                        red_green_status_ctrl = "red"
                            else:
                                if int(binary_status_ctrl[bit_number]) == 0:
                                    rfp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                    rfp_label.config(bg="PaleGreen3")
                                else:
                                    rfp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                    rfp_label.config(bg="salmon")
                                    if red_green_status_ctrl == "green":
                                        red_green_status_ctrl = "red"
                        else:
                            if int(binary_status_ctrl[bit_number]) == 0:
                                rfp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                                rfp_label.config(bg="PaleGreen3")
                            else:
                                rfp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                                rfp_label.config(bg="salmon")
                                if red_green_status_ctrl == "green":
                                    red_green_status_ctrl = "red"

                        if red_green_status_ctrl == "green":
                            stat_ctrl_label.config(text="OK", bg="PaleGreen3")
                        else:
                            stat_ctrl_label.config(text="❌", bg="salmon")

        def poa_start_command(manual_check=True):
            # Отправляет команду на запуск насоса системы охлаждения
            all_grey()
            request_response.command_sender(
                accepted_request=request_and_port_list.poa_request_dictionary["stop_poa_package"])
            answer = request_response.command_sender(
                accepted_request=request_and_port_list.poa_request_dictionary["start_poa_package"])
            if answer:
                if manual_check:
                    self.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
                    self.info_text_box.yview(END)
                self.last_command_except_status = request_and_port_list.poa_request_dictionary["start_poa_package"]
                transcript_statuses(answer, request_and_port_list.poa_request_dictionary["start_poa_package"])
                transcript_other_stuff(answer)
                if manual_check:
                    self.info_text_box.insert(END, " состояние расшифровано\n", 'tag_green_text')
                    self.info_text_box.yview(END)
            else:
                if manual_check:
                    self.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                              'tag_red_text')
                    self.info_text_box.yview(END)

        def poa_stop_command():
            # Отправляет команду на остановку насоса системы охлаждения
            all_grey()
            answer = request_response.command_sender(
                accepted_request=request_and_port_list.poa_request_dictionary["stop_poa_package"])
            if answer:
                self.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.last_command_except_status = request_and_port_list.poa_request_dictionary["stop_poa_package"]
                transcript_statuses(answer, request_and_port_list.poa_request_dictionary["stop_poa_package"])
                transcript_other_stuff(answer)
                self.info_text_box.insert(END, " состояние расшифровано\n", 'tag_green_text')
                self.info_text_box.yview(END)
            else:
                self.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                          'tag_red_text')
                self.info_text_box.yview(END)

        def poa_version_command():
            # Отправляет команду на запрос версии системы охлаждения
            all_grey()
            answer = request_response.command_sender(
                accepted_request=request_and_port_list.poa_request_dictionary["version_poa_package"])
            if answer:
                version_answer_hex = str()
                for bit_number in range(2, 16):
                    version_answer_hex = str(version_answer_hex) + str(answer[bit_number])
                version_answer_ascii = bytearray.fromhex(version_answer_hex).decode(encoding='ascii')
                self.info_text_box.insert(END, "✔ Ответ от контроллера:\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ HEX:    " + answer.upper() + "\n⫸ ASCII:  " + version_answer_ascii +
                                          "\n", 'tag_black_text')
                self.info_text_box.yview(END)
            else:
                self.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                          'tag_red_text')
                self.info_text_box.yview(END)

        def poa_status_command(manual_check=True):
            # Отправляет команду на запрос статуса системы охлаждения
            all_grey()
            answer = request_response.command_sender(
                accepted_request=request_and_port_list.poa_request_dictionary["status_poa_package"])
            if answer:
                if manual_check:
                    self.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
                    self.info_text_box.yview(END)
                transcript_statuses(answer, request_and_port_list.poa_request_dictionary["status_poa_package"])
                transcript_other_stuff(answer)
                if manual_check:
                    self.info_text_box.insert(END, " состояние расшифровано\n", 'tag_green_text')
                    self.info_text_box.yview(END)
            else:
                if manual_check:
                    self.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                              'tag_red_text')
                    self.info_text_box.yview(END)

        def poa_dry_command():
            # Отправляет команду на откачку воды в системе охлаждения
            all_grey()
            request_response.command_sender(
                accepted_request=request_and_port_list.poa_request_dictionary["stop_poa_package"])
            answer = request_response.command_sender(
                accepted_request=request_and_port_list.poa_request_dictionary["dry_poa_package"])
            if answer:
                self.info_text_box.insert(END, "✔ Команда выполнена, ответ получен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.last_command_except_status = request_and_port_list.poa_request_dictionary["dry_poa_package"]
                transcript_statuses(answer, request_and_port_list.poa_request_dictionary["dry_poa_package"])
                transcript_other_stuff(answer)
                self.info_text_box.insert(END, " состояние расшифровано\n", 'tag_green_text')
                self.info_text_box.yview(END)
            else:
                self.info_text_box.insert(END, "❌ Нет ответа контроллера\n * проверьте подключение устройства *\n",
                                          'tag_red_text')
                self.info_text_box.yview(END)

        def poa_info_command():
            # Команда, вызывающая файл с основной информацией по подсистеме охлаждения
            pass

        # Прописывает с нуля интерфейсный фрейм
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        # Заполняет настройки серийного порта
        self.bytesize_combobox.set(request_and_port_list.com_port_settings["bytesize"])
        self.timeout_combobox.set(request_and_port_list.com_port_settings["timeout"])
        self.baudrate_combobox.set(request_and_port_list.com_port_settings["baudrate"])
        self.port_combobox.set(request_and_port_list.com_port_settings["comport"])

        """
        Информационное поле полученной и расшифрованной команды
        """

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

        """
        Поле отображения информации Status Control
        """

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

        acf_label = Label(frame_for_acf, text=" - Вкл. вентилятора воздушного охлажд. (PWM)", width=40, height=1,
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

        rfe_label = Label(frame_for_rfe, text=" - Вкл. вентилятора воздушного охлажд. (MAX)", width=40, height=1,
                          bg="gray95", relief=SUNKEN, anchor=W)
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

        """
        Поле отображения информации Status Sensors
        """

        # интерфейс расшифровки статуса датчика температуры холодной воды
        frame_for_wts1 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_wts1.pack(side=TOP, padx=1, pady=1, fill=X)

        wts1_bit = Label(frame_for_wts1, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        wts1_bit.pack(side=LEFT, padx=3, pady=1)

        wts1_label = Label(frame_for_wts1, text=" - Сработка датчика крана горячей воды", width=40, height=1,
                           bg="gray95", relief=SUNKEN, anchor=W)
        wts1_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки статуса датчика температуры холодной воды
        frame_for_wts2 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_wts2.pack(side=TOP, padx=1, pady=1, fill=X)

        wts2_bit = Label(frame_for_wts2, text="-", width=6, height=1, bg="gray95", relief=SUNKEN)
        wts2_bit.pack(side=LEFT, padx=3, pady=1)

        wts2_label = Label(frame_for_wts2, text=" - Сработка датчика крана холодной воды", width=40, height=1,
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

        # фрэймы поля кнопок управления системой охлаждения
        frame_for_start_stop_buttons = LabelFrame(self.frame_for_units, bg="gray80")
        frame_for_start_stop_buttons.pack(side=RIGHT, padx=4, pady=1, fill=X)

        frame_for_dry_status_buttons = LabelFrame(self.frame_for_units, bg="gray80")
        frame_for_dry_status_buttons.pack(side=RIGHT, padx=4, pady=1, fill=X)

        frame_for_version_info_buttons = LabelFrame(self.frame_for_units, bg="gray80")
        frame_for_version_info_buttons.pack(side=LEFT, padx=4, pady=1, fill=X)

        # подполе мини-терминала
        self.info_text_box = Text(self.frame_for_units, relief=GROOVE, width=41, height=6,
                                  selectbackground="grey60")
        self.info_text_box.pack(side=RIGHT, padx=13, pady=10, fill=X)
        self.info_text_box.tag_config('tag_red_text', foreground='red')
        self.info_text_box.tag_config('tag_green_text', foreground='green')
        self.info_text_box.tag_config('tag_black_text', foreground='black')

        # подполе кнопок управления
        start_button = Button(frame_for_start_stop_buttons, text="Start", relief=GROOVE, width=14, height=2,
                              bg="gray60", command=poa_start_command)
        start_button.pack(side=TOP, pady=4, padx=4)

        stop_button = Button(frame_for_start_stop_buttons, text="Stop", relief=GROOVE, width=14, height=2,
                             bg="gray60", command=poa_stop_command)
        stop_button.pack(side=TOP, pady=4, padx=4)

        version_button = Button(frame_for_version_info_buttons, text="Version", relief=GROOVE, width=14, height=2,
                                bg="gray60", command=poa_version_command)
        version_button.pack(side=TOP, pady=4, padx=4)

        info_button = Button(frame_for_version_info_buttons, text="Info", relief=GROOVE, width=14, height=2,
                             bg="gray60", command=poa_info_command)
        info_button.pack(side=TOP, pady=4, padx=4)

        dry_button = Button(frame_for_dry_status_buttons, text="Dry", relief=GROOVE, width=14, height=2,
                            bg="gray60", command=poa_dry_command)
        dry_button.pack(side=TOP, pady=4, padx=4)

        status_button = Button(frame_for_dry_status_buttons, text="Status", relief=GROOVE, width=14, height=2,
                               bg="gray60", command=poa_status_command)
        status_button.pack(side=TOP, pady=4, padx=4)

        # Изменяет состояние кнопок в окне в случае автоматического режима
        if auto:
            self.poa_button.configure(bg="green3", state='disabled', relief=RIDGE)
            self.sth1_button.configure(bg="gray60", state='disabled', relief=GROOVE)
            self.sth2_button.configure(bg="gray60", state='disabled', relief=GROOVE)
            self.sth3_button.configure(bg="gray60", state='disabled', relief=GROOVE)
            self.as_button.configure(bg="gray60", state='disabled', relief=GROOVE)
            self.sc_button.configure(bg="gray60", state='disabled', relief=GROOVE)
            self.ck_button.configure(bg="gray60", state='disabled', relief=GROOVE)
            start_button.configure(bg="gray60", state='disabled', relief=GROOVE)
            stop_button.configure(bg="gray60", state='disabled', relief=GROOVE)
            version_button.configure(bg="gray60", state='disabled', relief=GROOVE)
            info_button.configure(bg="gray60", state='disabled', relief=GROOVE)
            dry_button.configure(bg="gray60", state='disabled', relief=GROOVE)
            status_button.configure(bg="gray60", state='disabled', relief=GROOVE)
        else:
            self.poa_button.configure(bg="green3", state='disabled', relief=RIDGE)
            self.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
            self.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
            self.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
            self.as_button.configure(bg="gray60", state='normal', relief=GROOVE)
            self.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
            self.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)

        if auto:

            def error_control(exception='None'):
                # Функция проверки ошибок из команд от автоматического скрипта
                reset = False

                if exception == "key_exception":
                    poa_auto_errors["key_error"] = False

                for error, status in poa_auto_errors.items():
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
                                              message="Проверьте достаточность подаваемого тока на плату "
                                                      "системы охлаждения (до 3А) - разъём X9, правильность "
                                                      "подключения шлангов, либо корректность подключения датчика и "
                                                      "корректность отображаемых датчиком данных. При повторяющейся "
                                                      "ошибке пересбросьте питание.\n\n"
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

            def step_1():
                self.info_text_box.delete('1.0', END)
                self.start_window.update_idletasks()
                self.info_text_box.insert(END, "⫸ Прогресс ◖▒▒▒▒▒▒▒▒▒▒ 00% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения команды START\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_start_command(False)

                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(2)
                poa_status_command(False)
                return error_control()

            def step_2():
                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖██▒▒▒▒▒▒▒▒ 10% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "[общий анализ]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)

                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.5)
                return error_control()

            def step_3():
                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 20% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "запрос [1]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)
                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)

                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖████▒▒▒▒▒▒ 22% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "запрос [2]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)
                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)

                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖█████▒▒▒▒▒ 25% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "запрос [3]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)
                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)

                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖█████▒▒▒▒▒ 27% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "запрос [4]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)
                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)

                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████▒▒▒▒ 30% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "запрос [5]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)
                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)
                return error_control()

            def step_4():
                self.info_text_box.delete('1.0', END)
                self.start_window.update_idletasks()
                self.info_text_box.insert(END, "⫸ Прогресс ◖████████▒▒ 40% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения команды STOP\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)
                poa_stop_command()

                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(2)
                poa_status_command(False)
                return error_control()

            def step_5():
                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 50% ▒▒▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "[общий анализ]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)

                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.5)
                return error_control()

            def step_6():
                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 60% ██▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "запрос [1]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)
                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)

                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 62% ██▒▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "запрос [2]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)
                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)

                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 65% ███▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "запрос [3]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)
                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)

                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 67% ███▒▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "запрос [4]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)
                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)

                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 70% ████▒▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "запрос [5]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)
                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)
                return error_control()

            def step_7():
                result = askyesno(title="Проверка режима откачки",
                                  message="Поверните ключ в положение <ОТКАЧКА>\n\n"
                                          "<Да> - для продолжения проверки\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            def step_8():
                self.info_text_box.delete('1.0', END)
                self.start_window.update_idletasks()
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 75% █████▒▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения команды DRY\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)
                poa_dry_command()

                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(2)
                poa_status_command(False)
                return error_control()

            def step_9():
                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 80% ██████▒▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "[общий анализ]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)

                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.5)
                return error_control()

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

            def step_11():
                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 85% ███████▒▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "[общий анализ]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)
                poa_status_command(False)

                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)
                return error_control("key_exception")

            def step_12():
                self.info_text_box.delete('1.0', END)
                self.start_window.update_idletasks()
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 90% ████████▒▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения команды START\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.1)
                poa_start_command()

                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(2)
                poa_status_command(False)
                return error_control()

            def step_13():
                self.info_text_box.delete('1.0', END)
                self.info_text_box.insert(END, "⫸ Прогресс ◖██████████ 95% █████████▒◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Проверка выполнения опроса состояния \nсистемы (STATUS) - "
                                               "[общий анализ]\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)

                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                time.sleep(0.5)
                return error_control()

            def step_14():
                time.sleep(0.1)
                poa_stop_command()
                time.sleep(2)
                self.info_text_box.delete('1.0', END)
                self.start_window.update_idletasks()
                self.info_text_box.insert(END, "⫸ Прогресс ◖█████████ 100% ██████████◗\n", 'tag_green_text')
                self.info_text_box.insert(END, "⫸ Остановка работы системы\n", 'tag_black_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                poa_status_command(False)
                time.sleep(0.1)
                self.info_text_box.insert(END, "✔ Ответ получен и проверен\n", 'tag_green_text')
                self.info_text_box.yview(END)
                self.start_window.update_idletasks()
                return error_control()

            def step_15():
                result = askyesno(title="Проверка работы завершена",
                                  message="Проверка завершена успешно.\nПоказатели соответствуют норме.\n\n"
                                          "<Да> - для повторной проверки\n\n"
                                          "<Нет> - для выхода в ручной режим")
                if result:
                    return True
                else:
                    return False

            def check_step(step_number):
                out = None

                if step_number == 1:
                    out = step_1()
                elif step_number == 2:
                    out = step_2()
                elif step_number == 3:
                    out = step_3()
                elif step_number == 4:
                    out = step_4()
                elif step_number == 5:
                    out = step_5()
                elif step_number == 6:
                    out = step_6()
                elif step_number == 8:
                    out = step_8()
                elif step_number == 9:
                    out = step_9()
                elif step_number == 10:
                    out = step_10()
                elif step_number == 11:
                    out = step_11()
                elif step_number == 12:
                    out = step_12()
                elif step_number == 13:
                    out = step_13()
                elif step_number == 14:
                    out = step_14()
                elif step_number == 15:
                    out = step_15()

                if poa_auto_errors["beeper_error"]:
                    while poa_auto_errors["beeper_error"]:
                        time.sleep(1)
                        poa_status_command(False)
                if out:
                    while out:
                        if step_number != 1:
                            if step_number == 1 or step_number == 2 or step_number == 3 or step_number == 12 or \
                                    step_number == 13:
                                poa_stop_command()
                                poa_start_command(False)
                            if step_number == 4 or step_number == 5 or step_number == 6 or step_number == 9 or \
                                    step_number == 11 or step_number == 14:
                                poa_stop_command()
                            if step_number == 8:
                                poa_dry_command()
                        if step_number == 1:
                            out = step_1()
                        elif step_number == 2:
                            out = step_2()
                        elif step_number == 3:
                            out = step_3()
                        elif step_number == 4:
                            out = step_4()
                        elif step_number == 5:
                            out = step_5()
                        elif step_number == 6:
                            out = step_6()
                        elif step_number == 8:
                            out = step_8()
                        elif step_number == 9:
                            out = step_9()
                        elif step_number == 11:
                            out = step_11()
                        elif step_number == 12:
                            out = step_12()
                        elif step_number == 13:
                            out = step_13()
                        elif step_number == 14:
                            out = step_14()
                    else:
                        if out is None:
                            pass
                        else:
                            self.manual_parameters()
                            self.poa_unit()
                            self.info_text_box.delete('1.0', END)
                            self.info_text_box.insert(END, "❌ АВТОМАТИЧЕСКАЯ ПРОВЕРКА ОСТАНОВЛЕНА\n", 'tag_red_text')
                            self.info_text_box.insert(END, "⫸ Программа переведена в ручной режим\n", 'tag_black_text')
                            self.info_text_box.yview(END)
                            self.start_window.update_idletasks()
                            return True
                elif out is None:
                    pass
                else:
                    self.manual_parameters()
                    self.poa_unit()
                    self.info_text_box.delete('1.0', END)
                    self.info_text_box.insert(END, "❌ АВТОМАТИЧЕСКАЯ ПРОВЕРКА ОСТАНОВЛЕНА\n", 'tag_red_text')
                    self.info_text_box.insert(END, "⫸ Программа переведена в ручной режим\n", 'tag_black_text')
                    self.info_text_box.yview(END)
                    self.start_window.update_idletasks()
                    return True
                return

            def start_check():
                # Запуск скрипта автоматической проверки системы охлаждения
                if not check_step(1):
                    if not check_step(2):
                        if not check_step(3):
                            if not check_step(4):
                                if not check_step(5):
                                    if not check_step(6):
                                        if not step_7():
                                            self.manual_parameters()
                                            self.poa_unit()
                                            self.info_text_box.delete('1.0', END)
                                            self.info_text_box.insert(END, "❌ АВТОМАТИЧЕСКАЯ ПРОВЕРКА ОСТАНОВЛЕНА\n",
                                                                      'tag_red_text')
                                            self.info_text_box.insert(END, "⫸ Программа переведена в ручной режим\n",
                                                                      'tag_black_text')
                                            self.info_text_box.yview(END)
                                            self.start_window.update_idletasks()
                                            return
                                        else:
                                            if not check_step(8):
                                                if not check_step(9):
                                                    if not step_10():
                                                        self.manual_parameters()
                                                        self.poa_unit()
                                                        self.info_text_box.delete('1.0', END)
                                                        self.info_text_box.insert(END,
                                                                                  "❌ АВТОМАТИЧЕСКАЯ ПРОВЕРКА "
                                                                                  "ОСТАНОВЛЕНА\n", 'tag_red_text')
                                                        self.info_text_box.insert(END,
                                                                                  "⫸ Программа переведена в ручной "
                                                                                  "режим\n", 'tag_black_text')
                                                        self.info_text_box.yview(END)
                                                        self.start_window.update_idletasks()
                                                        return
                                                    else:
                                                        if not check_step(11):
                                                            if not check_step(12):
                                                                if not check_step(13):
                                                                    if not check_step(14):
                                                                        if not step_15():
                                                                            self.manual_parameters()
                                                                            self.poa_unit()
                                                                            self.info_text_box.delete('1.0', END)
                                                                            self.info_text_box.insert(END,
                                                                                                      "❌ АВТОМАТИЧЕСКАЯ"
                                                                                                      " ПРОВЕРКА"
                                                                                                      " ОСТАНОВЛЕНА\n",
                                                                                                      'tag_red_text')
                                                                            self.info_text_box.insert(END,
                                                                                                      "⫸ Программа "
                                                                                                      "переведена в "
                                                                                                      "ручной режим\n",
                                                                                                      'tag_black_text')
                                                                            self.info_text_box.yview(END)
                                                                            self.start_window.update_idletasks()
                                                                            return
                                                                        else:
                                                                            start_check()

            start_check()

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
        # Устанавливает параметры COM-порта
        bytesize = self.bytesize_combobox.get()
        request_and_port_list.com_port_settings["bytesize"] = bytesize
        self.bytesize_combobox.configure(foreground="green3")
        timeout = self.timeout_combobox.get()
        request_and_port_list.com_port_settings["baudrate"] = timeout
        self.timeout_combobox.configure(foreground="green3")
        baudrate = self.baudrate_combobox.get()
        request_and_port_list.com_port_settings["baudrate"] = baudrate
        self.baudrate_combobox.configure(foreground="green3")
        comport = self.port_combobox.get()
        request_and_port_list.com_port_settings["comport"] = comport
        self.port_combobox.configure(foreground="green3")
        try:
            serial.Serial(request_and_port_list.com_port_settings["comport"])
            self.set_button.configure(background="PaleGreen3")
            self.info_text_box.insert(END, "✔ Подключено к порту " + comport + "\n", 'tag_green_text')
            self.info_text_box.yview(END)
        except serial.serialutil.SerialException:
            self.port_combobox.configure(foreground="brown1")
            self.set_button.configure(background="brown1")
            self.info_text_box.insert(END, "❌ Порт " + comport + " недоступен\n", 'tag_red_text')
            self.info_text_box.yview(END)

    def manual_parameters(self):
        # Функционал кнопки "Manual", разблокирует ручное управление
        self.auto_button.configure(bg="gray60", state="normal", relief=GROOVE)
        self.manual_button.configure(bg="PaleGreen3", state="disabled", relief=RIDGE)
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)
        self.poa_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth1_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth2_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sth3_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.as_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.sc_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.ck_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.set_button.configure(bg="gray60", state='normal', relief=GROOVE)
        self.timeout_combobox.configure(state='readonly')
        self.baudrate_combobox.configure(state='readonly')
        self.port_combobox.configure(state='readonly')
        self.bytesize_combobox.configure(state='readonly')

    def auto_parameters(self):
        # функционал кнопки "Auto" (не доработан)
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

        #
        ###
        #

        # Прописывает с нуля интерфейсный фрейм
        if self.frame_for_units:
            self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        def com_ports():
            # Функция работы с COM-портами
            
            def update_info(port_number, message):
                # Функция обновления отображений портов

                # Обновляю поле отчёта о поиске портов
                self.status_text_box.insert(END, message)
                self.status_text_box.update()
                self.status_text_box.yview(END)

                # обновляю шкалу загрузки
                process_progressbar["value"] = port_number * 2
                process_progressbar.update()

            def find_device():
                # Функция поиска подключённых устройств

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
                    request_and_port_list.com_port_settings["comport"] = extracted_port
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
                            answer = request_response.command_sender(accepted_request=request)
                            if answer:
                                poa_label.config(background="SeaGreen1")
                                poa_label.update()
                                answer = request_name
                                if self.start_window:
                                    self.start_window.destroy()
                                if self.full_auto_init_window:
                                    self.full_auto_init_window.destroy()
                                AdjustmentUtility().main_frame_unit(request_name)
                                return answer
                            else:
                                poa_label.config(background="gray90")
                                poa_label.update()

                        elif request_name == "sth_1_request":
                            sth1_label.config(background="deep sky blue")
                            sth1_label.update()
                            answer = request_response.command_sender(accepted_request=request)
                            if answer:
                                sth1_label.config(background="SeaGreen1")
                                sth1_label.update()
                                answer = request_name
                                if self.start_window:
                                    self.start_window.destroy()
                                if self.full_auto_init_window:
                                    self.full_auto_init_window.destroy()
                                AdjustmentUtility().main_frame_unit(request_name)
                                return answer
                            else:
                                sth1_label.config(background="gray90")
                                sth1_label.update()

                        elif request_name == "sth_2_request":
                            sth2_label.config(background="deep sky blue")
                            sth2_label.update()
                            answer = request_response.command_sender(accepted_request=request)
                            if answer:
                                sth2_label.config(background="SeaGreen1")
                                sth2_label.update()
                                answer = request_name
                                if self.start_window:
                                    self.start_window.destroy()
                                if self.full_auto_init_window:
                                    self.full_auto_init_window.destroy()
                                AdjustmentUtility().main_frame_unit(request_name)
                                return answer
                            else:
                                sth2_label.config(background="gray90")
                                sth2_label.update()

                        elif request_name == "sth_3_request":
                            sth3_label.config(background="deep sky blue")
                            sth3_label.update()
                            answer = request_response.command_sender(accepted_request=request)
                            if answer:
                                sth3_label.config(background="SeaGreen1")
                                sth3_label.update()
                                answer = request_name
                                if self.start_window:
                                    self.start_window.destroy()
                                if self.full_auto_init_window:
                                    self.full_auto_init_window.destroy()
                                AdjustmentUtility().main_frame_unit(request_name)
                                return answer
                            else:
                                sth3_label.config(background="gray90")
                                sth3_label.update()

                        elif request_name == "sc_request":
                            sc_label.config(background="deep sky blue")
                            sc_label.update()
                            answer = request_response.command_sender(accepted_request=request)
                            if answer:
                                sc_label.config(background="SeaGreen1")
                                sc_label.update()
                                answer = request_name
                                if self.start_window:
                                    self.start_window.destroy()
                                if self.full_auto_init_window:
                                    self.full_auto_init_window.destroy()
                                AdjustmentUtility().main_frame_unit(request_name)
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
            # Запускает поиск
            self.status_text_box.delete(0, END)
            self.device_signature = com_ports()
            no_signature()
            return

        def no_signature():
            # Исключение - ничего не нашло

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
                # БЛИН, ТУТ НУЖНО ЧТО-ТО ДУМАТЬ. СУММА НЕ ТО, ЧЕМ КАЖЕТСЯ
                # Проверяет контрольную сумму
                bit_1_hex = bit_1_entry.get().upper()
                bit_2_hex = bit_2_entry.get().upper()
                bit_3_hex = bit_3_entry.get().upper()
                bit_4_hex = bit_4_entry.get().upper()
                bit_5_hex = bit_5_entry.get().upper()
                bit_6_hex = bit_6_entry.get().upper()
                bit_7_hex = bit_7_entry.get().upper()
                print(bit_1_hex + bit_2_hex + bit_3_hex)

                bit_1_dec = int(bit_1_hex, 16)
                bit_2_dec = int(bit_2_hex, 16)
                bit_3_dec = int(bit_3_hex, 16)
                bit_4_dec = int(bit_4_hex, 16)
                bit_5_dec = int(bit_5_hex, 16)
                bit_6_dec = int(bit_6_hex, 16)
                bit_7_dec = int(bit_7_hex, 16)
                print(str(bit_1_dec) + ":" + str(bit_2_dec) + ":" + str(bit_3_dec))

                full_hex_summ = bit_1_dec + bit_2_dec + bit_3_dec + bit_4_dec + bit_5_dec + bit_6_dec + bit_7_dec
                print(full_hex_summ)
                # Округление до сотен

                def ceil_to(num, to):
                    return ceil(num / to) * to

                bit_8_max = ceil_to(full_hex_summ, 100)
                bit_8_dec = bit_8_max - full_hex_summ
                print(bit_8_dec)
                bit_8_hex = hex(bit_8_dec)
                print(bit_8_hex)

                """
                full_dec_summ = 0
                full_hex_summ = 0
                for bit in range(0, 20):
                    if bit % 2 != 0:
                        hex_bit = recieved_command[bit - 1] + recieved_command[bit]
                        full_dec_summ = full_dec_summ + int(hex_bit, 16)
                        full_hex_summ = hex(full_dec_summ)
                if full_hex_summ[len(full_hex_summ) - 1] == "0":
                    crc_label.config(bg="PaleGreen3", text="OK")
                    poa_auto_errors["crc_error"] = False
                else:
                    crc_label.config(bg="salmon", text=str(full_hex_summ))
                    poa_auto_errors["crc_error"] = True
                crc_data.config(text=recieved_command[18].upper() + recieved_command[19].upper())
                pass
                """

            def string_check_crc():
                pass

            def send_bit_command():
                left_terminal_text_box.insert(END, "40 15 74 1C 7E 00 00 68 ⮘ crc ok")
                left_terminal_text_box.update()
                left_terminal_text_box.yview(END)
                pass

            def send_string_command():
                pass

            def validate_command_1(bit):
                if len(bit) == 1:
                    return bit == "" or bit.isnumeric() or bit.isalpha()
                elif len(bit) == 2:
                    if bit[1].isnumeric() or bit[1].isalpha():
                        bit_2_entry.focus_set()
                        bit_1_entry.config(background="PaleGreen3")
                    return bit[1] == "" or bit[1].isnumeric() or bit[1].isalpha()
                else:
                    bit_1_entry.config(background="salmon")
                    bit_1_entry.update()
                    time.sleep(0.1)
                    bit_1_entry.config(background="PaleGreen3")
                    return bit == ""

            def validate_command_2(bit):
                if len(bit) == 1:
                    return bit == "" or bit.isnumeric() or bit.isalpha()
                elif len(bit) == 2:
                    if bit[1].isnumeric() or bit[1].isalpha():
                        bit_3_entry.focus_set()
                        bit_2_entry.config(background="PaleGreen3")
                    return bit[1] == "" or bit[1].isnumeric() or bit[1].isalpha()
                else:
                    bit_2_entry.config(background="salmon")
                    bit_2_entry.update()
                    time.sleep(0.1)
                    bit_2_entry.config(background="PaleGreen3")
                    return bit == ""

            def validate_command_3(bit):
                if len(bit) == 1:
                    return bit == "" or bit.isnumeric() or bit.isalpha()
                elif len(bit) == 2:
                    if bit[1].isnumeric() or bit[1].isalpha():
                        bit_4_entry.focus_set()
                        bit_3_entry.config(background="PaleGreen3")
                    return bit[1] == "" or bit[1].isnumeric() or bit[1].isalpha()
                else:
                    bit_3_entry.config(background="salmon")
                    bit_3_entry.update()
                    time.sleep(0.1)
                    bit_3_entry.config(background="PaleGreen3")
                    return bit == ""

            def validate_command_4(bit):
                if len(bit) == 1:
                    return bit == "" or bit.isnumeric() or bit.isalpha()
                elif len(bit) == 2:
                    if bit[1].isnumeric() or bit[1].isalpha():
                        bit_5_entry.focus_set()
                        bit_4_entry.config(background="PaleGreen3")
                    return bit[1] == "" or bit[1].isnumeric() or bit[1].isalpha()
                else:
                    bit_4_entry.config(background="salmon")
                    bit_4_entry.update()
                    time.sleep(0.1)
                    bit_4_entry.config(background="PaleGreen3")
                    return bit == ""

            def validate_command_5(bit):
                if len(bit) == 1:
                    return bit == "" or bit.isnumeric() or bit.isalpha()
                elif len(bit) == 2:
                    if bit[1].isnumeric() or bit[1].isalpha():
                        bit_6_entry.focus_set()
                        bit_5_entry.config(background="PaleGreen3")
                    return bit[1] == "" or bit[1].isnumeric() or bit[1].isalpha()
                else:
                    bit_5_entry.config(background="salmon")
                    bit_5_entry.update()
                    time.sleep(0.1)
                    bit_5_entry.config(background="PaleGreen3")
                    return bit == ""

            def validate_command_6(bit):
                if len(bit) == 1:
                    return bit == "" or bit.isnumeric() or bit.isalpha()
                elif len(bit) == 2:
                    if bit[1].isnumeric() or bit[1].isalpha():
                        bit_7_entry.focus_set()
                        bit_6_entry.config(background="PaleGreen3")
                    return bit[1] == "" or bit[1].isnumeric() or bit[1].isalpha()
                else:
                    bit_6_entry.config(background="salmon")
                    bit_6_entry.update()
                    time.sleep(0.1)
                    bit_6_entry.config(background="PaleGreen3")
                    return bit == ""

            def validate_command_7(bit):
                if len(bit) == 1:
                    return bit == "" or bit.isnumeric() or bit.isalpha()
                elif len(bit) == 2:
                    if bit[1].isnumeric() or bit[1].isalpha():
                        bit_check_crc_button.focus_set()
                        bit_7_entry.config(background="PaleGreen3")
                    return bit[1] == "" or bit[1].isnumeric() or bit[1].isalpha()
                else:
                    bit_7_entry.config(background="salmon")
                    bit_7_entry.update()
                    time.sleep(0.1)
                    bit_7_entry.config(background="PaleGreen3")
                    return bit == ""

            def validate_command_8(bit):
                if len(bit) == 1:
                    return bit == "" or bit.isnumeric() or bit.isalpha()
                elif len(bit) == 2:
                    if bit[1].isnumeric() or bit[1].isalpha():
                        bit_check_crc_button.focus_set()
                        bit_8_entry.config(background="PaleGreen3")
                    return bit[1] == "" or bit[1].isnumeric() or bit[1].isalpha()
                else:
                    bit_8_entry.config(background="salmon")
                    bit_8_entry.update()
                    time.sleep(0.1)
                    bit_8_entry.config(background="PaleGreen3")
                    return bit == ""

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
            check_1_bit = (frame_for_per_byte_command.register(validate_command_1), "%P")
            bit_1_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, background="grey100",
                                validate="key", validatecommand=check_1_bit)
            bit_1_entry.pack(side=LEFT, padx=1, pady=1, fill=X)
            bit_1_entry.focus_set()

            check_2_bit = (frame_for_per_byte_command.register(validate_command_2), "%P")
            bit_2_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, background="grey100",
                                validate="key", validatecommand=check_2_bit)
            bit_2_entry.pack(side=LEFT, padx=1, pady=1, fill=X)

            check_3_bit = (frame_for_per_byte_command.register(validate_command_3), "%P")
            bit_3_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, background="grey100",
                                validate="key", validatecommand=check_3_bit)
            bit_3_entry.pack(side=LEFT, padx=1, pady=1, fill=X)

            check_4_bit = (frame_for_per_byte_command.register(validate_command_4), "%P")
            bit_4_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, background="grey100",
                                validate="key", validatecommand=check_4_bit)
            bit_4_entry.pack(side=LEFT, padx=1, pady=1, fill=X)

            check_5_bit = (frame_for_per_byte_command.register(validate_command_5), "%P")
            bit_5_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, background="grey100",
                                validate="key", validatecommand=check_5_bit)
            bit_5_entry.pack(side=LEFT, padx=1, pady=1, fill=X)

            check_6_bit = (frame_for_per_byte_command.register(validate_command_6), "%P")
            bit_6_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, background="grey100",
                                validate="key", validatecommand=check_6_bit)
            bit_6_entry.pack(side=LEFT, padx=1, pady=1, fill=X)

            check_7_bit = (frame_for_per_byte_command.register(validate_command_7), "%P")
            bit_7_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, background="grey100",
                                validate="key", validatecommand=check_7_bit)
            bit_7_entry.pack(side=LEFT, padx=1, pady=1, fill=X)

            check_8_bit = (frame_for_per_byte_command.register(validate_command_8), "%P")
            bit_8_entry = Entry(frame_for_per_byte_command, relief=GROOVE, width=4, background="grey80",
                                validate="key", validatecommand=check_8_bit)
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

    def main_frame_unit(self, device):
        """Запускает первичное окно с основным функционалом, в которое потом интегрируются модули каждой из систем"""

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

        port_numbers = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10", "COM11",
                        "COM12", "COM13", "COM14", "COM15", "COM16", "COM17", "COM18", "COM19", "COM20"]
        self.port_combobox = ttk.Combobox(frame_for_settings, values=port_numbers, width=8, height=5, state="readonly")
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

        if device == "manual":
            self.manual_parameters()

        if device == "poa_request":
            self.poa_unit(True)

        self.start_window.mainloop()
