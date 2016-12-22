/**
 * Created by ha on 10/12/2016.
 */

function dataExNoTopicTable() {
    $('#exNoTopicTable').DataTable();
}
dataExNoTopicTable();

function addTopicForEx(id, exName, contributer) {
    $('#exNoTopic_name').text(exName);
    $('#exNoTopic_name').attr('data-value', id);
    $('#exNoTopic_contributer').text(contributer);
}

function actionAdd() {
    var exercise_id = $('#exNoTopic_name').data('value');
    var tag_id = $('#selectTopic').val();
    var data = {
        exercise_id: exercise_id,
        tag_id: tag_id
    };
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: 'add_tag',
        type: 'POST',
        data: data,
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", token);
            }
        },
        success: function (data) {
            $('#addTopicForEx').modal('hide');
            var row_remove = '#exercise_'+exercise_id;
            $(row_remove).remove();
            var count =1;
            $('.sorting_1').each(function () {
                $(this).html(count);
                count +=1;
            });
            $('#infor_change').css('display','');
            $('#message_add').html(data['message']);
            $('#infor_change').delay(5000).fadeOut();
        },
        error: function (error) {
            console.log(error);
        }
    })
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}