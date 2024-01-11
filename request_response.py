import serial.tools.list_ports
from tkinter.messagebox import showerror

import request_and_port_list


def command_sender(accepted_request=None):
    """Функция отправки запросов контроллеру подключённого устройства"""

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
        if len(answer) < 15 and answer:
            showerror(title="Некорректный ответ контроллера",
                      message="Часто появляется при незамкнутом датчике крана горячей воды (X6). Либо в случае "
                              "некорректного подключения устройства/проблемах связи с контроллером.\n\n"
                              "<Запрос>  -  " + str(accepted_request).upper() +
                              "\n<Ответ>    -   " + str(answer).upper())
        return answer
    else:
        port.close()
        return "No answer"
