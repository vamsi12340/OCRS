from django.urls import path
from CrimeReportingSystem import views
from django.contrib.auth import views as ad

urlpatterns=[
    path('',views.home,name="hm"),
    path('aboutus/',views.aboutus,name="au"),
    path('contactus/',views.contactus,name="cu"),
    path('login/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
    path('register/',views.register,name="rg"),

    path('myprofile/',views.profile,name="profile"),
    path('changepassword/',views.changepass,name="chp"),
    path('logout/',ad.LogoutView.as_view(template_name='html/logout.html'),name="lgo"),
    path('dash/',views.dashboard,name="dsh"),

    path('updatepro/',views.updateprofile,name="uppro"),
    path('crud/',views.crud,name="cr"),
    path('delete/<str:id>',views.deletedata,name="delete"),

    path('reset/',ad.PasswordResetView.as_view(template_name="html/reset_password.html"),name="rst"),
    path('reset_done/',ad.PasswordResetDoneView.as_view(template_name="html/reset_password_done.html"),name="password_reset_done"),
    path('reset_cf/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name="html/reset_password_confirm.html"),name="password_reset_confirm"),
    path('reset_cmplt/',ad.PasswordResetCompleteView.as_view(template_name="html/reset_password_complete.html"),name="password_reset_complete"),
]