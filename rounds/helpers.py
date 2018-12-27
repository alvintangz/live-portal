import os
import uuid

def submission_upload_to(instance, filename):
	path = "rounds/submissions/"
	file = "%s_%s" % (uuid.uuid4(), filename)
	return os.path.join(path, file)

def rubric_upload_to(instance, filename):
	path = "rounds/rubrics/"
	file = "%s_%s" % (uuid.uuid4(), filename)
	return os.path.join(path, file)