/**
 * Created by huynhduc on 16/12/2016.
 */

function _init_() {
    var exercise_length = $('#compare_elearning').data('length-exercise');
    console.log(exercise_length);
    var add_page = exercise_length % 5;
    var page = 0;
    if (add_page > 0) {
        page = Math.floor(exercise_length / 5) + 1;
    } else {
        page = Math.floor(exercise_length / 5);
    }
    for (var i = 2; i <= page; i++) {
        var li = document.createElement('li');
        if (i == page) {
            $(li).attr('data-last', 'true');
        }
        $(li).addClass('pagination_btn');
        $(li).attr('data-value', i);
        var span = document.createElement('span');
        $(span).css('cursor', 'pointer');
        var context = document.createTextNode(i);
        span.appendChild(context);
        li.appendChild(span);
        var ul = document.getElementById('pagination_elearning');
        var last_li = document.getElementById('last_pagination_elearning');
        ul.insertBefore(li, last_li);
    }
}
_init_();
$('.pagination_btn').click(function () {
        var self = $(this);
        $('.pagination_btn').removeClass('active');
        // self.addClass('active');
        var sort_option = $('#compare_elearning').val();
        var is_latest = self.data('last');
        var number_page = self.data('value');
        console.log(number_page);
        var number_option = undefined;
        if (number_page === '1') {
            $('#first_pagination_elearning').addClass('disable').css('cursor', 'not-allowed');
            $('#last_pagination_elearning').removeClass('disable').css('cursor', 'pointer');
            self.addClass('active');
            number_option = '1';
        } else if (is_latest === 'true') {
            $('#last_pagination_elearning').addClass('disable').css('cursor', 'not-allowed');
            $('#first_pagination_elearning').removeClass('disable').css('cursor', 'pointer');
            self.addClass('active');
            number_option = number_page;
        } else if (number_page === '-') {
            var current_page = Number($('#pagination_elearning').data('current-page')) - 1;
            $('.pagination_btn').each(function () {
                var value = $(this).data('value');
                if (Number(value) == current_page) {
                    $(this).addClass('active');
                }
            });
            number_option = current_page + '';

        } else if (number_page === '+') {
            var current_page = Number($('#pagination_elearning').data('current-page')) + 1;
            $('.pagination_btn').each(function () {
                var value = $(this).data('value');
                if (Number(value) == current_page) {
                    $(this).addClass('active');
                }
            });
            console.log(current_page);
            number_option = current_page + '';
        } else {
            self.addClass('active');
            number_option = number_page;
        }
        console.log(number_option);
        $('#pagination_elearning').attr('data-current-page', number_option);
        var page_name = 'index';
        var option_in_page = 'all';
        $.get('compare_exercise?page_name=' + page_name + '&option_in_page=' + option_in_page + '&sort_option=' + sort_option + '&number_page=' + number_page, function (data) {
            console.log(data);
        })
    }
);
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
