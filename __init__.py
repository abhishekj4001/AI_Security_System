#!/usr/bin/env python
from flask import Flask, render_template, Response, request, redirect, url_for 
import cv2
import sys
import numpy
import numpy as np
import time
import subprocess
from facerecognize import *
import time



app = Flask(__name__)

class Frame:

    def __init__(self,cam1):
        self.cam1 = cam1
    
    @app.route('/')
    def index():
        return render_template('login.html')

    @app.route('/login/', methods=["GET","POST"])
    def login_page():
        error=""
        try:
            if request.method == "POST":
                attempted_username = request.form['username']
                attempted_password = request.form['password']
                if attempted_username == "admin" and attempted_password == "redhat":
                    return render_template('index.html')
                                                                            
                else:
                    error = "Invalid Credentials. Try Again."
            return render_template("login.html", error=error)
        except Exception as e:
            return render_template("login.html", error=error)
    
    @app.route('/register')
    def gen():
        i=1
        while i<10:
            yield (b'--frame\r\n'
                b'Content-Type: text/plain\r\n\r\n'+str(i)+b'\r\n')
        i+=1

    def get_frame(self):
        camera_port=0
        ramp_frames=100
        falg = 0
        camera = cv2.VideoCapture(camera_port) #this makes a web cam object
        while True:
            retval, im = camera.read()
            self.cam1 = im
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            imgencode=cv2.imencode('.jpg',im)[1]
            stringData=imgencode.tostring()
            yield (b'--frame\r\n'
                    b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')    
        camera.release()
        cv2.destroyAllWindows()
    
    def frame(self,name):
            flag = 0
            while flag<=1:
                im  = self.cam1 
                face_recon(im,name)
                flag+=1
                
    
    def identify(self):
        im = self.cam1
        results=face_identify(im)
        print(results)
        if results=="Access Granted":
            return "Grant Access"
        else:
            return "Access Denied"

         
get1=Frame("data")


@app.route('/make/', methods=["GET","POST"])
def make():

    if request.method=="POST":
        name = request.form['data']
        report = "Visitor Added"
        get1.frame(name)
    return render_template('login.html', report=report)


@app.route('/calc')
def calc():
    
    return Response(get1.get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/identify')
def identifier():
    report = get1.identify()
    return render_template('login.html', report=report)
    


if __name__ == '__main__':
    app.run(host="192.168.1.228",debug=True, threaded=True)
