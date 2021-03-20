odoo.define('sale_web2.website_sale', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var d = new Date();

    $(document).ready(function() {
    	$('.no-minimum-amount, .no-minimum-amount2').on('click', function(ev){
    	    var self = this
    	    var min_amount = parseFloat($('#class_order_min_amount').val())
    	    var current_amount = parseFloat($('#order_total').find('.oe_currency_value').text().replace(',', ''))
            if (current_amount < min_amount ){
                $('.min_class').css('display', 'block')
            }
            else{
                $('#amount_matched').attr("href", "/shop/checkout?express=1")
                $('#amount_matched')[0].click()
            }
        });

        $('.close_btn').on('click', function(ev){
            $('.min_class').css('display', 'none')
        });



    });



});