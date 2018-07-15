from main import *
#Just a script
root = Tk()
root.geometry('700x500')
#root.iconbitmap('/PYTHON/mx/#mxMsg/mxMsg/client.ico')

#1920x1080
flt = flt(master=root, size='1000x800', flt_title='Module Test 01', info_frame=0, info_button=1, flt_info=0)
print(flt)
# imge = PhotoImage('/Users/Max/Desktop/imagegif.gif')
frame = Frame(flt).place(y=30, x=0, height=800, width=1000)
root.mainloop()
