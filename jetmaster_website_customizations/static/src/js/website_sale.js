odoo.define('jetmaster_website_customizations.WebsiteSaleInherit', function (require) {
"use strict";

$(document).ready(function(){

//        $(".show_quantity").css('visibility', 'hidden');
//        $(".show_minus_div").css('visibility', 'hidden');

//      $('.plus_button').click(function(){
//           var atribut_show = $(this).attr('data-product_show');
////           console.log(atribut_show)
//            $('.show_minus_div[data-product_hide="'+atribut_show+'"]').css('visibility', 'visible');
//            $('.show_quantity[data-product-id="'+atribut_show+'"]').css('visibility', 'visible');
//      })
//
//      $('.show_minus_div').click(function(){
//           var atribut_hide = $(this).attr('data-product_hide');
////           console.log(atribut_hide)
//           var curt_qty = $('.show_quantity[data-product-id="'+atribut_hide+'"]').val() - 1;
////           console.log("curt_qty",curt_qty)
//           if (curt_qty == 0)
//           {
//            $('.show_minus_div[data-product_hide="'+atribut_hide+'"]').css('visibility', 'hidden');
//            $('.show_quantity[data-product-id="'+atribut_hide+'"]').css('visibility', 'hidden');
//
//           }
//      })
//
      $('.add_all_items_in_cart').click(function(){
            var cart_prod_lst= [];
            $('.check_product_id').find('input').each(function()
            {
                if($(this).attr('name') == 'add_qty')
                {
                    if($(this).val() != '' && $(this).val() != 0)
                    {
                         var add_qty = $(this).val()
                         var product_id = $(this).data('product-id');
                         cart_prod_lst.push({product_id: product_id, add_qty : add_qty})

                    }
                }
            });

            if(cart_prod_lst.length != 0){
                var value = {'cart_lst' : JSON.stringify(cart_prod_lst)}

                $.ajax({
                    url : "/add_all_selected_items_to_cart",
                    data : value,
                    cache : "false",
                }).then(function (res) {
                    location.href = '/shop/cart';
                })
                .fail(function(){
                    alert("Unable to process the request!!!")
                })
            }

      })

});

});