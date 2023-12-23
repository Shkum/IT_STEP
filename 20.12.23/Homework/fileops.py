import tkinter.filedialog


def open_file():
    file = tkinter.filedialog.askopenfilename()
    return file


def save_file():
    file = tkinter.filedialog.asksaveasfilename()
    return file


if __name__ == '__main__':
    print(open_file())
    print(save_file())
