from django.db import models

class Ipaddress ( models.Model):

	status_list = (
		('in_use', 'in use'),
		('available', 'available'),
		('not_available', 'not available')
	)
	ipaddress = models.GenericIPAddressField(verbose_name='IP address', unique=True)
	status = models.CharField(verbose_name='Status', choices=status_list, max_length=16)
	description = models.CharField(verbose_name='Discription', blank = True, max_length=255)

	def __str__(self):
		return self.ipaddress
