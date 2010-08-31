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
from common.models import Widget


def test_test(request):

  
  mainmenu = Widget.get_by_key_name('nawadena.com/menu/main')
  
  goalkeepers = []
  defenders = []
  midfielders = []
  forwards = []
  team = Widget.get_by_key_name('nawadena.com/team/team1')
  
  for player in team.content["players"]:
    if  player["role"] == "Goalkeeper" :
      goalkeepers.append(player)
    if  player["role"] == "Defender" :
      defenders.append(player)
    if  player["role"] == "Midfielder" :
      midfielders.append(player)
    if  player["role"] == "Forward" :
      forwards.append(player)
      
 

  #t = loader.get_template('template1')
  t = loader.get_template('test/templates/base.html')
  c = RequestContext(request, locals())

  return HttpResponse(t.render(c));
