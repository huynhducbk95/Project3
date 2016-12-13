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