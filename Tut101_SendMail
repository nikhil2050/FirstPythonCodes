import smtplib

# creates SMTP session 
#s = smtplib.SMTP('smtp.gmail.com', 587)
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)

#s.ehlo()

# start TLS for security 
#s.starttls()

#Authentication
#Note : Goto to settings and switch on "Less secure app access"
s.login('nkjava2050@gmail.com','mypassword')

msg = 'Hi. Some msg.'

s.sendmail('nkjava2050@gmail.com','nikhilkshirsagar@mailinator.com',msg)

s.close()
print('Mail sent!')
