//funtion to call funtion DataTable() of framework jquery.datatable.min.js to
//add action search and fix size of table

$('#sidebar_manageTag').attr('class','active');
$('#sidebar_manageUser').removeAttr('class');
$('#sidebar_manageModerator').removeAttr('class');

var topicTable;
function dataTopicTable() {
    topicTable = $('#manageTopicTable').DataTable();
}
dataTopicTable();

function addTopic() {
    $('.modal-title').text('Add New Topic');
    $('#addTopicBtn').text('Add');
    $('#topicName').val("");
    $('#addTopicBtn').removeAttr('onclick');
    $('#addTopicBtn').attr('onclick', 'addTopicAction()');
    // console.log("click add topic");

}

function addTopicAction() {
    // alert('Add Topic!');
    topicName = $('#topicName').val();
    topicName = topicName.trim();
    if (checkNull('warning_topicName', topicName)) {
        return
    }
    // console.log(topicName);
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: 'manageTopic',
        type: 'POST',
        data: {topicName: topicName},
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", token);
            }
        },
        success: function (data) {
            // console.log(data);
            if (data['status'] == 'success') {
                var edit_function = "editTopic('" + topicName + "'," + data['tagID'] + ")";
                topicTable.row.add([
                    data['tagID'],
                    topicName,
                    0,
                    '<div class="row">' +
                    '<button class = "btn btn-primary" data-toggle = "modal" data-target = "#addTopicModal"' +
                    'onclick = "' + edit_function + '"> Edit' +
                    '</button >' +
                    '<button class = "btn btn-danger" data-toggle = "modal" data-target = "#modalDelete"> Delete' +
                    '</button > </div > '
                ]).draw(false);

                $('#addTopicModal').modal('hide');
            } else if (data['status'] == 'error') {
                alert(data['message']);
                return;
            }
        },
        error: function (err) {
            alert(err);
        }
    });


}

function editTopic(topicName, tagID) {
    $('#warning_topicName').attr('class', 'hide_warning');
    console.log(topicName + " " + tagID);
    // console.log("click add topic");
    $('.modal-title').text('Edit Topic');
    $('#addTopicBtn').text('Update');
    $('#topicName').val(topicName);
    $('#addTopicBtn').removeAttr('onclick');
    $('#addTopicBtn').attr('onclick', 'editTopicAction("' + topicName + '",' + tagID + ')');
    $('#addTopicBtn').attr('disabled', 'disabled');
}

$('#topicName').change(function () {
    $('#addTopicBtn').removeAttr('disabled');
})

function editTopicAction(old_topicName, tagID) {
    // alert('Edit Topic!');
    var new_topicName = $('#topicName').val();
    new_topicName = new_topicName.trim();
    if (new_topicName == old_topicName) {
        alert('No change to update');
    } else {
        $.ajax({
            url: "manageTopic?tagID=" + tagID + '&topicName=' + new_topicName,
            type: 'get',
            success: function (data) {
                // console.log("data");
                console.log(data['status']);

                $('#tagName' + tagID).text(new_topicName);

                $('#addTopicModal').modal('hide');
            },
            error: function (err) {
                alert(err);
            }
        });
    }
}

function deleteTopic(tag_name, tag_id) {
    $('#topicNameDelete').text(tag_name);
    $('#btn_ok_delete').attr('onclick', 'deleteTopicAction("' + tag_name + '",' + tag_id + ')');
}

function deleteTopicAction(tag_name, tag_id) {
    // alert('Delete '+tag_name +' - ' + tag_id);
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: 'manageTopic',
        type: 'POST',
        data: {topicName: tag_name, action: 'delete'},
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", token);
            }
        },
        success: function (data) {
            // console.log(data);
            if (data['status'] == 'success') {

                topicTable.row($('#rowTag'+tag_id))
                    .remove()
                    .draw();

                $('#modalDelete').modal('hide');
            } else if (data['status'] == 'error') {
                console.log('error');
                return;
            }
        },
        error: function (err) {
            console.log("Error!");
        }
    });
}

function checkNull(id, str) {
    if (str == null || str == "") {
        $('#' + id).removeAttr('class');
        return true;
    } else {
        $('#' + id).attr('class', 'hide_warning');
        return false;
    }
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}