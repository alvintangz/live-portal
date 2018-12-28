import os
import uuid

def round_details_upload_to(instance, filename):
	path = "rounds/details/"
	return os.path.join(path, filename)

def submission_upload_to(instance, filename):
	path = "rounds/submissions/"
	file = "%s_%s" % (uuid.uuid4(), filename)
	return os.path.join(path, file)

def rubric_upload_to(instance, filename):
	path = "rounds/rubrics/"
	return os.path.join(path, filename)

def video_upload_to(instance, filename):
	path = "rounds/videos/"
	file = "%s_%s" % (uuid.uuid4(), filename)
	return os.path.join(path, file)

def video_thumbnail_upload_to(instance, filename):
	path = "rounds/videos/thumbnails/"
	file = "%s_%s" % (uuid.uuid4(), filename)
	return os.path.join(path, file)