import os
import uuid

def resume_upload_to(instance, filename):
	path = "users/delegate/profile/resume/"
	file = "%s_%s" % (uuid.uuid1(), filename)
	return os.path.join(path, file)

def profile_picture_upload_to(instance, filename):
	path = "users/delegate/profile/picture/"
	file = "%s_%s" % (uuid.uuid1(), filename)
	return os.path.join(path, file)