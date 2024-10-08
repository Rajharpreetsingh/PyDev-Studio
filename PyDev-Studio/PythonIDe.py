from tkinter import*
from tkinter.filedialog import asksaveasfilename, askopenfilename
from CustomTkinterMessagebox import CTkMessagebox
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter
import subprocess
import os
import platform






def settings():
    setting_page = CTk();
    setting_page.title("Settings");
    setting_page.geometry("900x500");
    setting_page.iconbitmap("setting.ico");
    setting_page.mainloop();
    

def code_run():
    root1.destroy();
    
def Open_file():
    root1.destroy();
    open_file();



def Home():
    def code_run():
        root1.destroy();
    def Open_file():
        root1.destroy();
        editor();
        open_file();
        
    root1=customtkinter.CTk();
    root1.title("PyDev-Studio");
    root1.iconbitmap("py.ico");
    root1.geometry("900x600");
    customtkinter.set_appearance_mode("dark");
    customtkinter.set_default_color_theme("dark-blue");
    sidebar=customtkinter.CTkFrame(root1,width=250,height=900,bg="#292929");
    sidebar.pack(side="left",fill="both");
    frame=customtkinter.CTkFrame(root1,width=500,height=400,bg="gray");
    frame.pack(side="top",pady=50);
    button_frame=Frame(root1,bg="#212325",height=300,width=800);
    button_frame.pack();
    n= PhotoImage(file='n.png')
    o= PhotoImage(file='open.png')
    s= PhotoImage(file='set.png')
    sl=PhotoImage(file='side logo.png')
    button1=customtkinter.CTkButton(button_frame,text="",height=70,width=75,corner_radius=7,image=n,command=code_run);
    button1.pack(side="left",padx=40,expand=True);
    button2=customtkinter.CTkButton(button_frame,text="",height=70,width=75,corner_radius=4,image=o,command=Open_file);
    button2.pack(side="left",padx=40,expand=True);
    button3=customtkinter.CTkButton(button_frame,text="",height=70,width=75,corner_radius=4,image=s,command=settings);
    button3.pack(side="left",padx=40,expand=True);
    logo=Label(sidebar,bg="#292929",bd=0,image=sl);
    logo.pack();
    button4=Button(sidebar,text="Projects                                                      ",height=3,width=40,relief="sunken",bg="#292929",fg="white",bd=0);
    button4.pack(fill="x");
    button5=Button(sidebar,text="Learn PyDev-Studio                                  ",height=3,width=40,relief="sunken",bg="#292929",fg="white",bd=0);
    button5.pack(fill="x");
    button6=Button(sidebar,text="Support                                                    ",height=3,width=40,relief="sunken",bg="#292929",fg="white",bd=0);
    button6.pack(fill="x");
    label=Label(frame,text="Welcome to PyDev-Studio",font=("Arial", 24, "bold"),fg="white",bg="#212325");
    label.pack(expand=True);
    label1=Label(frame,text="Develop Advance Python projects from Scratch",font=("roboto", 14),fg="white",bg="#212325");
    label1.pack(expand=True);
    root1.mainloop();









file_path = '';
current_line_count = 1
terminal_visibility=True;
sidebar_visibility=True;

words_to_highlight = {"if": "#FF6188",
    "else": "#FF6188",
    "elif": "#FF6188",
    "while": "#FF6188",
    "break": "#FF6188",
    "return": "#FF6188",
    "and": "#FFD866",
    "or": "#FFD866",
    "not": "#FFD866",
    "is": "#FFD866",
    "in": "#FFD866",
    "True": "#78DCE8",
    "False": "#78DCE8",
    "None": "#78DCE8",
    "try": "#FC9867",
    "except": "#FC9867",
    "finally": "#FC9867",
    "raise": "#FC9867",
    "def": "#AB9DF2",
    "return": "#AB9DF2",
    "lambda": "#AB9DF2",
    "yield": "#AB9DF2",
    "await": "#AB9DF2",
    "class": "#A9DC76",
    "import": "#A9DC76",
    "with": "#A9DC76",
    "from": "#A9DC76",
    "pass": "#A9DC76",
    "global": "#A9DC76",
    "nonlocal": "#A9DC76",
    "continue": "#FF6188",
    "as": "#A9DC76",
    "del": "#A9DC76",
    "assert": "#FC9867",
    "for": "#FF6188",
    "async": "#AB9DF2",      
            };

def on_key_release(event=None):
    update_line_count(event);
    highlight_words(event);


def settings():
    setting_page = customtkinter.CTk();
    setting_page.title("Settings");
    setting_page.geometry("900x500");
    setting_page.iconbitmap("C:/Users/rajha/Desktop/STUDY MATERIAL/Figma Project/Python IDE/setting.ico");
    setting_page.mainloop();
    


def highlight_words(event=None):
    content = TextArea.get("1.0", "end-1c");
    for word in words_to_highlight:
        TextArea.tag_remove(word, "1.0", "end");
    for word, color in words_to_highlight.items():
        start_index = "1.0";
        while True:
            start_index = TextArea.search(word, start_index, stopindex="end");
            if not start_index:
                break;
            end_index = f"{start_index}+{len(word)}c";
            TextArea.tag_add(word, start_index, end_index);
            start_index = end_index;
        TextArea.tag_config(word, foreground=color);


def hide_side_bar():
    global sidebar_visibility;
    if(sidebar_visibility==True):
        sidebar_visibility=False;
        sidebar.pack_forget();
    else:
        messagebox.showerror("Error","sidebar is already Hidden");
    
    
    
    
     
    

def show_side_bar():
     global terminal_visibility;
     global sidebar_visibility;
     if(sidebar_visibility==False):
         frame.pack_forget();
         topbar.pack_forget();
         explorebutton.pack_forget();
         searchbutton.pack_forget();
         runbutton.pack_forget();
         settingbutton.pack_forget();
         LineNumber.pack_forget();
         NewFileButton.pack_forget();
         TextArea.pack_forget();
         lines.pack_forget();
         scrollbar.pack_forget();
         frame.pack(fill="both",expand=True);
         topbar.pack(side="top",fill="both")
         sidebar.pack(side="left",fill="both")
         explorebutton.pack(side="top",fill="x");
         searchbutton.pack(side="top",fill="both");
         runbutton.pack(side="top",fill="both");
         settingbutton.pack(side="bottom",fill="both");
         LineNumber.pack(side="left",fill="both");
         NewFileButton.pack(side="left");
         if(terminal_visibility==True):
             tFrame.pack(fill="both",side="bottom");
             tbar.pack(side="bottom",fill="both");
             theading.pack(side="left");
             TerminalTextArea.pack(fill="both", expand=True);
             tscrollbar.pack(side="right", fill="y");
             bottombar.pack(side="bottom",fill="both");
             TextArea.pack(fill="both",expand=True,side="left");
             lines.pack(pady=0,side="top");
             scrollbar.pack(side="right",fill="y");
             sidebar_visibility=True;
         else:
             TextArea.pack(fill="both",expand=True,side="left");
             lines.pack(pady=0,side="top");
             scrollbar.pack(side="right",fill="y");
             sidebar_visibility=True;
     else:
        messagebox.showerror("Error","sidebar is already visible");
    

    
     
    
def hide_terminal():
    global terminal_visibility;
    if(terminal_visibility==True):
         bottombar.pack_forget();
         TerminalTextArea.pack_forget();
         tscrollbar.pack_forget();
         theading.pack_forget();
         tFrame.pack_forget();
         tbar.pack_forget();
         terminal_visibility=False;
    else:
        messagebox.showerror("Error","Terminal is already Hidden");
        
   

def show_terminal():
    global terminal_visibility;
    global sidebar_visibility;
    if(terminal_visibility==False):
         frame.pack_forget();
         topbar.pack_forget();
         sidebar.pack_forget();
         explorebutton.pack_forget();
         searchbutton.pack_forget();
         runbutton.pack_forget();
         settingbutton.pack_forget();
         LineNumber.pack_forget();
         NewFileButton.pack_forget();
         TextArea.pack_forget();
         lines.pack_forget();
         scrollbar.pack_forget();
         frame.pack(fill="both",expand=True);
         topbar.pack(side="top",fill="both")
         if(sidebar_visibility==True):
                sidebar.pack(side="left",fill="both");
         explorebutton.pack(side="top",fill="x");
         searchbutton.pack(side="top",fill="both");
         runbutton.pack(side="top",fill="both");
         settingbutton.pack(side="bottom",fill="both");
         LineNumber.pack(side="left",fill="both");
         NewFileButton.pack(side="left");
         bottombar.pack(side="bottom",fill="both")
         tbar.pack(side="bottom",fill="both")
         theading.pack(side="left");
         tFrame.pack(fill="both",side="bottom");
         TerminalTextArea.pack(fill="both", expand=True)
         tscrollbar.pack(side="right", fill="y")
         TextArea.pack(fill="both",expand=True,side="left");
         lines.pack(pady=0,side="top");
         scrollbar.pack(side="right",fill="y");
         terminal_visibility=True;
    else:
        messagebox.showerror("Error","Terminal is already Visibile");

    
def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    if check_for_changes():
        try:
            path = askopenfilename(filetypes=[('Python Files', '*.py'),('ALL Files', '*.*')])
            if not path:
                return  # If the user cancels the open dialog, do nothing
            with open(path, 'r') as file:
                title=root.title();
                root.title(title+" "+path);
                code = file.read()
                TextArea.delete('1.0', END)
                TextArea.insert('1.0', code)
                set_file_path(path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {str(e)}")

def update_line_count(event=None):
    global current_line_count;
    # Get the current number of lines in the Text widget
    num_lines = int(TextArea.index('end-1c').split('.')[0])
    
    # If the number of lines increased, append new numbers to the label
    if num_lines > current_line_count:
        for i in range(current_line_count + 1, num_lines + 1):
            lines.config(text=lines.cget("text") + f"\n{i}")

    elif num_lines < current_line_count:
        line = lines.cget("text").split("\n")
        lines.config(text="\n".join(line[:num_lines]))

        
    current_line_count = num_lines




def check_for_changes():
    if TextArea.edit_modified():  # Check if the editor content has been modified
        response = messagebox.askyesno("Save Changes", "Do you want to save changes to your code?")
        if response:  # Yes, save changes
            save_as()
            return True
        elif response is None:  # Cancel the operation
            return False
    return True  # No changes or No, continue without saving


def on_closing():
    if check_for_changes():
        compiler.destroy()

def save():
    try:
        if not path:
            save_as();
        else:
            with open(path, 'w') as file:
                code = TextArea.get('1.0', END)
                file.write(code)
                set_file_path(path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    

def save_as():
    try:
        path = asksaveasfilename(filetypes=[('Python Files', '*.py'),('ALL Files', '*.*')])
        if not path:
            return  # If the user cancels the save dialog, do nothing

        with open(path, 'w') as file:
            code = TextArea.get('1.0', END)
            file.write(code)
            set_file_path(path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {str(e)}")



def about():
    info="PyDev-Studio is a powerful Integrated Development Environment (IDE) specifically designed for Python development. It offers a rich set of features that streamline coding, debugging, and project management , Created by Rajharpreet singh.PyDev-Studio is a powerful and versatile IDE that can greatly enhance your Python development experience. Whether you're a beginner or an experienced developer, it provides the tools and features you need to write high-quality Python code efficiently."
    messagebox.showinfo("Info",info);
    
def run():
    if str(TextArea.get(1.0, END)).isspace():
        messagebox.showerror("Error", "Please write some code to run.")
        return
    if file_path == '':
        messagebox.showerror("Error", "Please save the file first.");
        return;
    if check_for_changes():
        pass
    if platform.system() == 'Windows':
        # Open a new cmd window and run the Python script
        command = f'start cmd /k python "{file_path}"'
    elif platform.system() == 'Darwin':  # macOS
        command = f'open -a Terminal python3 "{file_path}"'
    else:  # Linux or others
        command = f'gnome-terminal -- python3 "{file_path}"'

    try:
        os.system(command)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run the script: {str(e)}")

        
   


Home();
customtkinter.set_appearance_mode("dark");
customtkinter.set_default_color_theme("dark-blue");
root = customtkinter.CTk()
root.iconbitmap("py.ico");
root.title("PyDev-Studio")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(str(screen_width-900)+"x"+str(screen_height-500));
frame=Frame(root,bg="#5E5E5E");
frame.pack(fill="both",expand=True);
topbar=Frame(master=frame,bg="#3C3C3C",height=60)
topbar.pack(side="top",fill="both")
sidebar=Frame(master=frame,bg="#333333",width=80)
sidebar.pack(side="left",fill="both")
exp_btn= PhotoImage(file='open.png')
search_btn= PhotoImage(file='search.png')
run_btn=PhotoImage(file='run.png')
setting_btn=PhotoImage(file='setting.png')
explorebutton=Button(sidebar,text="Explore",image=exp_btn,bg="#333333",fg="white",relief="sunken",width=60,height=80,bd=0,command=open_file);
explorebutton.pack(side="top",fill="x");
searchbutton=Button(sidebar,text="search",image=search_btn,bg="#333333",fg="white",relief="sunken",width=60,height=80,bd=0);
searchbutton.pack(side="top",fill="both");
runbutton=Button(sidebar,text="run",bg="#333333",image=run_btn,fg="white",relief="sunken",width=60,height=80,bd=0,command=run);
runbutton.pack(side="top",fill="both");
settingbutton=Button(sidebar,text="settings",image=setting_btn,bg="#333333",fg="white",relief="sunken",width=60,height=80,bd=0,command=settings);
settingbutton.pack(side="bottom",fill="both");
LineNumber=Frame(frame,bg="#1E1E1E",bd=10,width=32,highlightbackground="#565656", highlightthickness=0.5);
LineNumber.pack(side="left",fill="both");
NewFileButton=Button(topbar,text="Open File",bg="#3C3C3C",fg="white",relief="sunken",width=12,bd=0,command=open_file);
NewFileButton.pack(side="left");
NewFileButton=Button(topbar,text="Save File",bg="#3C3C3C",fg="white",relief="sunken",width=12,bd=0,command=save_as);
NewFileButton.pack(side="left");
NewFileButton=Button(topbar,text="Run",bg="#3C3C3C",fg="white",relief="sunken",width=12,bd=0,command=run);
NewFileButton.pack(side="left");
NewFileButton=Button(topbar,text="Show Sidebar",bg="#3C3C3C",fg="white",relief="sunken",width=12,bd=0,command=show_side_bar);
NewFileButton.pack(side="left");
NewFileButton=Button(topbar,text="Hide Sidebar",bg="#3C3C3C",fg="white",relief="sunken",width=12,bd=0,command=hide_side_bar);
NewFileButton.pack(side="left");
NewFileButton=Button(topbar,text="Show Terminal",bg="#3C3C3C",fg="white",relief="sunken",width=12,bd=0,command=show_terminal);
NewFileButton.pack(side="left");
NewFileButton=Button(topbar,text="Hide Terminal",bg="#3C3C3C",fg="white",relief="sunken",width=12,bd=0,command=hide_terminal);
NewFileButton.pack(side="left");
NewFileButton=Button(topbar,text="Help",bg="#3C3C3C",fg="white",relief="sunken",width=12,bd=0,command=about);
NewFileButton.pack(side="left");
bottombar=Frame(master=frame,bg="#1E1E1E",height=300,bd=0.5)
bottombar.pack(side="bottom",fill="both")
tbar=Frame(master=frame,bg="#323232",height=30)
tbar.pack(side="bottom",fill="both")
theading=Label(master=tbar,text="TERMINAL",bg="#323232",fg="white");
theading.pack(side="left");
tFrame=Frame(bottombar,bg="#1E1E1E",height=300,width=30)
tFrame.pack(fill="both",side="bottom");
TerminalTextArea = Text(tFrame, bg="#1E1E1E", fg="white", font=("verdana", 12), height=5)
TerminalTextArea.pack(fill="both", expand=True)
tscrollbar = customtkinter.CTkScrollbar(TerminalTextArea, command=TerminalTextArea.yview)
tscrollbar.pack(side="right", fill="y")
TerminalTextArea.config(yscrollcommand=tscrollbar.set)
TextArea=Text(frame,bg="#1E1E1E",fg="white",font=("verdana", 12),cursor="xterm #0000FF");
TextArea.pack(fill="both",expand=True,side="left");
TextArea.bind("<KeyRelease>", on_key_release);
scrollbar = customtkinter.CTkScrollbar(TextArea,command=TextArea.yview);
scrollbar.pack(side="right",fill="y");
TextArea.config(yscrollcommand=scrollbar.set)
lines=Label(LineNumber,text="1",bg="#1E1E1E",fg="#858585",font=("verdana", 10) );
lines.pack(pady=0,side="top");
root.mainloop()





        

    
