window.addEventListener('pageshow', function (event) {
  hide_loading()
});

$(document).ready(function () {

  if ($('#selected_class').text() == "") {
    $('#course_select').css('opacity', '0.5');
    $('#course_select').css('pointer-events', 'none');
    $('#course_select').css('filter', 'grayscale(100%)');
  }

  var courses_selected = [];

  $("#test_button").click(function () {
    for (let index = 0; index < 6; index++) {
      courses_selected[index] = $('.datalist' + index).map(function () {
        return $(this).val();
      }).get();
    }
    console.log($('#'));
  });

  $("#submit_timetable").click(function () {
    show_loading();

    let selected_courses = [];

    for (let index = 0; index < 6; index++) {
      selected_courses[index] = $('.datalist' + index).map(function () {
        let value = $(this).val().trim(); // Remover espaços em branco antes e depois
        console.log(value);
        return value;
      }).get();
    }

    console.log("for acabado");
    alert($("#selected_class").text());

    let csrftoken = getCookie('csrftoken');
    $.ajax({
      method: 'POST',
      url: window.location.href,
      data: {
        'selected_courses': JSON.stringify(selected_courses),
        'selected_class': $('#selected_class').text()
      },
      headers: {
        'X-CSRFToken': csrftoken
      },
      success: function (response) {

        if (response.erro) {
          $('#mensagem-erro').show();
          $('#mensagem-erro').text(response.mensagem).show();
          hide_loading();
        } else {
          console.log(response);
          show_loading();
          window.location.href = "/staff/grade/ver/?class=" + $('#selected_class').text();
        }
      },
      error: function (xhr, status, error) {
        console.log(error);
      }
    });
  });

});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function show_loading() {
  $('body').css('opacity', '0.5');
  $('.spinner-border').show();
}

function hide_loading() {
  $('body').css('opacity', '1');
  $('.spinner-border').hide();
}