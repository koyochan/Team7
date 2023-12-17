from Body_make import create_calendar_url, date_format, process_data
import smtplib
from email.mime.text import MIMEText
from Body_make import modify_calendar_url

def send_mail(slots, scales, me):
    to_email = me['email']
    print(to_email)
    GMAIL_ADDRESS = 'kkobayashi12356@gmail.com'   # Gmailアドレス 
    APP_PASSWORD = 'musl szie muey zien'  # アプリパスワード

    for scale in scales:
        if 'begin_at' in scale:
            year, month, day, hour, minute = date_format(scale['begin_at'])
            modified_url = create_calendar_url(project_name, year, month, day, hour, minute)
            print("Modified URL:", modified_url)

            TO_MAIL = 'kkobayashi12356@gmail.com' # 送信先メールアドレス（ここも書き換え必須）
            MAIL_TITLE = 'メールタイトル'
            MAIL_BODY =  f'''メール本文（１行目）{modified_url}
            メール本文の続き...'''

            # メールの設定処理
            msg = MIMEText(MAIL_BODY)    # メール本文（日本語が含まれるときは MIMEText必須）
            msg['Subject'] = MAIL_TITLE  # メールタイトル
            msg['From'] = GMAIL_ADDRESS  # 送信元メールアドレス
            msg['To'] = TO_MAIL          # 送信先メールアドレス

            # メールの送信処理
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login(GMAIL_ADDRESS, APP_PASSWORD)
            smtp.send_message(msg)
            smtp.close()
        if 
