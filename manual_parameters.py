from tkinter import *


def manual(gui):

    # Очищает базовый фрейм от мусора
    for widget in gui.frame_for_units.winfo_children():
        widget.destroy()

    # Делает интерфейс активным для взаимодействия
    gui.poa_button.configure(state="normal", bg="gray60")
    gui.sth1_button.configure(state="normal", bg="gray60")
    gui.sth2_button.configure(state="normal", bg="gray60")
    gui.sth3_button.configure(state="normal", bg="gray60")
    gui.as_button.configure(state="normal", bg="gray60")
    gui.sc_button.configure(state="normal", bg="gray60")
    gui.auc_button.configure(state="normal", bg="gray60")
    gui.ck_button.configure(state="normal", bg="gray60")
    gui.vs_button.configure(state="normal", bg="gray60")
    gui.refind_button.configure(state="normal", bg="gray60")
    gui.set_button.configure(state="normal", bg="gray60")
    gui.manual_button.configure(state="disabled", bg="SeaGreen1")
    gui.auto_button.configure(state="normal", bg="gray60")
    gui.terminal_button.configure(state="normal", bg="gray60")

    gui.bytesize_combobox.configure(state="normal")
    gui.timeout_combobox.configure(state="normal")
    gui.baudrate_combobox.configure(state="normal")
    gui.port_combobox.configure(state="normal")

    gui.bytesize_label.configure(fg="black")
    gui.timeout_label.configure(fg="black")
    gui.baudrate_label.configure(fg="black")
    gui.port_label.configure(fg="black")

    # Создаёт подсказки на начальном экране

    frame_for_cooling_system_label = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_cooling_system_label.pack(side=TOP, fill=BOTH, pady=2)

    cooling_system_label = Label(frame_for_cooling_system_label, text="  ⮜   Подсистема охлаждения дифрактометра",
                                 height=2, fg="white", bg="gray10", anchor="w", font=("Arial", 9, "bold"))
    cooling_system_label.pack(side=TOP, padx=3, pady=1, fill=BOTH)

    frame_for_sth1_label = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_sth1_label.pack(side=TOP, fill=BOTH, pady=1)

    sth1_label = Label(frame_for_sth1_label, text="  ⮜   Датчик температуры/влажности №1", height=2, fg="white",
                       bg="gray10", anchor="w", font=("Arial", 9, "bold"))
    sth1_label.pack(side=TOP, padx=3, pady=1, fill=BOTH)

    frame_for_sth2_label = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_sth2_label.pack(side=TOP, fill=BOTH, pady=2)

    sth2_label = Label(frame_for_sth2_label, text="  ⮜   Датчик температуры/влажности №2", height=2, fg="white",
                       bg="gray10", anchor="w", font=("Arial", 9, "bold"))
    sth2_label.pack(side=TOP, padx=3, pady=1, fill=BOTH)

    frame_for_sth3_label = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_sth3_label.pack(side=TOP, fill=BOTH, pady=1)

    sth3_label = Label(frame_for_sth3_label, text="  ⮜   Датчик температуры/влажности №3", height=2, fg="white",
                       bg="gray10", anchor="w", font=("Arial", 9, "bold"))
    sth3_label.pack(side=TOP, padx=3, pady=1, fill=BOTH)

    frame_for_as_label = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_as_label.pack(side=TOP, fill=BOTH, pady=2)

    as_label = Label(frame_for_as_label, text="  ⮜   Автоматический сменщик образцов", height=2, fg="white",
                     bg="gray10", anchor="w", font=("Arial", 9, "bold"))
    as_label.pack(side=TOP, padx=3, pady=1, fill=BOTH)

    frame_for_sc_label = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_sc_label.pack(side=TOP, fill=BOTH, pady=1)

    sc_label = Label(frame_for_sc_label, text="  ⮜   Автоматический вращатель образца", height=2, fg="white",
                     bg="gray10", anchor="w", font=("Arial", 9, "bold"))
    sc_label.pack(side=TOP, padx=3, pady=1, fill=BOTH)

    frame_for_auc_label = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_auc_label.pack(side=TOP, fill=BOTH, pady=1)

    auc_label = Label(frame_for_auc_label, text="  ⮜   Автоматический пробоподатчик", height=2, fg="white",
                     bg="gray10", anchor="w", font=("Arial", 9, "bold"))
    auc_label.pack(side=TOP, padx=3, pady=1, fill=BOTH)

    frame_for_ck_label = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_ck_label.pack(side=TOP, fill=BOTH, pady=2)

    ck_label = Label(frame_for_ck_label, text="  ⮜   Автоматический коллиматор-нож", height=2, fg="white", bg="gray10",
                     anchor="w", font=("Arial", 9, "bold"))
    ck_label.pack(side=TOP, padx=3, pady=1, fill=BOTH)

    frame_for_vs_label = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_vs_label.pack(side=TOP, fill=BOTH, pady=1)

    vs_label = Label(frame_for_vs_label, text="  ⮜   Автоматизированная варьируемая щель", height=2, fg="white",
                     bg="gray10", anchor="w", font=("Arial", 9, "bold"))
    vs_label.pack(side=TOP, padx=3, pady=1, fill=BOTH)

    frame_for_bottom_label = LabelFrame(gui.frame_for_units, bg="gray10")
    frame_for_bottom_label.pack(side=BOTTOM, fill=BOTH, pady=2)

    bottom_label = Label(frame_for_bottom_label, text="              ⮟⮟⮟                                             "
                                                      " ⮟⮟⮟---------------------------⮟⮟⮟---------------------------"
                                                      "-⮟⮟⮟--------------------------⮟⮟⮟", height=1, fg="white",
                         bg="gray10", anchor="w", font=("Arial", 9, "bold"))
    bottom_label.pack(side=BOTTOM, padx=3, pady=0, fill=BOTH)

    center_label = Label(frame_for_bottom_label,
                         text="Режим работы ПО                                                   Настройки для "
                              "подключения к требуемой системе вручную",
                         height=1, fg="white", bg="gray10", anchor="w", font=("Arial", 9, "bold"))
    center_label.pack(side=BOTTOM, padx=3, pady=0, fill=BOTH)

    upper_label = Label(frame_for_bottom_label,
                        text="\n 🡿 Кнопка ⭯ осуществляет автоматический поиск подключенного устройства без "
                             "последующей проверки",
                        height=4, fg="white", bg="gray10", anchor="w", font=("Arial", 9, "bold"))
    upper_label.pack(side=BOTTOM, padx=3, pady=8, fill=BOTH)
