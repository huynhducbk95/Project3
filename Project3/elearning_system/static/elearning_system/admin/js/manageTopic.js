function addTopic() {
    $('.modal-title').text('Add New Topic');
    $('#addTopicBtn').text('Add');
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

function editTopic(topicName) {
    console.log(topicName);
    // console.log("click add topic");
    $('.modal-title').text('Edit Topic');
    $('#addTopicBtn').text('Update');
    $('#topicName').val(topicName);
    $('#addTopicBtn').removeAttr('onclick');
    $('#addTopicBtn').attr('onclick','editTopicAction()');
}

function editTopicAction() {
    alert('Edit Topic!');
}

function deleteTopic() {
    alert('Action delete topic');
}