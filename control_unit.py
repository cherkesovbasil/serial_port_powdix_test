from tkinter import *
from tkinter import ttk


class AdjustmentUtility:
    """Главное окно взаимодействия с девайсами"""

    def __init__(self):
        self.start_window = None
        self.frame_for_units = None

    def poa_unit(self):
        self.frame_for_units.destroy()
        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        # центральное поле (поле юнитов)
        frame_for_analytical_label = LabelFrame(self.frame_for_units, bg="gray80")
        frame_for_analytical_label.pack(side=TOP, padx=1, pady=1, fill=X)

        analytical_label = Label(frame_for_analytical_label, text="Analytical unit:", width=14, height=1, bg="gray80")
        analytical_label.pack(side=LEFT, padx=3, pady=1)

        # поле отображения наименования полученной информации
        frame_for_response_name = LabelFrame(self.frame_for_units, bg="gray95")
        frame_for_response_name.pack(side=TOP, padx=1, pady=1, fill=X)

        device_name = Label(frame_for_response_name, text="Device", width=6, height=1, bg="gray90", relief=SUNKEN)
        device_name.pack(side=LEFT, padx=3, pady=1)

        stat_sens_name = Label(frame_for_response_name, text="Status Sensors", width=12, height=1, bg="gray90",
                               relief=SUNKEN)
        stat_sens_name.pack(side=LEFT, padx=3, pady=1)

        crc_name = Label(frame_for_response_name, text="CRC", width=6, height=1, bg="gray90", relief=SUNKEN)
        crc_name.pack(side=RIGHT, padx=3, pady=1)

        pwm_2_name = Label(frame_for_response_name, text="PWM 1", width=6, height=1, bg="gray90", relief=SUNKEN)
        pwm_2_name.pack(side=RIGHT, padx=3, pady=1)

        pwm_1_name = Label(frame_for_response_name, text="PWM 2", width=6, height=1, bg="gray90", relief=SUNKEN)
        pwm_1_name.pack(side=RIGHT, padx=3, pady=1)

        errors_name = Label(frame_for_response_name, text="Errors", width=6, height=1, bg="gray90", relief=SUNKEN)
        errors_name.pack(side=RIGHT, padx=3, pady=1)

        flow_name = Label(frame_for_response_name, text="Flow", width=6, height=1, bg="gray90", relief=SUNKEN)
        flow_name.pack(side=RIGHT, padx=3, pady=1)

        t_min_name = Label(frame_for_response_name, text="t min", width=6, height=1, bg="gray90", relief=SUNKEN)
        t_min_name.pack(side=RIGHT, padx=3, pady=1)

        t_max_name = Label(frame_for_response_name, text="t max", width=6, height=1, bg="gray90", relief=SUNKEN)
        t_max_name.pack(side=RIGHT, padx=3, pady=1)

        stat_ctrl_name = Label(frame_for_response_name, text="Status control", width=12, height=1, bg="gray90",
                               relief=SUNKEN)
        stat_ctrl_name.pack(side=RIGHT, padx=3, pady=1)

        # поле отображения обработанной информации
        frame_for_response_data = LabelFrame(self.frame_for_units, bg="gray95")
        frame_for_response_data.pack(side=TOP, padx=1, pady=1, fill=X)

        device_label = Label(frame_for_response_data, text="40", width=6, height=2, bg="chartreuse2", relief=SUNKEN)
        device_label.pack(side=LEFT, padx=3, pady=1)

        stat_sens_label = Label(frame_for_response_data, text="XX", width=12, height=2, bg="chartreuse2", relief=SUNKEN)
        stat_sens_label.pack(side=LEFT, padx=3, pady=1)

        crc_label = Label(frame_for_response_data, text="ok", width=6, height=2, bg="chartreuse2", relief=SUNKEN)
        crc_label.pack(side=RIGHT, padx=3, pady=1)

        pwm_2_label = Label(frame_for_response_data, text="30", width=6, height=2, bg="chartreuse2", relief=SUNKEN)
        pwm_2_label.pack(side=RIGHT, padx=3, pady=1)

        pwm_1_label = Label(frame_for_response_data, text="70", width=6, height=2, bg="chartreuse2", relief=SUNKEN)
        pwm_1_label.pack(side=RIGHT, padx=3, pady=1)

        errors_label = Label(frame_for_response_data, text="--", width=6, height=2, bg="chartreuse2", relief=SUNKEN)
        errors_label.pack(side=RIGHT, padx=3, pady=1)

        flow_label = Label(frame_for_response_data, text="3.2", width=6, height=2, bg="chartreuse2", relief=SUNKEN)
        flow_label.pack(side=RIGHT, padx=3, pady=1)

        t_min_label = Label(frame_for_response_data, text="22", width=6, height=2, bg="chartreuse2", relief=SUNKEN)
        t_min_label.pack(side=RIGHT, padx=3, pady=1)

        t_max_label = Label(frame_for_response_data, text="23", width=6, height=2, bg="chartreuse2", relief=SUNKEN)
        t_max_label.pack(side=RIGHT, padx=3, pady=1)

        stat_ctrl_label = Label(frame_for_response_data, text="XX", width=12, height=2, bg="chartreuse2", relief=SUNKEN)
        stat_ctrl_label.pack(side=RIGHT, padx=3, pady=1)

        # поле отображения первичной информации
        frame_for_response_clear_data = LabelFrame(self.frame_for_units, bg="gray95")
        frame_for_response_clear_data.pack(side=TOP, padx=1, pady=1, fill=X)

        device_data = Label(frame_for_response_clear_data, text="40", width=6, height=1, bg="gray90", relief=SUNKEN)
        device_data.pack(side=LEFT, padx=3, pady=1)

        stat_sens_data = Label(frame_for_response_clear_data, text="08", width=12, height=1, bg="gray90", relief=SUNKEN)
        stat_sens_data.pack(side=LEFT, padx=3, pady=1)

        crc_data = Label(frame_for_response_clear_data, text="3C", width=6, height=1, bg="gray90", relief=SUNKEN)
        crc_data.pack(side=RIGHT, padx=3, pady=1)

        pwm_2_data = Label(frame_for_response_clear_data, text="15", width=6, height=1, bg="gray90", relief=SUNKEN)
        pwm_2_data.pack(side=RIGHT, padx=3, pady=1)

        pwm_1_data = Label(frame_for_response_clear_data, text="25", width=6, height=1, bg="gray90", relief=SUNKEN)
        pwm_1_data.pack(side=RIGHT, padx=3, pady=1)

        errors_data = Label(frame_for_response_clear_data, text="00", width=6, height=1, bg="gray90", relief=SUNKEN)
        errors_data.pack(side=RIGHT, padx=3, pady=1)

        flow_data = Label(frame_for_response_clear_data, text="36", width=6, height=1, bg="gray90", relief=SUNKEN)
        flow_data.pack(side=RIGHT, padx=3, pady=1)

        t_min_data = Label(frame_for_response_clear_data, text="13", width=6, height=1, bg="gray90", relief=SUNKEN)
        t_min_data.pack(side=RIGHT, padx=3, pady=1)

        t_max_data = Label(frame_for_response_clear_data, text="78", width=6, height=1, bg="gray90", relief=SUNKEN)
        t_max_data.pack(side=RIGHT, padx=3, pady=1)

        stat_ctrl_data = Label(frame_for_response_clear_data, text="2E", width=12, height=1, bg="gray90", relief=SUNKEN)
        stat_ctrl_data.pack(side=RIGHT, padx=3, pady=1)

        # фреймы для расшифровки статусов
        frame_for_statuses = LabelFrame(self.frame_for_units, bg="gray95")
        frame_for_statuses.pack(side=TOP, padx=1, pady=1, fill=X)

        frame_for_status_sensors = LabelFrame(frame_for_statuses, bg="gray95", text="Status Sensors transcription")
        frame_for_status_sensors.pack(side=LEFT, padx=2, pady=1, fill=X)

        frame_for_status_control = LabelFrame(frame_for_statuses, bg="gray95", text="Status Control transcription")
        frame_for_status_control.pack(side=LEFT, padx=2, pady=1, fill=X)

        #
        # поле отображения информации Status Sensors
        #

        # интерфейс расшифровки статуса датчика температуры холодной воды
        frame_for_wts1 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_wts1.pack(side=TOP, padx=1, pady=1, fill=X)

        wts1_bit = Label(frame_for_wts1, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        wts1_bit.pack(side=LEFT, padx=3, pady=1)

        wts1_label = Label(frame_for_wts1, text=" - Температура горячей воды", width=26, height=1, bg="gray90",
                           relief=SUNKEN, anchor=W)
        wts1_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки статуса датчика температуры холодной воды
        frame_for_wts2 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_wts2.pack(side=TOP, padx=1, pady=1, fill=X)

        wts2_bit = Label(frame_for_wts2, text="1", width=6, height=1, bg="gray90", relief=SUNKEN)
        wts2_bit.pack(side=LEFT, padx=3, pady=1)

        wts2_label = Label(frame_for_wts2, text=" - Температура холодной воды", width=26, height=1, bg="gray90",
                           relief=SUNKEN, anchor=W)
        wts2_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки статуса пароводяного клапана
        frame_for_svs = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_svs.pack(side=TOP, padx=1, pady=1, fill=X)

        svs_bit = Label(frame_for_svs, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        svs_bit.pack(side=LEFT, padx=3, pady=1)

        svs_label = Label(frame_for_svs, text=" - Пароводяной клапан", width=26, height=1, bg="gray90",
                          relief=SUNKEN, anchor=W)
        svs_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки статуса ключа системы охлаждения
        frame_for_key = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_key.pack(side=TOP, padx=1, pady=1, fill=X)

        key_bit = Label(frame_for_key, text="1", width=6, height=1, bg="gray90", relief=SUNKEN)
        key_bit.pack(side=LEFT, padx=3, pady=1)

        key_label = Label(frame_for_key, text=" - Ключ системы охлаждения", width=26, height=1, bg="gray90",
                          relief=SUNKEN, anchor=W)
        key_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки статуса датчика уровня воды
        frame_for_wls = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_wls.pack(side=TOP, padx=1, pady=1, fill=X)

        wls_bit = Label(frame_for_wls, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        wls_bit.pack(side=LEFT, padx=3, pady=1)

        wls_label = Label(frame_for_wls, text=" - Датчик уровня воды", width=26, height=1, bg="gray90",
                          relief=SUNKEN, anchor=W)
        wls_label.pack(side=LEFT, padx=3, pady=1)

        # резервный бит reserve_1
        frame_for_reserve_1 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_reserve_1.pack(side=TOP, padx=1, pady=1, fill=X)

        reserve_1_bit = Label(frame_for_reserve_1, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        reserve_1_bit.pack(side=LEFT, padx=3, pady=1)

        reserve_1_label = Label(frame_for_reserve_1, text=" - Reserve", width=26, height=1, bg="gray90",
                                relief=SUNKEN, anchor=W)
        reserve_1_label.pack(side=LEFT, padx=3, pady=1)

        # резервный бит reserve_2
        frame_for_reserve_2 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_reserve_2.pack(side=TOP, padx=1, pady=1, fill=X)

        reserve_2_bit = Label(frame_for_reserve_2, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        reserve_2_bit.pack(side=LEFT, padx=3, pady=1)

        reserve_2_label = Label(frame_for_reserve_2, text=" - Reserve", width=26, height=1, bg="gray90",
                                relief=SUNKEN, anchor=W)
        reserve_2_label.pack(side=LEFT, padx=3, pady=1)

        # резервный бит reserve_3
        frame_for_reserve_3 = LabelFrame(frame_for_status_sensors, bg="gray95")
        frame_for_reserve_3.pack(side=TOP, padx=1, pady=1, fill=X)

        reserve_3_bit = Label(frame_for_reserve_3, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        reserve_3_bit.pack(side=LEFT, padx=3, pady=1)

        reserve_3_label = Label(frame_for_reserve_3, text=" - Reserve", width=26, height=1, bg="gray90",
                                relief=SUNKEN, anchor=W)
        reserve_3_label.pack(side=LEFT, padx=3, pady=1)

        #
        # поле отображения информации Status Control
        #

        # интерфейс расшифровки команды питания вентиляторов радиатора
        frame_for_rfp = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_rfp.pack(side=TOP, padx=1, pady=1, fill=X)

        rfp_bit = Label(frame_for_rfp, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        rfp_bit.pack(side=LEFT, padx=3, pady=1)

        rfp_label = Label(frame_for_rfp, text=" - Вкл. вентиляторы радиатора", width=26, height=1, bg="gray90",
                          relief=SUNKEN, anchor=W)
        rfp_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки команды питания помпы
        frame_for_wpp = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_wpp.pack(side=TOP, padx=1, pady=1, fill=X)

        wpp_bit = Label(frame_for_wpp, text="1", width=6, height=1, bg="gray90", relief=SUNKEN)
        wpp_bit.pack(side=LEFT, padx=3, pady=1)

        wpp_label = Label(frame_for_wpp, text=" - Вкл. питание помпы", width=26, height=1, bg="gray90",
                          relief=SUNKEN, anchor=W)
        wpp_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки команды питания вентилятора воздушного охлаждения
        frame_for_acf = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_acf.pack(side=TOP, padx=1, pady=1, fill=X)

        acf_bit = Label(frame_for_acf, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        acf_bit.pack(side=LEFT, padx=3, pady=1)

        acf_label = Label(frame_for_acf, text=" - Вкл. вентилятор возд. охл.", width=26, height=1, bg="gray90",
                          relief=SUNKEN, anchor=W)
        acf_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки команды включения петли безопасности
        frame_for_srs = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_srs.pack(side=TOP, padx=1, pady=1, fill=X)

        srs_bit = Label(frame_for_srs, text="1", width=6, height=1, bg="gray90", relief=SUNKEN)
        srs_bit.pack(side=LEFT, padx=3, pady=1)

        srs_label = Label(frame_for_srs, text=" - Вкл. петли безопасности", width=26, height=1, bg="gray90",
                          relief=SUNKEN, anchor=W)
        srs_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки команды активации пищалки
        frame_for_beeper = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_beeper.pack(side=TOP, padx=1, pady=1, fill=X)

        beeper_bit = Label(frame_for_beeper, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        beeper_bit.pack(side=LEFT, padx=3, pady=1)

        beeper_label = Label(frame_for_beeper, text=" - Вкл. звукового сигнала", width=26, height=1, bg="gray90",
                             relief=SUNKEN, anchor=W)
        beeper_label.pack(side=LEFT, padx=3, pady=1)

        # интерфейс расшифровки команды активации bRadiator_Fan_En
        frame_for_rfe = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_rfe.pack(side=TOP, padx=1, pady=1, fill=X)

        rfe_bit = Label(frame_for_rfe, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        rfe_bit.pack(side=LEFT, padx=3, pady=1)

        rfe_label = Label(frame_for_rfe, text=" - Вкл. bRadiator_Fan_En???", width=26, height=1, bg="gray90",
                          relief=SUNKEN, anchor=W)
        rfe_label.pack(side=LEFT, padx=3, pady=1)

        # резервный бит reserve_4
        frame_for_reserve_4 = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_reserve_4.pack(side=TOP, padx=1, pady=1, fill=X)

        reserve_4_bit = Label(frame_for_reserve_4, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        reserve_4_bit.pack(side=LEFT, padx=3, pady=1)

        reserve_4_label = Label(frame_for_reserve_4, text=" - Reserve", width=26, height=1, bg="gray90",
                                relief=SUNKEN, anchor=W)
        reserve_4_label.pack(side=LEFT, padx=3, pady=1)

        # резервный бит reserve_5
        frame_for_reserve_5 = LabelFrame(frame_for_status_control, bg="gray95")
        frame_for_reserve_5.pack(side=TOP, padx=1, pady=1, fill=X)

        reserve_5_bit = Label(frame_for_reserve_5, text="0", width=6, height=1, bg="gray90", relief=SUNKEN)
        reserve_5_bit.pack(side=LEFT, padx=3, pady=1)

        reserve_5_label = Label(frame_for_reserve_5, text=" - Reserve", width=26, height=1, bg="gray90",
                                relief=SUNKEN, anchor=W)
        reserve_5_label.pack(side=LEFT, padx=3, pady=1)

    def sth1_unit(self):
        self.frame_for_units.destroy()

    def sth2_unit(self):
        self.frame_for_units.destroy()

    def sth3_unit(self):
        self.frame_for_units.destroy()

    def as_unit(self):
        self.frame_for_units.destroy()

    def sc_unit(self):
        self.frame_for_units.destroy()

    def ck_unit(self):
        self.frame_for_units.destroy()

    def refind_device(self):
        pass

    def set_parameters(self):
        pass

    def manual_parameters(self):
        pass

    def main_frame_unit(self):
        """Запускает первичное окно с возможностью первичного просмотра баз данных, добавления, удаления, открытия"""

        self.start_window = Tk()
        self.start_window.title("Adjustment utility")

        # disables the ability to zoom the page
        self.start_window.minsize(800, 600)
        self.start_window.resizable(False, False)

        # базовые поля
        frame_for_device_buttons = LabelFrame(self.start_window, bg="gray90")
        frame_for_device_buttons.pack(side=LEFT, padx=1, pady=1, fill=Y)

        self.frame_for_units = LabelFrame(self.start_window, bg="gray90")
        self.frame_for_units.pack(side=TOP, padx=1, pady=1, fill=X)

        frame_for_settings = LabelFrame(self.start_window, bg="gray90")
        frame_for_settings.pack(side=BOTTOM, padx=1, pady=1, fill=X)

        # левое поле
        poa_button = Button(frame_for_device_buttons, text="POA", relief=GROOVE, width=5, height=3, bg="chartreuse2",
                            command=self.poa_unit)
        poa_button.pack(side=TOP, padx=1, pady=1)
        sth1_button = Button(frame_for_device_buttons, text="STH-1", relief=GROOVE, width=5, height=3, bg="gray60",
                             command=self.sth1_unit)
        sth1_button.pack(side=TOP, padx=1, pady=1)
        sth2_button = Button(frame_for_device_buttons, text="STH-2", relief=GROOVE, width=5, height=3, bg="gray60",
                             command=self.sth2_unit)
        sth2_button.pack(side=TOP, padx=1, pady=1)
        sth3_button = Button(frame_for_device_buttons, text="STH-3", relief=GROOVE, width=5, height=3, bg="gray60",
                             command=self.sth3_unit)
        sth3_button.pack(side=TOP, padx=1, pady=1)
        as_button = Button(frame_for_device_buttons, text="AS", relief=GROOVE, width=5, height=3, bg="gray60",
                           command=self.as_unit)
        as_button.pack(side=TOP, padx=1, pady=1)
        sc_button = Button(frame_for_device_buttons, text="SC", relief=GROOVE, width=5, height=3, bg="gray60",
                           command=self.sc_unit)
        sc_button.pack(side=TOP, padx=1, pady=1)
        ck_button = Button(frame_for_device_buttons, text="CK", relief=GROOVE, width=5, height=3, bg="gray60",
                           command=self.ck_unit)
        ck_button.pack(side=TOP, padx=1, pady=1)

        refind_button = Button(frame_for_device_buttons, text="RR", relief=GROOVE, width=5, height=2, bg="brown1",
                               command=self.refind_device)
        refind_button.pack(side=BOTTOM, padx=1, pady=1)

        # нижнее поле
        set_button = Button(frame_for_settings, text="Set", relief=GROOVE, width=8, height=2, bg="gray60",
                            command=self.set_parameters)
        set_button.pack(side=RIGHT, padx=3, pady=1)

        bytesize_list = ["8", "16", "∞"]
        bytesize_combobox = ttk.Combobox(frame_for_settings, values=bytesize_list, width=4, height=2, state="readonly")
        bytesize_combobox.pack(side=RIGHT, padx=3, pady=1)

        bytesize_label = Label(frame_for_settings, text="Bytesize:", width=8, height=2, bg="gray90")
        bytesize_label.pack(side=RIGHT, padx=3, pady=1)

        timeout_list = ["0.1", "0.3", "0.5", "1.0"]
        timeout_combobox = ttk.Combobox(frame_for_settings, values=timeout_list, width=4, height=2, state="readonly")
        timeout_combobox.pack(side=RIGHT, padx=3, pady=1)

        timeout_label = Label(frame_for_settings, text="Timeout(s):", width=8, height=2, bg="gray90")
        timeout_label.pack(side=RIGHT, padx=3, pady=1)

        baudrate_list = ["115200", "500000", "1000000"]
        port_combobox = ttk.Combobox(frame_for_settings, values=baudrate_list, width=8, height=2, state="readonly")
        port_combobox.pack(side=RIGHT, padx=3, pady=1)

        baudrate_label = Label(frame_for_settings, text="Baudrate:", width=8, height=2, bg="gray90")
        baudrate_label.pack(side=RIGHT, padx=3, pady=1)

        port_numbers = ["1", "2", "3", "4"]
        port_combobox = ttk.Combobox(frame_for_settings, values=port_numbers, width=4, height=2, state="readonly")
        port_combobox.pack(side=RIGHT, padx=3, pady=1)

        port_label = Label(frame_for_settings, text="Serial port (COM):", width=14, height=2, bg="gray90")
        port_label.pack(side=RIGHT, padx=3, pady=1)

        manual_button = Button(frame_for_settings, text="Manual", relief=GROOVE, width=8, height=2, bg="gray60",
                               command=self.manual_parameters)
        manual_button.pack(side=LEFT, padx=3, pady=1)

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


AdjustmentUtility().main_frame_unit()
