from django.db import models
from account_module.models import User
from product_module.models import Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,verbose_name='کاربر' , on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='نهایی شده / نشده')
    payment_date = models.DateField(null=True,blank=True,verbose_name='تاریخ پرداخت')

    def __str__(self):
        return str(self.user)

    def calculate_total_price(self):
        total_amount = 0
        if not self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        return total_amount

    class Meta:
        verbose_name='سبد خرید'
        verbose_name_plural= 'سبد های خرید کاربران'

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,verbose_name='سبد خرید',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name='محصول', on_delete=models.CASCADE)
    final_price= models.IntegerField(null=True,blank=True , verbose_name= 'قیمت نهایی تکی محصول')
    count= models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزئیات سبد خرید'
        verbose_name_plural = 'لیست جزئیات سبد خرید'
