import re


# {"useremail": "vsingh1918@gmail.com", "password": "vsingh1990"}


class Validators(object):
	"""
	validators for forms and other input fields
	"""

	email_regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'

	@classmethod
	def email_validator(cls,input_val):
		valid_email =  re.match(cls.email_regex, input_val)

		return valid_email

	@classmethod
	def mandatory_validation(cls,fields,data):
		missing_fields = []
		for field in fields:
			if not data.get(field):
				missing_fields.append(field)

		return missing_fields 



