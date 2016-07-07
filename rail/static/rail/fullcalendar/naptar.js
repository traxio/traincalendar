$(document).ready(function() {
    var obiektum = new Object;
    var ob_lista = [];
    console.log("valami1")
    /*
    jQuery.ajax({
            url: "http://127.0.0.1:8000/naptar/",
            type: "GET",

            contentType: 'application/json; charset=utf-8',
            success: function(info) {
                //here is your json.
                  // process it
                console.log("valami2")
                for (var numero = 0;numero < info.length;numero++) {
                    var fromdb = info[numero];
                    obiektum = {
                        "id":fromdb.id,
                        "start":moment(fromdb.indulas_ido),
                        "end":moment(fromdb.indulas_ido).add(3, 'hours'),
                        "allDay":false,
                        "editable":true};
                }
                ob_lista.push(obiektum);
            },
            error : function(jqXHR, textStatus, errorThrown) {
            },

            timeout: 120000,
    });


    */
	$.getJSON(album_src, function(info){
        console.log("valami2")
		for (var numero = 0;numero < info.length;numero++) {
            var fromdb = info[numero];
            obiektum = {
                "id":fromdb.id,
                "title":fromdb.vnev,
                "start":moment(fromdb.indulas_ido),
                "end":moment(fromdb.indulas_ido).add(3, 'hours'),
                "allDay":false,
                "editable":true};
		    ob_lista.push(obiektum);
		}
		console.log(ob_lista)
	}).then(function(){
        console.log("valami3")
        $('#calendar').fullCalendar({
            header: {
				left: 'prevYear,nextYear prev,next today',
				center: 'title',
				right: 'month,agendaWeek,agendaDay'
			},
			lang: 'hu',
			eventSources: [

                ob_lista

            ],
			//events: infoarray,
			'':.5
        })
    })
});