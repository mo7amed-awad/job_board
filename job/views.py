from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
# Create your views here.


def job_list(request):
    job_list = Job.objects.all()

    paginator = Paginator(job_list,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'job/job_list.html',{'jobs':page_obj})

def job_detail(request,id):
    job_detail = Job.objects.get(id=id)
    return render(request,'job/job_detail.html',{'job':job_detail})