from tkinter import *
from mydb import Database
from tkinter import messagebox
from tkinter import scrolledtext
import os
import nlpcloud

class NLPApp:

    def __init__(self):

        self.dbo = Database()

        self.root = Tk()
        self.root.title("NLPApp")
        self.root.iconbitmap(r"C:\Users\rajes\CampusXDSMP1.0\GUI development using python\resouces\favicon.ico")
        self.root.geometry("500x650")
        self.root.configure(bg="#101820")

        self.API_KEY = os.getenv("NLPCLOUD_API_KEY")

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):

        self.clear()
        
        heading = Label(self.root,text='Welcome To NLPApp',bg='#101820',fg='#A3EDE5')
        heading.pack(pady=(40,20))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text="Enter Email")
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=30)
        self.email_input.pack(pady=(5,10),ipady=3)

        label2 = Label(self.root,text="Enter Password")
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=30,show='*')
        self.password_input.pack(pady=(5,10),ipady=3)

        login_button = Button(self.root,text='Login',width=15,height=1,command=self.perform_login)
        login_button.pack(pady=(10,10))

        label3 = Label(self.root,text="Not a memeber?")
        label3.pack(pady=(20,10))

        redirect_button = Button(self.root,text='Register Now',command=self.register_gui)
        redirect_button.pack(pady=(10,10))

    def register_gui(self):

        self.clear()

        heading = Label(self.root,text='Welcome To NLPApp',bg='#101820',fg='#A3EDE5')
        heading.pack(pady=(40,20))
        heading.configure(font=('verdana',24,'bold'))

        label0 = Label(self.root,text="Enter Name")
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root,width=30)
        self.name_input.pack(pady=(5,10),ipady=3)

        label1 = Label(self.root,text="Enter Email")
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=30)
        self.email_input.pack(pady=(5,10),ipady=3)

        label2 = Label(self.root,text="Enter Password")
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=30,show='*')
        self.password_input.pack(pady=(5,10),ipady=3)

        register_button = Button(self.root,text='Register',width=15,height=1,command=self.perform_registration)
        register_button.pack(pady=(10,10))

        label3 = Label(self.root,text="Already a memeber?")
        label3.pack(pady=(20,10))

        redirect_button = Button(self.root,text='Login Now',command=self.login_gui)
        redirect_button.pack(pady=(10,10))


    def clear(self):
        
        for i in self.root.pack_slaves():
            i.destroy()

    
    def perform_registration(self):
        
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration successful. You can login now')
        else:
            messagebox.showerror('Error','Email already exists')

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Sucess','Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect email/password')


    def home_gui(self):

        self.clear()

        heading = Label(self.root,text='NLPApp Home Menu',bg='#101820',fg='#A3EDE5')
        heading.pack(pady=(40,20))
        heading.configure(font=('verdana',24,'bold'))

        ner_button = Button(self.root,text='NER (Entity Extraction)',width=30,height=2,command=self.ner_gui)
        ner_button.pack(pady=(10,10))

        sentiment_button = Button(self.root,text='Sentiment Analysis',width=30,height=2,command=self.sentiment_gui)
        sentiment_button.pack(pady=(10,10))

        heading_button = Button(self.root,text='Headline Generation',width=30,height=2,command=self.heading_gui)
        heading_button.pack(pady=(10,10))

        grammar_button = Button(self.root,text='Grammar and Spelling Correction',width=30,height=2,command=self.grammar_gui)
        grammar_button.pack(pady=(10,10))

        lang_button = Button(self.root,text='Language Detection',width=30,height=2,command=self.lang_gui)
        lang_button.pack(pady=(10,10))

        logout_button = Button(self.root,text='Logout',width=15,height=1,command=self.login_gui)
        logout_button.pack(pady=(10,10))

    def ner_gui(self):

        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#101820',fg='#A3EDE5')
        heading.pack(pady=(40,20))
        heading.configure(font=('verdana',24,'bold'))

        heading = Label(self.root,text='NER (Entity Extraction)',bg='#101820',fg='#A3EDE5')
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',24))

        label1 = Label(self.root, text='Enter the paragraph', bg='#101820', fg='white')
        label1.pack(pady=(10,5))

        self.par_input = scrolledtext.ScrolledText(self.root, width=50, height=8, wrap=WORD)
        self.par_input.pack(pady=(5,15))

        label2 = Label(self.root, text='What would you like to search',bg='#101820', fg='white')
        label2.pack(pady=(10,10))

        self.ser_input = Entry(self.root,width=30)
        self.ser_input.pack(pady=(5,10),ipady=3)

        ner_button = Button(self.root, text='Analyze NER',command=self.analyze_ner)
        ner_button.pack(pady=(10,10))

        self.ner_result = Label(self.root, text='',bg= '#101820',fg='white')
        self.ner_result.pack(pady=(10,10))
        self.ner_result.configure(font=('verdana',16))

        goback_button = Button(self.root, text='Go Back',command=self.home_gui)
        goback_button.pack(pady=(10,10))

    def analyze_ner(self):

        para = self.par_input.get('1.0',END).strip()
        search_term = self.ser_input.get().strip()

        if not self.API_KEY:
            messagebox.showerror("Error", "Missing NLPCloud API key.")
            return
        try:

            client = nlpcloud.Client("finetuned-llama-3-70b", self.API_KEY, gpu=True)

            if search_term:
                response = client.entities(para, searched_entity=search_term)
            else:
                response = client.entities(para)

            entities = response.get('entities',[])

            if entities:
                results = "\n".join([f"- {e.get('text')} ({e.get('type')})" for e in entities])
                self.ner_result.config(text=f"Entities Found:\n{results}")
            else:
                self.ner_result.config(text="No entities found.")

        except Exception as e:
            self.ner_result.config(text=f" error: {e}")

    def sentiment_gui(self):

        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#101820',fg='#A3EDE5')
        heading.pack(pady=(40,20))
        heading.configure(font=('verdana',24,'bold'))

        heading = Label(self.root,text='Sentiment Analysis',bg='#101820',fg='#A3EDE5')
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',24))

        label1 = Label(self.root, text='Enter the paragraph', bg='#101820', fg='white')
        label1.pack(pady=(10,5))

        self.par_input = scrolledtext.ScrolledText(self.root, width=50, height=8, wrap=WORD)
        self.par_input.pack(pady=(5,15))

        sentiment_button = Button(self.root, text='Analyze Sentiment',command=self.analyze_sentiment)
        sentiment_button.pack(pady=(10,10))

        self.sentiment_result = Label(self.root, text='',bg= '#101820',fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana',16))

        goback_button = Button(self.root, text='Go Back',command=self.home_gui)
        goback_button.pack(pady=(10,10))

    def analyze_sentiment(self):

        para = self.par_input.get('1.0',END).strip()

        if not self.API_KEY:
            messagebox.showerror("Error", "Missing NLPCloud API key.")
            return
        
        try:

            client = nlpcloud.Client("distilbert-base-uncased-finetuned-sst-2-english", self.API_KEY)

            response = client.sentiment(para)

            sentiment = response["scored_labels"][0]["label"]
            score = response["scored_labels"][0]["score"]
            
            if sentiment and score:
                self.sentiment_result.config(text=f"Sentiment: {sentiment}\nConfidence: {score:.2f}")
            else:
                self.sentiment_result.config(text="No sentiment found")
        except  Exception as s:
            self.sentiment_result.config(text=f"Error: {s}")

    def heading_gui(self):

        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#101820',fg='#A3EDE5')
        heading.pack(pady=(40,20))
        heading.configure(font=('verdana',24,'bold'))

        heading = Label(self.root,text='Headline Generation',bg='#101820',fg='#A3EDE5')
        heading.pack()
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',24))

        label1 = Label(self.root, text='Enter the paragraph', bg='#101820', fg='white')
        label1.pack(pady=(10,5))

        self.par_input = scrolledtext.ScrolledText(self.root, width=50, height=8, wrap=WORD)
        self.par_input.pack(pady=(5,15))

        headline_button = Button(self.root, text='Analyze Headline',command=self.analyze_headline)
        headline_button.pack(pady=(10,10))

        self.headline_result = Label(self.root, text='',bg= '#101820',fg='white')
        self.headline_result.pack(pady=(10,10))
        self.headline_result.configure(font=('verdana',16))

        goback_button = Button(self.root, text='Go Back',command=self.home_gui)
        goback_button.pack(pady=(10,10))

    def analyze_headline(self):

        para = self.par_input.get('1.0',END).strip()

        if not self.API_KEY:
            messagebox.showerror("Error", "Missing NLPCloud API key.")
            return
        
        try:

            client = nlpcloud.Client("t5-base-en-generate-headline", self.API_KEY, gpu=False)

            response = client.summarization(para)

            headline = response.get("summary_text","").strip()
            
            if headline:
                self.headline_result.config(text=f"Headline for your paragraph:\n{headline}")
            else:
                self.headline_result.config(text="No headline generated")
        except  Exception as s:
            self.headline_result.config(text=f"Error: {s}")

    def grammar_gui(self):

        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#101820',fg='#A3EDE5')
        heading.pack(pady=(40,20))
        heading.configure(font=('verdana',24,'bold'))

        heading = Label(self.root,text='Grammar and Spelling Correction',bg='#101820',fg='#A3EDE5')
        heading.pack()
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',24))

        label1 = Label(self.root, text='Enter the paragraph', bg='#101820', fg='white')
        label1.pack(pady=(10,5))

        self.par_input = scrolledtext.ScrolledText(self.root, width=50, height=8, wrap=WORD)
        self.par_input.pack(pady=(5,15))

        headline_button = Button(self.root, text='Correction',command=self.analyze_correction)
        headline_button.pack(pady=(10,10))

        self.correction_result = scrolledtext.ScrolledText(self.root,width = 60, height = 10, wrap = WORD,bg= '#101820',fg='white')
        self.correction_result.pack(pady=(10,10))
        self.correction_result.configure(font=('verdana',16))
        self.correction_result.config(state=DISABLED)

        goback_button = Button(self.root, text='Go Back',command=self.home_gui)
        goback_button.pack(pady=(10,10))

    def analyze_correction(self):

        para = self.par_input.get('1.0',END).strip()

        if not self.API_KEY:
            messagebox.showerror("Error", "Missing NLPCloud API key.")
            return
        
        try:

            client = nlpcloud.Client("gpt-oss-120b", self.API_KEY, gpu=True)

            response = client.gs_correction(para)
            correction = response.get("correction", "").strip()

            self.correction_result.config(state=NORMAL)
            self.correction_result.delete('1.0',END)

            if correction:
                self.correction_result.insert(END, f"Corrected text:\n\n{correction}")
            else:
                self.correction_result.insert(END, "No text found")

            self.correction_result.config(state=DISABLED)

        except Exception as s:
            self.correction_result.config(state=NORMAL)
            self.correction_result.delete('1.0', END)
            self.correction_result.insert(END, f"Error: {s}")
            self.correction_result.config(state=DISABLED)


    def lang_gui(self):

        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#101820',fg='#A3EDE5')
        heading.pack(pady=(40,20))
        heading.configure(font=('verdana',24,'bold'))

        heading = Label(self.root,text='Language Detection',bg='#101820',fg='#A3EDE5')
        heading.pack()
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',24))

        label1 = Label(self.root, text='Enter the paragraph', bg='#101820', fg='white')
        label1.pack(pady=(10,5))

        self.par_input = scrolledtext.ScrolledText(self.root, width=50, height=8, wrap=WORD)
        self.par_input.pack(pady=(5,15))

        headline_button = Button(self.root, text='Detect Languages',command=self.detect_language)
        headline_button.pack(pady=(10,10))

        self.language_result = Label(self.root, text='',bg= '#101820',fg='white')
        self.language_result.pack(pady=(10,10))
        self.language_result.configure(font=('verdana',16))

        goback_button = Button(self.root, text='Go Back',command=self.home_gui)
        goback_button.pack(pady=(10,10))


    def detect_language(self):

        para = self.par_input.get('1.0',END).strip()

        if not self.API_KEY:
            messagebox.showerror("Error", "Missing NLPCloud API key.")
            return
        
        try:

            client = nlpcloud.Client("python-langdetect", self.API_KEY, gpu=False)

            response = client.langdetection(para)
            print(response)

            detected_language = response.get('languages', [])
            
            if detected_language:
                result_text = "Detected languages:\n"
                for lang in detected_language:
                    code = list(lang.keys())[0].upper()
                    score = list(lang.values())[0]
                    result_text += f"{code} - {score:.2f}\n"
                self.language_result.config(text=result_text)
            else:
                self.language_result.config(text="No languages detected")
        except  Exception as s:
            self.language_result.config(text=f"Error: {s}")


if __name__ == "__main__":

    NLP = NLPApp()
