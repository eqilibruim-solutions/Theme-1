odoo.define('quick_order.website_sale', function (require) {
  "use strict";
  /* Copyright (c) 2018-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
  /* See LICENSE file for full copyright and licensing details. */
  var ajax = require('web.ajax');
  var core = require('web.core');
  var QWeb = core.qweb;
  
  
  
  $(document).ready(function() {
  	
  	
  	//ONCHANGE OF UoM VIEW PRICE ACCORDINGLY
  	$('.uom_id_quick').on('change', function(ev){
  		var base_price = $(this).parents('.uom_sel2').find('.base_price').text()
  		var price_ele = $(this).parents('tr').find('.oe_currency_value')
  		ajax.jsonRpc('/get_uom_price', 'call', {price: base_price, uom: $(this).val()}).then(function (data) {
              var result = JSON.parse(data);
              price_ele.text(result.price)
          });
  	});

  	$('.js_minus_cart_json_quick').on('click', function(ev){
  		var current = $(this).parents('.quick_qty2').find('.quantity').val()
  		current = parseInt(current)
  		if (current > 1){
  		    $(this).parents('.quick_qty2').find('.quantity').val((current - 1)+"")
  		}
  	});

  	$('.js_plus_cart_json_quick').on('click', function(ev){
  		var current = $(this).parents('.quick_qty2').find('.quantity').val()
  		current = parseInt(current)
  		$(this).parents('.quick_qty2').find('.quantity').val((current + 1)+"")
  	});

  });


});
