import request_and_port_list


def transcript_other_stuff(gui, recieved_command=None):
    # Расшифровка прочих параметров из полученной команды

    def transcript_status_device():
        # расшифровка поля Device

        device_hex = recieved_command[0] + recieved_command[1]
        if device_hex == "40":
            gui.device_label.config(text="OK", bg="PaleGreen3")
        else:
            gui.device_label.config(text="❌", bg="salmon")
        gui.device_data.config(text=device_hex.upper())

    def transcript_status_t_max():
        # расшифровка поля t_max

        t_max_hex = recieved_command[6] + recieved_command[7]
        t_max_dec = int(t_max_hex, 16)
        if 10 <= t_max_dec <= 45:
            gui.t_max_label.config(bg="PaleGreen3")
            gui.poa_auto_errors["t_max_error"] = False
        else:
            gui.poa_auto_errors["t_max_error"] = True
            if t_max_dec == 255:
                gui.poa_auto_errors["t_max_error"] = 255
            gui.t_max_label.config(bg="salmon")
        gui.t_max_label.config(text=str(t_max_dec).upper())
        gui.t_max_data.config(text=t_max_hex.upper())

    def transcript_status_t_min():
        # расшифровка поля t_min

        t_min_hex = recieved_command[8] + recieved_command[9]
        t_min_dec = int(t_min_hex, 16)
        if 10 <= t_min_dec <= 45:
            gui.t_min_label.config(bg="PaleGreen3")
            gui.poa_auto_errors["t_min_error"] = False
        else:
            gui.poa_auto_errors["t_min_error"] = True
            if t_min_dec == 255:
                gui.poa_auto_errors["t_min_error"] = 255
            gui.t_min_label.config(bg="salmon")
        gui.t_min_label.config(text=str(t_min_dec).upper())
        gui.t_min_data.config(text=t_min_hex.upper())

    def transcript_status_flow():
        # расшифровка поля flow

        flow_hex = recieved_command[10] + recieved_command[11]
        flow_dec = int(flow_hex, 16)
        flow_real = round(float(flow_dec / 73), 2)
        if gui.last_command_except_status == request_and_port_list.poa_request_dictionary["dry_poa_package"] \
                or gui.last_command_except_status == \
                request_and_port_list.poa_request_dictionary["stop_poa_package"]:
            if flow_real < 1:
                gui.flow_label.config(bg="PaleGreen3")
                gui.poa_auto_errors["flow_error"] = False
            else:
                gui.flow_label.config(bg="salmon")
                gui.poa_auto_errors["flow_error"] = True
        else:
            if 1.9 <= flow_real <= 5:
                gui.flow_label.config(bg="PaleGreen3")
                gui.poa_auto_errors["flow_error"] = False
            else:
                gui.flow_label.config(bg="salmon")
                gui.poa_auto_errors["flow_error"] = True
        gui.flow_label.config(text=str(flow_real))
        gui.flow_data.config(text=flow_hex.upper())

    def transcript_status_errors():
        # расшифровка поля errors
        errors_hex = recieved_command[12] + recieved_command[13]
        if errors_hex == "00" or errors_hex == "10":
            gui.errors_label.config(bg="PaleGreen3", text="OK")
            gui.poa_auto_errors["errors_error"] = False
        else:
            gui.errors_label.config(bg="salmon", text=errors_hex)
            gui.poa_auto_errors["errors_error"] = True
        gui.errors_data.config(text=errors_hex.upper())

    def transcript_status_pwm_1_2():
        # расшифровка полей pwm

        pwm_1_hex = recieved_command[14] + recieved_command[15]
        pwm_2_hex = recieved_command[16] + recieved_command[17]
        pwm_1_dec = int(pwm_1_hex, 16)
        pwm_2_dec = int(pwm_2_hex, 16)
        pwm_1_percent = int(pwm_1_dec * 100 / 254)
        pwm_2_percent = int(pwm_2_dec * 100 / 254)
        if gui.last_command_except_status == request_and_port_list.poa_request_dictionary["dry_poa_package"] \
                or gui.last_command_except_status == \
                request_and_port_list.poa_request_dictionary["stop_poa_package"]:
            if pwm_1_percent < 10:
                gui.pwm_1_label.config(bg="PaleGreen3", text=str(pwm_1_percent) + "%")
                gui.poa_auto_errors["pwm_1_2_error"] = False
            else:
                gui.pwm_1_label.config(bg="salmon", text=str(pwm_1_percent) + "%")
                gui.poa_auto_errors["pwm_1_2_error"] = True
            if pwm_2_percent < 10:
                gui.pwm_2_label.config(bg="PaleGreen3", text=str(pwm_2_percent) + "%")
                gui.poa_auto_errors["pwm_1_2_error"] = False
            else:
                gui.pwm_2_label.config(bg="salmon", text=str(pwm_2_percent) + "%")
                gui.poa_auto_errors["pwm_1_2_error"] = True
        else:
            if pwm_1_percent + pwm_2_percent == 100:
                gui.pwm_1_label.config(bg="PaleGreen3", text=str(pwm_1_percent) + "%")
                gui.pwm_2_label.config(bg="PaleGreen3", text=str(pwm_2_percent) + "%")
                gui.poa_auto_errors["pwm_1_2_error"] = False
            else:
                gui.pwm_1_label.config(bg="salmon", text=str(pwm_1_percent) + "%")
                gui.pwm_2_label.config(bg="salmon", text=str(pwm_2_percent) + "%")
                gui.poa_auto_errors["pwm_1_2_error"] = True
        gui.pwm_1_data.config(text=pwm_1_hex.upper())
        gui.pwm_2_data.config(text=pwm_2_hex.upper())

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
            gui.crc_label.config(bg="PaleGreen3", text="OK")
            gui.poa_auto_errors["crc_error"] = False
        else:
            gui.crc_label.config(bg="salmon", text=str(full_hex_summ))
            gui.poa_auto_errors["crc_error"] = True
        gui.crc_data.config(text=recieved_command[18].upper() + recieved_command[19].upper())

    transcript_status_device()
    transcript_status_t_max()
    transcript_status_t_min()
    transcript_status_flow()
    transcript_status_errors()
    transcript_status_pwm_1_2()
    check_crc()


def transcript_statuses(gui, recieved_command=None, send_command=None):
    # Расшифровывает статусы из полученных ответов от контроллера

    gui.poa_auto_errors = {
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

    if gui.last_command_except_status is None:
        gui.last_command_except_status = request_and_port_list.poa_request_dictionary["start_poa_package"]

    if recieved_command:

        # Превращает из хексов в бины и выводит значения
        status_ctrl_hex = recieved_command[2] + recieved_command[3]
        binary_status_ctrl = "{0:08b}".format(int(status_ctrl_hex, 16))
        gui.stat_ctrl_data.config(text=status_ctrl_hex.upper(), bg="gray90")

        # Превращает из хексов в бины и выводит значения
        status_sens_hex = recieved_command[4] + recieved_command[5]
        binary_status_sens = "{0:08b}".format(int(status_sens_hex, 16))
        gui.stat_sens_data.config(text=status_sens_hex.upper(), bg="gray90")

        # Расшифровки и отображение Статуса сенсоров
        red_green_status_sens = "green"
        red_green_status_ctrl = "green"

        for bit_number in range(0, 8):
            if bit_number == 0:
                if int(binary_status_sens[bit_number]) == 0:
                    gui.reserve_3_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                    gui.reserve_3_label.config(bg="PaleGreen3")
                else:
                    gui.reserve_3_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                    gui.reserve_3_label.config(bg="salmon")
                    if red_green_status_sens == "green":
                        red_green_status_sens = "red"

            if bit_number == 1:
                if int(binary_status_sens[bit_number]) == 0:
                    gui.reserve_2_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                    gui.reserve_2_label.config(bg="PaleGreen3")
                else:
                    gui.reserve_2_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                    gui.reserve_2_label.config(bg="salmon")
                    if red_green_status_sens == "green":
                        red_green_status_sens = "red"

            if bit_number == 2:
                if int(binary_status_sens[bit_number]) == 0:
                    gui.reserve_1_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                    gui.reserve_1_label.config(bg="PaleGreen3")
                else:
                    gui.reserve_1_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                    gui.reserve_1_label.config(bg="salmon")
                    if red_green_status_sens == "green":
                        red_green_status_sens = "red"

            if bit_number == 3:
                if int(binary_status_sens[bit_number]) == 0:
                    gui.wls_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                    gui.wls_label.config(bg="PaleGreen3")
                    gui.poa_auto_errors["wls_error"] = False
                else:
                    gui.wls_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                    gui.wls_label.config(bg="salmon")
                    gui.poa_auto_errors["wls_error"] = True
                    if red_green_status_sens == "green":
                        red_green_status_sens = "red"

            if bit_number == 4:
                if gui.last_command_except_status == \
                        request_and_port_list.poa_request_dictionary["stop_poa_package"]:
                    gui.key_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                    gui.key_label.config(bg="PaleGreen3")
                    gui.poa_auto_errors["key_error"] = False
                elif gui.last_command_except_status == \
                        request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                    if int(binary_status_sens[bit_number]) == 1:
                        gui.key_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                        gui.key_label.config(bg="salmon")
                        gui.poa_auto_errors["key_error"] = True
                        if red_green_status_sens == "green":
                            red_green_status_sens = "red"
                    else:
                        gui.key_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                        gui.key_label.config(bg="PaleGreen3")
                        gui.poa_auto_errors["key_error"] = False
                elif gui.last_command_except_status == \
                        request_and_port_list.poa_request_dictionary["start_poa_package"] or \
                        gui.last_command_except_status is None:
                    if int(binary_status_sens[bit_number]) == 0:
                        gui.key_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                        gui.key_label.config(bg="salmon")
                        gui.poa_auto_errors["key_error"] = True
                        if red_green_status_sens == "green":
                            red_green_status_sens = "red"
                    else:
                        gui.key_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                        gui.key_label.config(bg="PaleGreen3")
                        gui.poa_auto_errors["key_error"] = False

            if bit_number == 5:
                if int(binary_status_sens[bit_number]) == 0:
                    gui.svs_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                    gui.svs_label.config(bg="PaleGreen3")
                    gui.poa_auto_errors["svs_error"] = False
                else:
                    gui.svs_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                    gui.svs_label.config(bg="salmon")
                    gui.poa_auto_errors["svs_error"] = True
                    if red_green_status_sens == "green":
                        red_green_status_sens = "red"

            if bit_number == 6:
                if int(binary_status_sens[bit_number]) == 0:
                    gui.wts2_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                    gui.wts2_label.config(bg="PaleGreen3")
                    gui.poa_auto_errors["wts2_error"] = False
                else:
                    gui.wts2_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                    gui.wts2_label.config(bg="salmon")
                    gui.poa_auto_errors["wts2_error"] = True
                    if red_green_status_sens == "green":
                        red_green_status_sens = "red"

            if bit_number == 7:
                if int(binary_status_sens[bit_number]) == 0:
                    gui.wts1_bit.config(text=binary_status_sens[bit_number], bg="PaleGreen3")
                    gui.wts1_label.config(bg="PaleGreen3")
                    gui.poa_auto_errors["wts1_error"] = False
                else:
                    gui.wts1_bit.config(text=binary_status_sens[bit_number], bg="salmon")
                    gui.wts1_label.config(bg="salmon")
                    gui.poa_auto_errors["wts1_error"] = True
                    if red_green_status_sens == "green":
                        red_green_status_sens = "red"

            if red_green_status_sens == "green":
                gui.stat_sens_label.config(text="OK", bg="PaleGreen3")
            else:
                gui.stat_sens_label.config(text="❌", bg="salmon")

        """
        Раскидка битов и статусов по Статус контроль
        """

        for bit_number in range(0, 8):

            if bit_number == 0:
                if int(binary_status_ctrl[bit_number]) == 0:
                    gui.reserve_5_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                    gui.reserve_5_label.config(bg="PaleGreen3")
                else:
                    gui.reserve_5_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                    gui.reserve_5_label.config(bg="salmon")
                    if red_green_status_ctrl == "green":
                        red_green_status_ctrl = "red"

            if bit_number == 1:
                if int(binary_status_ctrl[bit_number]) == 0:
                    gui.reserve_4_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                    gui.reserve_4_label.config(bg="PaleGreen3")
                else:
                    gui.reserve_4_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                    gui.reserve_4_label.config(bg="salmon")
                    if red_green_status_ctrl == "green":
                        red_green_status_ctrl = "red"

            if send_command == request_and_port_list.poa_request_dictionary["status_poa_package"]:

                if bit_number == 2:
                    if gui.last_command_except_status == \
                            request_and_port_list.poa_request_dictionary["start_poa_package"] \
                            or gui.last_command_except_status is None:
                        if int(binary_status_ctrl[bit_number]) == 1:
                            gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.rfe_label.config(bg="PaleGreen3")
                        else:
                            gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            gui.rfe_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                    elif gui.last_command_except_status == \
                            request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.rfe_label.config(bg="PaleGreen3")
                        else:
                            gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                            gui.rfe_label.config(bg="RoyalBlue1")
                    else:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.rfe_label.config(bg="PaleGreen3")
                        else:
                            gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            gui.rfe_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"

                if bit_number == 3:
                    if gui.last_command_except_status == \
                            request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            gui.beeper_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.beeper_label.config(bg="PaleGreen3")
                            gui.poa_auto_errors["beeper_error"] = False
                        else:
                            gui.beeper_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                            gui.beeper_label.config(bg="RoyalBlue1")
                            gui.poa_auto_errors["beeper_error"] = False
                    else:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            gui.beeper_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.beeper_label.config(bg="PaleGreen3")
                            gui.poa_auto_errors["beeper_error"] = False
                        else:
                            gui.beeper_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            gui.beeper_label.config(bg="salmon")
                            gui.poa_auto_errors["beeper_error"] = True
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"

                if bit_number == 4:
                    if gui.last_command_except_status == \
                            request_and_port_list.poa_request_dictionary["start_poa_package"] \
                            or gui.last_command_except_status is None:
                        if int(binary_status_ctrl[bit_number]) == 1:
                            gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.srs_label.config(bg="PaleGreen3")
                        else:
                            gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            gui.srs_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                    elif gui.last_command_except_status == \
                            request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.srs_label.config(bg="PaleGreen3")
                        else:
                            gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                            gui.srs_label.config(bg="RoyalBlue1")
                    else:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.srs_label.config(bg="PaleGreen3")
                        else:
                            gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            gui.srs_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"

                if bit_number == 5:
                    if gui.last_command_except_status == \
                            request_and_port_list.poa_request_dictionary["start_poa_package"] \
                            or gui.last_command_except_status is None:
                        if int(binary_status_ctrl[bit_number]) == 1:
                            gui.acf_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.acf_label.config(bg="PaleGreen3")
                        else:
                            gui.acf_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            gui.acf_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                    else:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            gui.acf_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.acf_label.config(bg="PaleGreen3")
                        else:
                            gui.acf_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            gui.acf_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"

                if bit_number == 6:
                    if gui.last_command_except_status == \
                            request_and_port_list.poa_request_dictionary["start_poa_package"] \
                            or gui.last_command_except_status is None:
                        if int(binary_status_ctrl[bit_number]) == 1:
                            gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.wpp_label.config(bg="PaleGreen3")
                        else:
                            gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            gui.wpp_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                    elif gui.last_command_except_status == \
                            request_and_port_list.poa_request_dictionary["dry_poa_package"]:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.wpp_label.config(bg="PaleGreen3")
                        else:
                            gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                            gui.wpp_label.config(bg="RoyalBlue1")
                    else:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.wpp_label.config(bg="PaleGreen3")
                        else:
                            gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            gui.wpp_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"

            if send_command == request_and_port_list.poa_request_dictionary["start_poa_package"]:

                if bit_number == 2:
                    if int(binary_status_ctrl[bit_number]) == 0:
                        gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.rfe_label.config(bg="PaleGreen3")
                    else:
                        gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.rfe_label.config(bg="salmon")
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if bit_number == 3:
                    if int(binary_status_ctrl[bit_number]) == 0:
                        gui.beeper_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.beeper_label.config(bg="PaleGreen3")
                        gui.poa_auto_errors["beeper_error"] = False
                    else:
                        gui.beeper_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.beeper_label.config(bg="salmon")
                        gui.poa_auto_errors["beeper_error"] = True
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if bit_number == 4:
                    if int(binary_status_ctrl[bit_number]) == 1:
                        gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.srs_label.config(bg="PaleGreen3")
                    else:
                        gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.srs_label.config(bg="salmon")
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if bit_number == 5:
                    if int(binary_status_ctrl[bit_number]) == 1:
                        gui.acf_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.acf_label.config(bg="PaleGreen3")
                    else:
                        gui.acf_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.acf_label.config(bg="salmon")
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if bit_number == 6:
                    if int(binary_status_ctrl[bit_number]) == 0:
                        gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.wpp_label.config(bg="PaleGreen3")
                    else:
                        gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.wpp_label.config(bg="salmon")
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

            if send_command == request_and_port_list.poa_request_dictionary["stop_poa_package"]:

                if bit_number == 2:
                    if int(binary_status_ctrl[bit_number]) == 1:
                        gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.rfe_label.config(bg="PaleGreen3")
                    else:
                        gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                        gui.rfe_label.config(bg="RoyalBlue1")

                if bit_number == 3:
                    if int(binary_status_ctrl[bit_number]) == 0:
                        gui.beeper_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.beeper_label.config(bg="PaleGreen3")
                        gui.poa_auto_errors["beeper_error"] = False
                    else:
                        gui.beeper_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.beeper_label.config(bg="salmon")
                        gui.poa_auto_errors["beeper_error"] = True
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if bit_number == 4:
                    if int(binary_status_ctrl[bit_number]) == 1:
                        gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.srs_label.config(bg="PaleGreen3")
                    else:
                        gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.srs_label.config(bg="salmon")
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if bit_number == 5:
                    if int(binary_status_ctrl[bit_number]) == 0:
                        gui.acf_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.acf_label.config(bg="PaleGreen3")
                    else:
                        gui.acf_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.acf_label.config(bg="salmon")
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if bit_number == 6:
                    if int(binary_status_ctrl[bit_number]) == 1:
                        gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.wpp_label.config(bg="PaleGreen3")
                    else:
                        gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="RoyalBlue1")
                        gui.wpp_label.config(bg="RoyalBlue1")

            if send_command == request_and_port_list.poa_request_dictionary["dry_poa_package"]:

                if bit_number == 2:
                    if int(binary_status_ctrl[bit_number]) == 0:
                        gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.rfe_label.config(bg="PaleGreen3")
                    else:
                        gui.rfe_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.rfe_label.config(bg="salmon")
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if bit_number == 3:
                    if int(binary_status_ctrl[bit_number]) == 0:
                        gui.beeper_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.beeper_label.config(bg="PaleGreen3")
                        gui.poa_auto_errors["beeper_error"] = False
                    else:
                        gui.beeper_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.beeper_label.config(bg="salmon")
                        gui.poa_auto_errors["beeper_error"] = True
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if bit_number == 4:
                    if int(binary_status_ctrl[bit_number]) == 1:
                        gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.srs_label.config(bg="PaleGreen3")
                    else:
                        gui.srs_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.srs_label.config(bg="salmon")
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if bit_number == 5:
                    if int(binary_status_ctrl[bit_number]) == 0:
                        gui.acf_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.acf_label.config(bg="PaleGreen3")
                    else:
                        gui.acf_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.acf_label.config(bg="salmon")
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if bit_number == 6:
                    if int(binary_status_ctrl[bit_number]) == 0:
                        gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.wpp_label.config(bg="PaleGreen3")
                    else:
                        gui.wpp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.wpp_label.config(bg="salmon")
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

            if bit_number == 7:
                t_min_hex = recieved_command[8] + recieved_command[9]
                t_min_dec = int(t_min_hex, 16)
                t_max_hex = recieved_command[6] + recieved_command[7]
                t_max_dec = int(t_max_hex, 16)

                if send_command == request_and_port_list.poa_request_dictionary["status_poa_package"]:
                    if t_max_dec > 31 and gui.last_command_except_status == \
                            request_and_port_list.poa_request_dictionary["start_poa_package"] or \
                            t_min_dec > 31 and gui.last_command_except_status == \
                            request_and_port_list.poa_request_dictionary["start_poa_package"]:
                        if int(binary_status_ctrl[bit_number]) == 1:
                            gui.rfp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.rfp_label.config(bg="PaleGreen3")
                        else:
                            gui.rfp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            gui.rfp_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                    else:
                        if int(binary_status_ctrl[bit_number]) == 0:
                            gui.rfp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                            gui.rfp_label.config(bg="PaleGreen3")
                        else:
                            gui.rfp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                            gui.rfp_label.config(bg="salmon")
                            if red_green_status_ctrl == "green":
                                red_green_status_ctrl = "red"
                else:
                    if int(binary_status_ctrl[bit_number]) == 0:
                        gui.rfp_bit.config(text=binary_status_ctrl[bit_number], bg="PaleGreen3")
                        gui.rfp_label.config(bg="PaleGreen3")
                    else:
                        gui.rfp_bit.config(text=binary_status_ctrl[bit_number], bg="salmon")
                        gui.rfp_label.config(bg="salmon")
                        if red_green_status_ctrl == "green":
                            red_green_status_ctrl = "red"

                if red_green_status_ctrl == "green":
                    gui.stat_ctrl_label.config(text="OK", bg="PaleGreen3")
                else:
                    gui.stat_ctrl_label.config(text="❌", bg="salmon")
