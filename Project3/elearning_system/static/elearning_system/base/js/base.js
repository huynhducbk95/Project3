/**
 * Created by huynhduc on 11/12/2016.
 */

var pagination = $('.pagination_btn');
pagination.click(function () {

    console.log('dlkjfasldjfasdk');
    var self = $(this);
    $('.pagination_btn').removeClass('active');
    self.addClass('active');
});

$.typeahead({
    input: '.js-typeahead-hockey_v1',
    minLength: 1,
    maxItem: 8,
    maxItemPerGroup: 6,
    order: "asc",
    hint: true,
    cache: true,
    group: {
        key: "division",
        template: function (item) {

            var division = item.division;
            if (~division.toLowerCase().indexOf('north')) {
                division += " ---> Snow!";
            } else if (~division.toLowerCase().indexOf('south')) {
                division += " ---> Beach!";
            }

            return division;
        }
    },
    display: ["name", "city", "division"],
    dropdownFilter: [{
        key: 'conference',
        template: '<strong>test</strong> Conference',
        all: 'All Conferences'
    }],
    template: '<span>' +
    '<span class="name">test</span>' +
    '<span class="division">test test test</span>' +
    '<span class="team-logo">' +
    '<img src="/assets/jquerytypeahead/img/hockey_v1/{{img}}.gif">' +
    '</span>' +
    '</span>',
    correlativeTemplate: true,
    source: [{
        id: 1,
        author: "john",
        display: "item1"
    }, {
        id: 2,
        author: "eric",
        display: "item2"
    }, {
        id: 3,
        author: "carter",
        display: "item3"
    }]
});
var PATHNAME = window.location.pathname; // Returns path only
var URL_LOCATION = window.location.href;     // Returns full URL

$('#handle_login').click(function () {
    $('.error_form_elearning').remove();
    var username = $('#username_login').val();
    var password = $('#password_login').val();
    console.log(username + '   ' + password);
    var data = {
        username: username,
        password: password
    };
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: 'login',
        type: 'POST',
        data: data,
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", token);
            }
        },
        success: function (data) {
            console.log(data);
            if (data['result'] == 'successful') {
                $('#login-modal').modal('hide');
                change_status(data['account_name']);

            } else if (data['result'] == 'error') {
                $('.error_form_elearning').remove();
                var text = document.createTextNode('Username or password is wrong');
                var h4 = document.createElement('h5');
                $(h4).addClass('error_form_elearning');
                $(h4).css('color', 'red');
                h4.appendChild(text);
                var login_form = document.getElementById('login_form');
                var login_popup = document.getElementById('login_popup');
                login_popup.insertBefore(h4, login_form);
            }
        },
        error: function (err) {

        }
    })
});
function change_status(username) {
    $('#form_login_logout').empty();
    var ul = document.createElement('UL');
    $(ul).addClass('nav navbar-nav navbar-right');
    var li1 = document.createElement('LI');
    var a = document.createElement('a');
    $(a).attr('href', '#');
    var span = document.createElement('span');
    $(span).addClass('glyphicon glyphicon-user');
    var text = document.createTextNode(' Hi, ' + username);
    a.appendChild(span);
    a.appendChild(text);
    li1.appendChild(a);
    ul.appendChild(li1);
    var top_menu = document.getElementById('top_menu_elearning');
    // top_menu.appendChild(ul);

    var li2 = document.createElement('LI');
    var a2 = document.createElement('a');
    $(a2).attr('href', 'logout');
    var span2 = document.createElement('span');
    $(span2).addClass('glyphicon glyphicon-log-out');
    var text2 = document.createTextNode(' Logout');
    a2.appendChild(span2);
    a2.appendChild(text2);
    li2.appendChild(a2);
    ul.appendChild(li2);
    top_menu.appendChild(ul);
}
$('#handle_registry').click(function () {
    $('.error_form_elearning').remove();
    var username = $('#username_registry').val();
    var account_name = $('#account_registry').val();
    var password = $('#password_registry').val();
    var repassword = $('#repass_registry').val();
    var gmail = $('#gmail_registry').val();
    var registry_popup = $('#registry_popup').val();
    console.log(repassword + '   ' + password);
    if (password !== repassword) {
        $('.error_form_elearning').remove();
        var text = document.createTextNode('repassword is wrong');
        var h4 = document.createElement('h5');
        $(h4).addClass('error_form_elearning');
        $(h4).css('color', 'red');
        h4.appendChild(text);
        var registry_form = document.getElementById('registry_form');
        registry_form.insertBefore(h4, repass_registry);
    } else {
        data = {
            username: username,
            password: password,
            account_name: account_name,
            email: gmail
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
                if (data['result'] == 'successful') {
                    $('#logout-modal').modal('hide');
                    change_status(data['account_name']);

                }
            },
            error: function (error) {
                console.log('error');
            }

        })
    }

});
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
