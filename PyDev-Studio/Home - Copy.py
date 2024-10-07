from customtkinter import*
from tkinter import*
root=CTk();
root.title("PyDev-Studio");
root.iconbitmap("C:/Users/rajha/Desktop/STUDY MATERIAL/Figma Project/Python IDE/py.ico");
root.geometry("900x600");
set_appearance_mode("dark");
set_default_color_theme("dark-blue");
sidebar=CTkFrame(root,width=250,height=900,bg="#292929");
sidebar.pack(side="left",fill="both");

frame=CTkFrame(root,width=500,height=400,bg="gray");
frame.pack(side="top",pady=50);


button_frame=Frame(root,bg="#212325",height=300,width=800);
button_frame.pack();

n= PhotoImage(file='n.png')
o= PhotoImage(file='open.png')
s= PhotoImage(file='set.png')
sl=PhotoImage(file='side logo.png')



button1=CTkButton(button_frame,text="",height=70,width=75,corner_radius=7,image=n);
button1.pack(side="left",padx=40,expand=True);

button2=CTkButton(button_frame,text="",height=70,width=75,corner_radius=4,image=o);
button2.pack(side="left",padx=40,expand=True);


button3=CTkButton(button_frame,text="",height=70,width=75,corner_radius=4,image=s);
button3.pack(side="left",padx=40,expand=True);




logo=Label(sidebar,bg="#292929",bd=0,image=sl);
logo.pack();


button4=Button(sidebar,text="Projects                                                      ",height=3,width=40,relief="sunken",bg="#292929",fg="white",bd=0);
button4.pack();



button5=Button(sidebar,text="Learn PyDev-Studio                                  ",height=3,width=40,relief="sunken",bg="#292929",fg="white",bd=0);
button5.pack();

button6=Button(sidebar,text="Support                                                    ",height=3,width=40,relief="sunken",bg="#292929",fg="white",bd=0);
button6.pack();


label=Label(frame,text="Welcome to PyDev-Studio",font=("Arial", 24, "bold"),fg="white",bg="#212325");
label.pack(expand=True);

label1=Label(frame,text="Develop Advance Python projects from Scratch",font=("roboto", 14),fg="white",bg="#212325");
label1.pack(expand=True);


root.mainloop();
