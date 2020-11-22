odoo.define('clarico_ext.website_sale', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var d = new Date();


    
    if ( sessionStorage.getItem("plus18") + "" == "0" || sessionStorage.getItem("plus18") + "" == 'undefined' || sessionStorage.getItem("plus18") + "" == 'null') {
        $('#plus18').show();
    }



    $('#byear').keyup(function(event) {

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
                sessionStorage.setItem("plus18", "1");;
                $('#plus18').hide();
            }
        }
    });


    $('#bmont').keyup(function(event) {

        var year = $('#byear').val()
        var month = $('#bmonth').val()
        var day = $('#bday').val()

        if (year.length == 4 && month.length == 2 && day.length == 2) {

            var dateString = month + "/" + day + "/" + year;
            var dateObject = new Date(dateString);
            var diff = new Date(d - dateObject);
            var days = diff / 1000 / 60 / 60 / 24;
            days = days / 365;
            if (days > 18) {
                sessionStorage.setItem("plus18", "1");;
                $('#plus18').hide();
            }
        }

    });


    $('#byear').keyup(function(event) {

        var year = $('#byear').val()
        var month = $('#bmonth').val()
        var day = $('#bday').val()

        if (year.length == 4 && month.length == 2 && day.length == 2) {

            var dateString = month + "/" + day + "/" + year;
            var dateObject = new Date(dateString);
            var diff = new Date(d - dateObject);
            var days = diff / 1000 / 60 / 60 / 24;
            days = days / 365;
            if (days > 18) {
                sessionStorage.setItem("plus18", "1");;
                $('#plus18').hide();
            }
        }

    });





});