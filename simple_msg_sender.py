import smtplib
server = smtplib.SMTP('smtp.gmail.com',587) #if sender account is gmail
server.starttls()
server.login('youremail@gmail.com','yourpassword')
server.sendmail('youremail@gmail.com','reciver@mars.com','hi I am an automatic sender') #note your account should have the permisssion


