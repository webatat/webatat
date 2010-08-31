# -*- coding: utf-8 -*-
import logging
import random

from django.conf import settings
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect

from django_widgets import Widget as  WidgetLoader
from common.models import Widget


class HelloWorld(WidgetLoader):
	def render(self, context, value=None, options=None):
    		return u'Hello world!'

class jquery_featureList(WidgetLoader):
	template = 'featurelist'
	def get_context(self, value=None , options=None):
		global template
		template = 'featurelist'
		featurelist = Widget.get_by_key_name('nawadena.com/featureList/main')
		return {'featurelist':featurelist}
       



class top_scorers(WidgetLoader):
	template = 'widgets/templates/top_scorers.html'
	def get_context(self, value=None , options=None):
		return {}


class menu(WidgetLoader):
	template = 'widgets/templates/nav.html'
	def get_context(self, value=None , options=None):
		return {}
    
