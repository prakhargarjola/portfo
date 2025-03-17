from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def my_homepage(page_name):
    return render_template(page_name)

def writing_database(data):
    with open('Web_server\database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        comment = data['message']
        database.write(f'\n{email}, {subject}, {comment}')

def writing_csv(data):
    with open('Web_server\database2.csv', mode='a', newline = '') as database2:
        email = data['email']
        subject = data['subject']
        comment = data['message']
        writer = csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email, subject, comment])

@app.route("/submit_form", methods = ['GET', 'POST'])
def submit():
    if request.method == "POST":
        data = request.form.to_dict()
        writing_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'

