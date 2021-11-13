import smtplib
from email.message import EmailMessage

def send_email(user, password, title, destination, message):    
    try:
        msg = EmailMessage()
        msg['Subject'] = title #Titulo do email
        msg['From'] = user #Email de quem envia
        msg['To'] = destination #Email do destinatário
        msg.set_content(message) #Corpo do email

        #Envio do email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # 465 é porta do gmail
            smtp.login(user, password)
            smtp.send_message(msg)
    except:
        print('não foi possivel enviar email')
    else:
        print('email enviado com sucesso')
