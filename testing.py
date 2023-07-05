from tkinter import * 
from tkinter import messagebox as mb 
import random
import re

def msg_sub():
  mb.showerror("Error", "Select a subject")

def submit():
    global a
    global Numofqs
    a=get_subject.get()
    Numofqs=ques.get()

    if a!=1 and a!=2 and a!=3 and a!=4 and a!=5 :
      msg_sub()
    else:
      test()

def test():
  global root
  root = Toplevel(window)
  root.geometry("1200x600")
  root.title("BATCH 8")
  
  global a
  global b
  global Numofqs
  
  if a==1:
        b="Chemistry"
        from Chemistry import easy,moderate,tough
  elif a==2:
        b="Industry 4.0"
        from Industry4_0 import easy,moderate,tough
  elif a==3:
        b="Math"
        from Math import easy,moderate,tough
  elif a==4:
        b="Physics"
        from Physics import easy,moderate,tough
  elif a==5:
        b="OOP"
        from OOP import easy,moderate,tough

  import time  
  begin = time.time()

  random.shuffle(easy)
  random.shuffle(moderate)
  random.shuffle(tough)

  questioncount=0
  i=j=k=0
  q=[]
  options=[]
  a=[]
  User=[]
  
  def question_func(alist,i): 
      s=(alist[i].question)
      q.append(s)
      qaItem=alist[i]
      possible = qaItem.otherAnsw + [qaItem.corrAnsw]
      random.shuffle(possible)
      op=possible
      options.append(op)
      a.append(alist[i].corrAnsw)

  while True:
      if questioncount<int(Numofqs*0.33) :      
        question_func(easy,i)
        i+=1
      elif questioncount<int(Numofqs*0.67):
        question_func(moderate,j)
        j+=1
      else:
        question_func(tough,k)
        k+=1
      questioncount+=1
      if questioncount==Numofqs:
        break

  class Review:
    def __init__(self, question, correctAnswer, userAnswer):
      self.q = question
      self.cAnsw = correctAnswer
      self.uAnsw = userAnswer
    def display(self):
        if self.uAnsw=="No option":
          print("Q{}.{}".format(i+1,self.q))
          print("Your answer : You have not selected any option")
          print("Correct Answer :",self.cAnsw,"\n")
        else:
          print("Q{}.{}\nYour Answer : {}\nCorrect Answer : {}".format(i+1,self.q,self.uAnsw,self.cAnsw))
          if self.uAnsw == self.cAnsw:
            print("Your answer is correct\n")
          else:
            print("Your answer is wrong\n")

  class Quiz:
      def __init__(self, master):
          self.display_title(master) 
          self.opt_selected = IntVar()
          self.qn = 0
          self.correct = 0
          self.ques = self.create_q(master, self.qn)
          self.opts = self.create_options(master, 4)
          self.display_q(self.qn) 
          self.Notattempted=0
          self.button = Button(master, text="NEXT", command=self.next_btn,width=10,bg="green", fg="white",font=("ariel",16," bold"))
          self.button.place(x=300,y=500)
          self.quit_button = Button(master, text="QUIT", command=self.confirm,width=10,bg="red", fg="white",font=("ariel",16," bold"))
          self.quit_button.place(x=800,y=500)

      def confirm(self):
         answer = mb.askyesno(title='confirmation', message='Are you sure that you want to quit?')
         if answer:
            window.destroy()
            with open("Test Details.csv","a") as f:
              f.write(b+","+username1+","+str(Numofqs)+",-,-,-,-,")

      def display_title(self,master):
          title = Label(master, text="Test on "+b, 
          width=85, bg="violetred2",fg="white", font=("helvetica 14",18, "bold")) 
          title.place(x=0, y=2)
          return title

      def create_q(self, master, qn):
          w = Label(master, text=q[qn],width=100,fg="black", font=("ariel",16, "bold"),wraplength=900, justify="center")
          w.place(x=1,y=100)
          return w

      def create_options(self, master, n):
          b_val = 0
          b = []
          y_pos = 215
          while b_val < n:
              btn = Radiobutton(master, text="None", variable=self.opt_selected, value=b_val+1,fg="gray1",font = ("ariel",14),wraplength=900, justify="left")
              b.append(btn)
              btn.place(x = 120, y = y_pos)
              b_val = b_val + 1
              y_pos+=60
          return b

      def display_q(self, qn):
          b_val = 0
          self.opt_selected.set(0)
          self.ques['text'] = str(qn+1)+'. '+q[qn]
          for op in options[qn]:
              self.opts[b_val]['text'] = op
              b_val = b_val + 1            
       
      def check_q(self, qn):
          selected=self.opt_selected.get()
          if selected==0:
            self.Notattempted+=1
            userAnsw="No option"
            User.append(Review(q[qn],a[qn],userAnsw))
          else:  
            userAnsw=((options[qn])[self.opt_selected.get()-1])
            User.append(Review(q[qn],a[qn],userAnsw))         
            if (options[qn])[self.opt_selected.get()-1] == a[qn]:
                return True
          return False

      def print_results(self):
          wrong_count = len(q) - self.correct -self.Notattempted
          correct = self.correct
          wrong = wrong_count
          total=len(q)
          score = float(self.correct / len(q) * 100)
          score="{:.2f}".format(score)
          with open("Scores.txt","a") as f:
            f.write(score+"\n")
          l=[]
          with open("Scores.txt","r") as f:
              for line in f:
                   a = line.strip("\n")
                   a=float(a)
                   l.append(a)
          l.sort()
          h=l[len(l)-1]
          h="{:.2f}".format(h)
          mb.showinfo("Result","Total questions : {}\nCorrect : {}\nWrong : {}\nNot attempted : {}\nScore : {} %\nHighest Percentage scored : {} %".format(total,correct,wrong,self.Notattempted,score,h))
          with open("Test Details.csv","a") as f:
            f.write(b+","+username1+","+str(total)+","+str(correct)+","+str(wrong)+","+str(self.Notattempted)+","+str(score)+" %"+",")
          window.destroy()

      def next_btn(self):
          if self.check_q(self.qn):
              self.correct += 1
          self.qn = self.qn + 1
          if self.qn == len(q):
              self.button['state']=DISABLED  
              self.print_results()
              print("\nTEST COMPLETED")
          else:
              self.display_q(self.qn)

  app = Quiz(root)
  root.mainloop()

  time.sleep(1)
  end = time.time()
  total_sec=int(end - begin)
  hours = total_sec//3600
  minutes= (total_sec%3600)//60
  seconds=total_sec - ((hours*3600) + (minutes*60))

  print("\nTIME TAKEN : {} hour {} minutes {} seconds\n".format(hours,minutes,seconds))
  with open("Test Details.csv","a") as f:
            f.write("{}hour {}minutes {}seconds".format(hours,minutes,seconds))
            f.write("\n")
  print("-"*150,"\n")
  print("{:^150}".format("THE REVIEW OF THE TEST"))
  print("")
  print("-"*150,"\n")

  for i in range (len(User)):
      User[i].display()
      print("-"*150,"\n")
        
def testing():
    global window
    global get_subject
    global ques
    window = Tk()
    window.geometry("500x450")
    window.title("Subject")
    get_subject=IntVar()
    get_no=IntVar()

    subject=Label(window, text="Select a subject", font=("Calibri", 14,"bold"))
    subject.place(x=70,y=20)

    btn=Radiobutton(window, text="Chemistry",font=("Calibri", 13),variable=get_subject, value=1).place (x=70, y=60)
    btn=Radiobutton(window, text="Industry 4.0",font=("Calibri", 13),variable=get_subject, value=2).place (x=70, y=100)
    btn=Radiobutton(window, text="Math", font=("Calibri", 13),variable=get_subject,  value=3).place (x=70, y=140)
    btn=Radiobutton(window, text="Physics", font=("Calibri", 13),variable=get_subject, value=4).place (x=70, y=180)
    btn=Radiobutton(window, text="OOP", font=("Calibri", 13),variable=get_subject, value=5).place (x=70, y=220)
    
    noofqs=Label(window, text="Number of questions", font=("Calibri", 14,"bold"))
    noofqs.place(x=70,y=270)
    ques = Scale(window,from_=1, to=100,length=300, orient=HORIZONTAL)
    ques.place(x=70,y=300)
        
    sub=Button(window, text="START",width=10, bg="Red",fg="white",font=("Calibri", 13,"bold"),command=submit).place (x=250,y=370)    
    window.mainloop()

def msg_username():
    mb.showerror("Error", "The username isn\'t valid\nEnter a username")
def msg_password():
    mb.showerror("Error", "The passwords don\'t match\n Try again")
def register_success():
    mb.showinfo("Information", "Registration is successfully completed")
    
def register():
    global registerscr
    registerscr = Toplevel(main)
    registerscr.title("Register")
    registerscr.geometry("300x300")
 
    global username
    global password
    global username_entry
    global password_entry
    global password1
    global password1_entry
    username = StringVar()
    password = StringVar()
    password1= StringVar()  
 
    Label(registerscr, text="Enter the details below to register",width=200, bg="steel blue",font=("Calibri", 13,"bold")).pack()
    Label(registerscr, text="").pack()
    username_label = Label(registerscr, text="Username *",font=("Calibri", 12,"bold"))
    username_label.pack()
    username_entry = Entry(registerscr, textvariable=username)
    username_entry.pack()
    password_label = Label(registerscr, text="Password *",font=("Calibri", 12,"bold"))
    password_label.pack()
    password_entry = Entry(registerscr, textvariable=password, show='*')
    password_entry.pack()
    password1_label = Label(registerscr, text="Re-enter Password *",font=("Calibri", 12,"bold"))
    password1_label.pack()
    password1_entry = Entry(registerscr, textvariable=password1, show='*')
    password1_entry.pack()
    Label(registerscr, text="").pack()
    Button(registerscr, text="REGISTER", width=10, height=1, bg="indian red",font=("Calibri", 13,"bold"), command = register_user).pack()
    
def login():
    global loginscr
    loginscr = Toplevel(main)
    loginscr.title("Login")
    loginscr.geometry("300x250")
    Label(loginscr, text="Enter the details below to login",width=200, bg="orchid3", font=("Calibri", 13,"bold")).pack()
    Label(loginscr, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_loginentry
    global password_loginentry
 
    Label(loginscr, text="Username * ",font=("Calibri", 12,"bold")).pack()
    username_loginentry = Entry(loginscr, textvariable=username_verify)
    username_loginentry.pack()
    Label(loginscr, text="").pack()
    Label(loginscr, text="Password * ",font=("Calibri", 12,"bold")).pack()
    password_loginentry = Entry(loginscr, textvariable=password_verify, show= '*')
    password_loginentry.pack()
    Label(loginscr, text="").pack()
    Button(loginscr, text="LOGIN", width=10,bg="dark turquoise", height=1,font=("Calibri", 13,"bold"), command = login_verify).pack()
  
def register_user(): 
    username_info = username.get()
    password_info = password.get()
    password1_info = password1.get()

    x=0
    with open("Username Details.csv","r") as f:
        for line in f:
           a = line.strip(",")
           if username_info in a :
                mb.showerror("Error","The username already exists\nEither login with the existing username or use another username to register")
                username_entry.delete(0, END)
                x=1

    if x==0:
      if re.match(r"[\w.-]", username_info) ==None:
        msg_username()
        username_entry.delete(0, END)
      elif len(password_info)<6:
        mb.showerror("Error","The password should contain minimum 6 characters")
      elif re.search(r"[a-z]",password_info)== None:
        mb.showerror("Error","The password should contain atleast 1 lowercase letter")
      elif re.search(r"[A-Z]",password_info)== None:
        mb.showerror("Error","The password should contain atleast 1 uppercase letter")
      elif re.search(r"[0-9]",password_info)== None:
        mb.showerror("Error","The password should contain atleast 1 digit")
      elif re.search(r"\s",password_info):
        mb.showerror("Error","The password should not contain spaces")
      elif password_info!=password1_info:
        msg_password()
        password1_entry.delete(0, END)
      else:
         with open("Registration Details.csv","a") as f:
            f.write(username_info+","+password_info)
            f.write("\n")
         with open("Username Details.csv","a") as f:
            f.write(username_info+"\n")
         register_success()
         registerscr.destroy()

def login_sucess():
    mb.showinfo("Information", "Login is successfully completed")
    loginscr.destroy()
    main.destroy()
    testing()
 
def password_not_recognised():
     mb.showerror("Error", "Invalid password\nEnter the correct password")
 
def user_not_found():
    mb.showerror("Error", "User not found\nEnter a vaild username")
  
def login_verify():
    global username1
    global password2
    username1 = username_verify.get()
    password2 = password_verify.get()

    flag=0     
    with open("Registration Details.csv","r") as f:
        for line in f:
         a = line.strip(",")
         if username1 in a and password2 in a :
                login_sucess()
                flag=1
    if flag==0:
        if username1 not in a:
         username_loginentry.delete(0, END)
         password_loginentry.delete(0, END)
         user_not_found()
        elif password2 not in a:
          password_loginentry.delete(0, END)
          password_not_recognised()

def mainscreen():
    global main
    main = Tk()
    main.geometry("350x320")
    main.title("Account Login")
    Label(text="QUIZ-A-PRO", bg="chartreuse3", width="300", height="2", font=("Calibri", 14,"bold")).pack()
    Label(text="").pack()
    #Label(text="Select Your Choice", width="30", height="2", font=("Calibri", 13,"bold")).pack()
    Label(text="Already an existing user ?", width="30", font=("Calibri", 12)).pack()
    Label(text="").pack()
    Button(text="LOGIN", height="1", bg="coral3",width="20", font=("Calibri", 13,"bold"), command = login).pack()
    Label(text="").pack()
    Label(text="New user ?", width="30", font=("Calibri", 12)).pack()
    Label(text="").pack()
    Button(text="REGISTER", height="1",bg="goldenrod", width="20", font=("Calibri", 13,"bold"), command=register).pack()
 
    main.mainloop()
  
mainscreen()

