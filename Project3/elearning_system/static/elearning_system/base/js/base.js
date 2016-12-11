/**
 * Created by huynhduc on 11/12/2016.
 */

var pagination = $('.pagination_btn');
pagination.click(function () {
   var self = $(this);
    $('.pagination_btn').removeClass('active');
    self.addClass('active');
});