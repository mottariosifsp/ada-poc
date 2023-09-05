var json_data = document.currentScript.getAttribute("jsonData");
json_data = decodeURIComponent(JSON.parse('"' + json_data + '"'));
// console.log("Json data", JSON.parse(json_data));

$(document).ready(function () {

    $('#classs-container').hide();

    var jsonData = JSON.parse(json_data);
    var json_array = Array.isArray(jsonData) ? jsonData : [jsonData];

    $('.area').click(function () {

        // Marca o selecionado
        $('.area').removeClass('selected');
        $(this).addClass('selected');

        var registrationAreaId = $(this).data('registration_area_id');

        var filteredData = json_array.filter(function (object) {
            return object.registration_area_id === registrationAreaId;
        });

        $('#classs-container').empty();

        filteredData.forEach(function (object) {
            var classs = $('<div class="classs"></div>').text(object.registration_class_id);
            let isUpdating = false;

            classs.click(function () {
                var registration_class_id = $(event.target).text().trim();

                var url = "/professor/ver/?registration_class_id=" + registration_class_id;
                window.location.href = url;

            });

            $('#classs-container').append(classs);
        });

        $('#classs-container').show();
    });
});