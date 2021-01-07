odoo.define('clarico_ext.enroll', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var d = new Date();



    $(document).ready(function() {

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
    	
    	
    });


});