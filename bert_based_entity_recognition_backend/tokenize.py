
# from django.views.decorators.csrf import csrf_exemp
# # @api_view(["POST"])
# @csrf_exempt 
# def tokenize(request):
#     print("hello")
#     if request.method == "POST":
#         print("reached")
#         # return reached
#         # return HttpResponseRedirect(request('world:Profile'))

# ----------------------

from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import JsonResponse

class UserAccessView(View):
    http_method_names = ["post"]  

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if "tokenize" in request.path:
            return self.tokenize(request)
        return Response({"message": "Invalid request."})

    def tokenize(self, request):
        if request.method == "POST":
            return JsonResponse({"message": "Tokenization successful"})


