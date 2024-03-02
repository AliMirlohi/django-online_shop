from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from product_module.models import Product
from .models import Order, OrderDetail
from django.conf import settings
import requests
import json
from django.urls import reverse
# Create your views here.

MERCHANT = '5bbf840b-2645-4919-9ad8-ced35d39c17c'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "نهایی کردن خرید شما از سایت ما"  # Required
email = ''  # Optional
mobile = ''  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/order/verify-payment/'



def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'مقدار وارد شده معتبر نمی باشد.',
            'icon': 'warning',
            'confirmButtonText': 'مرسی از شما'
        })

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_delete=False, is_active=True).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()
            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد.',
                'icon': 'success',
                'confirmButtonText': 'باشه ممنونم'
            })
        else:
            return JsonResponse({
                'status': 'not found',
                'text': 'محصول مورد نظر یافت نشد.',
                'icon': 'error',
                'confirmButtonText': 'عجب'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای افزودن محصول به سبد خرید ابتدا می بایست وارد سایت شوید.',
            'icon': 'error',
            'confirmButtonText': 'ورود به سایت'
        })

# @login_required
# def request_payment(request: HttpRequest):
#     req_data = {
#         "merchant_id": MERCHANT,
#         "amount": amount,
#         "callback_url": CallbackURL,
#         "description": description,
#         "metadata": {"mobile": mobile, "email": email}
#     }
#     req_header = {"accept": "application/json", "content-type": "application/json'"}
#     req = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
#     authority = req.json()['data']['authority']
#     if len(req.json()['errors']) == 0:
#         return redirect(ZP_API_STARTPAY.format(authority=authority))
#     else:
#         e_code = req.json()['errors']['code']
#         e_message = req.json()['errors']['message']
#         return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
#
#
# def verify_payment(request: HttpRequest):
#     t_authority = request.GET['Authority']
#     if request.GET.get('Status') == 'OK':
#         req_header = {"accept": "application/json", "content-type": "application/json'"}
#         req_data = {
#             "merchant_id": MERCHANT,
#             "amount": amount,
#             "authority": t_authority
#         }
#         req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
#         if len(req.json()['errors']) == 0:
#             t_status = req.json()['data']['code']
#             if t_status == 100:
#                 return HttpResponse('Transaction success.\nRefID: ' + str(
#                     req.json()['data']['ref_id']
#                 ))
#             elif t_status == 101:
#                 return HttpResponse('Transaction submitted : ' + str(
#                     req.json()['data']['message']
#                 ))
#             else:
#                 return HttpResponse('Transaction failed.\nStatus: ' + str(
#                     req.json()['data']['message']
#                 ))
#         else:
#             e_code = req.json()['errors']['code']
#             e_message = req.json()['errors']['message']
#             return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
#     else:
#         return HttpResponse('Transaction failed or canceled by user')





# def request_payment(request: HttpRequest):
#     current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
#     total_price = current_order.calculate_total_price()
#     if total_price == 0:
#         return redirect(reverse('user_basket_page'))
#
#     data = {
#         "MerchantID": 982023032700373,
#         "Amount": total_price * 10,
#         "Description": description,
#         # "Phone": phone,
#         "CallbackURL": CallbackURL,
#     }
#     data = json.dumps(data)
#     # set content length by data
#     headers = {'content-type': 'application/json', 'content-length': str(len(data))}
#     try:
#         response = requests.post(ZP_API_REQUEST, data=data, timeout=10,headers=headers)
#
#         if response.status_code == 200:
#             response = response.json()
#             if response['Status'] == 100:
#                 return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
#                         'authority': response['Authority']}
#             else:
#                 return {'status': False, 'code': str(response['Status'])}
#         return response
#
#     except requests.exceptions.Timeout:
#         return {'status': False, 'code': 'timeout'}
#     except requests.exceptions.ConnectionError:
#         return {'status': False, 'code': 'connection error'}
# def verify_payment(request: HttpRequest):
#     print(request.user)
#     print(request.user.id)
#     data = {
#         "MerchantID": Merchant,
#         "Amount": amount,
#         "Authority": authority,
#     }
#     data = json.dumps(data)
#     # set content length by data
#     headers = {'content-type': 'application/json', 'content-length': str(len(data))}
#     response = requests.post(ZP_API_VERIFY, data=data,)
#
#     if response.status_code == 200:
#         response = response.json()
#         if response['Status'] == 100:
#             return {'status': True, 'RefID': response['RefID']}
#         else:
#             return {'status': False, 'code': str(response['Status'])}
#     return response
def zarin_link(request: HttpRequest):
    # current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    # total_price = current_order.calculate_total_price()
    data = {'amount':1000}
    # return redirect('https://zarinp.al/testtestcom')
    return requests.post('https://zarinp.al/testtestcom',data)


