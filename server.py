from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('./index.html' )



@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        firstname = data['firstname']
        email = data['email']
        number = data['number']
        message = data['message']
        file = database.write(f'\n{firstname} | {email} | {number} | {message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        firstname = data["firstname"]
        email = data["email"]
        number = data["number"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([firstname,email,number,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =="POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Try Again!!"