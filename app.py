from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='YOUR-EMAIL@gmail.com',
    MAIL_PASSWORD='PASSWORD'
)
mail = Mail(app)


@app.route('/')
def index():
    try:
        return render_template("index.html")
    except Exception as e:
        return(str(e))


@app.route('/send-mail', methods=['POST'])
def send_mail():
    try:
        msg = Message("[USER RESPONSE] Medicare - Get in touch",
                      sender=request.form['email'],
                      recipients=["YOUR-EMAIL@gmail.com"])
        msg.body = "name : {} \nemail : {} \nmessage: {}".format(request.form['name'], request.form['email'], request.form['message'])
        mail.send(msg)
        return redirect("/")
    except Exception as e:
        return(str(e))


if __name__ == '__main__':
    app.run()
