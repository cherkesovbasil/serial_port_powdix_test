import serial.tools.list_ports

# Сделать отправку команд снаружи и универсальной. Отдать файл под выполнение команд и возврат считанного результата

# Импортируем словарь!
import request_and_port_list


def command_sender(comport=request_and_port_list.com_port_settings["comport"],
                   user_baudrate=request_and_port_list.com_port_settings["baudrate"],
                   user_timeout=request_and_port_list.com_port_settings["timeout"],
                   user_bytesize=request_and_port_list.com_port_settings["bytesize"],
                   user_parity=request_and_port_list.com_port_settings["parity"],
                   user_stopbits=request_and_port_list.com_port_settings["stopbits"],
                   accepted_request=None
                   ):
    print(comport, user_baudrate, user_timeout, user_bytesize, user_parity, user_stopbits)
    port = serial.Serial(comport, baudrate=user_baudrate, timeout=user_timeout, bytesize=user_bytesize,
                         parity=user_parity, stopbits=user_stopbits, xonxoff=False, rtscts=False)

    port.write(accepted_request)
    answer = port.readline(10).hex()
    if not answer:
        port.write(accepted_request)
        answer = port.readline(10).hex()

    print("answer = " + str(answer))

    if answer is not None:
        print("Ответ от:", port.name, '\n')
        port.close()
        return answer
    else:
        port.close()
        return "No answer"
