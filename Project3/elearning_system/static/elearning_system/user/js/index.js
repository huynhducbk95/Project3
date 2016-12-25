/**
 * Created by huynhduc on 16/12/2016.
 */
var view_exercise_length = $('#page-selection').data('num_of_view_exercise');
var add_view_page = view_exercise_length % 4;
var page_view = 0;
if (add_view_page > 0) {
    page_view = Math.floor(view_exercise_length / 4) + 1;
} else {
    page_view = Math.floor(view_exercise_length / 4);
}
$('#page-selection').bootpag({
    total: page_view
}).on("page", function (event, /* page number here */ num) {
    $('.exercise_list_elearning').css('display', '');
    var page_name = 'index';
    var page_option = 'all';
    var page_compare = 'view';
    $.get('get_exercise_pagination?page_name=' + page_name +
        '&page_option=' + page_option +
        '&page_compare=' + page_compare +
        '&pagination_number=' + num
        , function (data) {
            console.log(data);
            var exercise_list = data['exercise_list'];
            var count = 0;
            $('.exercise_list_elearning').each(function () {
                if (count < exercise_list.length) {
                    $(this).find('.exercise_name').html(exercise_list[count]['name']);
                    $(this).find('.exercise_description').html(exercise_list[count]['description']);
                    $(this).find('.exercise_contributor').html(exercise_list[count]['contributor']);
                    $(this).find('.exercise_date').html(exercise_list[count]['date_created']);
                    $(this).find('.exercise_view').html(exercise_list[count]['view']);
                    count += 1;
                } else {
                    $(this).css('display', 'none');
                    count += 1;
                }

            })
        });
    $('#page-selection').attr('data-value', num);
});

var new_exercise_length = $('#new_page-selection').data('num_of_new_exercise');
var add_new_page = new_exercise_length % 4;
var page_new = 0;
if (add_new_page > 0) {
    page_new = Math.floor(new_exercise_length / 4) + 1;
} else {
    page_new = Math.floor(new_exercise_length / 4);
}
$('#new_page-selection').bootpag({
    total: page_new
}).on("page", function (event, /* page number here */ num) {
    $('.new_exercise_list_elearning').css('display', '');
    var page_name = 'index';
    var page_option = 'all';
    var page_compare = 'date';
    $.get('get_exercise_pagination?page_name=' + page_name +
        '&page_option=' + page_option +
        '&page_compare=' + page_compare +
        '&pagination_number=' + num
        , function (data) {
            console.log(data);
            var exercise_list = data['exercise_list'];
            var count = 0;
            $('.new_exercise_list_elearning').each(function () {
                if (count < exercise_list.length) {
                    $(this).find('.new_exercise_name').html(exercise_list[count]['name']);
                    $(this).find('.new_exercise_description').html(exercise_list[count]['description']);
                    $(this).find('.new_exercise_contributor').html(exercise_list[count]['contributor']);
                    $(this).find('.new_exercise_date').html(exercise_list[count]['date_created']);
                    $(this).find('.new_exercise_view').html(exercise_list[count]['view']);
                    count += 1;
                } else {
                    $(this).css('display', 'none');
                    count += 1;
                }

            })
        });
    $('#page-selection').attr('data-value', num);
});