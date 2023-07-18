var current_language = document.currentScript.getAttribute('data-lang');
var timeslots = []
var cell_left_number = 0
var cell_type_choosed = 0
var cell_situation = "not_checked" 

var user_blocks = document.currentScript.getAttribute('blocks');
var user_timetables = document.currentScript.getAttribute('timetables');
var timeslot_minutes = document.currentScript.getAttribute('variation_minutes');

$(document).ready(function() {
  $('.custom-icon').css('display', 'none');
  $('.cel-plus').css('display', 'none');

  //console.log("timeslot minutos", timeslot_minutes);

  $('input[name="regime"]').click(function() {
    $('#cel-regime').val('');
    var value = $(this).val();
    if (value == 'rde' || value == '40') {
      var this_duration = 24*60/timeslot_minutes;
      $('#cel-regime').text(this_duration);
      cell_left_number = this_duration
      cell_type_choosed = 40;
      cell_situation = "not_checked"
      $('.checkbox input[type="checkbox"]').prop('checked', false);
      $('label.checkbox').removeClass('active');
      timeslots = []
    } else {
      var this_duration = 12*60/timeslot_minutes;
      $('#cel-regime').text(this_duration);
      cell_left_number = this_duration
      cell_type_choosed = 20;
      cell_situation = "not_checked"
      $('.checkbox input[type="checkbox"]').prop('checked', false);
      $('label.checkbox').removeClass('active');
      timeslots = []
    }

    if ($('#error-alert-form').is(':visible')) {
      $('#error-alert-form').hide();
      $('label[for^="mon-"]').add('label[for^="tue-"]').add('label[for^="wed-"]').add('label[for^="thu-"]').add('label[for^="fri-"]').add('label[for^="sat-"]').removeClass('disabled').removeAttr('aria-disabled');
      $('input[type="checkbox"][id^="mon-"]').add('input[type="checkbox"][id^="tue-"]').add('input[type="checkbox"][id^="wed-"]').add('input[type="checkbox"][id^="thu-"]').add('input[type="checkbox"][id^="fri-"]').add('input[type="checkbox"][id^="sat-"]').prop('disabled', false);
    }

    $('tbody.block').find('*').css({
      "background-color": "",
      "color": "",
      "font-weight": ""
    });

    $('thead.block').find('*').css({
      "background-color": "",
      "color": "",
      "font-weight": ""
    });

    $('.custom-icon').css('display', 'none');
    $('.cel-plus').css('display', 'none');
    $('.cel').css('display', '');
  });

  // Limpar formulário inteiro
  $('#clean-fpa').click(function() {
    $('input[name="regime"]').prop('checked', false);
    $('.checkbox input[type="checkbox"]').prop('checked', false);
    $('label.checkbox').removeClass('active');
    $('#cel-regime').text("--");
    $('#error-alert-form').hide();

    window.scrollTo({
      top: $('#error-alert-form').offset().top - $('.navbar').outerHeight() - 30,
      behavior: 'smooth'
    });

    timeslots.length = 0;
    cell_left_number = 0;
  });

  // Pegar dados dos checkboxes
  $('.checkbox').click(function() {
    if(cell_left_number == 0 && cell_type_choosed == 0) {
      block_options();
    } else {
      var input_id = $(this).attr('for');
      var input_val = $('#' + input_id).val();
      var button_is_checked = $('#' + input_id).prop('checked');

      if(button_is_checked) {
        cell_left_number += 1;
        var [input_object, input_day] = input_val.split(',');
        var [timeslot_begin_hour, timeslot_end_hour] = input_object.split('-');

        if (cell_situation == "checked") {
          //pode causar conflito com regra de 8 horas e 11 
          $('input[type="checkbox"][id^="mon-"], input[type="checkbox"][id^="tue-"], input[type="checkbox"][id^="wed-"], input[type="checkbox"][id^="thu-"], input[type="checkbox"][id^="fri-"], input[type="checkbox"][id^="sat-"]').each(function() {
            if (!$(this).prop('checked')) {
              $(this).prop('disabled', false);
              $('label[for="' + $(this).attr('id') + '"]').removeClass('disabled').removeAttr('aria-disabled');
            }
          });
          cell_situation = "not_checked"
          cell_left_number += 1

          $('#error-alert-form').hide();
        }

        var index = timeslots.findIndex(function(lesson) {
          return lesson.id === input_id;
        });
        
        if (index !== -1) {
          timeslots.splice(index, 1);
        }

        var [id_day, id_period, id_timeslot] = input_id.split('-');

        $('#period-' + id_period).css({
          "background-color": "",
          "color": "",
          "font-weight": ""
        });
        $('#timeslot-' + id_period + '-' + id_timeslot).css({
          "background-color": "",
          "color": "",
          "font-weight": ""
        });
        $('#day_of_week-' + id_day).css({
          "background-color": "",
          "color": "",
          "font-weight": ""
        });

        if(cell_left_number < 0) {
          var positive_value = Math.abs(cell_left_number)
          $('#cel-regime').text('+'+positive_value);
          $('.custom-icon').css('display', '');
          $('.cel-plus').css('display', '');
          $('.cel').css('display', 'none');
        } else {
          $('#cel-regime').text(cell_left_number);
          $('.custom-icon').css('display', 'none');
          $('.cel-plus').css('display', 'none');
          $('.cel').css('display', '');
        }
      } else {
        if(cell_situation != "checked") {
          update_cell_left_number(button_is_checked);
          if (cell_situation != "checked") {
            var [input_object, input_day] = input_val.split(',');
            var [timeslot_begin_hour, timeslot_end_hour] = input_object.split('-');
            var lesson = {
              id: input_id,
              timeslot_begin_hour: timeslot_begin_hour,
              timeslot_end_hour: timeslot_end_hour,
              day_of_week: input_day,
            };

            timeslots.push(lesson) // mon-mor-1
          }
        }
      }
    }
  });

  // Enviar formulário inteiro
  $('#send-disponibility').click(function() {
    var user_regime =  $('input[name="regime"]:checked').val();
    var json_data = JSON.stringify(timeslots);

    let csrftoken = get_cookie('csrftoken');

    if (user_regime && timeslots.length !== 0) {
      if(cell_left_number <= 0) {
        $.ajax({
          type: 'post',
          url: '/' + current_language + '/professor/preferencia-atribuicao/criar-fpa/editar-cursos/',
          data: {
            user_regime: user_regime,
            user_timeslots: json_data
          },
          headers: {
            'X-CSRFToken': csrftoken
          },
          success: function(response) {
            $('input[name="regime"]:checked').prop('checked', false);
            $('#error-alert-form').hide();
            window.location.href = '/' + current_language + '/professor/preferencia-atribuicao/criar-fpa/editar-cursos/'
          },
          error: function(xhr, status, error) {
            $('#error-message-form').text('Ocorreu um erro no envio de FPA.');
            $('#error-alert-form').show();
            window.scrollTo({
              top: $('#error-alert-form').offset().top - $('.navbar').outerHeight() - 30,
              behavior: 'smooth'
            });
          }
        });
      } else {
        $('#error-message-form').text('Por favor insira todas as células.');
        $('#error-alert-form').show();
        window.scrollTo({
          top: $('#error-alert-form').offset().top - $('.navbar').outerHeight() - 30,
          behavior: 'smooth'
        });
      }
    } else {
      $('#error-message-form').text('Insira as informações pedidas em cada seção.');
      $('#error-alert-form').show();
      window.scrollTo({
        top: $('#error-alert-form').offset().top - $('.navbar').outerHeight() - 30,
        behavior: 'smooth'
      });
    }
  });

  function get_cookie(name) {
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
});

function period_input(value) {
  var element = document.getElementById("period-" + value);
  var backgroundColor = getComputedStyle(element).backgroundColor;
  var isTrue = backgroundColor == "rgb(80, 124, 117)";
  if(isTrue) {
    take_off_ckecked(value);

    $('#period-' + value).css({
      "background-color": "",
      "color": "",
      "font-weight": ''
    })
  } else {
    if(cell_left_number == 0 && cell_type_choosed == 0) {
      block_options();
      $('#error-message-form').text('Insira o regime de trabalho acrescestar sua disponibilidade.');
    } else {
      $('#period-' + value).css({
        "background-color": "#507c75",
        "color": "white",
        "font-weight": 700
      })

      take_off_ckecked(value);
      put_in_checked(value);
    }
  }
  
}

function timeslot_input(value) {
  var element = document.getElementById("timeslot-" + value);
  var backgroundColor = getComputedStyle(element).backgroundColor;
  var isTrue = backgroundColor == "rgb(80, 124, 117)";
  if(isTrue) {
    take_off_ckecked(value);

    $('#timeslot-' + value).css({
      "background-color": "",
      "color": "",
      "font-weight": ''
    })
  } else {
    if(cell_left_number == 0 && cell_type_choosed == 0) {
      block_options();
      $('#error-message-form').text('Insira o regime de trabalho acrescestar sua disponibilidade.');
    } else {
      $('#timeslot-' + value).css({
        "background-color": "#507c75",
        "color": "white",
        "font-weight": 700
      })

      take_off_ckecked(value);
      put_in_checked(value);
    }
  }
}

function day_of_week_input(value) {
  var element = document.getElementById("day_of_week-" + value);
  var backgroundColor = getComputedStyle(element).backgroundColor;
  var isTrue = backgroundColor == "rgb(80, 124, 117)";
  if(isTrue) {
    take_off_ckecked(value);

    $('#day_of_week-' + value).css({
      "background-color": "",
      "color": "",
      "font-weight": ''
    })
  } else {
    if(cell_left_number == 0 && cell_type_choosed == 0) {
      block_options();
      $('#error-message-form').text('Insira o regime de trabalho acrescestar sua disponibilidade.');
    } else {
      $('#day_of_week-' + value).css({
        "background-color": "#507c75",
        "color": "white",
        "font-weight": 700
      })

      take_off_ckecked(value);
      put_in_checked(value);
    }
  }
  
}

function block_options() {
  $('#cel-regime').text("--");
  $('label[for^="mon-"]').add('label[for^="tue-"]').add('label[for^="wed-"]').add('label[for^="thu-"]').add('label[for^="fri-"]').add('label[for^="sat-"]').addClass('disabled').attr('aria-disabled', 'true');
  $('input[type="checkbox"][id^="mon-"]').add('input[type="checkbox"][id^="tue-"]').add('input[type="checkbox"][id^="wed-"]').add('input[type="checkbox"][id^="thu-"]').add('input[type="checkbox"][id^="fri-"]').add('input[type="checkbox"][id^="sat-"]').prop('disabled', true);

  $('#error-message-form').text('Insira o regime de trabalho antes de continuar.');
  $('#error-alert-form').show();
  window.scrollTo({
    top: $('#error-alert-form').offset().top - $('.navbar').outerHeight() - 30,
    behavior: 'smooth'
  });
}

function take_off_ckecked(value) {
  var checkboxes_checked = Array.from(document.querySelectorAll('input[type="checkbox"]:checked[id*="'+value+'"]')).map(function(checkbox) {
    return checkbox.id;
  });

  for(var i = 0; i < checkboxes_checked.length; i++) {
    var checked_id = checkboxes_checked[i]
    var index = timeslots.findIndex(function(lesson) {
      return lesson.id === checked_id;
    });
    
    if (index !== -1) {
      timeslots.splice(index, 1);
    }

    var checkbox = document.getElementById(checked_id);
    if (checkbox) {
      checkbox.checked = false;
      var button = checkbox.parentElement;
      var label = button.parentElement;
      button.classList.remove("active");
      label.classList.remove("active");
    }

    cell_left_number += 1

    if(cell_left_number < 0) {
      var positive_value = Math.abs(cell_left_number)
      $('#cel-regime').text('+'+positive_value);
      $('.custom-icon').css('display', '');
      $('.cel-plus').css('display', '');
      $('.cel').css('display', 'none');
    } else {
      $('#cel-regime').text(cell_left_number);
      $('.custom-icon').css('display', 'none');
      $('.cel-plus').css('display', 'none');
      $('.cel').css('display', '');
    }
  }
}

function put_in_checked(value) {
  var checkboxes_not_checked = Array.from(document.querySelectorAll('input[type="checkbox"]:not(:checked)[id*="'+value+'"]')).map(function(checkbox) {
    return checkbox.id;
  });

  for(var i = 0; i < checkboxes_not_checked.length; i++) {
    var checked_id = checkboxes_not_checked[i];
    var checked_value = $('#' + checked_id).val();

    update_cell_left_number(false);
    var [checked_object, checked_day] = checked_value.split(',');
    var [timeslot_begin_hour, timeslot_end_hour] = checked_object.split('-');
    var lesson = {
      id: checked_id,
      timeslot_begin_hour: timeslot_begin_hour,
      timeslot_end_hour: timeslot_end_hour,
      day_of_week: checked_day,
    };

    timeslots.push(lesson)

    var checkbox = document.getElementById(checked_id);
    if (checkbox) {
      checkbox.checked = true;
      var button = checkbox.parentElement;
      var label = button.parentElement;
      button.classList.add("active");
      label.classList.add("active");
    }
  }
}

function update_cell_left_number(button_is_checked) {
  if(!button_is_checked) {
    if (cell_situation == "checked") {
      cell_left_number = 0;
      $('#cel-regime').text(cell_left_number);
    } else {
      cell_left_number -= 1;
      if(cell_left_number < 0) {
        var positive_value = Math.abs(cell_left_number)
        $('#cel-regime').text('+'+positive_value);
        $('.custom-icon').css('display', '');
        $('.cel-plus').css('display', '');
        $('.cel').css('display', 'none');
      } else {
        $('#cel-regime').text(cell_left_number);
        $('.custom-icon').css('display', 'none');
        $('.cel-plus').css('display', 'none');
        $('.cel').css('display', '');
      }
    }    
  }
}
