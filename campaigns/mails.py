from django.core.mail import mail_admins, EmailMultiAlternatives
from django.template.loader import render_to_string

def SendEmail(sub, msg, to, user):
	admin_sub = "New User Registered"
	
	if user.profile.is_beneficiary:
		admin_msg = render_to_string("email/admin_body.html", {"username":user.username, "ben":"Beneficiary"})
	else:
		admin_msg = render_to_string("email/admin_body.html", {"don":"Donor"})

	if sub == "reg_sub":
		subject = "Thanks for registering with Pratham Books"

	if msg == "reg_msg":
		message = render_to_string("email/registration_body.html", {"username":user.username})

	email = EmailMultiAlternatives(subject, "", "", ["shiva@agiliq.com"])
	email.attach_alternative(message, "text/html")
	email.send()
	mail_admins(admin_sub, "", html_message=admin_msg)