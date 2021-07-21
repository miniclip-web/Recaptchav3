import copy

from django import forms

class ContactForm(forms.Form):
    """
        Contact page form
    """

    HELP_TYPE_OPTIONS = (
        (None, '-Select One-'),
        ('Question About Getting A Loan', 'Question About Getting A Loan'),
        ('General Question About Personify Loans', 'General Question About Personify Loans'),
        ('Questions About An Existing Personify Loan', 'Questions About An Existing Personify Loan')
    )

    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtFirstName', 'autocomplete': False}))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtLastName', 'autocomplete': False}))
    email = forms.CharField(label='Your Email', max_length=254, widget=forms.EmailInput(
            attrs={'class': 'form-control', 'id': 'txtEmail', 'autocomplete': False}))
    mobile_phone = forms.CharField(label='Your Phone', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'txtPhone', 'autocomplete': False}))
    help_type = forms.CharField(label='How can we help you today?', required=True,
                                widget=forms.Select(choices=HELP_TYPE_OPTIONS,
                                                    attrs={
                                                        'class': 'form-control',
                                                        'id': 'ddlHelpType',
                                                        'autocomplete': False
                                                    }))
    message = forms.CharField(label='Message', widget=forms.Textarea(
            attrs={'class': 'form-control', 'id': 'txtMessage'}))

    def clean(self):
        data_dict = copy.deepcopy(self.cleaned_data)
        for field, value in data_dict.items():
            is_valid, error_msg = validate(value, field, validation_config.contact_mandatory_fields)
            if not is_valid:
                self.add_error(field, error_msg)
        return self.cleaned_data


class ComplaintContactForm(forms.Form):
    """
        Complaint Contact page form
    """

    RELATED_TO_OPTIONS = (
        (None, '-Select One-'),
        ('Application - Approval Process', 'Application - Approval Process'),
        ('Application - Decline Process', 'Application - Decline Process'),
        ('Call Center Practices', 'Call Center Practices'),
        ('Collection Practices', 'Collection Practices'),
        ('Credit Bureau Reporting Issue', 'Credit Bureau Reporting Issue'),
        ('Document Upload Process', 'Document Upload Process'),
        ('Payment Issue', 'Payment Issue'),
        ('Other', 'Other'),
    )

    full_name = forms.CharField(label='* Name', max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtFullName', 'autocomplete': False}))
    email = forms.CharField(label='* Email', max_length=254, widget=forms.EmailInput(
            attrs={'class': 'form-control', 'id': 'txtEmail', 'autocomplete': False}))
    phone_day = forms.CharField(label='Phone (day)', required=False, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtPhoneDay', 'autocomplete': False}))
    phone_evg = forms.CharField(label='Phone (evening)', required=False, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtPhoneEvg', 'autocomplete': False}))
    cell_phone = forms.CharField(label='Cell Phone', required=False, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtCellPhone', 'autocomplete': False}))
    loan_number = forms.CharField(label='Personify Loan Number (if applicable)', required=False, max_length=35, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtLoanNumber', 'autocomplete': False}))
    related_to = forms.CharField(label='Related to', required=False, widget=forms.Select(choices=RELATED_TO_OPTIONS,
                                                    attrs={
                                                        'class': 'form-control',
                                                        'id': 'ddlRelatedTo',
                                                        'autocomplete': False
                                                    }))
    complaint_message = forms.CharField(label='* Inquiry/Complaint', widget=forms.Textarea(
            attrs={'class': 'form-control', 'id': 'txtMessage'}))
    desired_resolution = forms.CharField(label='Desired Resolution', required=False, widget=forms.Textarea(
            attrs={'class': 'form-control', 'id': 'txtMessage'}))

    def clean(self):
        data_dict = copy.deepcopy(self.cleaned_data)
        for field, value in data_dict.items():
            is_valid, error_msg = validate(value, field, validation_config.complaint_contact_mandatory_fields)
            if not is_valid:
                self.add_error(field, error_msg)
        return self.cleaned_data


class COVIDRequestForm(forms.Form):
    """
        COVID-19 request form
    """

    full_name = forms.CharField(label='* Name', max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtFullName', 'autocomplete': False}))
    email = forms.CharField(label='* Email', max_length=254, widget=forms.EmailInput(
            attrs={'class': 'form-control', 'id': 'txtEmail', 'autocomplete': False}))
    phone_day = forms.CharField(label='Phone (day)', required=False, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtPhoneDay', 'autocomplete': False}))
    phone_evg = forms.CharField(label='Phone (evening)', required=False, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtPhoneEvg', 'autocomplete': False}))
    cell_phone = forms.CharField(label='Cell Phone', required=False, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtCellPhone', 'autocomplete': False}))
    covid_loan_number = forms.CharField(label='* Personify Loan Number', required=True, min_length=12, max_length=19, widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'txtLoanNumber', 'autocomplete': False}))
    request_message = forms.CharField(label='* Please explain your specific situation', widget=forms.Textarea(
            attrs={'class': 'form-control', 'id': 'txtMessage'}))

    def clean(self):
        data_dict = copy.deepcopy(self.cleaned_data)
        for field, value in data_dict.items():
            if field != 'covid_loan_number':
                is_valid, error_msg = validate(value, field, validation_config.covid_request_mandatory_fields)
                if not is_valid:
                    self.add_error(field, error_msg)
        return self.cleaned_data