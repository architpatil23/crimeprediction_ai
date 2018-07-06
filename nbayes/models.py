# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Result(models.Model):
	"""docstring for Result"""
	nbd = models.CharField(max_length=20)
	dist = models.CharField(max_length=20)
	hour = models.IntegerField()
	day = models.CharField(max_length=10)

	def __init__(self, arg):
		super(Result, self).__init__()
		self.arg = arg
		
	def __unicode__(self):
		return "{0} {1} {2} {3} {4}".format(self,self.nbd,self.dist,self.hour,self.day)
