from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import UploadedFileForm
from .utils import processfile
import string, random
import threading



def index(request):
    request.COOKIES["fileID"] = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    form = UploadedFileForm(initial={"file_id":request.COOKIES.get("fileID")})
    if request.method == "POST":
        file_id = request.POS["file_id"]
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            x =  threading.Thread(target=processfile, args=(file_id,), daemon=True)
            x.start()
            return redirect(f"/success/{file_id}/")

        else:
            print("Form Validation Failed")

    ctxt = {"form":form}
    return render(request, "home/index.html", ctxt)



def successview(request, fileID):
    result = UploadedFile.objects.get(file_id=fileID)
    ctxt = {"results":result}
    return render(request, "home/success.html", ctxt)













# Create your views here.
