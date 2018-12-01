# IMPORTANT VARIABLES - DO NOT SHARE

urls = {
	"portal": "https://portal.live-competition.org",
}

encoded_urls = {
	"alphabet": 'abcdefghijklmnopqrstuvwxyz1234567890',
	"salt": 'sprinkle some salt',
	"min_length": 8,
}

email = {
	"backend": 'django.core.mail.backends.smtp.EmailBackend',
	#"backend": 'django.core.mail.backends.console.EmailBackend',
	"host": 'smtp.sendgrid.net',
	"port": 587,
	"tls": True,
	"user": 'apikey',
	"password": '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',
	"from": 'contact@live-competition.org',
	"from_more": 'LIVE Competition <contact@live-competition.org>',
}

twilio = {
	"sid": 'AC1f3ababace34b895c68707c32ac74315',
	"token": '714e479cde7ff140367e7a857082845b',
	"number": '+16479515718',
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
			"remember. As well, you can now view the rounds, especially the " +
			"preliminary round. Good luck."),
		"html": ("<p>Hello <strong>%s</strong>,</p><p>Your LIVE Portal account "
			+ " is now activated. You can access the portal at " + 
			urls["portal"] + ". It is recommended that you update your " +
			"password to one that you can remember. As well, you can now view " +
			"the rounds, especially the preliminary round. Good luck.</p>")
	},
	"delegate_creation": {
		"plain": ("Hello %s. First off, we would like to welcome you to an " + 
			"exclusive platform which showcases elite talent amongst " +
			"partners and delegates. Now, it’s time to start competing! We " +
			"have posted the preliminary round on the LIVE Competition " +
			"Portal, powered by Microsoft Azure, which will be your online " +
			"gateway to view and submit rounds, as well as access tools that " +
			"may be useful for you. To access the portal, please active your " +
			"account, and complete your profile at %s, with the username %s " +
			"and password %s"),
		"html": ("<p>Hello <strong>%s</strong>,</p><p>First off, we would " + 
			"like to welcome you to an exclusive platform which showcases " +
			"elite talent amongst partners and delegates.</p><p>Now, it’s " +
			"time to start competing! We have posted the <strong>preliminary " +
			"round</strong> on the LIVE Competition Portal, powered by " +
			"Microsoft Azure, which will be your online gateway to view and " +
			"submit rounds, as well as access tools that may be useful for " +
			"you.</p><p>To access the portal, please active your account, and " +
			"complete your profile at <a href='%s'>%s</a>, with the username " +
			"<strong>%s</strong> and password <strong>%s</strong>."),
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