from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; }
            h1 { color: blue; }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>Welcome to my first Django app!</p>
        <script>
            console.log("Hello, World! from JS");
        </script>
    </body>
    </html>
    """
    return HttpResponse(html)
