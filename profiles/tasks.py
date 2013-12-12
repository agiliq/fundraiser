from django.core.mail import mail_admins, EmailMultiAlternatives
from django.template.loader import render_to_string

from celery import task


@task()
def sendemail(sub, msg, to, user=None):

    if sub == "reg_sub":
        subject = "Thanks for registering with Pratham Books"
    elif sub == "approve_sub":
        subject = "Campaign creation permission approved"

    if msg == "reg_msg":
        message = render_to_string("email/registration_body.html", {
                                   "username": user.username})
    elif msg == "approve_msg":
        message = render_to_string("email/campaign_approved.html", {
                                   "username": user.username})

    email = EmailMultiAlternatives(subject, "", "", [to])
    email.attach_alternative(message, "text/html")
    email.send()

    if not sub == "approve_sub":
        admin_sub = "New User Registered"
        if user.get_profile().is_beneficiary:
            admin_msg = render_to_string("email/admin_body.html", {
                                         "username": user.username, "ben": True})
        else:
            admin_msg = render_to_string("email/admin_body.html", {
                                         "username": user.username, "donr": True})
        mail_admins(admin_sub, "", html_message=admin_msg)


@task()
def massemail(sub, msg, email_list, user=None):
    if sub == "gmail_invite":
        sub = "Invitation from Pratham Books by {0}".format(user)
    if msg == "gm_invite_msg":
        msg = render_to_string(
            "email/invitation_email.html", {"username": user.username})
    email = EmailMultiAlternatives(sub, "", "", email_list)
    email.attach_alternative(msg, 'text/html')
    email.send()
