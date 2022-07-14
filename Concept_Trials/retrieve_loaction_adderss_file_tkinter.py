import tkinter
from tkinter import ttk, StringVar
from tkinter.filedialog import askopenfilename

class GUI:

    def __init__(self, window): 
        # 'StringVar()' is used to get the instance of input field
        self.input_text = StringVar()
        self.input_text1 = StringVar()
        self.path = ''
        self.path1 = ''

        window.title("Request Notifier")
        window.resizable(0, 0) # this prevents from resizing the window
        window.geometry("700x300")

        ttk.Button(window, text = "Users File", command = lambda: self.set_path_users_field()).grid(row = 0, ipadx=5, ipady=15) # this is placed in 0 0
        ttk.Entry(window, textvariable = self.input_text, width = 70).grid( row = 0, column = 1, ipadx=1, ipady=1) # this is placed in 0 1

        ttk.Button(window, text = "Enova File", command = lambda: self.set_path_Enova_field()).grid(row = 1, ipadx=5, ipady=15) # this is placed in 0 0
        ttk.Entry(window, textvariable = self.input_text1, width = 70).grid( row = 1, column = 1, ipadx=1, ipady=1) # this is placed in 0 1

        ttk.Button(window, text = "Send Notifications").grid(row = 2, ipadx=5, ipady=15) # this is placed in 0 0

    def set_path_users_field(self):
        self.path = askopenfilename() 
        self.input_text.set(self.path)

    def set_path_Enova_field(self):
        self.path1 = askopenfilename()
        self.input_text1.set(self.path1)

    def get_user_path(self): 
        """ Function provides the Users full file path."""
        return self.path

    def get_enova_path1(self):
        """Function provides the Enova full file path."""
        return self.path1


if __name__ == '__main__':
    window = tkinter.Tk()
    gui = GUI(window)
    window.mainloop()
    # Extracting the full file path for re-use. Two ways to accomplish this task is below. 
    print(gui.path, '\n', gui.path1) 
    print(gui.get_user_path(), '\n', gui.get_enova_path1())
