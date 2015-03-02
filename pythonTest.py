#!/usr/local/bin/python
import curses
class Contact:
	u'Class determin contact in notebook'
	__name=''
	__number=''
	def __init__(self):
		self.__name = 'defaultName'
		self.__number = 'defaultNumber'
	def __init__(self, name, number):
		self.__name=name
		self.__number=number
	def getName(self):
		return self.__name
	def getNumber(self):
		return self.__number

class Note:
	u'Class determin note in notebook'
	__note=''
	__date=''
	def __init__(self):
		self.__note = 'defaultName'
		self.__date = 'defaultDate'
	def __init__(self, note, date):
		self.__note=note
		self.__date=date
	def getNote(self):
		return self.__note
	def getDate(self):
		return self.__date
noteBook = []

def DoMainMenu():
    myscreen.erase()
    myscreen.addstr(1,1,  "========================================")
    myscreen.addstr(2,1,  "           Notebook")
    myscreen.addstr(3,1,  "========================================")
    myscreen.addstr(4,1,  "  s - Show All Notes")
    myscreen.addstr(5,1,  "  c - Add contact")
    myscreen.addstr(6,1,  "  n - Add note")
    myscreen.addstr(7,1,  "  e - Exit")
    myscreen.addstr(8,1, "========================================")
    myscreen.addstr(9,1, " Enter a selection: ")
    myscreen.move(9,21)
    myscreen.refresh()

def DoNotebook():
    myscreen.erase()
    myscreen.addstr(1,1,  "========================================")
    myscreen.addstr(2,1,  "           Notebook")
    myscreen.addstr(3,1,  "========================================")
    myscreen.addstr(4,1,  "Contacts:")
    iter=5
    if not noteBook:
            myscreen.addstr(iter,1,"    There is no contacts!")
            iter+=1
    else:
            for i in noteBook:
                if isinstance(i, Contact):
                        myscreen.addstr(iter,1,'    Contact: '+str(i.getName())+' '+str(i.getNumber()))
                        iter+=1
    myscreen.addstr(iter,1,  "Notes:")
    iter+=1
    if not noteBook:
            myscreen.addstr(iter,1,"    There is no notes!")
            iter+=1
    else:
            for i in noteBook:
                if isinstance(i, Note):
                        myscreen.addstr(iter,1,' Note: '+str(i.getNote())+' '+str(i.getDate()))
                        iter+=1
    myscreen.addstr(iter,1, "========================================")
    myscreen.addstr(iter+1,1, " Press any key to exit..")
    myscreen.refresh()
    myscreen.getch()
    DoMainMenu()

def AddContact():
    myscreen.erase()
    myscreen.addstr(1,1,  "========================================")
    myscreen.addstr(2,1,  "           Contact")
    myscreen.addstr(3,1,  "========================================")
    myscreen.addstr(4,1,  "Name: ")
    myscreen.addstr(5,1,  "Phone: ")
    myscreen.addstr(6,1,  "========================================")
    inpName = myscreen.getstr(4,7,15)
    inpNumber = myscreen.getstr(5,8,15)
    noteBook.append(Contact(inpName, inpNumber))
    DoMainMenu()

def AddNote():
    myscreen.erase()
    myscreen.addstr(1,1,  "========================================")
    myscreen.addstr(2,1,  "           Contact")
    myscreen.addstr(3,1,  "========================================")
    myscreen.addstr(4,1,  "Note: ")
    myscreen.addstr(5,1,  "Date: ")
    myscreen.addstr(6,1,  "========================================")
    inpNote = myscreen.getstr(4,7,15)
    inpDate = myscreen.getstr(5,8,15)
    noteBook.append(Note(inpNote, inpDate))
    DoMainMenu()

    
def InputFunc():
        (posY, posX) =myscreen.getyx()
	while True:
		inp = myscreen.getch(posY,posX)
                myscreen.addch(posY,posX,inp)
		if(inp==ord('s')):
			DoNotebook()
		if(inp==ord('e')):
			break
		if(inp==ord('c')):
                        AddContact()
		if(inp==ord('n')):
                        AddNote()
			
def LogicLoop():
    DoMainMenu()
    InputFunc()
 
#  MAIN LOOP
try:
    myscreen = curses.initscr()
    LogicLoop()
finally:
    curses.endwin()
