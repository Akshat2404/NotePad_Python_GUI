# Notepad using Python GUI [Tkinter]
# YouTube Video Link: 
# https://www.youtube.com/playlist?list=PLu0W_9lII9ajLcqRcj4PoEihkukF_OTzA -> Code with Harry

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import win32print, win32api
from fpdf import FPDF
import os
import time

from matplotlib.pyplot import show, text

screen_width=650
screen_height=450
cwd = os.getcwd().replace('\\', '/')
filename='Untitled'

root=Tk()
root.geometry(f'{screen_width}x{screen_height}')
root.minsize(screen_width, screen_height)
root.maxsize(1920, 1080)
root.title('NotePad: ' + cwd + '/' + filename + '.txt')
# root.wm_iconbitmap('1.ico')

def StatusUpdate(text, t):
    statusvar.set(text)
    sbar.update()
    time.sleep(t)
    statusvar.set('Working...')

def newfile():
    global file
    root.title('NotePad: ' + cwd + '/' + filename + '.txt')
    file=None
    TextArea.delete(1.0, END)
    StatusUpdate('New File Successful!', 3)

def openfile():
    global file
    file = askopenfilename(defaultextension='.txt', 
                        filetypes=[('All Files', '*.*'), 
                                ('Text Documents', '*.txt')])
    if file=='':
        file = None
        StatusUpdate('No File Existing', 3)
    else:
        root.title(os.path.basename(file) + ' - NotePad')
        TextArea.delete(1.0, END)
        f=open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()
        StatusUpdate('Opening File Successful!', 3)

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', 
                                defaultextension='.txt', 
                                filetypes=[('All Files', '*.*'), 
                                ('Text Documents', '*.txt')])

        if file=='':
            file = None
            StatusUpdate('File not saved!', 3)
        else:
            f=open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + ' - NotePad')
            print('File Saved')
            StatusUpdate('File Saved Successfully!', 3)
    else:
        f=open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()
        StatusUpdate('File Saved Successfully!', 3)

def saveasfile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', 
                                defaultextension='.txt', 
                                filetypes=[('All Files', '*.*'), 
                                ('Text Documents', '*.txt')])

        if file=='':
            file = None
            StatusUpdate('File not saved!', 3)
        else:
            f=open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + ' - NotePad')
            print('File Saved')
            StatusUpdate('File Saved Successfully!', 3)

    else:
        f=open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()
        StatusUpdate('File Saved Successfully!', 3)

def printfile():
    # printer=win32print.GetDefaultPrinter()
    # status_bar.config(text=printer)
    file_to_print = askopenfilename(defaultextension='.txt', 
                                filetypes=[('All Files', '*.*'), 
                                ('Text Documents', '*.txt')])
    if file_to_print:
        win32api.ShellExecute(0, 'print', file_to_print, None, '.', 0)
        StatusUpdate('File Printed Successfully!', 3)

def PDFfile():
    global file
    file = askopenfilename(defaultextension='.txt', 
                        filetypes=[('All Files', '*.*'), 
                        ('Text Documents', '*.txt')])
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=15)
    text_file=open(file, 'r')
    for text in text_file: 
        pdf.cell(200, 10, txt = text, ln=1,align='L')
    name=file.split('/')[-1]
    pdf.output(f"{name.split('.')[0]}.pdf")
    # info_label.config(text=f"{name} converted to {name.split('.')[0]}.pdf")
    StatusUpdate('File Converted Successfully!', 3)

def exitfile():
    root.destroy()

def undotext():
    TextArea.get(1.0, END).undo()

def redotext():
    TextArea.get(1.0, END).redo()

def cuttext():
    TextArea.event_generate(('<<Cut>>'))

def copytext():
    TextArea.event_generate(('<<Copy>>'))

def pastetext():
    TextArea.event_generate(('<<Paste>>'))

def findtext():
    pass

def replacetext():
    pass

def zoomin():
    pass

def zoomout():
    pass

def statusbar():
    pass

def about():
    showinfo('About NotePad', 'Python GUI-based NotePad model created by Akshat Shah')

# Xscrollbar=Scrollbar(root, orient=HORIZONTAL)
# Xscrollbar.pack(side=BOTTOM, fill=X)
Yscrollbar=Scrollbar(root)
Yscrollbar.pack(side=RIGHT, fill=Y)
TextArea = Text(root, font=('Lucida Console', 12), yscrollcommand=Yscrollbar.set,) # xscrollcommand=Xscrollbar.set
file=None
TextArea.pack(expand=True, fill=BOTH)
Yscrollbar.config(command=TextArea.yview)
# Xscrollbar.config(command=TextArea.xview)

mainmenu=Menu(root,)

file=Menu(mainmenu, tearoff=0)
file.add_command(label='New', command=newfile)
file.add_command(label='Open', command=openfile)
file.add_command(label='Save', command=savefile)
file.add_command(label='Save As', command=saveasfile)
file.add_separator()
file.add_command(label='Print', command=printfile)
export=Menu(file, tearoff=0)
export.add_command(label='PDF', command=PDFfile)
file.add_cascade(label='Export', menu=export)
file.add_separator()
file.add_command(label='Exit', command=exitfile)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='File', menu=file)

edit=Menu(mainmenu, tearoff=0)
edit.add_command(label='Undo', command=undotext)
edit.add_command(label='Redo', command=redotext)
edit.add_separator()
edit.add_command(label='Cut', command=cuttext)
edit.add_command(label='Copy', command=copytext)
edit.add_command(label='Paste', command=pastetext)
edit.add_separator()
edit.add_command(label='Find', command=findtext)
edit.add_command(label='Replace', command=replacetext)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Edit', menu=edit)

view=Menu(mainmenu, tearoff=0)
zoom=Menu(view, tearoff=0)
zoom.add_command(label='Zoom In', command=zoomin)
zoom.add_command(label='Zoom Out', command=zoomout)
view.add_cascade(label='Zoom', menu=zoom)
view.add_separator()
view.add_command(label='Status Bar', command=statusbar)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='View', menu=view)

helpMenu = Menu(mainmenu, tearoff=0)
helpMenu.add_command(label='About NotePad', command=about)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Help', menu=helpMenu)

statusvar = StringVar()
statusvar.set('Working...')
sbar=Label(root, textvariable=statusvar, anchor=W, bg='white')
sbar.pack(side=BOTTOM, fill=X)

root.mainloop()
