
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
import pickle
from transformers import pipeline
from transformers import BertTokenizerFast
import json

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
            data = json.loads(request.body)
            text = data.get("text")
            test_pickle = pickle.load(open("F:\\bert-based-entity-recognition-backend\\bert_based_entity_recognition_backend\\model.pkl", 'rb'))
            tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")
            nlp = pipeline("ner", model=test_pickle, tokenizer=tokenizer)
            ner_results = nlp(text)
            return JsonResponse({"message": json.dumps(str(ner_results))})


