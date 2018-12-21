# django modules
from django.core.mail import EmailMultiAlternatives
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from portal.custom_azure import AzureMediaStorage
from django.core.files import File
from django.conf import settings
# helpers
from hashids import Hashids
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from PIL import Image
import io
import os
from azure.storage.blob.blockblobservice import BlockBlobService
# constants
import portal.variables as imp

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

def resize_and_convert(image, width=500, height=500, container="media"):
	if settings.DEBUG:
		img = Image.open(image)
		img = img.resize((width, height), Image.ANTIALIAS)
		img = img.convert("RGB")
		img.save(image, format="JPEG")
	else:
		temp = io.BytesIO()
		img = Image.open(image)
		img = img.resize((width, height), Image.ANTIALIAS)
		img = img.convert("RGB")
		img.save(temp, format="JPEG")
		bbs = BlockBlobService(account_name='liveportal2019', 
			account_key=os.environ.get('LP_AZURE_STORAGE_KEY', ''))
		bbs.create_blob_from_bytes(
			container, 
			image.name,
			temp.getvalue())
	
def send_sms(to, body):
	account_sid = imp.twilio["sid"]
	auth_token  = imp.twilio["token"]
	client = Client(account_sid, auth_token)
	try:
		message = client.messages.create(
			to=to,
			from_=imp.twilio["number"],
			body=body)
	except TwilioRestException:
		pass

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