window.onload = function () {
    function update_trackdata() {
        $.getJSON("/get_madlibs/", function (data) {
            var div_data = "";
            $.each(data, function (i, data) {
                div_data += data;
            });
            $("#app").empty();
            $("#app").append(div_data);
        });
        $.getJSON("/get/madlib/gamemaster/", function (data) {
            var div_data = "";
            $.each(data, function (i, data) {
                div_data += data;
            });
            $("#gm-app").empty();
            $("#gm-app").append(div_data);
        });
        $.getJSON("/current/word/", function (data) {
            var div_data = "";
            $.each(data, function (i, data) {
                div_data += data;
            });
            $("#c_word").empty();
            $("#c_word").append(div_data);
        });
        $.getJSON("/current/winner/", function (data) {
            var div_data = "";
            $.each(data, function (i, data) {
                div_data += data;
            });
            $("#winner").empty();
            $("#winner").append(div_data);
        });
        return false;
    }

    update_trackdata();

    var interval = setInterval(update_trackdata, 2000);
}
