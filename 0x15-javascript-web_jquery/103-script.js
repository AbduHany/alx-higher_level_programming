$(document).ready(function () {
  function translate () {
    const lang = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
  $('INPUT#btn_translate').on('click', function () {
    translate();
  });
  $('INPUT#language_code').on('keypress', function (key) {
    if (key.which === 13) {
      translate();
    }
  });
});
