function approveEx() {
    // $.get('http://45.63.50.197/plugin/detail?exid=2',function (data) {
    //     console.log(data);
    // if(data.status == "success"){
    //     $('#status'+ id).text("Active");
    //     $('#' + id).text('Block');
    //     $('#' + id).removeAttr('onclick');
    //     $('#' + id).removeAttr('class');
    //     $('#' + id).attr('class','btn btn-danger');
    //     $('#' + id).attr('onclick','blockUser("'+username+'","'+email+'",'+id+')');
    // } else {
    //     alert("Error!");
    // }
    // $('#modalUser').modal('hide');
    // });

    $.ajax({
        url: "http://45.63.50.197/plugin/detail?exid=1",
        type: 'get',
        success: function (result) {
            console.log("data");
            console.log(result);
        },
        error: function (xhr) {
            alert("An error occured: " + xhr.status + " " + xhr.statusText);
        }
    });
}