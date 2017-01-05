function approve_ex(moderator_id,exercise_id) {
    var topic_selected = $('#exercise_topic').find(":selected").val();
    if(topic_selected == ""){
            alert("You must choose a topic for this exercise!");
    } else {
        $.get('upprove_exercise_status?moderator_id=' + moderator_id+'&exercise_id='+exercise_id+"&tag_id="+topic_selected,
        function (data) {
        console.log(data.status);
        if (data.status == "successful") {

        } else {
            alert("Error!");
        }
        $('#modalModerator').modal('hide');
    });
    }
}