from django.shortcuts import render

# Create your views here.


def main(request):
    template = 'index.html'
    return render(request, template)


def contract(request):
    template = 'contract/basic.html'
    context = temp_data()
    return render(request, template, context)


def temp_data():
    prop_type = ['아파트', '단독주택', '다세대주택', '다가구주택']
    prop = {'type': prop_type}

    context = {'prop': prop}
    return context
