from flask import Flask,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST','PUT'])

def helloworld():
  return("hello")

if __name__=="__main__":
    app.run()