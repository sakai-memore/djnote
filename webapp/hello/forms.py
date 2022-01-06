## https://gist.github.com/maraujop/1838193
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class CForm(forms.Form):
    txt_fld = forms.CharField(label='text field')
    txa_fld = forms.CharField(
        widget = forms.Textarea(),
        label='textarea field',
        required= False,
    )
    rdo_fld = forms.ChoiceField(
        choices = (
            ('rdo_one', 'Option One'),
            ('rdo_two', 'Option Two'),
        ),
        widget = forms.RadioSelect,
        label='radio button field',
        initial = 'rdo_one',
    )
    chk_fld = forms.MultipleChoiceField(
        choices = (
            ('chk_one', 'Check One'),
            ('chk_two', 'Check Two'),
            ('chk_three', 'Check Three'),
        ),
        widget = forms.CheckboxSelectMultiple,
        label='checkbox field',
        initial = 'chk_one',
        help_text = "<strong>note:</strong> Labels surround all the options."
    )
    appended_text = forms.CharField(
        help_text = "Here's more help text"
    )

    prepended_text = forms.CharField()
    
    prepended_text_two = forms.CharField()
    
    multicolon_select = forms.MultipleChoiceField(
        choices = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
    )

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('txt_fld', css_class='input-xlarge'),
        AppendedText('appended_text', '@gmail.com'),
        Field('txa_fld', rows="3", css_class='input-xlarge'),
        'rdo_fld',
        Field('chk_fld', style="background: #FAFAFA; padding: 10px;"),
        PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
        PrependedText('prepended_text_two', '@'),
        'multicolon_select',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel', css_class="btn-secondary"),
        )
    )    
