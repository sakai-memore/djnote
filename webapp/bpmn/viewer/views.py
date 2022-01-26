from django.views.generic import TemplateView

class CView(TemplateView):
    """ viewer View Class """
    ## template 
    TEMPLATE = '_bpmn_viewer.hbs'
    template_name = TEMPLATE
    ## context
    def get_context_data(self, **kwargs):
        MODULE_NAME = 'BPMN Viewer'
        context = super(CView, self).get_context_data(**kwargs)
        dict_cxt = {
            "title": MODULE_NAME
        }
        context.update(dict_cxt)
        return context

root = CView.as_view()

# from django.shortcuts import render
#
# # Create your views here.
# def root(request):
#     context = {
#         "title": "Django"
#     }
#     return render(request, '_viewer.hbs', context)
