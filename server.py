from flask import Flask, request
from flask_cors import CORS
from email.message import EmailMessage
import smtplib
from flask import render_template

app = Flask(__name__)
CORS(app)



@app.route('/send', methods=['POST'])
def send_mail():

    permit_no = request.form.get('permitNo','')
    bad = request.form.get('bad','')
    good = request.form.get('good','')
    etc = request.form.get('etc','')

    
    photo = request.files.get('photo')
    msg = EmailMassage()

    if photo and photo.filename != '':
        msg.add_attachment(
            photo.read(),
            maintype='application',
            subtype='octet-stream',
            filename=photo.filename
        )


    msg['Subject'] = 'LG화학 작업허가서 현장 점검'
    msg['From'] = 'lgchem.safety.report@gmail.com'
    msg['To'] = 'mpark10@lgchem.com'

    body = f"""
[LG화학 작업허가서 현장 점검]

■ 작업허가서 번호
{permit_no}

■ 부적합사항
{bad}

■ 우수사항
{good}

■ 기타
{etc}
"""

    msg.set_content(body)

    if photo:
        msg.add_attachment(
            photo.read(),
            maintype='applocation',
            subtype='octet-stream',
            filename=photo.filename
        )

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:

        smtp.starttls()

        smtp.login(
            'lgchem.safety.report@gmail.com',
            'sekj mrij ppxy mbqg'
        )

        smtp.send_message(msg)

    return '메일 전송 완료'

@app.route('/')
def home():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
