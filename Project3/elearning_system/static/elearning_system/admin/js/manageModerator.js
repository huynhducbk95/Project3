//funtion to call funtion DataTable() of framework jquery.datatable.min.js to
//add action search and fix size of table
function dataModeratorTable() {
    $('#manageModeratorTable').DataTable();
}
dataModeratorTable();

function blockModerator(moderatorFullName, email) {
    console.log(moderatorFullName + " - " + email);
    $('.warning-moderator').text("Bạn thực sự muốn Block moderator này?");
    $('#btn_moderator').attr('class', 'btn btn-danger');
    $('#btn_moderator').text('Block');
    $('#moderatorFullName').text(moderatorFullName);
    $('#moderator_email').text(email);
    $('#btn_moderator').removeAttr('onclick');
    $('#btn_moderator').attr('onclick', 'blockAction()');

}

function blockAction() {
    alert("Block moderator!");
}

function activeModerator(moderatorFullName, email) {
    console.log(moderatorFullName + " - " + email);
    $('.warning-moderator').text("Bạn thực sự muốn Active moderator này?");
    $('#btn_moderator').attr('class', 'btn btn-primary');
    $('#btn_moderator').text('Active');
    $('#moderatorFullName').text(moderatorFullName);
    $('#moderator_email').text(email);
    $('#btn_moderator').removeAttr('onclick');
    $('#btn_moderator').attr('onclick', 'activeAction()');
}

function activeAction() {
    alert("Active moderator");
}