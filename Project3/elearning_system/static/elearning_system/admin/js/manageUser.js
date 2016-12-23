//funtion to call funtion DataTable() of framework jquery.datatable.min.js to
//add action search and fix size of table

var t;
function dataUserTable() {
    t = $('#manageUserTable').DataTable();
}
dataUserTable();

function showModalAddUser(){
    $('#form_add_userName').val('');
    $('#form_add_fullName').val('');
    $('#form_add_email').val('');
    $('#form_add_phoneNumber').val('');
    $('#form_add_pass').val('');
    $('#form_add_rePass').val('');

    $('#warning_userName').attr('class', 'hide_warning');
    $('#warning_fullName').attr('class', 'hide_warning');
    $('#warning_email').attr('class', 'hide_warning');
    $('#warning_numberPhone').attr('class', 'hide_warning');
    $('#warning_pass').attr('class', 'hide_warning');
    $('#warning_rePass').attr('class', 'hide_warning');
}

function blockUser(username, email, id) {
    $('.warning-user').text("Bạn thực sự muốn Block user này?");
    $('#btn_user').attr('class', 'btn btn-danger');
    $('#btn_user').text('Block');
    $('#user_name').text(username);
    $('#user_email').text(email);
    $('#btn_user').removeAttr('onclick');
    $('#btn_user').attr('onclick', 'blockAction("' + username + '","' + email + '",' + id + ')');

}

function blockAction(username, email, id) {
    // alert("Block user! " + id);
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
        $('#modalUser').modal('hide');
    });
}

function activeUser(username, email, id) {
    $('.warning-user').text("Bạn thực sự muốn Active user này?");
    $('#btn_user').attr('class', 'btn btn-primary');
    $('#btn_user').text('Active');
    $('#user_name').text(username);
    $('#user_email').text(email);
    $('#btn_user').removeAttr('onclick');
    $('#btn_user').attr('onclick', 'activeAction("' + username + '","' + email + '",' + id + ')');
    // console.log('activeAction("'+username+'","'+email+'",'+id+')');
}

function activeAction(username, email, id) {
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
        $('#modalUser').modal('hide');
    })
}

function addUser() {
    // alert('them');
    var userName = $('#form_add_userName').val();
    userName = userName.trim();
    if (checkNull('warning_userName', userName)) {
        return
    }

    var fullName = $('#form_add_fullName').val();
    fullName = fullName.trim();
    if (checkNull('warning_fullName', fullName)) {
        return
    }

    var email = $('#form_add_email').val();
    email = email.trim();
    if (!checkNull('warning_email', email)) {
        var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;
        if (testEmail.test(email)) {
            $('#warning_email').attr('class', 'hide_warning');
        } else {
            $('#warning_email').removeAttr('class');
            return
        }
    } else {
        return
    }

    var numberPhone = $('#form_add_phoneNumber').val();
    numberPhone = numberPhone.trim();
    if (!checkNull('warning_numberPhone', numberPhone)) {

        if (parseInt(numberPhone) && (numberPhone.length > 9) && (numberPhone.length < 13)) {
            $('#warning_numberPhone').attr('class', 'hide_warning');
        } else {
            $('#warning_numberPhone').removeAttr('class');
            return
        }
    } else {
        return
    }

    var pass = $('#form_add_pass').val();
    pass = pass.trim();
    if (checkNull('warning_pass', pass)) {
        return
    }

    var rePass = $('#form_add_rePass').val();
    rePass = rePass.trim();
    if (!checkNull('warning_rePass', rePass)) {
        if (rePass == pass) {
            $('#warning_rePass').attr('class', 'hide_warning');
        } else {
            $('#warning_rePass').removeAttr('class');
            return
        }
    } else return

    var user = {user_name: userName,password:pass,full_name:fullName,email_address:email
                ,block_status: 'Active'};

    var token = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: 'manageUser',
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
                var moderatorID = data['newUserID'];
                var text = "blockUser('"+fullName+"','"+email+"',"+moderatorID+")";
                t.row.add( [
                    moderatorID,
                    userName,
                    fullName,
                    email,
                    "Active",
                    0,
                    0,
                    '<div class="row">' +
                    '<button class="btn btn-danger" data-toggle="modal" data-target="#modalModerator"' +
                    'onclick="'+text+
                    '>Block</button>' +
                    '</div>'
                ] ).draw( false );

                $('#modalAddUserd').modal('hide');
            } else if(data['status'] == 'error'){
                alert(data['message']);
                return;
            }
        },
        error: function (err) {
            alert('Error!');
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