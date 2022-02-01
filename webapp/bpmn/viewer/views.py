from django.views.generic import TemplateView

class CView(TemplateView):
    """ viewer View Class """
    ## template 
    TEMPLATE = '_bpmn_viewer.hbs'
    template_name = TEMPLATE
    ## context
    def get_context_data(self, pk, **kwargs):
        MODULE_NAME = 'BPMN Viewer'
        context = super(CView, self).get_context_data(**kwargs)
        file_name = ''
        if pk == 1:
            file_name = "PDM_Pizz_order.bpmn"
        elif pk == 2:
            file_name = "PDM_Pizz_delivery.bpmn"
        elif pk == 3:
            file_name = "PDM_Pizz_cooking.bpmn"
        else:
            file_name = "sample.bpmn"
        #
        dict_cxt = {
            "title": MODULE_NAME,
            "id": pk,
            "file_name": file_name,
        }
        context.update(dict_cxt)
        return context

root = CView.as_view()

