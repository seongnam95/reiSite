from django.shortcuts import render

# Create your views here.


def main(request):
    template = 'index.html'
    return render(request, template)


def contract(request):
    template = 'contract/basic.html'
    context = temp_data(request.GET.get('data'))
    print(render(request, template, context))
    return render(request, template, context)


def temp_data(data=None):
    contract_kind = ['일반 계약서', '표준임대차 계약서', '분양권']
    prop_type = ['아파트', '단독주택', '다세대주택', '다가구주택']
    prop = {'kind': contract_kind, 'type': prop_type}

    context = {'data': data, 'prop': prop}
    return context
