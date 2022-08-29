from flask import Flask, render_template, url_for
from flask import request
from flask_mail import Mail, Message



app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'millercm108@gmail.com'
app.config['MAIL_PASSWORD'] = 'aqlnicnoyuuxefdp'
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# mail = Mail()

# mail.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(f"SparkCode Website: Message from {name}", sender=email, recipients=['millercm108@gmail.com'])
        msg.body = message
        mail.send(msg)

        return render_template('contact.html', success=True)

    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)