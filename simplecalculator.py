from tkinter import *
import math
# put limit to the number of digits entered 
class Calculator(Frame):
    # constants
    BUTTON_MC = "MC"
    BUTTON_MR = "MR"
    BUTTON_MPLUS = "M+"
    BUTTON_MMINUS = "M-"
    BUTTON_MS = "MS"
    BUTTON_MV = "M∇"
    BUTTON_MPERC = "%"
    BUTTON_CE = "CE"
    BUTTON_C = "C"
    BUTTON_BS = "BS"
    BUTTON_FRAC = "1/x"
    BUTTON_POWER2 = "x^2"
    BUTTON_SQRT = "√"
    BUTTON_MULTI = "x"
    BUTTON_DIV = "÷"
    BUTTON_MINUS_PRESIGN = "+/-"
    def __init__(self,master=None):
        super().__init__(master)
        self.master.title("Simple calculator")
        self.master.config(bg="#F2F0EF")
        self.master.geometry("250x450+500+50")
        self.master.resizable(0,0)
        
        self.config(bg="#F2F0EF")
        self.pack(fill="both",expand=True)

        #create history button
        self.historybutton = Button(master=self,text="History",justify="right",command=self.pack_history_frame)
        self.historybutton.pack(anchor="ne",side="top",pady=.5,padx=.5)

        # create Entry widget that displays arithmatic operations
        self.displayVarTop = StringVar()
        self.displayingEntryWidgett = Entry(self,relief="flat",textvariable=self.displayVarTop,bg="#F2F0EF",font=("Times New Roman",10,"bold"),state=DISABLED,justify="right")
        self.displayingEntryWidgett.pack(fill="both",side="top",expand=True)

        self.vcmd = (self.register(self.validate_input),"%S")

        self.displayVarbottom = StringVar()
        self.displayingEntryWidgetb = Entry(self,relief="flat",textvariable=self.displayVarbottom,bg="#F2F0EF",font=("Times New Roman",14,"bold"),justify="right",validate="key",validatecommand=self.vcmd)
        self.displayingEntryWidgetb.insert(0,"0")
        self.displayingEntryWidgetb.focus()
        self.displayingEntryWidgetb.pack(fill="both",side="top",expand=True)

        self.displayingEntryWidgetb.bind("<Key>",self.key_handel)

        #create history frame and its contents
        self.hist_frame = Frame(self,bg="#F2F0EF",relief="solid",borderwidth=1)

        self.history_text_widget = Text(self.hist_frame,autoseparators=True)
        self.history_text_widget.pack(expand=1,fill="both",padx=.8,pady=.8)

        # create frames that contains buttons and their buttons
        self.buttonsFramesDict = {} #Dictionary to append frames contain buttons
        framesContents = ((self.BUTTON_MC,self.BUTTON_MR,self.BUTTON_MPLUS,self.BUTTON_MMINUS,self.BUTTON_MS,self.BUTTON_MV),(self.BUTTON_MPERC,self.BUTTON_CE,self.BUTTON_C,self.BUTTON_BS),(self.BUTTON_FRAC,self.BUTTON_POWER2,self.BUTTON_SQRT,self.BUTTON_DIV),("7","8","9",self.BUTTON_MULTI),("4","5","6","-"),("1","2","3","+"),(self.BUTTON_MINUS_PRESIGN,"0",".","="))

        for index,bf in enumerate(framesContents):
            buttonFrame = Frame(self,bg="#F2F0EF")
            buttonFrame.pack(fill="both",side="top",expand=True,padx=.8,pady=.8)
            self.buttonsFramesDict[buttonFrame] = []
            for b in bf:
                button = Button(master=buttonFrame,text=b,font=("Times New Roman",11,"bold"),command=lambda x=b:self.buttonAction(x))
                if index == 0:
                    button.config(relief="flat",bg="#F2F0EF")
                else:
                    button.config(relief="solid",width=3,bg="white",borderwidth=0)
                button.pack(fill="both",side="left",expand=True,padx=.8)
                self.buttonsFramesDict[buttonFrame].append(button)

    def key_handel(self,event):
        key = event.char
        keysym = event.keysym

        # Numbers and basic operators
        if key in "0123456789.":
            self.button_numbers(key)
        elif key in "+-":
            self.button_operationsigns(key)
        elif key == "*":
            self.button_operationsigns(self.BUTTON_MULTI)
        elif key == "/":
            self.button_operationsigns(self.BUTTON_DIV)

        # Special Keys
        elif keysym == "Return": # Enter key
            self.button_equalsign()
        elif keysym == "BackSpace":
            self.button_BS()
        elif keysym == "Escape":
            self.button_C()
        elif key == "%":
            self.button_percent()

        return "break"

    def buttonAction(self,buttonTXT):
        if buttonTXT in ("0","1","2","3","4","5","6","7","8","9","."):
            self.button_numbers(buttonTXT)
        elif buttonTXT in ("-","+",self.BUTTON_DIV,self.BUTTON_MULTI):
            self.button_operationsigns(buttonTXT)
        elif  buttonTXT == self.BUTTON_BS:
            self.button_BS()
        elif buttonTXT == self.BUTTON_C:
            self.button_C()
        elif buttonTXT == self.BUTTON_CE:
            self.button_CE()
        elif buttonTXT == "=":
            self.button_equalsign()
        elif buttonTXT == self.BUTTON_MPERC:
            self.button_percent()
        elif buttonTXT == self.BUTTON_POWER2:
            self.button_powerby2()
        elif buttonTXT == self.BUTTON_SQRT:
            self.button_sqrt()
        elif buttonTXT == self.BUTTON_FRAC:
            self.button_1byx()

    def button_1byx(self):
        try:
            current_val_b = self.displayVarbottom.get()

            # Don't do anything if it's just 0
            if not current_val_b:
                return

            current_val_b_f = float(current_val_b)

            if current_val_b_f == 0:
                return
            
            result = 1/current_val_b_f

            self.displayingEntryWidgetb.delete(0,END)
            self.displayVarbottom.set( str(result) )
            self.displayingEntryWidgetb.config(validate="key",invcmd=self.vcmd)
        except ValueError as e:
            self.displayingEntryWidgetb.delete(0,END)
            self.displayVarbottom.set( e )

    def button_sqrt(self):
        try:
            current_val_b = self.displayVarbottom.get()

            # Don't do anything if it's just 0
            if not current_val_b:
                return

            current_val_b_f = float(current_val_b)

            if current_val_b_f == 0:
                return
            
            result = math.sqrt(current_val_b_f)

            self.displayingEntryWidgetb.delete(0,END)
            self.displayVarbottom.set( str(result) )
            self.displayingEntryWidgetb.config(validate="key",invcmd=self.vcmd)
        except ValueError:
            pass

    def button_powerby2(self):
        try:
            current_val_b = self.displayVarbottom.get()

            # Don't do anything if it's just 0
            if not current_val_b:
                return

            current_val_b_f = float(current_val_b)

            if current_val_b_f == 0:
                return
            
            result = math.pow(current_val_b_f,2)

            self.displayingEntryWidgetb.delete(0,END)
            self.displayVarbottom.set( str(result) )
            self.displayingEntryWidgetb.config(validate="key",invcmd=self.vcmd)
        except ValueError:
            pass

    def button_MC(self):
        pass

    def button_MR(self):
        pass

    def button_Mplus(self):
        pass

    def button_Mminus(self):
        pass

    def button_MS(self):
        pass

    def button_Mv(self):
        pass

    def button_percent(self):
        try:
            current_val_b = self.displayVarbottom.get()

            # Don't do anything if it's just 0
            if not current_val_b:
                return

            current_val_b_f = float(current_val_b)

            if current_val_b_f == 0:
                return
            
            result = current_val_b_f / 100

            self.displayingEntryWidgetb.delete(0,END)
            self.displayVarbottom.set( str(result) )
            self.displayingEntryWidgetb.config(validate="key",invcmd=self.vcmd)
        except ValueError:
            pass

    def button_CE(self):
        self.displayVarbottom.set("0") 

    def button_C(self):
        self.button_CE()
        self.displayingEntryWidgett.config(state="normal")
        self.displayingEntryWidgett.delete(0,END)
        self.displayingEntryWidgett.config(state="disabled")

    def button_BS(self):
        current_val_b = self.displayingEntryWidgetb.get()

        if len(current_val_b) >= 1:
            current_val_b_new = current_val_b[:-1]
            self.displayingEntryWidgetb.delete(0,END)
            if current_val_b_new == "":
                self.displayingEntryWidgetb.insert(0,"0")
            else:
                self.displayingEntryWidgetb.insert(0,current_val_b_new)

    def button_numbers(self,buttonTXT):
        current_val_b = self.displayVarbottom.get()

        # Set your desired limit here (e.g., 12 digits)
        if len(current_val_b) >= 12:
            return

        if buttonTXT == "." and "." in current_val_b:
            return

        if buttonTXT == "." and (current_val_b == "" or current_val_b == "0"):
            self.displayingEntryWidgetb.insert( END, "0" )

        if current_val_b == "0" and buttonTXT != ".":
            self.displayingEntryWidgetb.delete(0,END)
            self.displayingEntryWidgetb.insert( END, buttonTXT )
        else:
            self.displayingEntryWidgetb.insert( END, buttonTXT )

    def check(self,buttonTXT,current_val_b,current_val_t):
        if current_val_t and current_val_t[-1] in f"/*-+{self.BUTTON_DIV}{self.BUTTON_MULTI}" and current_val_b == "":
            current_val_t = current_val_t[:-1]
            self.displayingEntryWidgett.delete(0,END)
            self.displayingEntryWidgett.insert(END,current_val_t)

        if buttonTXT == self.BUTTON_DIV :
            self.displayingEntryWidgett.insert(END,current_val_b + "/")
        elif buttonTXT == self.BUTTON_MULTI:
            self.displayingEntryWidgett.insert(END,current_val_b + "*")
        else:
            self.displayingEntryWidgett.insert(END,current_val_b + buttonTXT)

    def button_operationsigns(self,buttonTXT):
        current_val_b = self.displayingEntryWidgetb.get()

        self.displayingEntryWidgett.config(state="normal")
        current_val_t = self.displayingEntryWidgett.get()

        self.check(buttonTXT,current_val_b,current_val_t)

        self.displayingEntryWidgetb.delete(0,END)
        self.displayingEntryWidgett.config(state="disabled")

    def button_equalsign(self):
        current_val_t = self.displayVarTop.get()
        current_val_b = self.displayVarbottom.get()
        if current_val_t and current_val_t[-1] in f"/*-+{self.BUTTON_DIV}{self.BUTTON_MULTI}" and current_val_b == "":
            current_val_t = current_val_t[:-1]
            self.displayingEntryWidgett.delete(0,END)
            self.displayVarTop.set(current_val_t)

        current_val_t = self.displayVarTop.get() + current_val_b
        self.displayVarTop.set(current_val_t)
        try:
            result = eval(current_val_t)
            self.history_text_widget.insert(END,"\n"+current_val_t+"\n")
            self.displayVarTop.set("")
            self.displayingEntryWidgetb.delete(0,END)
            self.displayVarbottom.set(str(result))
            self.displayingEntryWidgetb.config(validate="key",invcmd=self.vcmd)
        except Exception as e:
            self.displayingEntryWidgetb.delete(0,END)
            self.displayingEntryWidgetb.insert(0,e)

        self.history_text_widget.insert(END,str(result))

    def unpack_history_frame(self):
        self.hist_frame.pack_forget()

        for frame,keyslist in self.buttonsFramesDict.items():
            frame.pack(fill="both",side="top",expand=True,padx=.8,pady=.8)

        self.historybutton.config(text="History",command=self.pack_history_frame)

    def pack_history_frame(self):
        sumheight = 0
        for frame,keyslist in self.buttonsFramesDict.items():
            frame.pack_forget()
            sumheight += frame.winfo_height()

        self.hist_frame.config(height=sumheight)
        self.hist_frame.pack(fill="both",side="top",expand=True,padx=.8,pady=.8)

        self.historybutton.config(text="cancel history",command=self.unpack_history_frame)

    def validate_input(self,char):
        # S is the character being typed
        current_val_b = self.displayVarbottom.get()
        # Prevent typing if length is already 12
        if len(current_val_b) >= 12:
            return False
        
        if char.isdigit() or (char == "." and "." not in current_val_b):
            return True
        
        return False
            
#################################################
app = Tk()
calc1 = Calculator(app)

if __name__ == "__main__":
    app.mainloop()




        