from django.shortcuts import render, redirect
from pytube import YouTube

# Create your views here.
def youtube(request):
  #check if request.method is post or not
  if request.method == 'POST':

    #getting link from frontend
    link = request.POST['link']
    video = YouTube(link)

    #setting video resolution
    stream = video.streams.get_lowest_resolution()

    #downloads video
    stream.download()

    #return HTML page
    return render(request, 'main/youtube.html')
  return render(request, 'main/youtube.html')