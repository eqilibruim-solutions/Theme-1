odoo.define('clarico_ext.website_sale', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var d = new Date();



    if ( $('.te_header_style_1_main').length > 0 ){
        
        $('.te_header_style_1_main').find('.img-fluid').css('width', '200px')
        $('.te_header_style_1_main').find('.img-fluid').css('height', '200px')
        
    }
    
    
    console.log(sessionStorage.getItem("plus18"), 'KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK')
    
    if ( sessionStorage.getItem("plus18") + "" == "0" || sessionStorage.getItem("plus18") + "" == 'undefined' || sessionStorage.getItem("plus18") + "" == 'null') {
        $('#plus18').show();
        $('#bmonth').focus();
    }


    
    function do_process(e){
    
        var year = $('#byear').val();
        var month = $('#bmonth').val();
        var day = $('#bday').val();
        if (year.length == 4 && month.length == 2 && day.length == 2) {

            var dateString = month + "/" + day + "/" + year;
            var dateObject = new Date(dateString);
            var diff = new Date(d - dateObject);
            var days = diff / 1000 / 60 / 60 / 24;
            days = days / 365;
            if (days > 18) {
                sessionStorage.setItem("plus18", "1");
                $('#plus18').hide();
            }
        }
    
    }

    $('#bday').keyup(function(event) {
        if ( $('#bday').val().length == 2 )
        {
            $('#byear').focus();
        }
        do_process();
    });


    $('#bmonth').keyup(function(event) {
        if ( $('#bmonth').val().length == 2 )
        {
            $('#bday').focus();
        }
        do_process();
    });


    $('#byear').keyup(function(event) {
        do_process();
    });





});