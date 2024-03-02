from django.shortcuts import render , redirect

from site_module.models import SiteSetting
# from .forms import ContactUsForm
from .forms import ContactUsModelForm
from django.urls import reverse
from .models import ContactUs,UserProfile
from django.views import View
from django.views.generic.edit import FormView,CreateView
from django.views.generic import ListView
# Create your views here.



# class ContactUsView(FormView):
#     template_name = 'contact_module/contact_us_page.html'
#     form_class = ContactUsModelForm
#     success_url = '/contact-us/'
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        setting : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting']= setting
        return context


# def store_file(file):
#     with open('temp/image.jpg','wb+') as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'


    # def get(self,request):
    #     form= ProfileForm()
    #     return render(request,'contact_module/create_profile_page.html',{'form':form})
    #
    # def post(self,request):
    #     submitted_form = ProfileForm(request.POST,request.FILES)
    #     if submitted_form.is_valid():
    #         # store_file(request.FILES['profile'])
    #         profile= UserProfile(image=request.FILES['user_image'])
    #         profile.save()
    #         return redirect('/contact-us/create-profile')
    #     return render(request, 'contact_module/create_profile_page.html', {'form': submitted_form})

class ProfilesView(ListView):
    template_name = 'contact_module/profiles_list_page.html'
    model = UserProfile
    context_object_name = 'profiles'



# class ContactUsView(View):
#
#     def get(self,request):
#         contact_form = ContactUsModelForm()
#         return render(request, 'contact_module/contact_us_page.html', {
#             'contact_form': contact_form
#         })4
#
#     def post(self,request):
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('home_page')
#         return render(request, 'contact_module/contact_us_page.html', {
#             'contact_form': contact_form
#         })
# def contact_us_page(request):
#     if request.method == 'POST':
#         # contact_form = ContactUsForm(request.POST)
#         contact_form = ContactUsModelForm(request.POST)
#         # if contact_form.is_valid():
#         #     print(contact_form.cleaned_data)
#         #     contact=ContactUs(
#         #         title = contact_form.cleaned_data.get('title'),
#         #         full_name= contact_form.cleaned_data.get('full_name'),
#         #         email= contact_form.cleaned_data.get('email'),
#         #         message= contact_form.cleaned_data.get('message')
#         #     )
#         #     contact.save()
#         contact_form.save()
#         return redirect('home_page')
#     else:
#         # contact_form = ContactUsForm()
#         contact_form = ContactUsModelForm()
#
#     return render(request,'contact_module/contact_us_page.html',{
#         'contact_form':contact_form
#     })

 