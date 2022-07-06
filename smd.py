import sqlite3
from tkinter import *

root = Tk()
root.title("Small Dictionary")
root.geometry("1280x720")
root.resizable(0,0)
root.configure(bg="#014852")

#Database
#create database or connect one
conn = sqlite3.connect('dictionary.db')
#create cursor
c = conn.cursor()
#create a Table
#c.execute('''CREATE TABLE dict(
#	chinese_word text,
#	english_word text)''')


def admin():
	adminp = Tk()
	adminp.title("Small Dictionary")
	adminp.geometry("700x500")
	adminp.resizable(0,0)
	adminp.configure(bg="#014852")
	def submit():
		#connenct database
		conn = sqlite3.connect('dictionary.db')
		# create cursor
		c = conn.cursor()

		#insert Into Table
		c.execute("INSERT INTO dict VALUES (:ch_entry, :en_entry)",
					{
					'ch_entry': ch_entry.get(),
					'en_entry': en_entry.get(),
					})

		#commit changes
		conn.commit()
		#close connection
		conn.close()

		ch_entry.delete(0,END)
		en_entry.delete(0,END)





	intro = Label(adminp, text="Input new word to database",font=("Roboto", 30), fg="white", bg="#014852", border=0)
	intro.place(x=100,y=50)

	ch_lbl = Label(adminp, text="Chinese",font=("Roboto", 24), fg="white", bg="#014852", border=0)
	ch_lbl.place(x=145,y=122)
	
	en_lbl = Label(adminp, text="English",font=("Roboto", 24), fg="white", bg="#014852", border=0)
	en_lbl.place(x=145,y=224)

	ch_entry = Entry(adminp, font=("Roboto", 24), fg="black", bg="white", border=0)
	ch_entry.place(x=145,y=158)

	en_entry = Entry(adminp, font=("Roboto", 24), fg="black", bg="white", border=0)
	en_entry.place(x=145,y=260)

	sub = Button(adminp, text="Submit", font=("Roboto", 24), fg="white", bg="#035460", border=0, command=submit)
	sub.place(x=275,y=371)


intro = Label(root, text="Small Self Dictionary",font=("Roboto", 48), fg="white", bg="#014852", border=0)
intro.place(x=350,y=63)

title = Label(root, text="Chinese ↔ English",font=("Roboto", 40), fg="white", bg="#014852", border=0)
title.place(x=400,y=170)

word= Entry(root, font=("Roboto", 35), fg="black", bg="white", border=0)
word.place(x=300,y=277)


	

def search():
	conn = sqlite3.connect('dictionary.db')
	search_text = word.get()
	c = conn.cursor()
	sql="SELECT * FROM dict WHERE chinese_word LIKE '"+ search_text +"'"
	c.execute(sql)
	records = c.fetchmany(3)
	for row in records:
		ch_result_lbl = Label(root, width=18, text=row[0],font=("Roboto", 36), fg="black", bg="white", border=0)
		ch_result_lbl.place(x=150,y=470)
			
		en_result_lbl = Label(root, width=18, text=row[1],font=("Roboto", 36), fg="black", bg="white", border=0)
		en_result_lbl.place(x=650,y=470)

		
	word.delete(0,END)	


searchb = Button(root, text="Search", font=("Roboto", 24), fg="white", bg="#035460", border=0, command=search)
searchb.place(x=839,y=277)

chinese_lbl = Label(root, width=18, text="Chinese",font=("Roboto", 36), fg="black", bg="white", border=0)
chinese_lbl.place(x=150,y=401)
	
english_lbl = Label(root, width=18, text="English",font=("Roboto", 36), fg="black", bg="white", border=0)
english_lbl.place(x=650,y=401)



adminb = Button(root, text="admin", font=("Roboto", 12), fg="white", bg="#035460", border=0, command=admin)
adminb.place(x=0,y=0)     # bu admin panelga olib baradigon knobka





root.mainloop()