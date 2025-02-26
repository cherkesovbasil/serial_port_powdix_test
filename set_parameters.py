import time

import request_and_port_list
import serial


def set_par(gui):

    if gui.port_combobox.get() == "":
        gui.port_label.configure(bg="red")
        gui.port_label.update()
        time.sleep(0.5)
        gui.port_label.configure(bg="gray90")
        gui.port_label.update()
        return

    if gui.baudrate_combobox.get() == "":
        gui.baudrate_label.configure(bg="red")
        gui.baudrate_label.update()
        time.sleep(0.5)
        gui.baudrate_label.configure(bg="gray90")
        gui.baudrate_label.update()
        return

    if gui.timeout_combobox.get() == "":
        gui.timeout_label.configure(bg="red")
        gui.timeout_label.update()
        time.sleep(0.5)
        gui.timeout_label.configure(bg="gray90")
        gui.timeout_label.update()
        return

    if gui.bytesize_combobox.get() == "":
        gui.bytesize_label.configure(bg="red")
        gui.bytesize_label.update()
        time.sleep(0.5)
        gui.bytesize_label.configure(bg="gray90")
        gui.bytesize_label.update()
        return

    try:
        ser = serial.Serial(gui.port_combobox.get())
        ser.close()
        gui.set_button.configure(bg="SeaGreen1")
        request_and_port_list.com_port_settings["comport"] = gui.port_combobox.get()
        request_and_port_list.com_port_settings["baudrate"] = gui.baudrate_combobox.get()
        request_and_port_list.com_port_settings["timeout"] = gui.timeout_combobox.get()
        if gui.bytesize_combobox.get() == "∞":
            request_and_port_list.com_port_settings["bytesize"] = "256"
        else:
            request_and_port_list.com_port_settings["bytesize"] = gui.bytesize_combobox.get()
        gui.set_button.update()
        time.sleep(0.5)
        gui.set_button.configure(bg="gray60")
        gui.set_button.update()
    except serial.serialutil.SerialException:
        gui.set_button.configure(bg="red")
        gui.set_button.update()
        time.sleep(0.5)
        gui.set_button.configure(bg="gray60")
        gui.set_button.update()
        pass
