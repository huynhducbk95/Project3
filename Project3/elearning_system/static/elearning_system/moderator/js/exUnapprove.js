/**
 * Created by ha on 10/12/2016.
 */

$('#sidebar_manageErrorMessage').removeAttr('class');
$('#sidebar_manageExApproved').removeAttr('class');
$('#sidebar_manageExUnapprove').attr('class','active');
$('#sidebar_manageExNoTopic').removeAttr('class');

function dataExUnapproveTable() {
    $('#exUnapproveTable').DataTable();
}
dataExUnapproveTable();

function viewExUnapproved(idEx){
    // alert('View exercise unapprove');
    // idEx = idEx - 20;
//     $.ajax({
//         url: "detail_exUnapprove?exid="+idEx,
//         type: 'get',
//         success: function (result) {
//             console.log("success");
//             // console.log(result);
//         },
//         error: function (xhr) {
//             alert("An error occured: " + xhr.status + " " + xhr.statusText);
//         }
//     });
}
