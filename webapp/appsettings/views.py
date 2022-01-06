from django.views.generic import TemplateView
from shared.services import uuid4_serv

class CView(TemplateView):
    """ settings View Class """
    ## template 
    TEMPLATE = '_appsettings.hbs'
    template_name = TEMPLATE
    ## context
    def get_context_data(self, **kwargs):
        context = super(CView, self).get_context_data(**kwargs)
        ## get data with service
        uuid_str = uuid4_serv.service()
        dict_cxt = {
            "title": "BPMN Application Settings",
            "SESSUUID": uuid_str,
        }
        context.update(dict_cxt)
        return context

## root function 
root = CView.as_view()
