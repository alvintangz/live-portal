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
	#"backend": 'django.core.mail.backends.smtp.EmailBackend',
	"backend": 'django.core.mail.backends.console.EmailBackend',
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

user_activation_urls = {
	"alphabet": 'abcdefghijklmnopqrstuvwxyz1234567890',
	"salt": 'bamblakat ayeee',
	"min_length": 12,
}