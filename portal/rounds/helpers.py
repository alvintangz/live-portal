import os
import uuid

def submission_upload_to(instance, filename):
	path = "rounds/submissions/"
	file = "%s_%s" % (uuid.uuid1(), filename)
	return os.path.join(path, file)

# from portal.functions import hashid_encode
# import os

# def submission_upload_to(instance, filename):
# 	path = "rounds/submissions/"
# 	file = "%s_%s_%s_%s_%s" % (instance.pk,
# 		hashid_encode(instance.pk, salt="submissions"),
# 		instance.asc_team.asc_round.number,
# 		instance.asc_team.number,
# 		filename)
# 	return os.path.join(path, file)