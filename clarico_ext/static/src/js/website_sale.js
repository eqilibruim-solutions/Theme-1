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
    	

    	$('.mobile_filters').on('click', function(ev){
        if ($('.filter_section').is(':visible')){
            $('.filter_section').css('display', 'none')
        }
        else{
            $('.filter_section').css('display', 'block')
        }
    });

    $('.custom_search').keypress(function (e) {
       if(e.which == 13){
            e.preventDefault()
            $('.oe_search_button_inherited').trigger("click");
       }
     });

    //ON FILTER CLICK
    $('.fcat, .fbrand, .oe_search_button_inherited').on('click', function(ev){
            var cats = []
            var brands = []
            var search_f = $('.custom_search').val()
            $('input:checkbox.fcat').each(function () {
                if (this.checked){
                    var id = $(this).val()
                    cats.push(id)
                }
            });

            $('input:checkbox.fbrand').each(function () {
                if (this.checked){
                    var id = $(this).val()
                    brands.push(id)
                }
            });

		    $.ajax({
            url : '/shop_filters',
            type : 'GET',
            data: { 'cats': JSON.stringify(cats), 'brands': JSON.stringify(brands), 'search_f': search_f },
            async : false,

            }).done(function(resp){
                var html_object = $($.parseHTML(resp));
                //$('.o_wsale_products_grid_table_wrapper').html(html_object.find('.o_wsale_products_grid_table_wrapper'))
                $('#products_grid').html(html_object.find('#products_grid'))
                $('.pagination.m-0.mt-2.ml-md-2').html(html_object.find('.pagination.m-0.mt-2.ml-md-2'))
                $('.pagination.m-0').html(html_object.find('.pagination.m-0'))
            });//done

    });



    	//ONCHANGE OF UoM VIEW PRICE ACCORDINGLY
    	$('.uom_id1').on('change', function(ev){
    		var base_price = $(this).parents('.uom_sel1').find('.base_price').text()
    		var price_ele = $(this).parents('.oe_product_cart').find('.o_wsale_product_information').find('.product_price').find('.oe_currency_value')
    		ajax.jsonRpc('/get_uom_price', 'call', {price: base_price, uom: $(this).val()}).then(function (data) {
                var result = JSON.parse(data);
                price_ele.text(result.price)
            });
    	});
    	
    	
    	//ONCHANGE OF UoM VIEW PRICE ACCORDINGLY
    	$('#uom_id').on('change', function(ev){
    		
    		var base_price = $('.base_price').text()
    		var price_ele = $(this).parents('.js_main_product').find('.oe_price_h4').find('.oe_currency_value')
    		ajax.jsonRpc('/get_uom_price', 'call', {price: base_price, uom: $(this).val()}).then(function (data) {
                var result = JSON.parse(data);
                price_ele.text(result.price)
            });
    	});
    	
    	
    	
    	
    /*	//TO MAKE MENU BAR WHITE COLOR WHEN SCROLLED DOWN
    	$(window).scroll(function() {
		  if ($(".affixed").length > 0){
			  $(".bg-light")[0].style.setProperty( 'background-color', 'white', 'important' );
			  $(".bg-light")[0].style.setProperty( 'box-shadow', '-46px 10px 53px 3px #888888', 'important' );
		  }
		  
		  else{
			  $(".bg-light")[0].style.setProperty( 'background-color', '#e8d6d6ad', 'important' );
			  $(".bg-light")[0].style.setProperty( 'box-shadow', '', 'important' );
		  }
		});*/
    	
    //ON CLICK FUNCTION FOR QUICK ADD CART ICON
        $('#products_grid').on('click', '#quick-add-razzos', function(event){
            //DIFFERENT STYLE CLICK EVENT TO BE WORK FOR DYNAMICALLY ADDED CONTENTS WITH CONSTANT ELEMENT products_grid
            var self = $(this);
//            self.find('.fa-shopping-cart').css('color', '#007bff');
//            self.find('.fa-shopping-cart').css('font-size', '22px');

            var product_id = $(this).attr('data-id');
            var product_qty = $(this).parent('.css_quantity').find('.quantity').val();
            var unit_id = $(this).parents('.o_wsale_product_information').find('.uom_id1').val();


            $.ajax({
                url : "/quick_add_product_razzos",
                data: { id: product_id, qty: product_qty, unit: unit_id},

                success : function(data) {
                    var data1 = JSON.parse(data);
                    $('.o_wsale_my_cart').removeClass('d-none');
	                $('.my_cart_quantity').text(data1.count+"");
                },
                fail: function(data){
                },
            });
        });


});
    
    


});