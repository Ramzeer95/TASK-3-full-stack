from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse

def http_response(request):
    return HttpResponse("Simple HttpResponse")

def http_response_sub(request):
    return HttpResponse("This is a subclass of HttpResponse", status=202)

def json_response(request):
    return JsonResponse({"message": "This is a JsonResponse"})

def streaming_response(request):
    def stream():
        yield "Streaming line 1\n"
        yield "Streaming line 2\n"
    return StreamingHttpResponse(stream(), content_type='text/plain')

def file_response(request):
    file_path = '/home/ramiroot/Desktop/djangofile'
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='download.txt')
