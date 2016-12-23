//funtion to call funtion DataTable() of framework jquery.datatable.min.js to
//add action search and fix size of table
var tableModerator;
function dataModeratorTable() {
    tableModerator = $('#manageModeratorTable').DataTable();
}
dataModeratorTable();

function showModalAddModerator(){
    $('#form_add_moderatorName').val('');
    $('#form_add_moderatorfullName').val('');
    $('#form_add_moderatorEmail').val('');
    $('#form_add_moderatorPhoneNumber').val('');
    $('#form_add_moderatorPass').val('');
    $('#form_add_moderatorRepass').val('');

    $('#warning_moderatorName').attr('class', 'hide_warning');
    $('#warning_moderatorFullName').attr('class', 'hide_warning');
    $('#warning_moderatorEmail').attr('class', 'hide_warning');
    $('#warning_moderatorNumberPhone').attr('class', 'hide_warning');
    $('#warning_moderatorPass').attr('class', 'hide_warning');
    $('#warning_moderatorRepass').attr('class', 'hide_warning');
}

function blockModerator(moderatorFullName, email,id) {
    console.log(moderatorFullName + " - " + email);
    $('.warning-moderator').text("Bạn thực sự muốn Block moderator này?");
    $('#btn_moderator').attr('class', 'btn btn-danger');
    $('#btn_moderator').text('Block');
    $('#moderatorFullName').text(moderatorFullName);
    $('#moderator_email').text(email);
    $('#btn_moderator').removeAttr('onclick');
    $('#btn_moderator').attr('onclick', 'blockAction("' + moderatorFullName + '","' + email + '",' + id + ')');

}

function blockAction(username,email,id) {
    // alert("Block moderator!");
    $.get('change_status_user?user_id=' + id, function (data) {
        if (data.status == "success") {
            $('#status' + id).text("Block");
            $('#' + id).text('Active');
            $('#' + id).removeAttr('onclick');
            $('#' + id).removeAttr('class');
            $('#' + id).attr('class', 'btn btn-primary');
            $('#' + id).attr('onclick', 'activeUser("' + username + '","' + email + '",' + id + ')');
        } else {
            alert("Error!");
        }
        $('#modalModerator').modal('hide');
    });
}

function activeModerator(moderatorFullName, email,id) {
    console.log(moderatorFullName + " - " + email);
    $('.warning-moderator').text("Bạn thực sự muốn Active moderator này?");
    $('#btn_moderator').attr('class', 'btn btn-primary');
    $('#btn_moderator').text('Active');
    $('#moderatorFullName').text(moderatorFullName);
    $('#moderator_email').text(email);
    $('#btn_moderator').removeAttr('onclick');
    $('#btn_moderator').attr('onclick', 'activeAction("' + moderatorFullName + '","' + email + '",' + id + ')');
}

function activeAction(username,email,id) {
    username = username.toString();
    email = email.toString();
    $.get('change_status_user?user_id=' + id, function (data) {
        console.log(data.status);
        if (data.status == "success") {
            $('#status' + id).text("Active");
            $('#' + id).text('Block');
            $('#' + id).removeAttr('onclick');
            $('#' + id).removeAttr('class');
            $('#' + id).attr('class', 'btn btn-danger');
            $('#' + id).attr('onclick', 'blockUser("' + username + '","' + email + '",' + id + ')');
        } else {
            alert("Error!");
        }
        $('#modalModerator').modal('hide');
    })
}

function addModerator() {
    // alert('them');
    var userName = $('#form_add_moderatorName').val();
    userName = userName.trim();
    if (checkNull('warning_moderatorName', userName)) {
        return
    }

    var fullName = $('#form_add_moderatorfullName').val();
    fullName = fullName.trim();
    if (checkNull('warning_moderatorFullName', fullName)) {
        return
    }

    var email = $('#form_add_moderatorEmail').val();
    email = email.trim();
    if (!checkNull('warning_moderatorEmail', email)) {
        var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
        if (testEmail.test(email)) {
            $('#warning_moderatorEmail').attr('class', 'hide_warning');
        } else {
            $('#warning_moderatorEmail').removeAttr('class');
            return
        }
    } else {
        return
    }

    var numberPhone = $('#form_add_moderatorPhoneNumber').val();
    numberPhone = numberPhone.trim();
    if (!checkNull('warning_moderatorNumberPhone', numberPhone)) {

        if (parseInt(numberPhone) && (numberPhone.length > 9) && (numberPhone.length < 13)) {
            $('#warning_moderatorNumberPhone').attr('class', 'hide_warning');
        } else {
            $('#warning_moderatorNumberPhone').removeAttr('class');
            return
        }
    } else {
        return
    }

    var pass = $('#form_add_moderatorPass').val();
    pass = pass.trim();
    if (checkNull('warning_moderatorPass', pass)) {
        return
    }

    var rePass = $('#form_add_moderatorRepass').val();
    rePass = rePass.trim();
    if (!checkNull('warning_moderatorRepass', rePass)) {
        if (rePass == pass) {
            $('#warning_moderatorRepass').attr('class', 'hide_warning');
        } else {
            $('#warning_moderatorRepass').removeAttr('class');
            return
        }
    } else return

    var user = {user_name: userName,password:pass,full_name:fullName,email_address:email
                ,block_status: 'Active'};

    var token = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: 'manageModerator',
        type: 'POST',
        data: user,
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", token);
            }
        },
        success: function (data) {
            // console.log(data);
            if (data['status'] == 'success') {
                // alert('add row');
                var text = "blockModerator('"+fullName+"','"+email+"',"+data['newModaretorID']+")";
                // console.log("text: " + text);
                tableModerator.row.add( [
                    data['newModaretorID'],
                    userName,
                    fullName,
                    email,
                    "Active",
                    '<div class="row">' +
                    '<button class="btn btn-danger" data-toggle="modal" data-target="#modalModerator"' +
                    'onclick="'+text+'")"'+
                    '>Block</button>' +
                    '</div>'
                ] ).draw( false );

                $('#modalAddModerator').modal('hide');
            } else if(data['status'] == 'error'){
                alert(data['message']);
                return;
            }
        },
        error: function (err) {
            alert(err);
        }
    });


function addRow(){
    // var t = $('#example').DataTable();
    t.row.add( [
            counter +'.1',
            counter +'.2',
            counter +'.3',
            counter +'.4',
            counter +'.5'
        ] ).draw( false );
}

    // console.log('gui xong');
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
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