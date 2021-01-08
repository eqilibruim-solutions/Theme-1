odoo.define('clarico_ext.enroll', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var d = new Date();



    $(document).ready(function() {
    	
    	
    	//ONCHANGE OF UoM VIEW PRICE ACCORDINGLY
    	$('.tab-1-next').on('click', function(ev){
    		$('.tab-1').css('display', 'none')
    		$('.tab-2').css('display', 'block')
    	});
    	
    	
    	$('.tab-2-pre').on('click', function(ev){
    		$('.tab-1').css('display', 'block')
    		$('.tab-2').css('display', 'none')
    	});
    	
    	
    	
    	
    	$('.tab-2-next').on('click', function(ev){
    		$('.tab-2').css('display', 'none')
    		$('.tab-3').css('display', 'block')
    	});
    	
    	
    	$('.tab-3-pre').on('click', function(ev){
    		$('.tab-2').css('display', 'block')
    		$('.tab-3').css('display', 'none')
    	});
    	
    	
    	$('.tab-3-next').on('click', function(ev){
    		$('.tab-4').css('display', 'block')
    		$('.tab-3').css('display', 'none')
    	});
    	

    	$('.tab-4-pre').on('click', function(ev){
    		$('.tab-3').css('display', 'block')
    		$('.tab-4').css('display', 'none')
    	});
    	
    	$('.tab-4-next').on('click', function(ev){
    		$('.tab-5').css('display', 'block')
    		$('.tab-4').css('display', 'none')
    	});
    	
    	
    	$('.tab-5-pre').on('click', function(ev){
    		$('.tab-4').css('display', 'block')
    		$('.tab-5').css('display', 'none')
    	});
    	
    	
    	$('.tab-5-next').on('click', function(ev){
    		
    		var formData = $('#new-form').serializeArray();
			
			var signature_whole = $('input[name ="signature_whole"]')[0].files;

			ajax.jsonRpc('/page/submit_enroll_action', 'call', {'data' : formData}).then(function (data) {
                var result = JSON.parse(data);
                alert(result.created);
            });
			
    		
    	});
    	
    	
    });


});


