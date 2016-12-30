/**
 * Created by ha on 07/12/2016.
 */

//funtion to call funtion DataTable() of framework jquery.datatable.min.js to
//add action search and fix size of table

$('#sidebar_manageErrorMessage').attr('class','active');
$('#sidebar_manageExApproved').removeAttr('class');
$('#sidebar_manageExUnapprove').removeAttr('class');
$('#sidebar_manageExNoTopic').removeAttr('class');

function dataErrorMessageTable() {
    $('#errorMessageTable').DataTable();
}
dataErrorMessageTable();

function viewErrorMessage(){

}