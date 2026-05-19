@app.route('/send', methods=['POST'])
def send_mail():

    permit_no = request.form.get('permitNo', '')
    bad = request.form.get('bad', '')
    good = request.form.get('good', '')
    etc = request.form.get('etc', '')

    photo = request.files.get('photo')

    # ✅ 1. 먼저 msg 생성
    msg = EmailMessage()

    msg['Subject'] = 'LG화학 작업허가서 현장 점검'
    msg['From'] = '본인gmail@gmail.com'
    msg['To'] = '본인회사메일@회사.com'

    # ✅ 2. 본문
    body = f"""
[LG화학 작업허가서 현장 점검]

허가서번호: {permit_no}

부적합사항:
{bad}

우수사항:
{good}

기타:
{etc}
"""

    msg.set_content(body)

    # ✅ 3. 사진 첨부
    if photo and photo.filename != '':
        msg.add_attachment(
            photo.read(),
            maintype='application',
            subtype='octet-stream',
            filename=photo.filename
        )

    # ✅ 4. 메일 전송
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(
            '본인gmail@gmail.com',
            '앱비밀번호'
        )
        smtp.send_message(msg)

    return '메일 전송 완료'
