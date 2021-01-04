odoo.define('clarico_ext.enroll', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var d = new Date();



    $(document).ready(function() {
    	
    	$("#new-form").submit(function(){
    		
			var formData = new FormData($(this)[0]);
			
			var signature_whole = $('input[name ="signature_whole"]')[0].files;
    	    alert(signature_whole)[0]
    	    
    	    formData.append("signature_whole", signature_whole[0]);
    	    
    	    ajax.jsonRpc("/page/submit_enroll_action", 'call', {
			                'kwargs' : formData,
			          })
			.then(function (data) {
			      console.log('QQQQQQ')
			});
    	    
    	    
    	});
    	
    	
    	
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
    		
    		$('#new-form').submit()
    		
    	});
    	
    	
    });


});


