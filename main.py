#HT: <Frame input, Finish the Description, Focus on MainUi by using TaskerUi>
#MB: <Maximize Button [using screenwidth]>
#HT=HaveTo MB= Maybe WOT= WorkOnThis
import tkinter.messagebox
from tkinter import *
import linecache
Description = '''
+-+-+-+-+-+-+-+-+-+-+
How to use this modul:

    Example:

         import flt
         root = flt()

         size = '700x500'
         root.geometry(size)

         root.iconbitmap('fav.ico')


         af = Frame(root, bg='white')
         af.place(x=0, y=0, height=500, width=700)


         flt(master=root, size=size, flt_title='Test', info_button=1, flt_info=1)

+-+-+-+-+-+-+-+-+-+-+
'''
def flt(master, size='700x500', flt_title='^Please^fill^the^title^', frame=0, info_frame=0,info_button=0, flt_info=0):
    master.resizable(width=FALSE, height=FALSE)
    master.attributes("-alpha", 0.0)
    master.title(flt_title)
    root = Toplevel(master)
    split_size = size.split('x')
    height = int(split_size[1])
    width = int(split_size[0])
    corr_height = str(height+30)
    corr_width = str(width)
    corr_size = str(corr_width + 'x' + corr_height)
    #print(corr_size)
    root.geometry(corr_size)
    root.overrideredirect(1)

    def onMasterIconify(event):
        root.withdraw()
    master.bind("<Unmap>", onMasterIconify)
    def onMasterDeiconify(event):
        root.deiconify()
    master.bind("<Map>", onMasterDeiconify)
    def destroy_master():
        master.destroy()
    root.protocol("WM_DELETE_WINDOW", destroy_master)

    class WindowDraggable():

        def __init__(self, label):
            self.label = label
            label.bind('<ButtonPress-1>', self.StartMove)
            label.bind('<ButtonRelease-1>', self.StopMove)
            label.bind('<B1-Motion>', self.OnMotion)

        def StartMove(self, event):
            self.x = event.x
            self.y = event.y

        def StopMove(self, event):
            self.x = None
            self.y = None

        def OnMotion(self,event):
            x = (event.x_root - self.x - self.label.winfo_rootx() + self.label.winfo_rootx())
            y = (event.y_root - self.y - self.label.winfo_rooty() + self.label.winfo_rooty())
            root.geometry("+%s+%s" % (x, y))
    grip = Frame(root, height=25, width=width, bg = '#2C3E50')
    grip.place(x=0, y=0, height=30, width=width)
    WindowDraggable(grip)


    def center_window(width=width, height=height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    center_window()



    def quit():
        messagebox.showinfo("Attention", "You are quitting the program!")
        root.destroy()
    def minimize():
        master.iconify()
    global inout
    inout = 'in'
    def di_info():
        global inout
        if inout == 'in':
            info_out()
            inout = 'out'
        elif inout == 'out':
            info_in()
            inout = 'in'
        else:
            return 1
            print('er/cod1')
    def info_in():
        str_height = str(height)
        str_width = str(corr_width)
        newize = str_width +'x'+ str_height
        root.geometry(newize)
    def info_out():
        str_height = str(height)
        str_width = str(width + 200)
        newize = str_width +'x'+ str_height
        root.geometry(newize)

    quit = Button(grip, text="X", bg='red', relief='flat', command=quit)
    quit_placex = width-50
    quit.place(x=quit_placex, y=0, height=30, width=50)
    mini_placex = width-100
    mini = Button(grip, text="_", bg='yellow', relief='flat', command=minimize)
    mini.place(x=mini_placex, y=0, height=30, width=50)
    info_placex = width-150
    info = Button(grip, text="?", bg='white', relief='flat', command=di_info)
    if info_button == 1:
        info.place(x=info_placex, y=0, height=30, width=50)
    else:
        pass

    #Info content
    info_con = Frame(root, bg='black')
    info_con.place(x=width, y=0, height=height, width=200)



    #Title
    label = Label(grip, text=flt_title, font=("akkadian", 11), bg='#2C3E50', fg='white')
    label.place(y='-7',x=0)
    #Flt Info
    if flt_info == 1:
        print(Description)
    else:
        pass


    fltroot = root
    return fltroot

# #Just a script
# root = Tk()
# root.geometry('700x500')
# #root.iconbitmap('/PYTHON/mx/#mxMsg/mxMsg/client.ico')
#
# #1920x1080
# flt = flt(master=root, size='1000x800', flt_title='Module Test 01', info_frame=0, info_button=1, flt_info=0)
# print(flt)
# imge = PhotoImage('/Users/Max/Desktop/imagegif.gif')
# frame = Frame(flt, image=imge).place(y=30, x=0, height=800, width=1000)
