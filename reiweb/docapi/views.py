from django.contrib.staticfiles import finders
from django.shortcuts import render

# importing the necessary libraries
import os
from io import BytesIO, StringIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings

from xhtml2pdf import pisa
from django.views.generic import View


# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, context_dict=None):
    if context_dict is None: context_dict = {}

    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, debug=1, encoding='UTF-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def main(request):
    template = 'index.html'
    if request.method == 'GET':
        address = '서울특별시 중랑구 봉우재로154'
        land = {'category': '대', 'area': '122.2'}
        bld = {'structure': '철근콘크리트', 'purpose': '다세대', 'area': '88.87'}
        rent = {'part': '702호', 'area': '27.85'}
        pay = {'sum': '이억삼천만원', 'down': '이천삼백만원', 'middle': '', 'balance': '이억칠백만원', 'rent': ''}
        day = {'middle': '', 'balance': '2022년 5월 9일', 'rent': ''}
        clause = [{'num': '제 1조 ', 'title': '[ 목적 ]',
                   'content': '위 부동산의 임대차에 한하여 임대인과 임차인은 합의에 의하여 임차보증금 및 차임을 아래와 같이 지불하기로 한다.'},
                  {'num': '제 2조 ', 'title': '[ 존속기간 ]',
                   'content': '임대인은 위 부동산을 임대차 목적대로 사용수익 할 수 있는 상태로        년       월       일까지 임차인에게 인도하며, 임대차 기간은 인도일로부터        년       월       일까지 (       개월)로 한다.'},
                  {'num': '제 3조 ', 'title': '[ 용도변경 및 전대 등 ]',
                   'content': '임차인은 임대인의 동의없이 위 부동산의 용도나 구조를 변경하거나 전대, 임차권 양도 또는 담보 제공을 하지 못하며 임대차 목적 이외의 용도로 사용할 수 없다.'},
                  {'num': '제 4조 ', 'title': '[ 계약의 해지 ]',
                   'content': '임차인의 차임 연체액이 (         )기의 차임액에 달하거나, 제3조를 위반하였을 때 임대인은 즉시 본 계약을 해지 할 수 있다.'},
                  {'num': '제 5조 ', 'title': '[ 계약의 종료 ]',
                   'content': '임대차계약이 종료된 경우에 임차인은 위 부동산을 원상으로 회복하여 임대인에게 반환한다. 이러한 경우 임대인은 보증금을 임차인에게 반환하고, 연체 임대료 또는 손해배상금이 있을 때는 이들을 제하고 그 잔액을 반환한다.'},
                  {'num': '제 6조 ', 'title': '[ 계약의 해제 ]',
                   'content': '임차인이 임대인에게 중도금(중도금이 없을 때는 잔금)을 지불하기 전까지 임대인은 계약금의 배액을 상환 하고, 임차인은 계약금을 포기하고 이 계약을 해제할 수 있다.'},
                  {'num': '제 7조 ', 'title': '[ 채무불이행과 손해배상의 예정 ]',
                   'content': '임대인 또는 임차인은 본 계약상의 내용에 대하여 불이행이 있을 경우 그 상대방은 불이행 한 자에 대하여 서면으로 최고하고 계약을 해제 할 수 있다. 이 경우 계약 당사자는 계약해제에 따른 손해배상을 각각 상대방에게 청구할 수 있으며, 손해배상에 대하여 별도의 약정이 없는 한 계약금을 손해배상의 기준으로 본다.'},
                  {'num': '제 8조 ', 'title': '[ 중개보수 ]',
                   'content': '개업공인중개사는 임대인 또는 임차인의 본 계약 불이행에 대하여 책임을 지지 않는다. 또한 중개보수는 본 계약 체결에 따라 계약 당사자 쌍방이 각각 지불하며, 개업공인중개사의 고의나 과실 없이 본 계약이 무효, 취소 또는 해제되어도 중개보수는 지급한다. 공동중개인 경우에 임대인과 임차인은 자신이 중개 의뢰한 개업공인중개사에게 각각 중개보수를 지급한다'},
                  {'num': '제 9조 ', 'title': '[ 중개대상물 확인설명서 교부 등 ]',
                   'content': '개업공인중개사는 중개대상물 확인설명서를 작성하고 업무보증관계증서(공제증서 등) 사본을 첨부하여 계약체결과 동시에 거래당사자 쌍방에게 교부한다. (교부일자 :        년      월      일)'},
                  ]
        agrs = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">1. 임차인 현장 방문후 현 시설물 상태의 계약임.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">2. 현 등기사항 증명서상 권리는 임차인 전입신고 다음날까지 유지하기로함.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">3. 임대인은 전세자금 대출에 동의,적극 협조하기로 하며 본 건물로 대출 불가시 계약은 무효임.(계약금 전액 반환)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">4. 계약을 중도 해지할 시, 각종 부대비용(중개보수 등)은 해지를 희망하는 자가 부담하기로하며,퇴실시엔 차기임차인을 구할수 있도록 상호 협조하기로함.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">5.본계약은 매매 계약이 된 상태로 소유권 이전이 있음을 고지하고 매매 계약서을 첨부함.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">6. 관리비는 본 건물 관리 규약에 따름.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">7. 임대인, 임차인 개인정보활용에 동의 하였음. </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">8. 기타 사항은 민법 임대차보호법  및 부동산 임대차 계약 일반 관례에 따르기로 함.</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">9. 임대인 계좌번호: 예금주  허태우:우리은행 1002-660-489981</p></body></html>
        """
        contractor = [{'kind': '임 대 인', 'name': '서수연', 'rr_num': '711115-2528217', 'mobile': '010-9386-7937',
                       'address': '서울특별시 중랑구 봉우재로 154, 702호 (다원빌)'},
                      {'kind': '임 차 인', 'name': '장성남', 'rr_num': '950509-1323418', 'mobile': '010-2486-1307',
                       'address': '서울특별시 중랑구 봉우재로 154, 702호 (다원빌)'}
                      ]
        agent = [{'kind': '공인중개사', 'address': '서울특별시 상봉동 122-76번지', 'bs_nm': '하울공인중개사사무소',
                  'gen': '02-435-9600', 'rr_num': '11260-2020-00049'}]

        context = {'address': address, 'land': land, 'bld': bld, 'rent': rent, 'pay': pay, 'day': day, 'clause': clause,
                   'agrs': agrs, 'contractor': contractor, 'agent': agent}

        pdf = html_to_pdf(template, context)
        return render(request, template, context)
        # return HttpResponse(pdf, content_type='application/pdf')
    return render(request, 'index.html')
