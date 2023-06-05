$(document).ready(function() {


  if($('#selected_class').text() == "") {
    // $('#course_select').hide();
    $('#course_select').css('opacity', '0.5');
    $('#course_select').css('pointer-events', 'none');
    $('#course_select').css('filter', 'grayscale(100%)');
  }




  var courses_selected = [];

  $("#test_button").click(function() {
    for (let index = 0; index < 6; index++) {
      courses_selected[index] = $('.datalist'+index).map(function() {
        return $(this).val();
      }).get();      
    }
    console.log($('#'));  
  });

  $("#submit_timetable").click(function() {
    let selected_courses = [];
    
    for (let index = 0; index < 6; index++) {
      selected_courses[index] = $('.datalist'+index).map(function() {
        return $(this).val();
      }).get();        
    }
    
    let csrftoken = getCookie('csrftoken');
      $.ajax({
        method: 'POST',
        url: '/staff/grade/confirmar/', 
        data: {
          'selected_courses': JSON.stringify(selected_courses),
          'selected_class': $('#selected_class').text(),
        },
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function(response) {
          window.location.href = '/staff/grade/confirmar/';
        },
        error: function(xhr, status, error) {
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