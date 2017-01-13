/**
 * Created by huynhduc on 11/12/2016.
 */
$('.li_search_option').click(function () {
    var option = $(this).data('value');
    $('#search_concept').html(option);
});

var timeout = null;

function doDelayedSearch(val) {
    if (timeout) {
        clearTimeout(timeout);
    }
    timeout = setTimeout(function () {
        doSearch(val); //this is your existing function
    }, 2000);
}
function doSearch(value) {
    $('#typeahead_search').empty();
    $('#typeahead_search').css('display', 'none');
    var quick_search_url = $('#test_test').data('quicksearch');
    if (value.length > 0) {
        $.get(quick_search_url+'?keyword=' + value, function (data) {
            console.log(data);
            exercise_list = data['exercise_list'];
            var count = 0;
            for (var i = 0; i < exercise_list.length; i++)
                if (count < 5) {
                    var li = document.createElement('li');
                    $(li).attr('id', 'exercise_search');
                    var a = document.createElement('a');
                    $(a).css('color', 'black');
                    $(a).css('cursor', 'pointer');
                    $(a).attr('href',"/exercise/exercise_detail/"+exercise_list[i]['id']);
                    var h4 = document.createElement('h4');
                    var ex_name = document.createTextNode(exercise_list[i]['name']);
                    h4.appendChild(ex_name);
                    var span = document.createElement('span');
                    var ex_description = document.createTextNode(exercise_list[i]['description']);
                    span.appendChild(ex_description);
                    a.appendChild(h4);
                    a.appendChild(span);
                    li.appendChild(a);
                    $('#typeahead_search').css('display', '');
                    var ul = document.getElementById('typeahead_search');
                    ul.appendChild(li);
                    count += 1;
                }
            if (exercise_list.length > 5) {
                console.log('vao di ma');
                var li = document.createElement('li');
                $(li).attr('id', 'exercise_search');
                var a = document.createElement('a');
                $(a).attr('href',"/search?search="+value+"&search_option=All");
                var h4 = document.createElement('h4');
                var ex_name = document.createTextNode('See more ' + exercise_list.length + ' exercise >>');
                h4.appendChild(ex_name);
                $(a).attr('id', 'see_more_exercise');
                a.appendChild(h4);
                li.appendChild(a);
                var ul = document.getElementById('typeahead_search');
                ul.appendChild(li);
            }
        })

    }

}
$('#search_handle').click(function () {
    var search_option = $('#search_concept').text();
    if (search_option == 'Sort by') {
        search_option = 'All'
    }
    var input = document.createElement('input');
    $(input).attr({
        type: 'hidden',
        id: 'foo',
        name: 'search_option'
    });
    $(input).val(search_option);
    var form = document.getElementById('form_search');
    form.appendChild(input);
});
