#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:25:33 2019

@author: rzd
"""

from tkinter import *
from respond import send_messages
from extractdata import get_request_data
import time

state=0
currency_information={}
condition=None
def main():


    def sendMsg():#发送消息
        strMsg = "Me:" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+ '\n'
        txtMsgList.insert(END, strMsg, 'greencolor')
        message=txtMsg.get('0.0',END)
        global state,currency_information,condition
        request_data,currency_information,condition=get_request_data(message,currency_information,condition)
        state,res=send_messages(message,state)
        respond=res+"\n"
        data="The request data is here: "+str(request_data)+"\n"
        txtMsgList.insert(END, message)
        robMsg="Robot:"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+ '\n'
        txtMsgList.insert(END,robMsg,'greencolor')
        txtMsgList.insert(END,respond)
        if request_data!=None:
            txtMsgList.insert(END,data)
        txtMsg.delete('0.0', END)

    def cancelMsg():#取消信息
        txtMsg.delete('0.0', END)

    def sendMsgEvent(event):#发送消息事件
        if event.keysym =='Up':
            sendMsg()   
                  
    #创建窗口
    app = Tk()
    app.title('与Robot聊天')

    #创建frame容器
    frmLT = Frame(width = 500, height = 300, bg = 'white')
    frmLC = Frame(width = 500, height = 60, bg = 'white')
    frmLB = Frame(width = 500, height = 30)

    #创建控件
    txtMsgList = Text(frmLT)
    txtMsgList.tag_config('greencolor',foreground = '#008C00')#创建tag
    txtMsg = Text(frmLC)
    txtMsg.bind("<KeyPress-Up>", sendMsgEvent)
    btnSend = Button(frmLB, text = '发送', width = 8, command = sendMsg)
    btnCancel =Button(frmLB, text = '取消', width = 8, command = cancelMsg)


    #窗口布局
    frmLT.grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 3)
    frmLC.grid(row = 1, column = 0, columnspan = 2, padx = 1, pady = 3)
    frmLB.grid(row = 2, column = 0, columnspan = 2)

    #固定大小
    frmLT.grid_propagate(0)
    frmLC.grid_propagate(0)
    frmLB.grid_propagate(0)

    btnSend.grid(row = 2, column = 0)
    btnCancel.grid(row = 2, column = 1)
    txtMsgList.grid()
    txtMsg.grid()

    #主事件循环
    app.mainloop()

if  __name__ == "__main__":
    main()

          
        
    

    

    
