#A First(Real) Example
'''This is a simple feet to meter converter'''
# from tkinter import *
# from tkinter import ttk
#
# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set((0.3048*value*10000.0+0.5)/10000.0)
#     except ValueError:
#         print 'Please input correct number'
#
# root=Tk()
# root.title('Feet to Meters')
#
# mainframe = ttk.Frame(root,padding='3 3 12 12')
# mainframe.grid(column=0,row=0,sticky=(N,W,S,E))
# mainframe.columnconfigure(0,weight=1)
# mainframe.rowconfigure(0,weight=1)
#
# feet=StringVar()
# meters=StringVar()
#
# feet_entry = ttk.Entry(mainframe,width=7,textvariable=feet)
# feet_entry.grid(column=2,row=1,sticky=(W,E))
#
# ttk.Label(mainframe,textvariable=meters).grid(column=2,row=2,sticky=E)
# ttk.Button(mainframe,text='Calculate',command=calculate).grid(column=1,row=2,sticky=E)
# ttk.Label(mainframe,text='meters').grid(column=3,row=2,sticky=W)
#
# for child in mainframe.winfo_children(): child.grid_configure(padx=5,pady=5)
#
# feet_entry.focus()
# root.bind('<Return>',calculate)
#
# root.mainloop()

'''Step-by-Step Walkthrough
Widgets are often referred to as 'controls', or 'windows'. 

The "root" window is the only exception in widgets that is the toplevel windows 
and contains everythin else. The "root" is automatically created and does not has a parent.
'''
# root = Tk()
# content = ttk.Frame(root)
# button = ttk.Button(content)
#
# #Configuration Options
# from tkinter import *
# from tkinter import ttk
# root = Tk()
# #create a button, passing two options:
# button = ttk.Button(root, text="Hello", command="buttonpressed")
# button.grid()
# #check the current value of the text option:
# button['text']
# #'Hello'
# #change the value of the text option:
# button['text'] = 'goodbye'
# #another way to do the same thing:
# button.configure(text='goodbye')
# #check the current value of the text option:
# button['text']
# #'goodbye'
# #get all information about the text option:
# button.configure('text')
# ('text', 'text', 'Text', '', 'goodbye')
# #get information on all options for this widget:
# button.configure()
# '''
# {'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 'style': ('style', 'style', 'Style', '', ''),
# 'default': ('default', 'default', 'Default', <index object at 0x00DFFD10>, <index object at 0x00DFFD10>),
# 'text': ('text', 'text', 'Text', '', 'goodbye'), 'image': ('image', 'image', 'Image', '', ''),
# 'class': ('class', '', '', '', ''), 'padding': ('padding', 'padding', 'Pad', '', ''),
# 'width': ('width', 'width', 'Width', '', ''),
# 'state': ('state', 'state', 'State', <index object at 0x0167FA20>, <index object at 0x0167FA20>),
# 'command': ('command', 'command' , 'Command', '', 'buttonpressed'),
# 'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''),
# 'compound': ('compound', 'compound', 'Compound', <index object at 0x0167FA08>, <index object at 0x0167FA08>),
# 'underline': ('underline', 'underline', 'Underline', -1, -1),
# 'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '', 'ttk::takefocus')}
# '''

'''Event Bindings'''
'''"Bind" command reference link: http://www.tcl.tk/man/tcl8.5/TkCmd/bind.htm'''
# from tkinter import *
# from tkinter import ttk
#
# root=Tk()
# l=ttk.Label(root,text='starting...')
# l.grid()
# l.bind('<Enter>',lambda e: l.configure(text='Moved mouse inside'))
# l.bind('<Leave>',lambda e: l.configure(text='Moved mouse outside'))
# l.bind('<1>', lambda e:l.configure(text='Click left mouse button'))
# l.bind('<Double-1>', lambda e:l.configure(text='Double left clicked'))
# l.bind('<B3-Motion>', lambda e:l.configure(text='right button drage to %d,%d'%(e.x,e.y)))
#
# if __name__ == '__main__':
#     root.mainloop()
#






