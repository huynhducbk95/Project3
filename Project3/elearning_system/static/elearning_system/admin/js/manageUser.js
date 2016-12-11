function blockUser(username,email){
    $('.warning-user').text("Bạn thực sự muốn Block user này?");
    $('#btn_user').attr('class','btn btn-danger');
    $('#btn_user').text('Block');
    $('#user_name').text(username);
    $('#user_email').text(email);
    $('#btn_user').removeAttr('onclick');
    $('#btn_user').attr('onclick','blockAction()');

}

function blockAction(){
    alert("Block user!");
}

function activeUser(username,email) {
    $('.warning-user').text("Bạn thực sự muốn Active user này?");
    $('#btn_user').attr('class','btn btn-primary');
    $('#btn_user').text('Active');
    $('#user_name').text(username);
    $('#user_email').text(email);
    $('#btn_user').removeAttr('onclick');
    $('#btn_user').attr('onclick','activeAction()');
}

function activeAction(){
    alert("Active user");
}