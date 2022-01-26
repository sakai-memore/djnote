from django.views.generic import TemplateView

from shared.services import tinydb_serv as serv, config

class CView(TemplateView):
    """ modeler View Class """
    ## template 
    TEMPLATE = '_bpmn_modeler.hbs'
    template_name = TEMPLATE
    ## context
    def get_context_data(self, pk, **kwargs):
        MODULE_NAME = 'BPMN Modeler'
        context = super(CView, self).get_context_data(**kwargs)
        dict_cxt = {
            "title": MODULE_NAME,
            "id": pk,
            "file_name": "sample.bpmn",
        }
        context.update(dict_cxt)
        return context

root = CView.as_view()
