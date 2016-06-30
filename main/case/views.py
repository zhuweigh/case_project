from django.shortcuts import render
import pdfcrowd
from case.models import Content
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .forms import  SearchForm
from haystack.query import SearchQuerySet
from easy_pdf.views import PDFTemplateView
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from easy_pdf.rendering import render_to_pdf_response
def test_pdf(request,case_id=5):
	#case = Content.objects.filter(id=1)
	#path = request.path
	#a = '/case/detail/5/'
	#path=path.split("/")
	#print(path)
	#p_num = path[-2]
	#print(int(p_num))
	case = get_object_or_404(Content,id=case_id)
	return render_to_pdf_response(request,'case/detail.html',{'case':case})

def case_search(request):
	query_ = request.GET
	cd={'query':' '}
	results=None
	total_results=None
	form = SearchForm()
	if 'query' in request.GET:
		form = SearchForm(request.GET)
		if form.is_valid():
			cd = form.cleaned_data
			results = SearchQuerySet().models(Content).filter(content=cd['query']).load_all()
			total_results = results.count()
	return render(request,'case/search.html',
				{'form': form,'cd': cd,
				'results': results,
				'total_results': total_results,'query_':query_,'cd':cd,'resylts':results})
def  CaseList(request):
	Cobj_list = Content.objects.all()
	paginator = Paginator(Cobj_list, 3) # 3 posts in each page
	page = request.GET.get('page')
	try:
   		cases = paginator.page(page)
	except PageNotAnInteger:
   		# If page is not an integer deliver the first page
   		cases = paginator.page(1)
	except EmptyPage:
  		# If page is out of range deliver last page of results
   		cases = paginator.page(paginator.num_pages)
		#posts = Post.published.all()
	return render(request,'case/list.html',{'cases': cases,'page':page})	
def CaseDetail(request,case_id):
	#path = request.path
	#print(path)
	case = get_object_or_404(Content,id=case_id)
	return render(request, 'case/detail.html',{'case':case})
#####################
no useful
###################
def export_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #p.drawString(100, 100, "Hell")
    p.drawString(100, 100, "case/templates/case/detail.html")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

class HelloPDFView(PDFTemplateView):
    template_name = "case/detail.html"
    #template_name = "http://192.168.1.131:7000/case/detail/4/"

    def get_context_data(self, **kwargs):
        return super(HelloPDFView, self).get_context_data(
            pagesize="A4",
            title="Hi there!",
            **kwargs
        )

def generate_pdf_view(request):
    try:
        # create an API client instance
        client = pdfcrowd.Client("username", "apikey")

        # convert a web page and store the generated PDF to a variable
        pdf = client.convertURI("http://www.baidu.com")

         # set HTTP response headers
        response = HttpResponse(mimetype="application/pdf")
        response["Cache-Control"] = "max-age=0"
        response["Accept-Ranges"] = "none"
        response["Content-Disposition"] = "attachment; filename=google_com.pdf"

        # send the generated PDF
        response.write(pdf)
    except pdfcrowd.Error as  why:
        response = HttpResponse(mimetype="text/plain")
        response.write(why)
    return response
