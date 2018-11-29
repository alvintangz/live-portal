from portal.functions import hashid_encode
import os

def resume_upload_to(instance, filename):
	path = "users/delegate/profile/resume/"
	file = "%s_%s_%s" % (instance.pk, hashid_encode(
		str(instance.pk), salt="resume_upload_to"), filename)
	return os.path.join(path, file)

def profile_picture_upload_to(instance, filename):
	path = "users/delegate/profile/picture/"
	file = "%s_%s_%s" % (instance.pk, hashid_encode(
		str(instance.pk), salt="profile_picture_upload_to"), filename)
	return os.path.join(path, file)