$(document).ready(function(){
      $("#txt_deposit").blur(function(){
      });

    // 금액 입력 시
    $("#txt_deposit").on("change keyup paste", function() {
        var str = $("#txt_deposit").val();
        console.log(str);
        str = str.replace(/(\d)(?=(?:\d{3})+(?!\d))/g, '$1,')
        $("#txt_deposit").val(str);
        var convVal = viewKorean(str);
        $("#hint_deposit").text(convVal);
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

// 금액표기 한글 변환
function viewKorean(num) {
    var hanA = new Array("","일","이","삼","사","오","육","칠","팔","구","십");
    var danA = new Array("","십","백","천","","십","백","천","","십","백","천","","십","백","천");
    var result = "";
    for(i=0; i<num.length; i++) {
        str = "";
        han = hanA[num.charAt(num.length-(i+1))];
        if(han != "") str += han+danA[i];
        if(i == 4) str += "만";
        if(i == 8) str += "억";
        if(i == 12) str += "조";
        result = str + result;
    }
    if(num != 0)
        result = result + "원";
    return result ;
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