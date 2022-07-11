
import os
import base64
import json
import pdfkit

from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import get_template


def main(request):
    template = 'index.html'
    if request.method == 'GET':
        context = json.loads(request.body)
        context = json.loads(context)

        template = get_template(template)
        html = template.render(context)

        pdf_options = {
            'page-size': 'A4',
            'margin-top': '0in',
            'margin-bottom': '0in',
            'margin-right': '0in',
            'margin-left': '0in',
            'encoding': "UTF-8",
            'footer-center': '[page]',
            "quiet": "",
            'no-outline': None,
        }

        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        pdf_file = pdfkit.from_string(html, configuration=config, options=pdf_options)
        sitename_base64 = base64.b64encode(pdf_file).decode('utf8')
        return JsonResponse({'pdf': sitename_base64})

    return render(request, 'index.html')


def wish_lists_pdf(user):
    pdf_heading = "Thank you!"
    pdf_subheading = "Please find the Wish Lists you signed up to sponsor listed below."

    pdf_context = {
        'heading': pdf_heading,
        'subheading': pdf_subheading,
        'user': user,
    }
    css = os.path.join(basedir, 'static/main.css')
    pdf_content = render_template(
        'partials/email_lists_pdf.html', **pdf_context)

    path_wkhtmltopdf = app.config['WKHTMLTOPDF_EXE']
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    pdf_file = pdfkit.from_string(pdf_content, False, configuration=config, css=css)

    return pdf_file
