from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import VideoModel,VideoMeta
from .forms import VideoMetaForm
import datetime
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip
import uuid
from django.contrib import messages
# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def table(request):
    video_obj = VideoModel.objects.all()
    if request.POST:
        video_pk_list = request.POST.getlist('tableField', None)
        print(video_pk_list[0])
        video_obj = VideoModel.objects.order_by(video_pk_list[0])
    return render(request, 'videoList.html', {'video_obj' : video_obj})

def showvideo(request):
    if request.method == 'POST':
        thumbnail_obj = request.FILES['video']
        name_obj = thumbnail_obj.name.split('.')[0]
        id_obj = uuid.uuid1()
        created_obj = datetime.datetime.now()
        clip = VideoFileClip(thumbnail_obj.temporary_file_path())
        duration_obj =clip.duration
        status_obj = 'Ready'
        VideoModel.objects.get_or_create(Thumbnail=thumbnail_obj , Name=name_obj ,VideoId=id_obj , Created_on = created_obj,Duration=duration_obj, Status=status_obj )[0]
    return redirect('table')

def AcceseMeta(request,VideoId):
    details = get_object_or_404(VideoModel, VideoId=VideoId)
    file_url=details.Thumbnail.url

    v_form = VideoMetaForm(request.POST, request.FILES)
    if v_form.is_valid():
        n_form = v_form.save(commit = False)
        n_form.Video = details
        n_form.save()
    else:
        form = VideoMetaForm()
    context = {
    'file_url' :file_url,
    'details':details,
    'v_form'  :v_form
    }
    return render(request, 'createVideo.html', context)
