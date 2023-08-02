import customtkinter as CTk
from tkinter import messagebox
import time

CTk.set_appearance_mode('Dark')
CTk.set_appearance_mode('blue')

app = CTk.CTk()
app.title("問題ゲーム")
app.geometry("450x320")

def lv1():
    game_label.destroy()
    next_btn1.destroy()
    label1.pack()
    label1.place(x=115, y=25)
    write_ans.pack()
    write_ans.place(x=225, y=100)
    write_box.pack()
    write_box.place(x=125, y=95)
    ok_btn.pack()
    ok_btn.place(x=190, y=140)

def lv2():
    label1.destroy()
    ok_btn.destroy()
    next_lv2.destroy()
    write_ans.delete(0, CTk.END)
    label2.pack()
    label2.place(x=115, y=25)
    ok_btn2.pack()
    ok_btn2.place(x=190, y=140)

def lv3():
    label2.destroy()
    ok_btn2.destroy()
    next_lv3.destroy()
    write_ans.delete(0, CTk.END)
    label3.pack()
    label3.place(x=115, y=25)
    ok_btn3.pack()
    ok_btn3.place(x=190, y=140)

def lv4():
    label3.destroy()
    ok_btn3.destroy()
    next_lv4.destroy()
    write_ans.delete(0, CTk.END)
    label4.pack()
    label4.place(x=115, y=25)
    ok_btn4.pack()
    ok_btn4.place(x=190, y=140)

def endgame():
    app.destroy()    
    


#-レベル1-------------------------------------------------------------------

game_label = CTk.CTkLabel(master=app, text="問題ゲームへようこそ！\nここでは問題に答えてもらいます。", bg_color='#393a3b', text_color="#5ce9ff", font=('Heaveltica', 24, 'bold'), )
game_label.pack()
game_label.place(x=25, y=100)

next_btn1 = CTk.CTkButton(master=app, text="次へ", command=lv1, font=('Heaveltica', 23, 'bold'), height=45)
next_btn1.pack()
next_btn1.place(x=155, y=165)

def q1():
    if write_ans.get()=='8':
        messagebox.showinfo('結果', '正解！レベル2に進めます！')
        next_lv2.pack()
        next_lv2.place(x=115, y=185)

    else:
        a = messagebox.askyesno('結果', '不正解...もう一度挑戦しますか？')
        if a==False:
            app.destroy()

label1 = CTk.CTkLabel(master=app, text="問題1\n\n 6x8÷6=?", text_color="#78ebff", bg_color="black", font=('Heaveltica', 20, 'bold'), height=20, width=200)
write_ans = CTk.CTkEntry(master=app, width=70, height=35, font=("Heaveltica", 25, 'bold'))
write_box = CTk.CTkLabel(master=app, text="入力欄: ", height=45, width=60, font=('Heaveltica', 23, 'bold'))
ok_btn = CTk.CTkButton(master=app, text="解答", height=30, width=50, font=('Heaveltica', 18, 'bold'), text_color="#00ff04", command=q1)
next_lv2 = CTk.CTkButton(master=app, text="次のレベルに挑戦する", font=('Heaveltica', 17, 'bold'), command=lv2)

#-レベル2----------------------------------------------------------------------------------

def q2():
    if write_ans.get()== '28':
        messagebox.showinfo('結果', '正解！レベル3に進めます！')
        next_lv3.pack()
        next_lv3.place(x=115, y=185)
    else:
        a = messagebox.askyesno('結果', '不正解...もう一度挑戦しますか？')    
        if a==False:
            app.destroy()

label2 = CTk.CTkLabel(master=app, text="問題2\n\n14x8÷4=?", text_color="#78ebff", bg_color="black", font=('Heaveltica', 20, 'bold'), height=20,width=200)
ok_btn2 = CTk.CTkButton(master=app, text="解答", height=30, width=50, font=('Heaveltica', 18, 'bold'), text_color="#00ff04", command=q2)
next_lv3 = CTk.CTkButton(master=app, text="次のレベルに挑戦する", font=('Heaveltica', 17, 'bold'), command=lv3)

#-レベル3---------------------------------------------

def q3():
    if write_ans.get()== '170':
        messagebox.showinfo('結果', '正解です！すごいですね！\n次のレベルが最後です。')
        next_lv4.pack()
        next_lv4.place(x=115, y=185)
    else:
        a = messagebox.askyesno('結果', '不正解...もう一度挑戦しますか？')
        if a== False:
            app.destroy()

label3 = CTk.CTkLabel(master=app, text="問題3\n\n(9x15)+35=?", text_color="#78ebff", bg_color="black", font=('Heaveltica', 20, 'bold'), height=20,width=200)
ok_btn3 = CTk.CTkButton(master=app, text="解答", height=30, width=50, font=('Heaveltica', 18, 'bold'), text_color="#00ff04", command=q3)
next_lv4 = CTk.CTkButton(master=app, text="次のレベルに挑戦する", font=('Heaveltica', 17, 'bold'), command=lv4)

#-ラスボス------------------------------

def q4():
    if write_ans.get()== '2654':
        messagebox.showinfo('結果', '正解！これで全クリだ！おめでとう！')
        endgames.pack()
        endgames.place(x=115, y=185)
    else:
        messagebox.askyesno('結果', '不正解...ラスボスに倒された\n君は気を失った...')
        time.sleep(0.3)
        app.destroy()

label4 = CTk.CTkLabel(master=app, text="ラスボス問題\n\n1852+4800+2-4000", text_color="#78ebff", bg_color="black", font=('Heaveltica', 20, 'bold'), height=20,width=200)
ok_btn4 = CTk.CTkButton(master=app, text="解答", height=30, width=50, font=('Heaveltica', 18, 'bold'), text_color="#00ff04", command=q4)
endgames = CTk.CTkButton(master=app, text="ゲーム終了する", font=('Heaveltica', 17, 'bold'), command=endgame)



app.mainloop()