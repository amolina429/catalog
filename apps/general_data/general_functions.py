import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from decouple import config
from email.mime.application import MIMEApplication
from pandas import ExcelWriter
import pandas as pd
from datetime import datetime

def send_mail(subject,to_email,html):
    from_email = config('EMAIL_USER')
    to_email = ['andresg.molina429@gmail.com', 'andresm@stc-sas.com']
    password = config('EMAIL_PASSWORD')
    smtp_server = config('EMAIL_SMTP')
    smtp_port = config('EMAIL_PORT')

    msgRoot = MIMEMultipart('related')
    # setup the parameters of the message
    msgRoot['From'] = from_email
    msgRoot['To'] = ", ".join(to_email)
    # msgRoot['Cc'] = ", ".join(destinatarios)
    msgRoot['Subject'] = subject

    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)
    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText(html, 'html')

    msgAlternative.attach(msgText)

    # create server
    mail = '%s: %s' % (smtp_server, smtp_port)
    server = smtplib.SMTP_SSL(mail)

    # server.starttls()

    # Login Credentials for sending the mail
    server.login(msgRoot['From'], password)
    # Validacion de envio de copias
    sendto = [msgRoot['To']]
    # sendto.extend(destinatarios)

    # send the message via the server.
    server.sendmail(msgRoot['From'], sendto, msgRoot.as_string())
    server.quit()


    print('Correo enviado exitosamente.')

def html_body(html):
    html_body = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Actualización de Producto</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
                text-align: center;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                background-color: #f9f9f9;
                padding: 20px;
                border-radius: 10px;
            }
            .header {
                background-color: #4CAF50;
                color: #ffffff;
                padding: 10px 0;
                border-radius: 10px 10px 0 0;
            }
            .content {
                margin-top: 20px;
            }
            .button {
                display: inline-block;
                padding: 10px 20px;
                font-size: 16px;
                text-align: center;
                text-decoration: none;
                background-color: #4CAF50;
                color: #ffffff;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="container">
           %s
        </div>
    </body>
    </html>
    '''%(html)
    return html_body

def formatear_fecha(date):
    date = datetime.strftime(date,'%Y-%m-%d %H:%M:%S')
    return date

def generate_excel(data,path_excel):
    writer = ExcelWriter(path_excel, engine='xlsxwriter')
    df = pd.DataFrame(data)
    print(df)
    df['query_date'] = df['query_date'].apply(formatear_fecha)
    df.to_excel(writer, 'Sheet1', index=False, startrow=1)
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']
    merge_format = workbook.add_format({
    'bold': 2,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#01a9d2'})

    # format1 = workbook.add_format({'num_format': '$#,##0'})
    worksheet.set_column('A:Z', 18)
    #alphabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG']
    # lettere = alphabeto[len_columns - 1]

    cell_format = workbook.add_format({'bold': True, 'bg_color': '#01a9d2'})
    # encabezados = ['CONCEPTO','R','CANTIDAD GALONES GRAVADOS','TARIFA','% ALCOHOL CARBURANTE','BASE GRAVABLE','SOBRETASA','AJUSTE DB','AJUSTE CR','DECLARACIONES']
    # worksheet.merge_range('A1:%s1'%(lettere),'Excel: %s'%(name), merge_format)
    # # worksheet.set_column('C:J', 18, format1)
    # pos = 0
    # for tit in encabezados:
    #     worksheet.write(1, pos, tit, cell_format)
    #     pos += 1
    writer.close()
    return {
            'excel': path_excel
        }

