import os
import speech_recognition as sr
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "C:/Users/rushil thareja/Desktop/website"
ALLOWED_EXTENSIONS = set(['txt', 'wav'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    



@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file=request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        j=file.filename
        text=''
        if j.find(".wav")!=-1:
            r = sr.Recognizer()
            audio = j
            with sr.AudioFile(audio) as source:
                audio= r.record(source)
            try:
                text =r.recognize_google(audio)
            except Exception as e:
                print (e)
            contents = text

            s=""
            for i in contents:
                    if i==" ":
                            break
                    else:
                            s=s+i 			#s=1st word of the file


            a=3
            b=5
            n=8+len(s)//2					 #number of terms needed

            interpasswd="" 					 #interpasswd is the intermediate password string
            while(n-2):
                c=a+b
                a=b
                b=c
                interpasswd=interpasswd+contents[c]
                n=n-1

            finalpasswd=""				#finalpasswd is the final password made
            for i in interpasswd:
                    if ord(i)==32:
                            finalpasswd=finalpasswd+"$0"
                    elif i.upper:
                            finalpasswd=finalpasswd+chr(ord(i)-10)
                    elif i.lower:
                            finalpasswd=finalpasswd+chr(ord(i)+7)
                    else:
                            finalpasswd=finalpasswd+i

            #print(interpasswd)
            return render_template("password.html",name=finalpasswd)
        else:
            file1 = open(j,"r")
            contents = file1.read()

            s=""
            for i in contents:
                    if i==" ":
                            break
                    else:
                            s=s+i 			#s=1st word of the file


            a=3
            b=5
            n=8+len(s)//2					 #number of terms needed

            interpasswd="" 					 #interpasswd is the intermediate password string
            while(n-2):
                c=a+b
                a=b
                b=c
                interpasswd=interpasswd+contents[c]
                n=n-1

            finalpasswd=""				#finalpasswd is the final password made
            for i in interpasswd:
                    if ord(i)==32:
                            finalpasswd=finalpasswd+"$0"
                    elif i.upper:
                            finalpasswd=finalpasswd+chr(ord(i)-10)
                    elif i.lower:
                            finalpasswd=finalpasswd+chr(ord(i)+7)
                    else:
                            finalpasswd=finalpasswd+i

            #print(interpasswd)
            return render_template("password.html",name=finalpasswd)


            #print(interpasswd)


                        #print(interpasswd)




if __name__=='__main__':
    app.run(debug=True)
