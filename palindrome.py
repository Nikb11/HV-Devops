from flask import Flask,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST','PUT'])
num = int(request.args.get('num1'))
temp = num
rev = 0
while (num > 0):
       dig = num % 10
       rev = rev * 10 + dig
       num = num // 10
if (temp == rev):
 
 return "The number is a palindrome!"
else:
 return "The number isn't a palindrome!"
               
