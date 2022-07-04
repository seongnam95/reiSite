from django.shortcuts import render

# Create your views here.


def main(request):
    template = 'index.html'
    if request.method == 'GET':
        print('진입')
        context = {'typeCd': '2',       # 0: 매매, 1: 전세, 2: 월세
                   'kindCd': '01',      #

                   }
        return render(request, template, context)
    return render(request, 'index.html')
