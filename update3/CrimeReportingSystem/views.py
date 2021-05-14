from django.shortcuts import render,redirect
from django.http import HttpResponse
from CrimeReportingSystem.forms import UserRegistrationForm,MyProfileForm,ChangepassForm,ComplaintForm,ContactForm
from CrimeReportingSystem.models import MyProfile
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
	return render(request,'html/home.html')

def aboutus(request):
	return render(request,'html/aboutus.html')

def contactus(r):
	if r.method == "POST":
		i=ContactForm(r.POST)
		if i.is_valid():
			i.save()
			return redirect('/')

	i=ContactForm()
	return render(r,'html/contactus.html',{'u':i})

# def login(r):
    # return render(r,'html/login.html')
 
def register(r):
	if r.method == "POST":
		p=UserRegistrationForm(r.POST)
		if p.is_valid():
			p.save()
			return redirect('/login')

	p=UserRegistrationForm()
	return render(r,'html/register.html',{'u':p})

@login_required
def profile(r):
	p=MyProfileForm()
	return render(r,'html/profile.html',{'p':p})

@login_required
def dashboard(r):
	return render(r,'html/dashboard.html')

@login_required
def changepass(request):
 	if request.method=="POST":
 		c=ChangepassForm(user=request.user,data=request.POST)
 		if c.is_valid():
 			c.save()
 			return redirect('/login')

 	c=ChangepassForm(user=request)
 	return render(request,'html/changepassword.html',{'t':c})

@login_required
def updateprofile(request):
	if request.method == "POST":
		u=UserupdateForm(request.POST,instance=request.user)
		i=MyProfileForm(request.POST,request.FILES,instance=request.user.myprofile)
		if u.is_valid() and i.is_valid():
			u.save()
			i.save()
			return redirect('/myprofile')
	u=UserupdateForm(instance=request.user)
	i=MyProfileForm(instance=request.user.myprofile)
	return render(request,'html/updateprofile.html',{'us':u,"imp":i})


def complaint(req):
	if req.method=="POST":
		data=ComplaintForm(req.POST)
		if data.is_valid():
			subject='Confirmation_Complaint'
			body="thank you for complaint"+req.POST['p_name']
			receiver=req.POST['p_email']
			sender=settings.EMAIL_HOST_USER
			send_mail(subject,body,sender,[receiver])
			data.save()
			messages.success(req,"Successfully sent to your mail "+receiver)
			return redirect('/')
	form=ComplaintForm()
	return render(req,'html/complaint.html',{'c':form})


	
def crud(request):
	if request.method=="POST":
		c=UserRegistrationForm(request.POST)
		if c.is_valid():
			c.save()
			return render(request,'html/actions.html',{'o':c})
	c=UserRegistrationForm()
	return render(request,'html/actions.html',{'o':c})


def deletedata(req,id):
 	c=UserRegistration.objects.get(id=id)
 	c.delete()
 	return redirect('/crud')
