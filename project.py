

#!-------------------------------------------------------------------------------------------------------------------------!
                                                     #   Project
#!--------------------------------------------------------------------------------------------------------------------------!
import cv2
from tkinter import *
import tkinter.messagebox
import numpy as np
root=Tk()
root.title("Welcome to the project")
root.geometry("700x450")
root.configure(background="powder blue")
label=Label(root,text='Python!',fg='Black',bg='powder blue',font=(None,60),height=1,width=15)
label.pack(side=TOP)
root1=Frame(root,bg='powder blue')
#!---------------------------------------------------------------------------------------------------------------!
                            #                  Reads the image
#!----------------------------------------------------------------------------------------------------------------!
def read():
        img=cv2.imread('a.jpg')
        cv2.imshow('output image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#!----------------------------------------------------------------------------------------------------------------!
                              #                Converting to binary
#!----------------------------------------------------------------------------------------------------------------!

def binimg():
        img=cv2.imread('a.jpg',0) #convert to greyscale
      #  cv2.imshow('gray',img)
       # cv2.waitKey(0)
        ret,bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

        cv2.imshow('binary',bw)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
#!------------------------------------------------------------------------------------------------------------------!
                                #                  Exit function  
#!-------------------------------------------------------------------------------------------------------------------!

def exitt():
    tkinter.messagebox.showinfo("Example","Do you want to Exit??")
    exit()
    root.destroy()
#!-------------------------------------------------------------------------------------------------------------------!
                                #                   Extracting RGB
#!--------------------------------------------------------------------------------------------------------------------!
def rgb():
        import numpy as np 
        img=cv2.imread('a.jpg')
        #cv2.imshow("orginal",img)
        #cv2.waitKey(0)
# now extract R G B 

        B,G,R=cv2.split(img)
        #print("\033[1;35;40m",img.shape)
        zeros=np.zeros(img.shape[:2],dtype="uint8")
        cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
        cv2.imshow("GREEn",cv2.merge([zeros,G,zeros]))
        cv2.imshow("BLUE",cv2.merge([B,zeros,zeros]))
        cv2.imshow("MERGE all three bgr=orginalimage",cv2.merge([B,G,R]))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
#!---------------------------------------------------------------------------------------------------------------------!
                                #                   Edge detection
#!---------------------------------------------------------------------------------------------------------------------!
def edge():
    img=cv2.imread("a.jpg",0)
    height,width=img.shape
    canny=cv2.Canny(img,20,170)
    cv2.imshow("Canny edge",canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#!---------------------------------------------------------------------------------------------------------------------!
                               #                   Blur image
#!----------------------------------------------------------------------------------------------------------------------!

def blur1():
    img=cv2.imread("a.jpg")
    bilateral=cv2.bilateralFilter(img,9,75,75)
    cv2.imshow("Bilateral blur image",bilateral)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#!------------------------------------------------------------------------------------------------------------------------!
                                     #              Gray scale image
#!-------------------------------------------------------------------------------------------------------------------------!
def grayy():
    img = cv2.imread("a.jpg")
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
    cv2.imshow("Gray scale img",gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#!--------------------------------------------------------------------------------------------------------------------------!
                                        #       Negative of image
#!---------------------------------------------------------------------------------------------------------------------------!
def negative():
    import cv2
    img_1=cv2.imread("a.jpg",0)
    img_2=255-img_1
    cv2.imshow("Negative image",img_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#!----------------------------------------------------------------------------------------------------------------------------!
                                       #   Logrithm image
#!-----------------------------------------------------------------------------------------------------------------------------!
def log1():
        img_1=cv2.imread("ab.jpg",0)
        img_2=np.uint8(np.log1p(img_1))
        thresh=1
        img_3=cv2.threshold(img_2,thresh,255,cv2.THRESH_BINARY)[1]
        cv2.imshow("Input image",img_1)
        cv2.imshow("Log transformed",img_3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


#-----------------------------------------------------------------------------------------------------------------------------!

#!------------------------------------------------------------------------------------------------------------------------------!
btn1=Button(root1,text="Original image",fg="red",command=read, width=25,height=2)
btn1.grid(row=0,column=0,pady=10,padx=25)
btn2=Button(root1,text="Binary image",fg="red",command=binimg,width=25,height=2)
btn2.grid(row=1,column=0,pady=10,padx=25)
btn3=Button(root1,text="Extract RGB",fg="red",command=rgb,width=25,height=2)
btn3.grid(row=2,column=0,pady=10,padx=25)
btn4=Button(root1,text="Detect Edge",fg="red",command=edge,width=25,height=2)
btn4.grid(row=3,column=0,pady=10,padx=25)
btn5=Button(root1,text="Blur",fg="red",command=blur1,width=25,height=2)
btn5.grid(row=4,column=0,pady=10,padx=25)
btn6=Button(root1,text="Gray Scale",fg="red",command=grayy,width=25,height=2)
btn6.grid(row=0,column=1,pady=10,padx=25)
btn7=Button(root1,text="Negative",fg="red",command=negative,width=25,height=2)
btn7.grid(row=1,column=1,pady=10,padx=25)
btn8=Button(root1,text="log",fg="red",command=log1,width=25,height=2)
btn8.grid(row=2,column=1,pady=10,padx=25)
btn=Button(root1,text="Exit",fg="red",command=exitt,width=25,height=2)
btn.grid(row=3,column=1,pady=10,padx=25)

root1.pack(side=BOTTOM)
root.mainloop()