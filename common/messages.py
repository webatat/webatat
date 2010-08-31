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

"""User-visible strings for confirmation and flash messages.
"""
from django.utils.encoding import smart_str, smart_unicode

from django.utils.translation import ugettext as _
__author__ = 'mikie@google.com (Mika Raento)'

# api call -> (confirmation message, flash message)
# If the confirmation message is None, no confirmation is required.
_message_table__ = {
  'activation_activate_mobile':
      (None,
       _('Mobile activated.')),
  'activation_request_email':
      (None,
       _('Email confirmation has been sent.')),
  'activation_request_mobile':
      (None,
       _('Mobile activation code has been sent.')),
  'actor_add_contact':
      (None,
       _('Contact added.')),
  'actor_remove' :
      (None,
       _('Deleted')),
  'actor_remove_contact':
      (None,
       _('Contact removed.')),
  'channel_create':
      (None,
       _('Channel created')),
  'channel_join':
      (None,
       _('You have joined the channel.')),
  'channel_update':
      (None,
       _('Channel settings updated.')),
  'channel_part':
      (None,
       _('You have left the channel.')),
  'channel_post':
      (None,
       _('Message posted.')),
  'entry_add_comment':
      (None,
       _('Comment added.')),
  'entry_mark_as_spam':
      ('Mark this item as spam',
       _('Marked as spam.')),
  'entry_remove' :
      ('Delete this post',
       _('Post deleted.')),
  'entry_remove_comment':
      ('Delete this comment',
       _('Comment deleted.')),
  'invite_accept':
      (None,
       _('Invitation accepted')),
  'invite_reject':
      (None,
       _('Invitation rejected')),
  'invite_request_email':
      (None,
       _('Invitation sent')),
  'login_forgot':
      (None,
       _('New Password Emailed')),
  'oauth_consumer_delete':
      ('Delete this key',
       _('API Key deleted')),
  'oauth_consumer_update':
      (None,
       _('API Key information updated')),
  'oauth_generate_consumer':
      (None,
       _('New API key generated')),
  'oauth_revoke_access_token':
      (None,
       _('API token revoked.')),
  'presence_set':
      (None,
       _('Location updated')),
  'post':
      (None,
       _('Message posted.')),
  'settings_change_notify':
      (None,
       _('Settings updated.')),
  'settings_change_privacy':
      (None,
       _('privacy updated')),
  'settings_hide_comments':
      (None,
       _('Comments preferenced stored.')),
  'settings_update_account':
      (None,
       _('profile updated')),
  'subscription_remove':
      (None,
       _('Unsubscribed.')),
  'subscription_request':
      (None,
       _('Subscription requested.')),
}

def confirmation(api_call):
  msg = title(api_call)
  if msg is None:
    return None
  return ('Are you sure you want to ' +
          msg +
          '?')

def title(api_call):
  if _message_table__.has_key(api_call):	
    return _message_table__[api_call][0]
    
  return None

def flash(api_call):
  return smart_str(_message_table__[api_call][1])
