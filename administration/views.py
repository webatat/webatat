# -*- coding: utf-8 -*-
# Copyright 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import random

from django.conf import settings
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
try:
  import cPickle as pickle
except ImportError:
  import pickle

from common import exception
import simplejson as json

from google.appengine.ext import db
from google.appengine.api.datastore_types import Blob

from common.api import admin_required

from common.models import Widget
from common.models import FlatPage
from common.models import Template
from common.properties import DictProperty

admin_menu_key_name = Widget.key_from(website='nawadena.com',name='admin', wtype='menu')

def admin_admin(request):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)
  title = ""
  if request.POST:
     wtype = request.POST.get('wtype')
     website = request.POST.get('website')
     name = request.POST.get('name')
     title = request.POST.get('title')
     content = request.POST.get('content')	

     w = Widget(key_name = pk)
     w.title = title
     w.wtype = wtype
     w.content = json.loads(content)
     w.put()

  
 

    
  t = loader.get_template('administration/templates/base-admin.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));


#@admin_required
def admin_add_widget(request):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)
  action = "add"
  if request.POST:   
     title = request.POST.get('title')
     wtype = request.POST.get('wtype')
     website = request.POST.get('website')
     name = request.POST.get('name')
     content = request.POST.get('content')	
     content = content.replace('\r' ,'').replace('\n' ,'')
     key_name = Widget.key_from(website=website,name=name, wtype=wtype)
     w = Widget(key_name = key_name)
     w.title = title
     w.wtype = wtype
     w.website = website
     w.name = name
     w.content = json.loads(content)
     w.put()

    
  t = loader.get_template('administration/templates/form_widget.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));

def admin_update_widgets(request):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)
  widgets = Widget.all()
  action = "update"
    
  t = loader.get_template('administration/templates/form_widget.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));


def admin_update_widget(request, website, wtype, name):

  mainmenu = Widget.get_by_key_name(admin_menu_key_name)
  widgets = Widget.all()

  action = "update"
  pk = '%(website)s/%(wtype)s/%(name)s' % {'website' : website, 'wtype' : wtype, 'name' : name}
  w = Widget.get_by_key_name(pk)
  title = w.title
  wtype = w.wtype
  content = json.dumps(w.content, ensure_ascii=False)
  

  if request.POST:
     
     title = request.POST.get('title')
     content = request.POST.get('content')
     content = content.replace('\r' ,'').replace('\n' ,'')
    
     w.title = title
     w.content = json.loads(content)
     w.put()
    
  t = loader.get_template('administration/templates/form_widget.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));

def admin_delete_widget(request, website, wtype, name):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)
  pk = '%(website)s/%(wtype)s/%(name)s' % {'website' : website, 'wtype' : wtype, 'name' : name}
  if request.POST:
    try:
      w = Widget.get_by_key_name(pk)
      w.delete()
    except exception.NoWidgetToDelete:
      return None

    except AttributeError:
      return HttpResponseRedirect("/_admin/update/widget/")
    return HttpResponseRedirect("/_admin/update/widget/")

  t = loader.get_template('administration/templates/form_widget_delete.html')
  c = RequestContext(request, locals())
  return HttpResponse(t.render(c));

def admin_add_flatpage(request):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)

  action = "add"

  if request.POST:   
     name = request.POST.get('name')
     title = request.POST.get('title')
     website = request.POST.get('website')
     status = request.POST.get('status')
     content = request.POST.get('content')	

     key_name = FlatPage.key_from(website=website,name=name)
     flatpage = FlatPage(key_name = key_name)
     flatpage.title = title
     flatpage.name = name
     flatpage.website = website
     flatpage.status = int(status)
     flatpage.content = json.loads(content)
     flatpage.put()
    
  t = loader.get_template('administration/templates/form_flatpage.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));

def admin_update_flatpages(request):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)
  flatpages = FlatPage.all()
  action = "update"
    
  t = loader.get_template('administration/templates/form_flatpage.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));


def admin_update_flatpage(request, website, name):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)
  flatpages = FlatPage.all()
  action = "update"
  pk = FlatPage.key_from(website=website,name=name)
  f = FlatPage.get_by_key_name(pk)
  name = f.name
  title = f.title
  website = f.website
  status = f.status
  content = json.dumps(f.content, ensure_ascii=False)
  

  if request.POST:     
     
     title = request.POST.get('title')
     status = request.POST.get('status')
     content = request.POST.get('content')
     content = content.replace('\r' ,'').replace('\n' ,'')
    
     f.title = title
     f.status = int(status)
     f.content = json.loads(content)
     f.put()
    
  t = loader.get_template('administration/templates/form_flatpage.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));



def admin_delete_flatpage(request, website, name):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)
  pk = FlatPage.key_from(website=website,name=name)
  if request.POST:
    try:
      f = FlatPage.get_by_key_name(pk)
      f.delete()
    except exception.NoWidgetToDelete:
      return None

    except AttributeError:
      return HttpResponseRedirect("/_admin/update/flatpage/")
    return HttpResponseRedirect("/_admin/update/flatpage/")

  t = loader.get_template('administration/templates/form_flatpage_delete.html')
  c = RequestContext(request, locals())
  return HttpResponse(t.render(c));










def admin_add_template(request):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)

  action = "add"

  if request.POST:   
     name = request.POST.get('name')
     website = request.POST.get('website')
     content = request.POST.get('content')	

     key_name = Template.key_from(website=website,name=name)
     template = Template(key_name = key_name)
     template.name = name
     template.website = website
     template.content = content
     template.put()
    
  t = loader.get_template('administration/templates/form_template.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));

def admin_update_templates(request):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)
  templates = Template.all()
  action = "update"
    
  t = loader.get_template('administration/templates/form_template.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));


def admin_update_template(request, website, name):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)
  templates = Template.all()
  action = "update"
  pk = Template.key_from(website=website,name=name)
  t = Template.get_by_key_name(pk)
  name = t.name
  website = t.website
  content = t.content
  

  if request.POST:     
     
     content = request.POST.get('content')
     #content = content.replace('\r' ,'').replace('\n' ,'')
    
     t.content = content
     t.put()
    
  t = loader.get_template('administration/templates/form_template.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));



def admin_delete_template(request, website, name):
  mainmenu = Widget.get_by_key_name(admin_menu_key_name)
  pk = Template.key_from(website=website,name=name)
  if request.POST:	
    try:
      t = Template.get_by_key_name(pk)
      t.delete()
    except exception.NoWidgetToDelete:
      return None

    except AttributeError:
      return HttpResponseRedirect("/_admin/update/template/")
    return HttpResponseRedirect("/_admin/update/template/")

  t = loader.get_template('administration/templates/form_template_delete.html')
  c = RequestContext(request, locals())
  return HttpResponse(t.render(c));




