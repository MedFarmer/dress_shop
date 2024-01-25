from django.dispatch import Signal
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string

purchase_signal = Signal()

@receiver(purchase_signal)
def purchase_handler(sender, user, context, **kwargs):
    # Customize the email subject and message
    
    context['first_name'] = user.first_name
    html_message = render_to_string('purchase_email.html', context)
    
    subject = "Purchase Confirmation"
        
    from_email = 'medet20231020@gmail.com'
    recipient_list = [user.email]

    # Send the email
    send_mail(subject, 'You purchased from onlin shop', from_email, recipient_list, html_message=html_message)
