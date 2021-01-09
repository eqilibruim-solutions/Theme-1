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
    	
    	
    	
    	function setupReader(file, id, field, done) {
    		if (file){
	            var name = file.name;
	            var file_datas = [];
	            var reader = new FileReader();  
	            reader.readAsDataURL(file);
	            
	            reader.onload = function(e) {  
	                file_datas.push([file.name, e.target.result]);
	                ajax.jsonRpc("/page/submit_enroll_images", 'call', {
	                					bin_data : file_datas[0][1],
	                					'id': id,
	                					'field': field,
	                					'done': done,
	                             })
	                
	            };
    		}
    	}
            
            
            
    	$('.tab-5-next').on('click', function(ev){
    		
    		$('.loadclass').addClass("loading-submit");
    		
    		var formData = $('#new-form').serializeArray();
			
    		

			ajax.jsonRpc('/page/submit_enroll_action', 'call', {'data' : formData})
			.then(function (data) {
                var result = JSON.parse(data);
                if (result.created != 0){
                	setupReader($('.signature_whole')[0].files[0], result.created, 'signature_whole', 'no');

                	setupReader($('.client_signature')[0].files[0], result.created, 'client_signature', 'no');
                	setupReader($('.client_name_customer_bank_off_sig')[0].files[0], result.created, 'client_name_customer_bank_off_sig', 'no');
                	
                	setupReader($('.aggreement_bottom_signature')[0].files[0], result.created, 'aggreement_bottom_signature', 'no');
                	
                	setupReader($('.signature_deal')[0].files[0], result.created, 'signature_deal', 'no');
                	
                	setupReader($('.signature_po_customer')[0].files[0], result.created, 'signature_po_customer', 'yes');
                	
                }
            });
			
			
			setTimeout(
			  function() 
			  {
				  window.location.replace("/page/enrolled")
				  
			  }, 3000);
			
			
    		
    	});
    	
    	
    });


});


