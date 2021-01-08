odoo.define('clarico_ext.website_sale', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var d = new Date();



    if ( $('.te_header_style_1_main').length > 0 ){
        
        $('.te_header_style_1_main').find('.img-fluid').css('width', '200px')
        $('.te_header_style_1_main').find('.img-fluid').css('height', '200px')
        
    }
    
    
    
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

    
    
    
    function check_exist_class1(e){
        var self = this;
        setTimeout(function() {
            if ($(".img-fluid-equal").length > 0){
            	$('.img-fluid-equal').find('.img-fluid').css('min-height', '140px')
            	$('.img-fluid-equal').find('.img-fluid').css('max-height', '140px')
            }
            else{
            	check_exist_class1();
            }
            
        }, 100);
    }
    
    
    $(document).ready(function() {
    	
    	check_exist_class1();
    	
    	
    	//ONCHANGE OF UoM VIEW PRICE ACCORDINGLY
    	$('#uom_id').on('change', function(ev){
    		var base_price = $('.base_price').text()
    		var price_ele = $(this).parents('.o_wsale_product_information').find('.o_wsale_product_information_text').find('.product_price').find('.oe_currency_value')
    		ajax.jsonRpc('/get_uom_price', 'call', {price: base_price, uom: $(this).val()}).then(function (data) {
                var result = JSON.parse(data);
                price_ele.text(result.price)
            });
    	});
    	
    	
    	
    	
    	//TO MAKE MENU BAR WHITE COLOR WHEN SCROLLED DOWN
    	$(window).scroll(function() {
		  if ($(".affixed").length > 0){
			  $(".bg-light")[0].style.setProperty( 'background-color', 'white', 'important' );
			  $(".bg-light")[0].style.setProperty( 'box-shadow', '-46px 10px 53px 3px #888888', 'important' );
		  }
		  
		  else{
			  $(".bg-light")[0].style.setProperty( 'background-color', '#e8d6d6ad', 'important' );
			  $(".bg-light")[0].style.setProperty( 'box-shadow', '', 'important' );
		  }
		});
    	
    	
    	
    	
    });
    
    


});