
from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText

def send_email(sender,message,receiver,subject):
    
    try:
        msg = MIMEText(message, 'html')
        msg['Subject']  = subject
        msg['From']=sender
        msg['Reply-to'] = 'no-reply'
        msg['To'] = receiver
        s = smtplib.SMTP('localhost')
        s.sendmail(sender, [receiver], msg.as_string())
        
        s.close()
    except smtplib.SMTPException as smtpEx:
        error_code = 1
        return [error_code, smtpEx.as_text()]
    else:
        error_code = 0
        return [error_code, "success"]
    
def email5(request):
    unknown_error=0
    
    if request.method == 'POST' :
        sender=request.POST['user']
        message=request.POST['content']
        receiver=request.POST['receiver']
        subject=request.POST['subject']
        unknown_error,feed_back_msg =send_email(sender,message,receiver,subject)
        
        if unknown_error==1:
            return render(request, 'email5.html', {'unknown_error': feed_back_msg,})
            
        feedback_sent=1
        return render(request, 'email5.html', {'feedback_sent': feedback_sent,})
    else:
        return render(request, 'email5.html', {})

