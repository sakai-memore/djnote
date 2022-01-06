from django.views.generic import TemplateView

class CView(TemplateView):
    """ modeler View Class """
    ## template 
    TEMPLATE = '_modeler.hbs'
    template_name = TEMPLATE
    ## context
    def get_context_data(self, **kwargs):
        MODULE_NAME = 'BPMN Modeler'
        context = super(CView, self).get_context_data(**kwargs)
        dict_cxt = {
            "title": MODULE_NAME
        }
        context.update(dict_cxt)
        return context

root = CView.as_view()
