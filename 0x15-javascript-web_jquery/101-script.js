$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').prepend('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list > li:first-child').remove();
  });
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list li').remove();
  });
});
