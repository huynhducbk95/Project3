/**
 * Created by huynhduc on 19/12/2016.
 */

var PAGINATION_NUMBER = 1;
var exercise_length = $('#compare_elearning').data('length-exercise');
console.log(exercise_length);
var add_page = exercise_length % 5;
var page = 0;
if (add_page > 0) {
    page = Math.floor(exercise_length / 5) + 1;
} else {
    page = Math.floor(exercise_length / 5);
}
var PATHNAME = window.location.href;
$('#page-selection').bootpag({
    total: page
}).on("page", function (event, /* page number here */ num) {
    $('.exercise_list_elearning').css('display','');
    var page_name = 'tag';
    var page_option = PATHNAME.split('=')[1];
    var page_compare = $('#compare_elearning').val();
    $.get('get_exercise_pagination?page_name=' + page_name +
        '&page_option=' + page_option +
        '&page_compare=' + page_compare +
        '&pagination_number=' + num
        , function (data) {
            var exercise_list = data['exercise_list'];
            var remove_index = 5 - exercise_list.length;
            var count = 0;
            $('.exercise_list_elearning').each(function () {
                if (count < exercise_list.length) {
                    $(this).find('.exercise_name').html(exercise_list[count]['name']);
                    $(this).find('.exercise_description').html(exercise_list[count]['description']);
                    $(this).find('.exercise_contributor').html(exercise_list[count]['contributor']);
                    $(this).find('.exercise_passed').html(exercise_list[count]['passed']);
                    $(this).find('.exercise_view').html(exercise_list[count]['view']);
                    count += 1;
                }else{
                    $(this).css('display','none');
                    count += 1;
                }

            })
        });
    $('#page-selection').attr('data-value', num);
    PAGINATION_NUMBER = num;
});


$('#compare_elearning').change(function () {
    var value = $(this).val();
    var page_option = PATHNAME.split('=')[1];
    console.log(page_option);
    $.get('get_exercise_pagination?page_compare=' + value
        + '&page_name=tag'
        + '&page_option=' + page_option
        + '&pagination_number=' + PAGINATION_NUMBER, function (data) {
        var count = 0;
        $('.exercise_list_elearning').each(function () {
            var self = $(this);
            var exercise_name = $(this).find('.exercise_name').html(data['exercise_list'][count]['name']);
            var exercise_description = $(this).find('.exercise_description').html(data['exercise_list'][count]['description']);
            var exercise_contributor = $(this).find('.exercise_contributor').html(data['exercise_list'][count]['contributor']);
            var exercise_passed = $(this).find('.exercise_passed').html(data['exercise_list'][count]['passed']);
            var exercise_view = $(this).find('.exercise_view').html(data['exercise_list'][count]['view']);
            count += 1;
        })
    })
});
