from tkinter import *
from tkinter import ttk

root=Tk()

if __name__ == '__main__':
    root.mainloop()

'''Frame Module'''
# root1=Tk()
#
# frame1=ttk.Frame(root1)
# # frame1.configure(padding=(100,100))
# frame1['padding']=(5,10)
# # frame1.configure(border=2)
# frame1['border']=2
# # frame1.configure(style='sunken')
# frame1['relief']='sunken'
#
# frame1.pack()
#
# if __name__ == '__main__':
#     root1.mainloop()

'''Label Module'''
#
# root=Tk()
#
# label1=ttk.Label(root,text='Full Name')
# resultsContents = StringVar()
# label1['textvariable']=resultsContents
# resultsContents.set('New value to display')
# '''
# Building "resultsContents" variable and assgin to "Label1" variable;
# The variable can only changed by method of "set" and of "get".
# '''
# label1.pack()
#
# root.mainloop()
#
# '''Display Images'''
# image1=PhotoImage(file='muimage.gif')
# label['image']=image1

'''Button Module'''

# button1=ttk.Button(root,text='Okay',command=submitForm)
# button1.invoke() #Command button callback ???
#
# '''Button State'''
# button.state(['disabled'])         # set the disabled flag, disabling the button
# button.state(['!disabled'])        # clear the disabled flag
# button.instate(['disabled'])       # return true if the button is disabled, else false
# button.instate(['!disabled'])      # return true if the button is not disabled, else false
# button.instate(['!disabled'], cmd) # execute 'cmd' if the button is not disabled
#
'''CheckButton'''
#
# measureSystem =StringVar()
# check1 = ttk.Checkbutton(root,text='Use Metric', command=metricChanged,
#                           variable=measureSystem, onvalue='metric',
#                            offvalue='imperal')
#
# '''
# For 'variable', value==1 when checked, value==0 when not checked
# This can be changed to adjust anything using 'onvalue' and 'offvalue'.
# The "tristate" or indeterminate mode exists when the state flage "alternate"
# is set, and it can be checked with method "instate".
# '''
# check1.instate('[alternate]')
#

''' Radiobutton  '''

# phone1=StringVar()
# home = ttk.Radiobutton(root,text='Home',variable=phone1,value='home')
# office = ttk.Radiobutton(root,text='Office',variable=phone,value='office')
# cell = ttk.Radiobutton(root,text='Mobile',variable=phone1,value='cell')
#
# ''' Radiobutton is similar to Checkbutton, except the "onvalue" and "offvalue"
# being replaced by a single value "value" option.
# raiable=given value  == the radiobutton is selected
# '''
#
'''Entry Module'''
# Username1=StringVar()
# name = ttk.Entry(root,textvariable=Username1)
#
# print('current value is %s' % name.get())
# name.delete(0,'end')          # delete between two indices, 0-based
# name.insert(0, 'your name')   # insert new text at a given index

#Entry states can be set by set by "state" command and queried with "instate"
#The state can be set on "Readonly", "invalid"

'''Combobox Module'''
countryvar = StringVar()
country = ttk.Combobox(root,textvariable=countryvar)
country.bind('<<ComoboboxSeleted>>',function)
# country.configure(values=('USA','Canada','Australia'))
country['values']=('USA','Canada','Australia')

