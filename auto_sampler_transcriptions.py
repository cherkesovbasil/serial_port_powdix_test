import tkinter as tk
from tkinter import *


def transcript_status_l(gui, recieved_command=None):
    # Расшифровка прочих параметров из полученной команды

    gui.device_name.configure(text="Устройство")
    gui.stat_request.configure(text="Статус")
    gui.reserve_1.configure(text="Резерв")
    gui.state_1.configure(text="Состояние 1")
    gui.rotate_low.configure(text="Вращ. ШД3")
    gui.rotate_high.configure(text="Вращ. ШД3")
    gui.errors.configure(text="Ошибки")
    gui.state_2.configure(text="Состояние 2")
    gui.state_set_sample.configure(text="Уст. обр.")
    gui.crc_name.configure(text="Сумм (CRC)")

    def transcript_name_device():
        # расшифровка поля device

        device_hex = recieved_command[0] + recieved_command[1]
        if device_hex == "50":
            gui.device_name_label.config(text="OK", bg="PaleGreen3")
        else:
            gui.device_name_label.config(text="❌", bg="salmon")
            gui.auto_sampler_real_state["incorrect_answer"] = True
        gui.device_name_data.config(text=device_hex.upper())

    def transcript_status_device():
        # расшифровка поля status

        status_hex = recieved_command[2] + recieved_command[3]
        if status_hex == "78":
            gui.stat_request_label.config(text="OK", bg="PaleGreen3")
        else:
            gui.stat_request_label.config(text="❌", bg="salmon")
            gui.auto_sampler_real_state["incorrect_answer"] = True
        gui.stat_request_data.config(text=status_hex.upper())

    def transcript_reserve():
        # расшифровка поля reserve

        reserve = recieved_command[4] + recieved_command[5]
        gui.reserve_1_label.config(text="No check")
        gui.reserve_1_data.config(text=reserve.upper())

    def transcript_state_1():
        # расшифровка поля state_1

        state_1 = recieved_command[6] + recieved_command[7]
        gui.state_1_label.config(text="No check")
        gui.state_1_data.config(text=state_1.upper())

    def transcript_rotate_low():
        # расшифровка поля rotate_low

        rotate_low = recieved_command[8] + recieved_command[9]
        gui.rotate_low_data.config(text=rotate_low.upper())

    def transcript_rotate_high():
        # расшифровка поля rotate_high

        rotate_high = recieved_command[10] + recieved_command[11]
        gui.rotate_high_data.config(text=rotate_high.upper())

    def transcript_full_speed():
        # расшифровка full_speed
        gui.auto_sampler_real_state["engine3_state"] = False
        speed_hex = recieved_command[10] + recieved_command[11] + recieved_command[8] + recieved_command[9]
        speed_dec = int(speed_hex, 16)
        if speed_dec != 0:
            real_speed = int(60 / (6 * speed_dec * 64 * 0.000001))
        else:
            real_speed = 0
        set_speed = int(gui.speed_engine_3_combobox.get())
        if gui.auto_sampler_last_command == "set_sample" or gui.auto_sampler_last_command == "engine3_right" or \
                gui.auto_sampler_last_command == "engine3_left":
            if set_speed - 12 < real_speed < set_speed + 6:
                if gui.wait_status:
                    gui.speed_textbox.config(state="normal", bg="gray70")
                    gui.speed_textbox.delete('1.0', END)
                    gui.speed_textbox.insert(tk.END, real_speed)
                    gui.speed_textbox.config(state="disabled")
                    gui.rotate_low_label.config(text="...", bg="gray70")
                    gui.rotate_high_label.config(text="...", bg="gray70")
                else:
                    gui.speed_textbox.config(state="normal", bg="PaleGreen3")
                    gui.speed_textbox.delete('1.0', END)
                    gui.speed_textbox.insert(tk.END, real_speed)
                    gui.speed_textbox.config(state="disabled")
                    gui.rotate_low_label.config(text="OK", bg="PaleGreen3")
                    gui.rotate_high_label.config(text="OK", bg="PaleGreen3")
            else:
                if gui.wait_status:
                    gui.speed_textbox.config(state="normal", bg="gray70")
                    gui.speed_textbox.delete('1.0', END)
                    gui.speed_textbox.insert(tk.END, real_speed)
                    gui.speed_textbox.config(state="disabled")
                    gui.rotate_low_label.config(text="...", bg="gray70")
                    gui.rotate_high_label.config(text="...", bg="gray70")
                else:
                    gui.speed_textbox.config(state="normal", bg="salmon")
                    gui.speed_textbox.delete('1.0', END)
                    gui.speed_textbox.insert(tk.END, real_speed)
                    gui.speed_textbox.config(state="disabled")
                    gui.rotate_low_label.config(text="❌", bg="salmon")
                    gui.rotate_high_label.config(text="❌", bg="salmon")
                    gui.auto_sampler_real_state["engine3_state"] = [set_speed, real_speed]
        else:
            if real_speed == 0:
                if gui.wait_status:
                    gui.speed_textbox.config(state="normal", bg="gray70")
                    gui.speed_textbox.delete('1.0', END)
                    gui.speed_textbox.insert(tk.END, real_speed)
                    gui.speed_textbox.config(state="disabled")
                    gui.rotate_low_label.config(text="...", bg="gray70")
                    gui.rotate_high_label.config(text="...", bg="gray70")
                else:
                    gui.speed_textbox.config(state="normal", bg="PaleGreen3")
                    gui.speed_textbox.delete('1.0', END)
                    gui.speed_textbox.insert(tk.END, real_speed)
                    gui.speed_textbox.config(state="disabled")
                    gui.rotate_low_label.config(text="OK", bg="PaleGreen3")
                    gui.rotate_high_label.config(text="OK", bg="PaleGreen3")
            else:
                if gui.wait_status:
                    gui.speed_textbox.config(state="normal", bg="gray70")
                    gui.speed_textbox.delete('1.0', END)
                    gui.speed_textbox.insert(tk.END, real_speed)
                    gui.speed_textbox.config(state="disabled")
                    gui.rotate_low_label.config(text="...", bg="gray70")
                    gui.rotate_high_label.config(text="...", bg="gray70")
                else:
                    gui.speed_textbox.config(state="normal", bg="salmon")
                    gui.speed_textbox.delete('1.0', END)
                    gui.speed_textbox.insert(tk.END, real_speed)
                    gui.speed_textbox.config(state="disabled")
                    gui.rotate_low_label.config(text="❌", bg="salmon")
                    gui.rotate_high_label.config(text="❌", bg="salmon")
                    gui.auto_sampler_real_state["engine3_state"] = [set_speed, real_speed]

    def transcript_errors():
        # расшифровка поля errors

        errors = recieved_command[12] + recieved_command[13]
        if errors == "00":
            gui.errors_label.config(text="OK", bg="PaleGreen3")
        else:
            gui.errors_label.config(text="❌", bg="salmon")
            gui.auto_sampler_real_state["movement_errors"] = True
        gui.errors_data.config(text=errors.upper())

    def transcript_state_2():
        # расшифровка поля state_2

        state_2 = recieved_command[14] + recieved_command[15]
        gui.state_2_label.config(text="No check")
        gui.state_2_data.config(text=state_2.upper())

    def transcript_state_set_sample():
        # расшифровка поля state_set_sample
        gui.wait_status = False
        state_set_sample = recieved_command[16] + recieved_command[17]
        gui.state_set_sample_data.config(text=state_set_sample.upper())
        if gui.auto_sampler_last_command == "set_sample":
            if state_set_sample == "f8":
                gui.state_set_sample_label.config(text="OK", bg="PaleGreen3")

                gui.full_set_textbox.config(state="normal", bg="PaleGreen3")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Установлен")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="PaleGreen3")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Поднят")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="PaleGreen3")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Позиция найдена")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = False

            if state_set_sample == "a8":
                gui.state_set_sample_label.config(text="...", bg="gray70")

                gui.full_set_textbox.config(state="normal", bg="gray70")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Ожидание барабана")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Ожидание барабана")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="gray70")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Ищет позицию")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = True

            if state_set_sample == "e8":
                gui.state_set_sample_label.config(text="...", bg="gray70")

                gui.full_set_textbox.config(state="normal", bg="gray70")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Ожидание лифта")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Поднимается")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="PaleGreen3")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Позиция установл.")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = True

            if state_set_sample == "88":
                gui.state_set_sample_label.config(text="...", bg="gray70")

                gui.full_set_textbox.config(state="normal", bg="gray70")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "В процессе")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Опускается")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="gray70")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Ожидание лифта")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = True

            if state_set_sample == "00":
                gui.state_set_sample_label.config(text="❌", bg="salmon")

                gui.full_set_textbox.config(state="normal", bg="salmon")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Не производится")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="salmon")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "В базе")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="salmon")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Не производится")
                gui.position_textbox.config(state="disabled")
                gui.auto_sampler_real_state["set_sample_state"] = "lift_fault"
                gui.wait_status = False

            if state_set_sample == "a0":
                gui.state_set_sample_label.config(text="❌", bg="salmon")

                gui.full_set_textbox.config(state="normal", bg="gray70")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Ошибка барабана")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "не использовался")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="salmon")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Позиция не найдена")
                gui.position_textbox.config(state="disabled")
                gui.auto_sampler_real_state["set_sample_state"] = "engine1"
                gui.wait_status = False

            if state_set_sample == "e0":
                gui.state_set_sample_label.config(text="❌", bg="salmon")

                gui.full_set_textbox.config(state="normal", bg="salmon")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Ошибка лифта")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Лифт не поднялся")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="PaleGreen3")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Позиция установл.")
                gui.position_textbox.config(state="disabled")
                gui.auto_sampler_real_state["set_sample_state"] = "lift_up"
                gui.wait_status = False

            if state_set_sample == "80":
                gui.state_set_sample_label.config(text="❌", bg="salmon")

                gui.full_set_textbox.config(state="normal", bg="salmon")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Ошибка лифта")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Лифт не опустился")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="gray70")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Не использовался")
                gui.position_textbox.config(state="disabled")
                gui.auto_sampler_real_state["set_sample_state"] = "lift_down"
                gui.wait_status = False

        else:
            gui.state_set_sample_label.config(text="OK", bg="PaleGreen3")

            gui.full_set_textbox.config(state="normal", bg="gray70")
            gui.full_set_textbox.delete('1.0', END)
            gui.full_set_textbox.config(state="disabled")

            gui.lift_textbox.config(state="normal", bg="gray70")
            gui.lift_textbox.delete('1.0', END)
            gui.lift_textbox.config(state="disabled")

            gui.position_textbox.config(state="normal", bg="gray70")
            gui.position_textbox.delete('1.0', END)
            gui.position_textbox.config(state="disabled")
            gui.wait_status = False

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
        else:
            gui.crc_label.config(bg="salmon", text=str(full_hex_summ))
            gui.auto_sampler_real_state["incorrect_answer"] = True
        gui.crc_data.config(text=recieved_command[18].upper() + recieved_command[19].upper())

    transcript_name_device()
    transcript_status_device()
    transcript_reserve()
    transcript_state_1()
    transcript_rotate_low()
    transcript_rotate_high()
    transcript_errors()
    transcript_state_2()
    transcript_state_set_sample()
    check_crc()

    transcript_full_speed()


def transcript_status(gui, recieved_command=None):
    # Расшифровка прочих параметров из полученной команды

    gui.device_name.configure(text="Устройство")
    gui.stat_request.configure(text="Команда")
    gui.reserve_1.configure(text="Позиция")
    gui.state_1.configure(text="Дробление")
    gui.rotate_low.configure(text="Уст. обр.")
    gui.rotate_high.configure(text="Состояние 2")
    gui.errors.configure(text="Ошибки")
    gui.state_2.configure(text="Лифт")
    gui.state_set_sample.configure(text="Статус")
    gui.crc_name.configure(text="Сумм (CRC)")

    def transcript_name_device():
        # расшифровка поля device

        device_hex = recieved_command[0] + recieved_command[1]
        if device_hex == "50":
            gui.device_name_label.config(text="OK", bg="PaleGreen3")
        else:
            gui.device_name_label.config(text="❌", bg="salmon")
            gui.auto_sampler_real_state["incorrect_answer"] = True
        gui.device_name_data.config(text=device_hex.upper())

    def transcript_command():
        # расшифровка поля status

        status_hex = recieved_command[2] + recieved_command[3]
        if status_hex == "73":
            gui.stat_request_label.config(text="OK", bg="PaleGreen3")
        else:
            gui.stat_request_label.config(text="❌", bg="salmon")
            gui.auto_sampler_real_state["incorrect_answer"] = True
        gui.stat_request_data.config(text=status_hex.upper())

    def transcript_position():
        # расшифровка поля reserve
        position_numbers = {
            "00": None,
            "01": 1,
            "02": 2,
            "04": 3,
            "08": 4,
            "10": 5,
            "20": 6,
            "40": 7,
            "80": 8,
        }
        position = recieved_command[4] + recieved_command[5]
        position_number = position_numbers[position]

        if position_number:
            gui.reserve_1_label.config(text="No check")
            gui.reserve_1_data.config(text=position.upper())
        else:
            gui.reserve_1_label.config(text="Между")
            gui.reserve_1_data.config(text=position.upper())

        if gui.auto_sampler_last_command == "engine1":
            set_position = gui.speed_engine_1_combobox.get()
            if str(position_number) != str(set_position) and position_number is not None:
                gui.reserve_1_label.config(text="№ " + str(position_number))
                gui.reserve_1_label.config(bg="salmon")
                gui.auto_sampler_real_state["engine1_state"] = "Fault"
            else:
                if position_number is None:
                    gui.reserve_1_label.config(text="Между")
                    gui.reserve_1_label.config(bg="salmon")
                    gui.auto_sampler_real_state["engine1_state"] = "Wait"
                else:
                    gui.reserve_1_label.config(text="№ " + str(position_number))
                    gui.reserve_1_label.config(bg="PaleGreen3")
                    gui.auto_sampler_real_state["engine1_state"] = "Done"

    def transcript_divider():
        # расшифровка поля divider
        dividers = {
            "00": 0,
            "02": 2,
            "04": 4,
            "06": 8,
            "08": 16,
            "0A": 32
        }

        divider_hex = recieved_command[6] + recieved_command[7]
        divider = dividers[divider_hex]

        gui.state_1_label.config(text="/ " + str(divider))
        gui.state_1_data.config(text=divider_hex.upper())

    def transcript_state_set_sample():
        # расшифровка поля state_set_sample
        gui.wait_status = False
        state_set_sample = recieved_command[8] + recieved_command[9]
        gui.rotate_low_data.config(text=state_set_sample.upper())
        if gui.auto_sampler_last_command == "set_sample":
            if state_set_sample == "f8":
                gui.rotate_low_label.config(text="OK", bg="PaleGreen3")

                gui.full_set_textbox.config(state="normal", bg="PaleGreen3")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Установлен")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="PaleGreen3")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Поднят")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="PaleGreen3")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Позиция найдена")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = False

            if state_set_sample == "a8":
                gui.rotate_low_label.config(text="...", bg="gray70")

                gui.full_set_textbox.config(state="normal", bg="gray70")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Ожидание барабана")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Ожидание барабана")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="gray70")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Ищет позицию")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = True

            if state_set_sample == "e8":
                gui.rotate_low_label.config(text="...", bg="gray70")

                gui.full_set_textbox.config(state="normal", bg="gray70")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Ожидание лифта")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Поднимается")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="PaleGreen3")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Позиция установл.")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = True

            if state_set_sample == "88":
                gui.rotate_low_label.config(text="...", bg="gray70")

                gui.full_set_textbox.config(state="normal", bg="gray70")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "В процессе")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Опускается")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="gray70")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Ожидание лифта")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = True

            if state_set_sample == "00":
                gui.rotate_low_label.config(text="❌", bg="salmon")

                gui.full_set_textbox.config(state="normal", bg="salmon")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Не производится")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="salmon")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "В базе")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="salmon")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Не производится")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = False

            if state_set_sample == "a0":
                gui.rotate_low_label.config(text="❌", bg="salmon")

                gui.full_set_textbox.config(state="normal", bg="gray70")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Ошибка барабана")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "не использовался")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="salmon")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Позиция не найдена")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = False

            if state_set_sample == "e0":
                gui.rotate_low_label.config(text="❌", bg="salmon")

                gui.full_set_textbox.config(state="normal", bg="salmon")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Ошибка лифта")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Лифт не поднялся")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="PaleGreen3")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Позиция установл.")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = False

            if state_set_sample == "80":
                gui.rotate_low_label.config(text="❌", bg="salmon")

                gui.full_set_textbox.config(state="normal", bg="salmon")
                gui.full_set_textbox.delete('1.0', END)
                gui.full_set_textbox.insert(tk.END, "Ошибка лифта")
                gui.full_set_textbox.config(state="disabled")

                gui.lift_textbox.config(state="normal", bg="gray70")
                gui.lift_textbox.delete('1.0', END)
                gui.lift_textbox.insert(tk.END, "Лифт не опустился")
                gui.lift_textbox.config(state="disabled")

                gui.position_textbox.config(state="normal", bg="gray70")
                gui.position_textbox.delete('1.0', END)
                gui.position_textbox.insert(tk.END, "Не использовался")
                gui.position_textbox.config(state="disabled")
                gui.wait_status = False

        else:
            gui.rotate_low_label.config(text="OK", bg="PaleGreen3")

            gui.full_set_textbox.config(state="normal", bg="gray70")
            gui.full_set_textbox.delete('1.0', END)
            gui.full_set_textbox.config(state="disabled")

            gui.lift_textbox.config(state="normal", bg="gray70")
            gui.lift_textbox.delete('1.0', END)
            gui.lift_textbox.config(state="disabled")

            gui.position_textbox.config(state="normal", bg="gray70")
            gui.position_textbox.delete('1.0', END)
            gui.position_textbox.config(state="disabled")
            gui.wait_status = False

    def transcript_state_2():
        # расшифровка поля state_2

        state_2 = recieved_command[10] + recieved_command[11]
        gui.rotate_high_label.config(text="No check")
        gui.rotate_high_data.config(text=state_2.upper())

    def transcript_errors():
        # расшифровка поля errors

        errors = recieved_command[12] + recieved_command[13]
        if errors == "00":
            gui.errors_label.config(text="OK", bg="PaleGreen3")
        else:
            gui.errors_label.config(text="❌", bg="salmon")
            gui.auto_sampler_real_state["movement_errors"] = True
        gui.errors_data.config(text=errors.upper())

    def transcript_driver_fault():
        # расшифровка поля driver_fault

        rotate_low = recieved_command[14] + recieved_command[15]
        if str(rotate_low) == "10":
            gui.state_2_label.config(text="Внизу", bg="gray90")
            gui.state_2_data.config(text=rotate_low.upper())
            gui.auto_sampler_real_state["lift_status"] = "Down"
        elif str(rotate_low) == "20":
            gui.state_2_label.config(text="Вверху", bg="gray90")
            gui.state_2_data.config(text=rotate_low.upper())
            gui.auto_sampler_real_state["lift_status"] = "Up"
        elif str(rotate_low) == "30":
            gui.state_2_label.config(text="Между", bg="gray90")
            gui.state_2_data.config(text=rotate_low.upper())
            gui.auto_sampler_real_state["lift_status"] = "Between"
        else:
            gui.state_2_label.config(text="Fault", bg="salmon")
            gui.state_2_data.config(text=rotate_low.upper())
            gui.auto_sampler_real_state["incorrect_answer"] = "Fault"

    def transcript_status_3():
        # расшифровка поля status_3

        rotate_high = recieved_command[10] + recieved_command[11]
        if str(rotate_high) == "49":
            gui.state_set_sample_label.config(text="Двигаюсь", bg="gray90")
            gui.state_set_sample_data.config(text=rotate_high.upper())
        elif str(rotate_high) == "45":
            gui.state_set_sample_label.config(text="Установл.", bg="gray90")
            gui.state_set_sample_data.config(text=rotate_high.upper())
        elif str(rotate_high) == "41":
            gui.state_set_sample_label.config(text="Ожидаю", bg="gray90")
            gui.state_set_sample_data.config(text=rotate_high.upper())
        else:
            gui.state_set_sample_label.config(text="Fault", bg="salmon")
            gui.state_set_sample_data.config(text=rotate_high.upper())
            gui.auto_sampler_real_state["incorrect_answer"] = True

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
        else:
            gui.crc_label.config(bg="salmon", text=str(full_hex_summ))
            gui.auto_sampler_real_state["incorrect_answer"] = True
        gui.crc_data.config(text=recieved_command[18].upper() + recieved_command[19].upper())

    transcript_name_device()
    transcript_command()
    transcript_position()
    transcript_divider()
    transcript_state_set_sample()
    transcript_state_2()
    transcript_errors()
    transcript_driver_fault()
    transcript_status_3()
    check_crc()
