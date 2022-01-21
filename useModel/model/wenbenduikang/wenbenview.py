import json

from django.http import HttpResponse


def post_json(request):
    json_str = request.body

    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])
    return HttpResponse('OK')




    # return JsonResponse(book_list, safe=False)