from django.views.generic import TemplateView
from django.conf import settings


### Template View
class CView(TemplateView):
    """ BPMN List View Class """
    TEMPLATE = '_bpmn_list.hbs'
    ## template 
    template_name = TEMPLATE
    ## context
    def get_context_data(self, **kwargs):
        context = super(CView, self).get_context_data(**kwargs)
        dict_cxt = {
            "title": "BPM Modeling and Analysis",
            "APP_NAME": settings.APP_NAME,
        }
        context.update(dict_cxt)
        return context

root = CView.as_view()
