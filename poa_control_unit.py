from tkinter import *


def init_start_window(self):
    """Запускает первичное окно с возможностью первичного просмотра баз данных, добавления, удаления, открытия"""

    self.start_window = Tk()
    self.start_window.title("Adjustment utility")

    # disables the ability to zoom the page
    self.start_window.minsize(500, 100)
    self.start_window.resizable(False, False)

    # frame for the main interface
    frame_for_buttons_start_window = LabelFrame(self.start_window, bg="grey90")
    frame_for_buttons_start_window.pack(side=LEFT, padx=1, pady=1)

    # outputs the information about the absolute error in the GUI
    self.manual_button = Button(frame_for_buttons_start_window, text="Manual", relief=GROOVE, width=20, height=2,
                                bg="gray60", command=self.run_manual)
    self.manual_button.pack(side=LEFT, padx=10, pady=10)
    self.full_auto_button = Button(frame_for_buttons_start_window, text="Full-Auto", relief=GROOVE, width=20,
                                   height=2, bg="SeaGreen1", command=self.run_full_auto)
    self.full_auto_button.pack(side=LEFT, padx=10, pady=10)

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