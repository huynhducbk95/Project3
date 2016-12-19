//funtion to call funtion DataTable() of framework jquery.datatable.min.js to
//add action search and fix size of table
function dataTopicTable() {
    $('#manageTopicTable').DataTable();
}
dataTopicTable();

function addTopic() {
    $('.modal-title').text('Add New Topic');
    $('#addTopicBtn').text('Add');
    $('#topicName').val("");
    $('#addTopicBtn').removeAttr('onclick');
    $('#addTopicBtn').attr('onclick','addTopicAction()');
    // console.log("click add topic");

}

function addTopicAction() {
    alert('Add Topic!');
}

// function add() {

    // var topicName = $('#topicName').val();
    // var pass = $('#pwd').val();
    // console.log(topicName + " - " + pass);
// }

function editTopic(topicName,tagID) {
    console.log(topicName + " " + tagID);
    // console.log("click add topic");
    $('.modal-title').text('Edit Topic');
    $('#addTopicBtn').text('Update');
    $('#topicName').attr('value',topicName);
    $('#addTopicBtn').removeAttr('onclick');
    $('#addTopicBtn').attr('onclick','editTopicAction()');
}

function editTopicAction() {
    alert('Edit Topic!');
}

function deleteTopic() {
    alert('Action delete topic');
}