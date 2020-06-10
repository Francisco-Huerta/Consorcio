
// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/farmacias',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        filterer: function(numeroComuna, nombreFarmacia) {
            let ajax_options = {
                type: 'POST',
                url: 'api/farmacias',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'numeroComuna': numeroComuna,
                    'nombreFarmacia': nombreFarmacia
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },

        'comunas': function(){
            let ajax_options = {
                type: 'GET',
                url: 'api/comunas',
                accepts: 'application/json',
                contentType: 'text/html; charset=UTF-8',
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_charge_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
        
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $numeroComuna = $('#numeroComuna'),
        $nombreFarmacia = $('#nombreFarmacia');
    // return the API
    return {
        build_select: function(comunas) {
            console.log(comunas);
            if (comunas) {
                $("#mySelect").append(comunas);
                console.log($('#mySelect'))
            }
        },
        build_table: function(farmacias) {
            let rows = ''

            // Limpiamos la tabla
            $('.people table > tbody').empty();

            // Revisamos si tenemos la lista de farmacias
            if (farmacias) {
                for (let i=0, l=farmacias.length; i < l; i++) {
                    rows += `<tr><td class="numeroComuna">${farmacias[i].local_nombre}</td><td class="nombreFarmacia">${farmacias[i].local_direccion}</td><td>${farmacias[i].local_telefono}</td><td>${farmacias[i].local_lat}</td><td>${farmacias[i].local_lng}</td></tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        // $numeroComuna = $('#numeroComuna'),
        $nombreFarmacia = $('#nombreFarmacia');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
        model.comunas();
    }, 100)


    // Create our event handlers
    $('#filterer').click(function(e) {
        let numeroComuna = $('#mySelect').find(":selected")[0].value,
            nombreFarmacia = $nombreFarmacia.val();
        e.preventDefault();

        model.filterer(numeroComuna, nombreFarmacia)
    });
    $('#reset').click(function() {
        view.reset();
    })

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
    });

    $event_pump.on('model_charge_success', function(e, data) {
        view.build_select(data);
    });
    

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    });
}(ns.model, ns.view));