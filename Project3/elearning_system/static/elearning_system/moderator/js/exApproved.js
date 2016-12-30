/**
 * Created by ha on 10/12/2016.
 */

$('#sidebar_manageErrorMessage').removeAttr('class');
$('#sidebar_manageExApproved').attr('class','active');
$('#sidebar_manageExUnapprove').removeAttr('class');
$('#sidebar_manageExNoTopic').removeAttr('class');

function dataExApprovedTable() {
    $('#exApprovedTable').DataTable();
}
dataExApprovedTable();

function viewExApproved(){
    // alert('Show view edit exercise approved');
}
