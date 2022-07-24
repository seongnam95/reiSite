$(document).ready(function(){
    // 가격 정보 입력
    $("input[name=price]").on("change keyup paste", function() {
        inputNumberFormat(this);
        console.log($(this).parent("div").parent("div"));

        // 한글 금액표기
        priceStr = this.value;
        if(priceStr) {
            priceKr = String(parseInt(uncomma(priceStr)) * 10000);
            convVal = numberToKorean(priceKr);

            parent_div = $(this).parent("div").parent("div");
            parent_div.find(".price_kor").text(convVal);
        };
    });

    // 셀렉트 Box
    var selectTarget = $('.selectbox select');
    selectTarget.on('blur', function(){
        $(this).parent().removeClass('focus');
    });

    selectTarget.change(function(){
        const target = $(this);

        var target_val = $(this).children('option:selected').text();
        target.siblings('label').text(target_val);

        if (target.prop("id") == $("#opt_type").prop("id")){
            if (target_val != "계약서 선택") {
                $.ajax({
                    url: "/main/contract/",
                    type: "GET",
                    data: {'data': target_val},
                    dataType: "html",
                    success:function(){ },
                    error: function(request, status, error){
                      alert('서버와의 연결에 실패하였습니다.');
                    }
                });
            }
        }
    });
});

function comma(str) {str = String(str); return str.replace(/(\d)(?=(?:\d{3})+(?!\d))/g, '$1,');}
function uncomma(str) { str = String(str); return str.replace(/[^\d]+/g, ''); }
function inputNumberFormat(obj) { obj.value = comma(uncomma(obj.value)); }
function inputOnlyNumberFormat(obj) { obj.value = onlynumber(uncomma(obj.value)); }
function onlynumber(str) { str = String(str); return str.replace(/(\d)(?=(?:\d{3})+(?!\d))/g,'$1'); }

// 금액표기 한글 변환
  function numberToKorean(number) {
    var inputNumber = number < 0 ? false : number;
    var unitWords = ["", "만", "억 ", "조 ", "경 "];
    var splitUnit = 10000;
    var splitCount = unitWords.length;
    var resultArray = [];
    var resultString = "";

    for (var i = 0; i < splitCount; i++) {
      var unitResult =
        (inputNumber % Math.pow(splitUnit, i + 1)) / Math.pow(splitUnit, i);
      unitResult = Math.floor(unitResult);
      if (unitResult > 0) {
        resultArray[i] = unitResult;
      }
    }
    for (var i = 0; i < resultArray.length; i++) {
      if (!resultArray[i]) continue;
      resultString = String(resultArray[i]) + unitWords[i] + resultString;
    }
    return resultString.trimEnd() + '원';
  }

function commas(t) {
	// 콤마 빼고
	var x = t.value;
	x = x.replace(/,/gi, '');

    // 숫자 정규식 확인
	var regexp = /^[0-9]*$/;
	if(!regexp.test(x)){
		$(t).val("");
		alert("숫자만 입력 가능합니다.");
	} else {
		x = x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
		$(t).val(x);
	}
}