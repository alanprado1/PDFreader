from tkinter import *
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.geometry('+%d+%d' % (700, 100))

# logo and browse button
header = Frame(root, width=800, height=175, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

# main content area, text and image extraction
main_content = Frame(root, width=800, height=250, bg="#20bebe",)
main_content.grid(columnspan=3, rowspan=2, row=2)
# logo
logo = Image.open("./images/logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bg="white")
logo_label.image = logo
logo_label.grid(column=0, row=0)

# Intructions
# instructions = tk.Label(root, text="Select PDF file to extract", bg="white",)
# instructions.grid(columnspan=3, column=2, row=1)


def open_file():
    browse_text.set("Loading...")
    files = askopenfile(parent=root, mode='rb', title='Choose a file',
                        filetypes=[("Pdf file", "*.pdf")])
    if files:
        read_pdf = PyPDF2.PdfReader(files)
        page = read_pdf.numPages
        for i in range(page):
            pages = read_pdf.getPage(i)
            page_content = pages.extractText()
        print(page_content)
        browse_text.set("Browse")

        # Text box
        text_box = tk.Text(root, height=15, width=90, padx=15, pady=-15,)
        text_box.insert(1.0, page_content)
        text_box.tag_configure('center', justify='center')
        text_box.tag_add('center', 1.0, 'end')

        text_box.grid(columnspan=3,  row=3)


# browse buttom
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text,
                       bg="#20bebe", fg="white", height=2, width=17, font=(20), command=lambda: open_file())
browse_text.set("Browse")
browse_btn.grid(column=2, row=0)


root.mainloop()
