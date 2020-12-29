from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import numpy as np


# Create your views here.
def telecom_homepage(request):
    return render(request, "Telecom/index.html")


def telecom_result(request):
    if request.POST:
        request_dict = request.POST.dict()

        gender_val_male, gender_val_female = get_gender_value(request_dict)
        if gender_val_male is False or gender_val_female is False:
            return HttpResponse('<h1>Invalid Gender Selection</h1>')

        sen_cit_val = get_sen_citizen_status(request_dict)
        if sen_cit_val is False:
            return HttpResponse('<h1>Invalid Senior Citizen Selection</h1>')

        partner_val = get_partner_status(request_dict)
        if partner_val is False:
            return HttpResponse('<h1>Invalid Partner Selection</h1>')

        dependents_val = get_dependents_status(request_dict)
        if dependents_val is False:
            return HttpResponse('<h1>Invalid Dependents Selection</h1>')

        tenure_val = get_tenure_value(request_dict)
        if tenure_val is False:
            return HttpResponse('<h1>Invalid Tenure Value</h1>')

        phn_service_val = get_phn_service_status(request_dict)
        if phn_service_val is False:
            return HttpResponse('<h1>Invalid Phone Service Status</h1>')

        contract_val_month, contract_one_year, contract_two_year = get_contract_status(request_dict)
        if contract_val_month is False or contract_one_year is False or contract_two_year is False:
            return HttpResponse('<h1>Invalid Contract Value</h1>')

        paperless_val = get_paperless_status(request_dict)
        if paperless_val is False:
            return HttpResponse('<h1>Invalid Paperless Value</h1>')

        payment_method_val_bk, payment_method_val_cc, payment_method_val_ec, payment_method_val_mc = get_payment_method_status(request_dict)
        if payment_method_val_bk is False or payment_method_val_cc is False or payment_method_val_ec is False or payment_method_val_mc is False:
            return HttpResponse('<h1>Invalid Payment Method Status</h1>')

        monthly_charge_val = get_monthly_charge_value(request_dict)
        if monthly_charge_val is False:
            return HttpResponse('<h1>Invalid Monthly Charge Value</h1>')

        tot_charge_val = get_total_charge_value(request_dict)
        if tot_charge_val is False:
            return HttpResponse('<h1>Invalid Total Charge Value</h1>')

        get_multiple_line_val = get_multiple_line_status(request_dict)
        if get_multiple_line_val is False:
            return HttpResponse('<h1>Invalid Multiple Line Status</h1>')

        internet_service_val_no, internet_service_val_dsl, internet_service_val_fiber = get_internet_service_status(request_dict)
        if internet_service_val_no is False or internet_service_val_dsl is False or internet_service_val_fiber is False:
            return HttpResponse('<h1>Invalid Internet Service</h1>')

        online_security_val = get_online_security_status(request_dict)
        if online_security_val is False:
            return HttpResponse('<h1>Invalid Online Security Value</h1>')

        online_backup_val = get_online_backup_status(request_dict)
        if online_backup_val is False:
            return HttpResponse('<h1>Invalid Online Backup status</h1>')

        device_protect_val = get_device_protect_status(request_dict)
        if device_protect_val is False:
            return HttpResponse('<h1>Invalid Device Protection Status</h1>')

        tech_support_val = get_tech_support_status(request_dict)
        if tech_support_val is False:
            return HttpResponse('<h1>Invalid Tech Support Value</h1>')

        stream_tv_val = get_stream_tv_status(request_dict)
        if stream_tv_val is False:
            return HttpResponse('<h1>Invalid Streaming TV status</h1>')

        stream_movie_val = get_stream_movie_status(request_dict)
        if stream_movie_val is False:
            return HttpResponse('<h1>Invalid Streaming Movies Status</h1>')

        current_input_value_array = np.array([paperless_val, dependents_val, contract_one_year, contract_two_year,
                                              payment_method_val_ec, payment_method_val_mc, internet_service_val_fiber,
                                              internet_service_val_no, online_security_val, online_backup_val,
                                              tech_support_val, stream_tv_val])

        model_coef_ = np.array([0.33110004, -0.30942262, -1.23635693, -2.15960791, 0.51741586, 0.25072624, 0.69389611,
                                -1.1915759, -0.44440307, -0.47156352, -0.58696704, 0.18726024])
        model_intercept_ = -0.7795178
        value = sum(current_input_value_array * model_coef_) + model_intercept_
        churn_rate = round((1/(1+(np.exp(-value)))) * 100, 2)
        # print('Chances of Customer Churning (Leaving) Is:', churn_rate, '%')
        context = {'churn_rate_var': churn_rate}
        return render(request, "Telecom/final_msg.html", context)


def get_gender_value(request_dict):
    try:
        temp_val = int(request_dict.get('gender'))
    except:
        return False, False
    else:
        if temp_val not in [0, 1]:
            return False, False
        else:
            if temp_val == 0:
                return 0, 1
            elif temp_val == 1:
                return 1, 0


def get_sen_citizen_status(request_dict):
    try:
        temp_val = int(request_dict.get('sen_citizen'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val


def get_partner_status(request_dict):
    try:
        temp_val = int(request_dict.get('partner'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val


def get_dependents_status(request_dict):
    try:
        temp_val = int(request_dict.get('dependents'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val


def get_tenure_value(request_dict):
    try:
        temp_val = int(request_dict.get('tenure'))
    except:
        return False
    else:
        if (temp_val <= 0) or (temp_val > 120):
            return False
        else:
            return temp_val


def get_phn_service_status(request_dict):
    try:
        temp_val = int(request_dict.get('phone_ser'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val


def get_contract_status(request_dict):
    try:
        temp_val = int(request_dict.get('contract'))
    except:
        return False, False, False
    else:
        if temp_val not in [0, 1, 2]:
            return False, False, False
        else:
            if temp_val == 0:
                return 1, 0, 0
            elif temp_val == 1:
                return 0, 1, 0
            elif temp_val == 2:
                return 0, 0, 1


def get_paperless_status(request_dict):
    try:
        temp_val = int(request_dict.get('paperless'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val


def get_payment_method_status(request_dict):
    try:
        temp_val = int(request_dict.get('payment_method'))
    except:
        return False, False, False, False
    else:
        if temp_val not in [0, 1, 2, 3]:
            return False, False, False, False
        else:
            if temp_val == 0:
                return 1, 0, 0, 0
            elif temp_val == 1:
                return 0, 1, 0, 0
            elif temp_val == 2:
                return 0, 0, 1, 0
            elif temp_val == 3:
                return 0, 0, 0, 1


def get_monthly_charge_value(request_dict):
    try:
        temp_val = int(request_dict.get('mon_charge'))
    except:
        return False
    else:
        return temp_val


def get_total_charge_value(request_dict):
    try:
        temp_val = int(request_dict.get('tot_charge'))
    except:
        return False
    else:
        return temp_val


def get_multiple_line_status(request_dict):
    try:
        temp_val = int(request_dict.get('multiple_line'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val


def get_internet_service_status(request_dict):
    try:
        temp_val = int(request_dict.get('internet_ser'))
    except:
        return False
    else:
        if temp_val not in [0, 1, 2]:
            return False
        else:
            if temp_val == 0:
                return 1, 0, 0
            elif temp_val == 1:
                return 0, 1, 0
            elif temp_val == 2:
                return 0, 0, 1


def get_online_security_status(request_dict):
    try:
        temp_val = int(request_dict.get('online_sec'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val


def get_online_backup_status(request_dict):
    try:
        temp_val = int(request_dict.get('online_backup'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val


def get_device_protect_status(request_dict):
    try:
        temp_val = int(request_dict.get('device_protect'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val


def get_tech_support_status(request_dict):
    try:
        temp_val = int(request_dict.get('tech_support'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val


def get_stream_tv_status(request_dict):
    try:
        temp_val = int(request_dict.get('stream_tv'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val


def get_stream_movie_status(request_dict):
    try:
        temp_val = int(request_dict.get('stream_movie'))
    except:
        return False
    else:
        if temp_val not in [0, 1]:
            return False
        else:
            return temp_val
