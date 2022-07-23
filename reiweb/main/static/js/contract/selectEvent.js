
$(document).ready(function() {
    $("#opt_type option:selected").change(function () {
        month = $('#opt_type option:selected').val();
        $('.form').submit();
    });

});