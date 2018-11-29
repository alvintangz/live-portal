from django.core.mail import EmailMultiAlternatives
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from hashids import Hashids
import portal.variables as imp
from twilio.rest import Client
from PIL import Image

def hashid_encode(value, salt=imp.encoded_urls["salt"], min_length=imp.encoded_urls["min_length"]):
	hashids = Hashids(alphabet=imp.encoded_urls["alphabet"],
		salt=salt,
		min_length=min_length)
	return hashids.encode(value)

def hashid_decode(value, salt=imp.encoded_urls["salt"], min_length=imp.encoded_urls["min_length"]):
	hashids = Hashids(alphabet=imp.encoded_urls["alphabet"],
		salt=salt,
		min_length=min_length)
	if len(hashids.decode(value)) == 0:
		return None
	else:
		return hashids.decode(value)[0]

def resize_and_convert(image, width=500, height=500):
	image = Image.open(image)
	image = image.resize((width, height), Image.ANTIALIAS)
	# Convert to RGB with no transparency
	image = image.convert("RGB")
	return image

def send_sms(to, body):
	account_sid = imp.twilio["sid"]
	auth_token  = imp.twilio["token"]
	client = Client(account_sid, auth_token)
	message = client.messages.create(
		to=to,
		from_=imp.twilio["number"],
		body=body)

def default_strftime(datetime):
	return datetime.strftime("%I:%M %p on %A, %B %d, %Y")

def default_shortstrftime(datetime):
	return datetime.strftime("%I:%M %p on %b %d, %Y")

def send_email(subject, message, receiver, html_message=None, sender=imp.email["from_more"]):
	if html_message is None:
		html_message = message
	plain_context = {'message': message, 'sent_by': "The LIVE Team"}
	html_context = {'message': mark_safe(html_message), 'sent_by': "The LIVE Team"}
	plain_text = get_template('email/email.txt').render(plain_context)
	html = get_template('email/email.html').render(html_context)
	msg = EmailMultiAlternatives(subject, plain_text, sender, [receiver])
	msg.attach_alternative(html, "text/html")
	msg.send()