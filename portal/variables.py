import os

urls = {
	"portal": "https://portal.live-competition.org",
}

encoded_urls = {
	"alphabet": 'abcdefghijklmnopqrstuvwxyz1234567890',
	"salt": 'sprinkle some salt',
	"min_length": 8,
}

email = {
	#"backend": 'django.core.mail.backends.smtp.EmailBackend',
	"backend": 'django.core.mail.backends.console.EmailBackend',
	"host": os.environ.get('LP_EMAIL_HOST', ''),
	"port": os.environ.get('LP_EMAIL_PORT', ''),
	"tls": True,
	"user": 'apikey',
	"password": os.environ.get('LP_EMAIL_PASSWORD', ''),
	"from": 'contact@live-competition.org',
	"from_more": 'LIVE Competition <contact@live-competition.org>',
}

twilio = {
	"sid": os.environ.get('LP_TWILIO_SID', ''),
	"token": os.environ.get('LP_TWILIO_TOKEN', ''),
	"number": os.environ.get('LP_TWILIO_NUMBER', ''),
}

sms_messages = {
	"added_number": ("Hey %s. Your phone number was just added to your " + 
		"LIVE Portal account. We will send any urgent messages to you via " +
		"SMS. To disable this, you can remove your phone number from your " +
		"account under 'Edit Profile' on Portal, or email us at " +
		"contact@live-competition.org."),
	"delegate_activation": ("Your LIVE Portal account is now activated. " +
		"You can access the portal at " + urls["portal"] + ". It is recommended " +
		"that you update your password to one that you can remember."),
}

email_messages = {
	"delegate_activation": {
		"plain": ("Hello %s. Your LIVE Portal account is now activated. " +
			"You can access the portal at " + urls["portal"] + ". It is " +
			"recommended that you update your password to one that you can " +
			"remember. As well, you can now upload you and your team's solution" +
			" to the prelimenary round. Good luck."),
		"html": ("<p>Hello <strong>%s</strong>,</p><p>Your LIVE Portal account "
			+ " is now activated. You can access the portal at " + 
			urls["portal"] + ". It is recommended that you update your " +
			"password to one that you can remember. As well, you can now upload " +
			"you and your team's solution to the prelimenary round. Good luck.</p>")
	},
	"delegate_creation": {
		"plain": ("Hello %s. LIVE Competition Portal, powered by Microsoft " +
			"Azure, is your online gateway to view and submit rounds, as well " +
			"as access tools that may be useful for you. To access Portal, "
			+ "please active your account, and complete your profile at %s, " +
			"with the username %s and password %s. Afterwards, please view " +
			"the preliminary round and submit your team's solution on portal."),
		"html": ("<p>Hello <strong>%s</strong>,</p><p>LIVE Competition Portal, "+
			"powered by Microsoft Azure, is your online gateway to view and " +
			"submit rounds, as well as access tools that may be useful for " +
			"you.</p><p>To access Portal, please active your account, and " +
			"complete your profile at <a href='%s'>%s</a>, with the username " +
			"<strong>%s</strong> and password <strong>%s</strong>.</p>" +
			"<p>Afterwards, please view the preliminary round and submit your " +
			"team's solution on Portal."),
	},
}

user_activation_urls = {
	"alphabet": 'abcdefghijklmnopqrstuvwxyz1234567890',
	"salt": 'bamblakat ayeee',
	"min_length": 12,
}

django_messages = {
	"not_activated": ("Your account exists, but has was not activated. " +
		"Please activate your account first, before logging in."),
	"restricted": ("You are entering a restricted part of the portal which is "
		+ "only meant for another type of user to see."),
}