import tkinter
from math import *
import numpy as np
import tkinter as tk   # python3
from numpy import unravel_index
import copy
TITLE_FONT = ("Helvetica", 18, "bold")

class AlgorithmApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button1 = tk.Button(self, text="Needleman Wunsch",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Smith Waterman",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.gap_penalty = -1
        self.match_award = 1
        self.mismatch_penalty = -1
        self.seq1 = ""
        self.seq2 = ""
        self.n = 0
        self.m = 0
        self.score = []
        self.scoreArrow=[]
        self.index = 0
        self.index2 = 0
        self.i = 0
        self.j = 0
        self.align1 = ""
        self.align2 = ""

        def zeros(rows, cols):
            retval = []
            for x in range(rows):
                retval.append([])
                for y in range(cols):
                    retval[-1].append(0)

            return retval

        def match_score(alpha, beta):
            if alpha == beta:
                return self.match_award
            elif alpha == '-' or beta == '-':
                return self.gap_penalty
            else:
                return self.mismatch_penalty
            

        def needleman_wunsch(i,j):
            match = self.score[i - 1][j - 1] + match_score(self.seq1[j - 1], self.seq2[i - 1])
            delete = self.score[i - 1][j] + self.gap_penalty
            insert = self.score[i][j - 1] + self.gap_penalty
            self.score[i][j] = max(match, delete, insert)

            self.scoreArrow = copy.deepcopy(self.score)
            showMatrix(self.scoreArrow)
            
            #signing from which refference-cell the score come
            if self.score[i][j] == match:
                self.scoreArrow[i-1][j-1]="↘"
                e = tk.Label(frame1,relief="solid",bd=1,fg="red")
                e.config(text=str(self.scoreArrow[i-1][j-1]))
                e.grid(row=i, column=j,stick="nsew")

                
            if self.score[i][j] == delete:
                self.scoreArrow[i-1][j]="↓"
                e = tk.Label(frame1,relief="solid",bd=1,fg="red")
                e.config(text=str(self.scoreArrow[i-1][j]))
                e.grid(row=i, column=j+1,stick="nsew")

                 
            if self.score[i][j] == insert:
                self.scoreArrow[i][j-1]="→"
                e = tk.Label(frame1,relief="solid",bd=1,fg="red")
                e.config(text=str(self.scoreArrow[i][j-1]))
                e.grid(row=i+1, column=j,stick="nsew")

        
        def needleman_wunsch_back(i,j):
            match = self.score[i - 1][j - 1] + match_score(self.seq1[j - 1], self.seq2[i - 1])
            delete = self.score[i - 1][j] + self.gap_penalty
            insert = self.score[i][j - 1] + self.gap_penalty
            self.score[i][j] = max(match, delete, insert)
            
            showMatrix(self.score)
            
            #signing from which refference-cell the score come
            if self.score[i][j] == match:
                self.score[i][j]=0
                e = tk.Label(frame1,relief="solid",bd=1,fg="red")

                e.config(text=str(self.score[i][j]))
                e.grid(row=i, column=j,stick="nsew")

                
            if self.score[i][j] == delete:
            
                self.score[i][j]=0
                e = tk.Label(frame1,relief="solid",bd=1,fg="red")

                e.config(text=str(self.score[i][j]))
                e.grid(row=i, column=j,stick="nsew")

                 
            if self.score[i][j] == insert:
          
                self.score[i][j]=0               
                e = tk.Label(frame1,relief="solid",bd=1,fg="red")
     
                e.config(text=str(self.score[i][j]))
                e.grid(row=i, column=j,stick="nsew")
                
        def traceback():
            if self.i > 0 and self.j > 0:
                score_current = self.score[self.i][self.j]
                score_diagonal = self.score[self.i - 1][self.j - 1]
                score_up = self.score[self.i][self.j - 1]
                score_left = self.score[self.i - 1][self.j]
                if score_current == score_diagonal + match_score(self.seq1[self.j - 1], self.seq2[self.i - 1]):
                    self.align1 += self.seq1[self.j - 1]
                    self.align2 += self.seq2[self.i - 1]
                    e = tk.Label(frame1,relief="solid",bd=1,bg="green")
                    e.config(text=str(score_diagonal))
                    e.grid(row=self.i, column=self.j,stick="nsew")
                    self.i -= 1
                    self.j -= 1
                elif score_current == score_up + self.gap_penalty:
                    self.align1 += self.seq1[self.j - 1]
                    self.align2 += '-'
                    e = tk.Label(frame1,relief="solid",bd=1,bg="green")
                    e.config(text=str(score_up))
                    e.grid(row=self.i+1, column=self.j,stick="nsew")
                    self.j -= 1
                elif score_current == score_left + self.gap_penalty:
                    self.align1 += '-'
                    self.align2 += self.seq2[self.i - 1]
                    e = tk.Label(frame1,relief="solid",bd=1,bg="green")
                    e.config(text=str(score_left))
                    e.grid(row=self.i, column=self.j+1,stick="nsew")
                    self.i -= 1
            #마지막 시퀀스 유사도 결과를 위한 것 
            elif self.j > 0:
                self.align1 += self.seq1[self.j - 1]
                self.align2 += '-'
                self.j -= 1

            elif self.i > 0:
                self.align2 += '-'
                self.align2 += self.seq2[self.i - 1]
                self.i -= 1

            else:
                self.align1 = self.align1[::-1]
                self.align2 = self.align2[::-1]

                label.config(text=self.align1 + '\n' + self.align2)
                       
                   
        def all_children (window) :
            _list = window.winfo_children()
            for item in _list :
                if item.winfo_children() :
                    _list.extend(item.winfo_children())
            return _list
        
        def initialize():
            self.index = 0
            self.index2 = 0
            widget_list = all_children(frame1)
            for item in widget_list:
                item.grid_forget()
            self.seqA= entry1.get()
            self.seqB= entry2.get()    
            self.seq1= self.seqA.upper()
            self.seq2= self.seqB.upper()
            self.gap_penalty = int(entry3.get())
            self.mismatch_penalty = int(entry3.get())
            self.n= len(self.seq1)
            self.m= len(self.seq2)
            self.i = self.m
            self.j = self.n
            self.score= zeros(self.m + 1, self.n + 1)
            self.align1 = "" #delete previous result for a new alignment
            self.align2 = "" #delete previous result for a new alignment
            
            for i in range(len(self.seq1)):
                e = tk.Label(frame1)
                e.config(text=self.seq1[i])
                e.grid(row=0,column=i+2)
                
            for i in range(len(self.seq2)):
                e = tk.Label(frame1)
                e.config(text=self.seq2[i])
                e.grid(row=i+2,column=0)
                
            for i in range(0, self.m + 1):
                self.score[i][0] = self.gap_penalty * i
            for j in range(0, self.n + 1):
                self.score[0][j] = self.gap_penalty * j
            
            label['text']=''
            showMatrix(self.score)
            
        def rightButton():
            if self.index <= self.n and self.index2 <= self.m:
                self.index = self.index+1
                if self.index%self.n == 1:
                    self.index = 1
                    self.index2 = self.index2+1
            ButtonEventRight()
            
        def leftButton():
            
            if self.index >=1 and self.index2 >=1:
                self.index = self.index-1
                if self.index == 0:
                    self.index = self.n
                    self.index2 = self.index2-1 
            ButtonEventLeft()
            
        def ButtonEventRight():
            if self.index <= self.n and self.index2 <=self.m:
                needleman_wunsch(self.index2,self.index)
            else:
                traceback()
                
        def ButtonEventLeft():
            if self.index >=1 and self.index2 >= 1:
                needleman_wunsch_back(self.index2,self.index)
            else:
                traceback()
            
        def showMatrix(score):
            entry = {}
            # create the table of widgets
            for row in range(len(score)):
                for column in range(len(score[0])):
                    index = (row, column)
                    e = tk.Label(frame1,relief="solid",bd=1)
                    e.config(text=str(score[row][column]))
                    e.grid(row=row+1, column=column+1, stick="nsew")
                    entry[index] = e 
            e = tk.Label(frame1,relief="solid",bd=1,bg="yellow")
            e.config(text=str(score[self.index2][self.index]))
            e.grid(row=self.index2+1, column=self.index+1,stick="nsew")
            #entry[(self.index2,self.index)] = e
                    
        

        frame1 = tkinter.Frame(self,relief="solid",bd=1)
        frame1.pack(side="left",fill="both",expand=True)
        frame2 = tkinter.Frame(self)
        frame2.pack(side="right", fill="both", expand=True)

        label1 = tkinter.Label(frame2, text="seq1")
        entry1 = tkinter.Entry(frame2)
        label2 = tkinter.Label(frame2, text="seq2")
        entry2 = tkinter.Entry(frame2)
        label3 = tkinter.Label(frame2,text="penalty")
        entry3 = tkinter.Entry(frame2)

        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)
        label2.grid(row=1, column=0)
        entry2.grid(row=1, column=1)
        label3.grid(row=2, column=0)
        entry3.grid(row=2, column=1)

        button1 = tkinter.Button(frame2, text="execution", width=10, command=initialize)
        button1.grid(row=3, column=1)
        button2 = tkinter.Button(frame2, text="<", width=3, command=leftButton)
        button2.grid(row=3, column=2)
        button3 = tkinter.Button(frame2, text=">", width=3, command=rightButton)
        button3.grid(row=3, column=3)

        label = tkinter.Label(frame2)
        label.grid(row=4, column=1)

        button = tk.Button(frame2, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=5, column=1)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.gap_penalty = -1
        self.match_award = 1
        self.mismatch_penalty = -1
        self.seq1 = ""
        self.seq2 = ""
        self.n = 0
        self.m = 0
        self.score = []
        self.npscore=[]
        self.max_score = 0
        self.index = 0
        self.index2 = 0
        self.i = 0
        self.j = 0
        self.align1 = ""
        self.align2 = ""
        self.index_maxi=0
        self.index_maxj=0

        def zeros(rows, cols):
            retval = []
            for x in range(rows):
                retval.append([])
                for y in range(cols):
                    retval[-1].append(0)

            return retval

        def match_score(alpha, beta):
            if alpha == beta:
                return self.match_award
            elif alpha == '-' or beta == '-':
                return self.gap_penalty
            else:
                return self.mismatch_penalty
            
        def smith_waterman(i,j):
            match = self.score[i - 1][j - 1] + match_score(self.seq1[j - 1], self.seq2[i - 1])
            delete = self.score[i - 1][j] + self.gap_penalty
            insert = self.score[i][j - 1] + self.gap_penalty
            self.score[i][j] = max(0,match, delete, insert) #change by add 0
            
            showMatrix(self.score)
            
            if self.score[i][j] == match:
                e = tk.Label(frame1,relief="solid",bd=1,fg="red")
                e.config(text=str(self.score[i-1][j-1]))
                e.grid(row=i, column=j,stick="nsew")
            if self.score[i][j] == delete:
                e = tk.Label(frame1,relief="solid",bd=1,fg="red")
                e.config(text=str(self.score[i-1][j]))
                e.grid(row=i, column=j+1,stick="nsew")
            if self.score[i][j] == insert:
                e = tk.Label(frame1,relief="solid",bd=1,fg="red")
                e.config(text=str(self.score[i][j-1]))
                e.grid(row=i+1, column=j,stick="nsew")    

        def traceback(i,j):##################################################
            
            if self.score[self.i][self.j] ==0: #if zero element has been reached 
                    self.align1 = self.align1[::-1]
                    self.align2 = self.align2[::-1]

                    label.config(text=self.align1 + '\n' + self.align2)
                    
            elif self.i > 0 and self.j > 0:
                score_current = self.score[self.i][self.j]
                score_diagonal = self.score[self.i - 1][self.j - 1]
                score_up = self.score[self.i][self.j - 1]
                score_left = self.score[self.i - 1][self.j]
                
                if score_current == score_diagonal + match_score(self.seq1[self.j - 1], self.seq2[self.i - 1]):
                    self.align1 += self.seq1[self.j - 1]
                    self.align2 += self.seq2[self.i - 1]
                    e = tk.Label(frame1,relief="solid",bd=1,bg="green")
                    e.config(text=str(score_diagonal))
                    e.grid(row=self.i, column=self.j,stick="nsew")
                    self.i -= 1
                    self.j -= 1
                elif score_current == score_up + self.gap_penalty:
                    self.align1 += ''#######
                    self.align2 += ''#######
                    e = tk.Label(frame1,relief="solid",bd=1,bg="green")
                    e.config(text=str(score_up))
                    e.grid(row=self.i+1, column=self.j,stick="nsew")
                    self.j -= 1
                elif score_current == score_left + self.gap_penalty:
                    self.align1 += ''#######
                    self.align2 += ''#######
                    e = tk.Label(frame1,relief="solid",bd=1,bg="green")
                    e.config(text=str(score_left))
                    e.grid(row=self.i, column=self.j+1,stick="nsew")
                    self.i -= 1
            elif self.j > 0:
                self.align1 += ''#######
                self.align2 += ''#######
                self.j -= 1

            elif self.i > 0:
                self.align2 += ''#######
                self.align2 += ''#######
                self.i -= 1

            else:
                self.align1 = self.align1[::-1]
                self.align2 = self.align2[::-1]

                label.config(text=self.align1 + '\n' + self.align2)
            
        def all_children (window) :
            _list = window.winfo_children()
            for item in _list :
                if item.winfo_children() :
                    _list.extend(item.winfo_children())
            return _list
        
        def initialize():
            self.index = 0
            self.index2 = 0
            widget_list = all_children(frame1)
            for item in widget_list:
                item.grid_forget()
            self.seqA= entry1.get()
            self.seqB= entry2.get()    
            self.seq1= self.seqA.upper()
            self.seq2= self.seqB.upper()
            self.gap_penalty = int(entry3.get())
            self.mismatch_penalty = int(entry3.get())
            self.n= len(self.seq1)
            self.m= len(self.seq2)
            self.i = self.m
            self.j = self.n
            self.score= zeros(self.m + 1, self.n + 1)
            self.align1 = "" #delete previous result for a new alignment
            self.align2 = "" #delete previous result for a new alignment
            
            for i in range(len(self.seq1)):
                e = tk.Label(frame1)
                e.config(text=self.seq1[i])
                e.grid(row=0,column=i+2)
                
            for i in range(len(self.seq2)):
                e = tk.Label(frame1)
                e.config(text=self.seq2[i])
                e.grid(row=i+2,column=0)
                
            for i in range(0, self.m + 1):
                self.score[i][0] = 0
            for j in range(0, self.n + 1):
                self.score[0][j] = 0
            
            label['text']=''
            showMatrix(self.score)
            
        def rightButton():
            if self.index <= self.n and self.index2 <= self.m:
                self.index = self.index+1
                if self.index%self.n == 1:
                    self.index = 1
                    self.index2 = self.index2+1
            ButtonEventRight()
            
        def leftButton():
            
            if self.index >=1 and self.index2 >=1:
                self.index = self.index-1
                if self.index == 0:
                    self.index = self.n
                    self.index2 = self.index2-1 
            ButtonEventLeft()
            
        def ButtonEventRight():
            if self.index <= self.n and self.index2 <=self.m:
                smith_waterman(self.index2,self.index)
            if self.index==self.n and self.index2==self.m:
                self.npscore=np.array(self.score) #seearching for max value
                (self.i,self.j)=unravel_index(self.npscore.argmax(), self.npscore.shape)
                traceback(self.i,self.j)#trace from max value
                e = tk.Label(frame1,relief="solid",bd=1,bg="red")
                e.config(text=str(self.score[self.i+1][self.j+1]))
                e.grid(row=self.i+2, column=self.j+2,stick="nsew")
            else:
                traceback(self.index,self.index2)

        def ButtonEventLeft():
            if self.index >=1 and self.index2 >= 1:
                smith_waterman(self.index2,self.index)
            else:
                traceback(self.index,self.index2)
                
        def showMatrix(score):
            entry = {}
            # create the table of widgets
            for row in range(len(score)):
                for column in range(len(score[0])):
                    index = (row, column)
                    e = tk.Label(frame1,relief="solid",bd=1)
                    e.config(text=str(score[row][column]))
                    e.grid(row=row+1, column=column+1, stick="nsew")
                    entry[index] = e 
            e = tk.Label(frame1,relief="solid",bd=1,bg="yellow")
            e.config(text=str(score[self.index2][self.index]))
            e.grid(row=self.index2+1, column=self.index+1,stick="nsew")
#             entry[(self.index2,self.index)] = e
                    
        
        frame1 = tkinter.Frame(self,relief="solid",bd=1)
        frame1.pack(side="left",fill="both",expand=True)
        frame2 = tkinter.Frame(self)
        frame2.pack(side="right", fill="both", expand=True)

        label1 = tkinter.Label(frame2, text="seq1")
        entry1 = tkinter.Entry(frame2)
        label2 = tkinter.Label(frame2, text="seq2")
        entry2 = tkinter.Entry(frame2)
        label3 = tkinter.Label(frame2,text="penalty")
        entry3 = tkinter.Entry(frame2)

        label1.grid(row=0, column=0)
        entry1.grid(row=0, column=1)
        label2.grid(row=1, column=0)
        entry2.grid(row=1, column=1)
        label3.grid(row=2, column=0)
        entry3.grid(row=2, column=1)

        button1 = tkinter.Button(frame2, text="execution", width=10, command=initialize)
        button1.grid(row=3, column=1)
        button2 = tkinter.Button(frame2, text="<", width=3, command=leftButton)
        button2.grid(row=3, column=2)
        button3 = tkinter.Button(frame2, text=">", width=3, command=rightButton)
        button3.grid(row=3, column=3)

        label = tkinter.Label(frame2)
        label.grid(row=4, column=1)

        button = tk.Button(frame2, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=5, column=1)
    
if __name__ == "__main__":
    app = AlgorithmApp()
    app.mainloop()
