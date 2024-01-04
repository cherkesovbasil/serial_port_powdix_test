import serial.tools.list_ports
from tkinter.messagebox import showerror, showwarning, showinfo

# Импортируем словарь!
import request_and_port_list


def command_sender(accepted_request=None):

    port = serial.Serial(request_and_port_list.com_port_settings["comport"],
                         baudrate=int(request_and_port_list.com_port_settings["baudrate"]),
                         timeout=float(request_and_port_list.com_port_settings["timeout"]),
                         bytesize=int(request_and_port_list.com_port_settings["bytesize"]),
                         parity=request_and_port_list.com_port_settings["parity"],
                         stopbits=int(request_and_port_list.com_port_settings["stopbits"]),
                         xonxoff=False, rtscts=False)

    port.write(accepted_request)
    answer = port.readline(10).hex()
    if not answer:
        port.write(accepted_request)
        answer = port.readline(10).hex()

    if answer is not None:
        port.close()
        return answer
    else:
        port.close()
        return "No answer"
