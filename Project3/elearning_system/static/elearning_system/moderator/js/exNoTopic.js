/**
 * Created by ha on 10/12/2016.
 */

function dataExNoTopicTable() {
    $('#exNoTopicTable').DataTable();
}
dataExNoTopicTable();

function addTopicForEx(exName,contributer) {
    // alert("Add topic for exercise");
    $('#exNoTopic_name').text(exName);
    $('#exNoTopic_contributer').text(contributer);
}

function actionAdd (){
    alert('action add tag');
}