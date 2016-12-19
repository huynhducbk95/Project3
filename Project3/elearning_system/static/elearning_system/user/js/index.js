/**
 * Created by huynhduc on 16/12/2016.
 */
var exercise_length = $('#compare_elearning').data('length-exercise');
console.log(exercise_length);
$('#compare_elearning').change(function () {
    var value = $(this).val();
    console.log(value);
    if (value !== 'compare') {
        $.get('compare_exercise?option=' + value + '&page=index', function (data) {
            console.log(data);
            count = 0;
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
    }
});
