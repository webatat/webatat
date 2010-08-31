from django.conf import settings
from django.template import TemplateDoesNotExist

from common.models import Template

def load_template_source(template_name, template_dirs=None):

    display_name = 'db:%s:%s:%s' % ("webatat",
                                    template_name, settings.DOMAIN)

    try:
	key_name = Template.key_from(website=settings.DOMAIN,name=template_name)
	template = Template.get_by_key_name(key_name)

        return (template.content, display_name)
        #return (key_name, template_name)
    except:
        pass
    raise TemplateDoesNotExist(template_name)
load_template_source.is_usable = True


