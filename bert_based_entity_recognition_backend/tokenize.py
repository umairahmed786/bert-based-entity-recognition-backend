
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
# @api_view(["POST"])
def tokenize(request):
    if request.method == "POST":
        print("reached")
        return reached