/**
 * Created by huynhduc on 18/12/2016.
 */
$('#btn_sign_up_elearning').click(function () {
    var user_name = $('#user_name_signup').val();
    var full_name = $('#full_name_signup').val();
    var password = $('#password_signup').val();
    var email = $('#email_signup').val();
    var repassword = $('#repassword_signup').val();
    if(user_name ==  ''){
        $('#message_signup').html('User name is not valid');
    }else if (full_name == '') {
        $('#message_signup').html('Full name is not valid');
    }else if (password == '') {
        $('#message_signup').html('Password is not valid');
    }else if (repassword != password) {
        $('#message_signup').html('Repassword is not valid');
    } else if (!validateEmail(email)) {
        $('#message_signup').html('Email address is not valid');
    } else {
        var data = {
            user_name: user_name,
            password: password,
            full_name: full_name,
            email: email
        };
        var token = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: 'registry',
            type: 'POST',
            data: data,
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", token);
                }
            },
            success: function (data) {
                if (data['result']==='error'){
                    $('#message_signup').html(data['message']);
                }else {
                    console.log('click');
                    document.getElementById("redirect_to_index").click();
                }
            },
            error: function (error) {
                console.log(error);
            }
        })
    }
});
function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}