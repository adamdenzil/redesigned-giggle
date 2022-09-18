from tkinter import *
root=Tk() 
root.title("Multidimensional") 
root.geometry("500x500")

label=Label(root)

array_1d=["adam","mehtab"]

array_2d=[["adam","A+"],["mehtab","A"]]

array_3d=[["adam","A+","Science"],["mehtab","A","Math"]]


print(array_3d[0][0][2])

def result():
    
 label["text"] = array_3d[0][0][0] + " got grade " + array_3d[0][0][1] +" and she is doing " + array_3d[0][0][2]   

btn=Button(root,text="show result",command=result )

btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)


root.mainloop()