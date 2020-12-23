odoo.define('jetmaster_website_customizations.ProductEnquiryCustom', function (require) {
"use strict";


    $(document).ready(function() {
        
        // Select all links with hashes
$('a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function(event) {
    // On-page links
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
      && 
      location.hostname == this.hostname
    ) {
      // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      // Does a scroll target exist?
      if (target.length) {
        // Only prevent default if animation is actually gonna happen
        event.preventDefault();
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000, function() {
          // Callback after animation
          // Must change focus!
          var $target = $(target);
          $target.focus();
          if ($target.is(":focus")) { // Checking if the target was focused
            return false;
          } else {
            $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
            $target.focus(); // Set focus again
          };
        });
      }
    }
  });
        
  // Complete Anchor link smooth funcnality      
     
        
        
        $("div.free_standing_type").hide();
        $("input[name$='unit-type']").click(function() {
            var test = $(this).val();
//            console.log("test:::::::::::::;",test)
            if (test == "free_standing_type")
            {
                $("div.inbuilt_type").hide();
                $("#" + test).show();
            }
            else
            {
                $("div.free_standing_type").hide();
                $("#" + test).show();
                $('#inbuilt_type1').show();
            }

        });


      $(".gallery-popup_view").click(function (){
    //       alert("IN POPUP")
           var gallery_image = $(this).attr('data-gallery-image')
           var prod_id = $(this).attr('data-product_id')
           var product_slug_url = $(this).attr('data_product_slug_url')
           document.getElementById("gallery_image_popup").src = 'data:image/png;base64,' + gallery_image
           $("#gallery_product_id").val(prod_id)
           document.getElementById("view_more_product").href = product_slug_url;
      })


      $(".promocode_message").click(function(){
            if($('#promo-code').val() != '' )
            {
               alert("Promo code added successfully")
            }
            else
            {
                alert("Add a promo code")
            }
      })

    });
    
    $(document).ready(function() {

    
/*--jQuery('#phonenumber').keyup(function() {
       if (this.value.match(/[^0-9]/g)) {
      this.value = this.value.replace(/[^0-9]/g, '');
    }
   });--*/     
    
// START Product Enquiry Validation     
  $('#addproduct_enquiry').click(function(e) {

    e.preventDefault();
    var first_name = $('#first_name').val();
    var last_name = $('#last_name').val();
    var streetaddress = $("#streetaddress").val();
    var addressline_2 = $("#addressline_2").val();
    var city = $("#city").val();
    var state_region = $("#state_region").val();
    var zip_code = $("#state_region").val();
    var phonenumber = $("#phonenumber").val();
    var email = $("#email").val();  
    


    $(".error").remove();

    if (first_name.length < 1) {
      $('.name-errormsg').show();
        $('.name-section').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }

    if (last_name.length < 1) {
      $('.name-errormsg').show();
        $('.name-section').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }
      
    if (streetaddress.length < 1 ) {
      $('.addressdiv-errormsg').show();
         $('.full_addesssec').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }
      
      
        if (addressline_2.length < 1) {
      $('.addressdiv-errormsg').show();
        $('.full_addesssec').addClass("error-section");
            $('.main-validation_error').show();
            return false
    }  
      
      
      if (city.length < 1) {
      $('.addressdiv-errormsg').show();
          $('.full_addesssec').addClass("error-section");
          $('.main-validation_error').show();
          return false
    }  
      
      
      if (state_region.length < 1) {
      $('.addressdiv-errormsg').show();
          $('.full_addesssec').addClass("error-section");
          $('.main-validation_error').show();
          return false
    }  
      
      
      if (zip_code.length < 1) {
      $('.addressdiv-errormsg').show();
         $('.full_addesssec').addClass("error-section");
          $('.main-validation_error').show();
          return false
    }
      
      
      
      
      if (phonenumber.length < 1) {
      $('.phone-errormsg').show();
         $('.phone_section').addClass("error-section");
          $('.main-validation_error').show();
          return false
    } 
      
      
      if (email.length < 1) {
        $('.email-errormsg').show();
         $('.email_section').addClass("error-section");
          $('.main-validation_error').show();
          $('#email').after('<span class="error">This field is required</span>');
          return false
      }
   
    /*if (email.length < 1) {
      $('#email').after('<span class="error">This field is required</span>');
      return false
    }
      
      else {
      var regEx = /^[A-Z0-9][A-Z0-9._%+-]{0,63}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/;
      var validEmail = regEx.test(email);
      if (!validEmail) {
        $('#email').after('<span class="error">Enter a valid email</span>');
        return false
      }
    }*/

    $('#first_form').submit();
       return true

  });
        
// END Product Enquiry Validation 
        
        
        
    $("#what-service-required").change(function() {
        if ($(this).data('options') === undefined) {
            $(this).data('options', $('#fireplace-model option').clone());
        }

        var id = $(this).val();
//        alert(id)
        if (id != "")
        {
            var options = $(this).data('options').filter('[data-input-id=' + id + ']');
            $('#fireplace-model').html(options);
            $('#fireplace-model-div').css('display','block');
        }
        else
        {
            $('#fireplace-model-div').css('display','none');
        }

    });

$('#fireplace-model-div').css('display','none');
        
$('#bookservice_first_name').change(function() {
    $('#bookservice_details_fname').val($(this).val());
});
        
$('#bookservice_last_name').change(function() {
    $('#bookservice_details_lname').val($(this).val());
});        
        
// START Book a Service Validation         
        
    $('#bookaservice-submit').click(function(e) {
//    alert("Rohit");
    e.preventDefault();
    var bookservice_first_name = $('#bookservice_first_name').val();
    var bookservice_last_name = $('#bookservice_last_name').val();
    var bookservice_address = $("#bookservice_address").val();
    var bookservice_suburb = $("#bookservice_suburb").val();
    var bookservice_contact = $("#bookservice_contact").val();
    var bookservice_email = $("#bookservice_email").val();
    var bookservice_details_fname = $("#bookservice_details_fname").val();    
    
    $(".error").remove();    
        
    if (bookservice_first_name.length < 1) {
      $('.name-errormsg').show();
        $('.bookservice-namesection').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }

    if (bookservice_last_name.length < 1) {
      $('.name-errormsg').show();
        $('.bookservice-namesection').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }
        
     if (bookservice_address.length < 1) {
      $('.name-errormsg').show();
        $('.bookservice-addresssection').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }     
        
        
     if (bookservice_suburb.length < 1) {
      $('.name-errormsg').show();
        $('.bookservice-suburbsection').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }   
      
        
     if (bookservice_contact.length < 1) {
      $('.name-errormsg').show();
        $('.bookservice-contactsection').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }   
        
    if (bookservice_email.length < 1) {
      $('.name-errormsg').show();
        $('.bookservice-emailsection').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }
        
        
    if (jQuery('#condition1, #condition2, #condition3, #condition4 ').is(":not(:checked)")) {
      $('.name-errormsg').show();
        $('.termscondition-sec').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }
        

                
    /*    
     if (jQuery('#condition1').is(":not(:checked)")) {
                    alert('Please check Terms and Conditions');
                    return false
                }
        
        if (jQuery('#condition2').is(":not(:checked)")) {
                    alert('Please check Terms and Conditions');
                    return false
                }
        
        if (jQuery('#condition3').is(":not(:checked)")) {
                    alert('Please check Terms and Conditions');
                    return false
                }
        
       if (jQuery('#condition4').is(":not(:checked)")) {
                    alert('Please check Terms and Conditions');
                    return false
                } 
        */
        
       $('#book_service_form_id').submit();
           return true
        
        
});        
 // END Book a Service Validation       
        
        
        
        
        
 // START Contact Details Validation
 $('#addcontact_details').click(function(e) {
    e.preventDefault();
    var contact_name = $('#contact_name').val(); 
    var contact_email = $('#contact_email').val(); 
    var contact_phone = $('#contact_phone').val(); 
     
  if (contact_name.length < 1) {
      $('.name-emailmsg').show();
        $('.name_emailsec').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }
      
    if (contact_email.length < 1) {
      $('.name-emailmsg').show();
        $('.name_emailsec').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }
      
     
    if (contact_phone.length < 1 ) {
      $('.phone_postcodemsg').show();
         $('.phone_postcodesec').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }

    $('#contact_us_form_id').submit();
       return true
     

 });
       
 // END Contact Details Validation  
        
        
 /*=============== Gallery popup Validation ======*/       

$('#addgallery_query').click(function(e) {
//    alert("IN GALLERY")
    e.preventDefault();
    var gallery_name = $('#gallery-name').val(); 
    var gallery_email = $('#gallery-email').val(); 
    var gallery_phone = $('#gallery-phone').val(); 

  if (gallery_name.length < 1) {
      $('.name-validatemsg').show();
        $('.name-gallerysec').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }
      
    if (gallery_email.length < 1) {
      $('.email-validatemsg').show();
        $('.email-gallerysec').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }
      
     
    if (gallery_phone.length < 1 ) {
      $('.phone-validatemsg').show();
         $('.phone-gallerysec').addClass("error-section");
        $('.main-validation_error').show();
        return false
    }

     $('#gallery_queries_form_id').submit();
        return true
 
 });       
        

$('.phone').on('keypress', function(e) {
  var key = e.charCode || e.keyCode || 0;
  var phone = $(this);
  if (phone.val().length === 0) {
    phone.val(phone.val() + '(');
  }
  // Auto-format- do not expose the mask as the user begins to type
  if (key !== 8 && key !== 9) {
    if (phone.val().length === 4) {
      phone.val(phone.val() + ')');
    }
    if (phone.val().length === 5) {
      phone.val(phone.val() + ' ');
    }
    if (phone.val().length === 9) {
      phone.val(phone.val() + '-');
    }
    if (phone.val().length >= 14) {
      phone.val(phone.val().slice(0, 13));
    }
  }

  // Allow numeric (and tab, backspace, delete) keys only
  return (key == 8 ||
    key == 9 ||
    key == 46 ||
    (key >= 48 && key <= 57) ||
    (key >= 96 && key <= 105));
})


});

})
