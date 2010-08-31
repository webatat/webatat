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

from common.models import Widget


def front_front(request):

	

  if 'theme' in request.GET and request.GET['theme']:
    theme = request.GET.get('theme')
    settings.DEFAULT_THEME = theme

  mainmenu = Widget.get_by_key_name('nawadena.com/menu/main')
  sectionmenu = Widget.get_by_key_name('nawadena.com/menu/section')
  accordion = Widget.get_by_key_name('nawadena.com/accordion/main')
  featurelist = Widget.get_by_key_name('nawadena.com/featureList/main')
  topscorers = Widget.get_by_key_name('nawadena.com/sport_top_scorers/1')
  standings = Widget.get_by_key_name('nawadena.com/sport_standings/1')
  anythingslider = Widget.get_by_key_name('nawadena.com/anythingslider/main')

  
  q = Widget.all()
  q.filter("wtype" , "article")
  articles = q.fetch(2)

  pageIndex = 0 
  menuItems = mainmenu.content.get('items')
  menuItems[pageIndex]['class'] = 'selected'

  t = loader.get_template('front/templates/base.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));


def front_gallery(request, name):

  mainmenu = Widget.get_by_key_name('nawadena.com/menu/main')
  
  menuItems = mainmenu.content.get('items')
  for item in menuItems:    
    if item['path'] == "/gallery/%(name)s" % {'name':name} :
      item['class'] = 'selected'

  gallery = Widget.get_by_key_name('nawadena.com/gallery/%s' % name)

  t = loader.get_template('front/templates/gallery/base-gallery.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));




def front_article(request, title):

  a= 'nawadena.com/article/%s' % title
  mainmenu = Widget.get_by_key_name('nawadena.com/menu/main')
  article = Widget.get_by_key_name('nawadena.com/article/%s' % title)
  sectionmenu = Widget.get_by_key_name('nawadena.com/menu/section')
  anythingslider = Widget.get_by_key_name('nawadena.com/anythingslider/main')
  q = Widget.all()
  q.filter("wtype" , "article")
  articles = q.fetch(2)

  t = loader.get_template('front/templates/articles/base-article.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));

def front_articles(request):

  accordion = Widget.get_by_key_name('nawadena.com/accordion/main')
  featurelist = Widget.get_by_key_name('nawadena.com/featureList/main')
  topscorers = Widget.get_by_key_name('nawadena.com/sport_top_scorers/1')
  standings = Widget.get_by_key_name('nawadena.com/sport_standings/1')
  mainmenu = Widget.get_by_key_name('nawadena.com/menu/main')  
  sectionmenu = Widget.get_by_key_name('nawadena.com/menu/section')

  q = Widget.all()
  q.filter("wtype" , "article")
  articles = q.fetch(10)

  t = loader.get_template('front/templates/articles/base-articles.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));




def front_sport_champion(request, champion):
  sectionmenu = Widget.get_by_key_name('nawadena.com/menu/section')
  q = Widget.all()
  q.filter("wtype" , "article")
  articles = q.fetch(2)

  champion_key_name = "nawadena.com/champion/%s" % champion	
  mainmenu = Widget.get_by_key_name('nawadena.com/menu/main')
  champion = Widget.get_by_key_name(champion_key_name)

  t = loader.get_template('front/templates/sport/base-champion.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));


def front_sport_champion_match(request, champion, iday, imatch):
  sectionmenu = Widget.get_by_key_name('nawadena.com/menu/section')
  q = Widget.all()
  q.filter("wtype" , "article")
  articles = q.fetch(3)

  champion_key_name = "nawadena.com/champion/%s" % champion	
  mainmenu = Widget.get_by_key_name('nawadena.com/menu/main')
  champion = Widget.get_by_key_name(champion_key_name)
  match = champion.content["days"][int(iday)]["matches"][int(imatch)]
 
  t = loader.get_template('front/templates/sport/base-champion-match.html')
  c = RequestContext(request, locals())
  return HttpResponse(t.render(c));
