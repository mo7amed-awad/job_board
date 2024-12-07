from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm,JobForm
# Create your views here.


def job_list(request):
    job_list = Job.objects.all()
    total_jobs = job_list.count()  # Total number of jobs

    paginator = Paginator(job_list,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'job/job_list.html', {'jobs': page_obj, 'total_jobs': total_jobs})



def job_detail(request,slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()

    else:
        form = ApplyForm()

    return render(request,'job/job_detail.html',{'job':job_detail,'form':form})



def add_job(request):

    if request.method=='POST':
        form1 = JobForm(request.POST , request.FILES)
        if form1.is_valid():
            myform = form1.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form1 = JobForm()

    return render(request,'job/add_job.html',{'form1':form1})