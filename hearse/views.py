from django.shortcuts import render, redirect,get_object_or_404
from .models import Hearse, Request
from django.http import Http404, HttpResponse
from .forms  import user_detail

# pdf files import
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from app.models import User

# Create your views here.

# def hearses(request):
#     hearse = Hearse.objects.all()
#     return render(request, 'hearse.html',{'hearses':hearse})

def hearses(request, user_id):
    hearses = Hearse.objects.all()
    
    # hearses = User.objects.all()
    user_id = request.session.get('user_id', None)
    context ={
        "hearses":hearses,
        'user_id': user_id,        
    }
    return render(request, 'hearse.html', context)



# requests view
def request_data(request, user_id):
    frm = user_detail()
    person = get_object_or_404(User, id=user_id)
    user_id = person.id
    try:
        hearse_row = Hearse.objects.get(id=user_id)  # Retrieve object by primary key
    except Hearse.DoesNotExist:  # Handle object not found
        raise Http404("Row not found")
        # redirect('hearses')
    if request.method == "POST":
        frm = user_detail(request.POST, request.FILES)
        user_id = request.session.get('user_id', None)
        if frm.is_valid():
            frm.save()
            return redirect('hearses',user_id)
        else:
            frm = user_detail()

    return render(request, 'booking.html', {'hearse_row':hearse_row, 'frm':frm, 'user_id': user_id})




# print a pdf
def show_pdf(request):
    # h_id = int(h_id)
    try:
        details = Request.objects.all().last()  # Retrieve object by primary key
    except Request.DoesNotExist:  # Handle object not found
        raise Http404("Row not found")
    # creating bytestream buffer
    buf = io.BytesIO()
    # creating canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # text 
    textobj = c.beginText()
    textobj.setTextOrigin(inch,inch)
    textobj.setFont('Helvetica', 14)
    lines =[]
    # venues = Request.objects.all()
    
    
    # for detail in details:
    #     lines.append(detail.fullname)
    #     lines.append(detail.From)
    #     lines.append(detail.To)
    #     lines.append(detail.email)
    #     lines.append(detail.Day)
    #     # lines.append(venue.updated_time)
    #     lines.append('* Thanks for Reaching to us *')

        #finish up
    
    # formatted_date = event_date.strftime("%d/%m/%Y")
    if details:
        lines.append(details.fullname)
        lines.append(details.From)
        lines.append(details.To)
        lines.append(details.email)
        lines.append(details.Day.strftime("%d/%m/%Y"))
        lines.append('* Thanks for Reaching to us *')

    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj) 
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="details.pdf")