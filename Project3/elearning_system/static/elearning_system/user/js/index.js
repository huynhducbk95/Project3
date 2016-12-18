/**
 * Created by huynhduc on 16/12/2016.
 */
console.log('come on');
$('#menu_compare_elearning').click(function () {
   var value = $(this).val();
    console.log(value);
    $.get('compare_exercise?option='+value,function (data) {
        console.log(data);
    })
});
