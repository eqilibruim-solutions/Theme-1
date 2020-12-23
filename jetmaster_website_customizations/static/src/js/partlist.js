odoo.define('jetmaster_website_customizations.partlist', function(require){
	'use strict';

	function partListRequest(product_id){

		var formatted_table = null;

			$.ajax({
			url : '/get_partlist_data',
			data : {'product_id': product_id},
			async : false
		}).done(function(response){
			 let parsed_response = JSON.parse(response)
			let formatted_table_start = `
			<div class="container">
			<center><h2>Partlist</h2></center>
			<div class="row">
				<div class="col-md-12">
					<center>
						<img class="img-responsive" src="data:image/png;base64,${parsed_response.exploded_view}"/>
					</center>
				</div>




			<div class="col-md-12 partlist-table">
			<table border="1" width="100%">
<thead class="thead-dark">
			<tr>
				<th>Ref N	o.</th>
				<th>Item Title</th>
				<th>Item Comment</th>
				<th>Item Part Number</th>
				<th></th>
			</tr>
</thead>`
			let table_data = ''

			for(let i=0; i<parsed_response.data.length; i++){

				table_data += `<tr>
				<td>${parsed_response.data[i].item_no}</td>
				<td>${parsed_response.data[i].item_title}</td>
				<td>${parsed_response.data[i].item_comment}</td>
				<td>${parsed_response.data[i].item_partno}</td>
				<td><form id="partlist_frm" action="/update_partlist_in_cart" method="POST">
				        <input type="hidden" name="csrf_token" t-att-value="request.csrf_token()"/>
				        <input type="hidden" class="product_id" name="product_id" value="${parsed_response.data[i].product_id}"/>
				        <input type="hidden" name="partlist_ordering"/>
						<input type="number" name="add_qty" value="1"/>
						${parsed_response.data[i].child_bom_id ? '<input type="button" id="btnPartlist" value="Partlist" class="btn btn-primary"/>' : '<input type="submit" class="btn btn-primary" value="Add to Cart"/>'}
					</form>
				</td>
				</tr>
				`
			}
			let formatted_table_end = `</table></div></div></div>`
			formatted_table = formatted_table_start + table_data + formatted_table_end;

	});
		return formatted_table
	}//partlistRequest

	$("#btn_partlist_show").click(function(){

			$("body,html").animate(
		      {
		        scrollTop: $("#partlist_data").offset().top
		      },
		      700 //speed
		    );
			let product_id = $(this).attr('data')

			let formatted_table = partListRequest(product_id)
			$("#partlist_data").html(formatted_table)

			document.getElementById("btnPartlist").addEventListener ("click", showPartList, false);

			function showPartList() {
				let product_id = $(this)[0].form[1].value
				let table_response = partListRequest(product_id)
				$('#partlistModal').find('.modal-body').html(table_response)
				$('#partlistModal').find('.modal-header').empty()
				$("#partlistModal").modal()


			}

		});

});
