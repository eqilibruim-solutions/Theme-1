odoo.define('jetmaster_website_customizations.LocationCustom', function (require) {
"use strict";

//alert("HELLO")
var map;
var infoWindow = new google.maps.InfoWindow();
var geocoder = new google.maps.Geocoder();
var partner_markers_arr =[]
var markers_on_map = [];
var start_loc = "210 Elizabeth St, Melbourne VIC 3000, Australia"
var positionOption = { timeout: 500, enableHighAccuracy: true };
var start_lat =-37.8136276;
var start_lng =144.9630576;


var address_icon = {
    url: '/jetmaster_website_customizations/static/src/images/address_marker.png', // url
    scaledSize: new google.maps.Size(50, 50), // scaled size
    origin: new google.maps.Point(0,0), // origin
    anchor: new google.maps.Point(0, 0) // anchor
};

var dealers_icon = {
    url: '/jetmaster_website_customizations/static/src/images/dealers_markers.png', // url
    scaledSize: new google.maps.Size(50, 50), // scaled size
    origin: new google.maps.Point(0,0), // origin
    anchor: new google.maps.Point(0, 0) // anchor
};


$(document).ready(function(){

    initialize();
//    get_current_location()
    $('.no_results').css('display', 'none')
    $('.show_all_dealers').css('display', 'none')

    $('.search_dealers').click(function (){

//        $('#show_all_dealers_default').css('display', 'none')
        $('.no_results').css('display', 'none')
        $('.no_results').empty()

        var coords ={}
         var address = $('#searchpostcode').val();
         setTimeout(function(i){
          geocoder.geocode( { 'address': address}, function(results, status) {

          if (status == google.maps.GeocoderStatus.OK) {
            var latitude = results[0].geometry.location.lat();
            var longitude = results[0].geometry.location.lng();
            coords['lat']=results[0].geometry.location.lat();
            coords['lng']=results[0].geometry.location.lng();
            showDealersLocations(coords, address);
           }
           else
           {
                alert("Something went wrong!!!!!!")
           }
        })
        },1000);
    });

    $(document).on("click", ".view_on_map_location", function() {
//        alert("view on map")
        var partner_id = $(this).attr('data-partner_id')
        var index = partner_markers_arr.findIndex(partner_markers_arr => partner_markers_arr.partner === parseInt(partner_id))
//        console.log("INDEX::::::::::::::;",index,partner_id)
        if(index != -1)
        {
           google.maps.event.trigger(partner_markers_arr[index].marker, 'click');

        }
        else
        {
            alert('Something went wrong!!!!!!!!!')
        }
    })
});

    function initialize(){
       var input = document.getElementById('searchpostcode');
       var autocomplete = new google.maps.places.Autocomplete(input);
       var partners_arr1 = []

       var latlng = new google.maps.LatLng(start_lat,start_lng);
          var myOptions = {
            zoom: 2,
            center: latlng,
            mapTypeControl: true,
            mapTypeControlOptions: {style: google.maps.MapTypeControlStyle.DROPDOWN_MENU},
            navigationControl: true,
            mapTypeId: google.maps.MapTypeId.ROADMAP
          };
          map = new google.maps.Map(document.getElementById("direction-map"), myOptions);

          var start_loc_marker = new google.maps.Marker({
                            position: latlng,
                            map: map,
                            icon:address_icon,
                            title: "Start Location",
                        });

          markers_on_map.push(start_loc_marker)
          var result_search = $('#result_limit').val();
          var value ={'result_search':result_search}

         $.ajax({
            url : "/get_all_dealers_location",
            data: value,
            cache : "false",
        }).then(function (res) {
            var result = JSON.parse(res)
            var res_partners = result['partners']
            for (var j = 0; j < res_partners.length; j++) {
                (function (partner) {
                  var marker_lat_lng = new google.maps.LatLng(partner.lat, partner.lng);
                  var new_marker = new google.maps.Marker({
                            position: marker_lat_lng,
                            map: map,
                            icon:dealers_icon,
                            title: partner.name,
                        });
//                        console.log("NEW MARKER",new_marker)
                        var directions_link;
                         var addr = partner.street + ',' + partner.city + ',' + partner.state + ',' +partner.country + ',' + partner.zip;
//
                        directions_link ="http://maps.google.com/maps/dir/"+start_loc+'/'+ addr
                         var contentString = '<div id="gmap-content">'+
                                '<div id="gmap-siteNotice">'+
                                '</div>'+
                                '<h2 id="gmap-firstHeading" class="gmap-firstHeading">'+partner.name+'</h2>'+
                                '<div id="gmap-bodyContent">'+
                                    '<p><b>Address</b>:<br>' + partner.address +
                                        '<br>'+
                                         '<p><b>Phone</b>: ' + partner.phone +
                                        '<br>'+
                                        '<strong><a href="'+directions_link+'" title="Get Directions" target="_blank">Directions</a></strong><br>'+
                                    '</p>'+
                                    '<div class="clear clearfix"></div>'+
                                '</div>'+
                                '</div>';
                        google.maps.event.addListener(new_marker, 'click', function () {
                            infoWindow.setContent(contentString);
                            infoWindow.open( map, new_marker );
                        });
                        partner_markers_arr.push({partner: partner.id, marker : new_marker})
                        markers_on_map.push(new_marker);
                        partners_arr1.push(res_partners[j])


                })(res_partners[j]);
             }
//               console.log("ALL PARTNERS",partners_arr1)
            if(partners_arr1.length >= 1)
            {
                $.each(partners_arr1, function(i){ //Loop the array
                    var partner = partners_arr1[i]
                    var html = '<li>'+
                                    '<div class="wpsl-store-location">'+
                                        '<p>'+
                                            '<strong>'+partner.name+'</strong>'+
                                            '<span class="wpsl-street">'+partner.street + '</span>' +
                                            '<span class="wpsl-street">' + partner.city + '</span>' +
                                            '<span class="wpsl-street">' + partner.zip + '</span>' +
                                        '</p>'+
                                        '<p class="wpsl-contact-details">'+
                                               '<span><strong>Phone</strong>: ' + partner.phone + '</span>' +
                                        '</p>'+
                                        '<p>'+
                                            '<a class="wpsl-store-details view_on_map_location" id="view_on_map_location" href="#"'+
                                            'data-partner_id='+partner.id+'>view on map'+
                                            '</a>'+
                                        '</p>'+
                                    '</div>'+
                                '</li>';
//                    var html = '<li data-store-id="'+partner.id+'"><div class="wpsl-store-location"><p>' +partner.address+'</p>'
//                    html += '<p class="wpsl-contact-details"><span><strong>Phone</strong>:'+partner.phone+'/></span></p>'
//                    html += '<p><a class="psl-store-details view_on_map_location" id="view_on_map_location" data-partner_id='+ partner.id +' href="#">view on map</a></p></div></li>'
                    $('.show_all_dealers ul').append(html);
                    $('.show_all_dealers').css('display', 'block')

                })
            }
            else
            {
                $('.show_all_dealers ul').empty();
                $('.no_results').append("<p><strong><center>No Results Found</center></strong></p>");
                $('.show_all_dealers').css('display', 'none')
                $('.no_results').css('display', 'block')

            }

         })

    }

    function showDealersLocations(coords,address)
    {
//        alert("IN showDealersLocations")
        var i;
        var radius_km = $('#radius_km').val();
        var result_search = $('#result_limit').val();

        for (i = 0; i < markers_on_map.length; i++) {
            if (markers_on_map[i]) {
                markers_on_map[i].setMap(null);
                markers_on_map[i] = null;
            }
        }

        partner_markers_arr = []
        var partners_arr= [];

        var address_lat_lng = new google.maps.LatLng(coords.lat,coords.lng);
        var address1 = $('#searchpostcode').val();

        var address_marker = new google.maps.Marker({
                position: address_lat_lng,
                map: map,
                icon : address_icon,
                title: "Start Location",
            });

        markers_on_map.push(address_marker)


         var value ={'result_search':result_search,'address':address1}
         $.ajax({
            url : "/get_all_dealers_location",
            data: value,
            cache : "false",
        }).then(function (res) {
            var result = JSON.parse(res)
            var res_partners = result['partners']
            for (var j = 0; j < res_partners.length; j++) {
                (function (partner) {
//                    console.log("partnerS",partner.lat, partner.lng)
                    var marker_lat_lng = new google.maps.LatLng(partner.lat, partner.lng);
                    var distance_from_location = google.maps.geometry.spherical.computeDistanceBetween(address_lat_lng, marker_lat_lng); //distance in meters between your location and the marker
//                    console.log("distance_from_location",distance_from_location)
//                    console.log("RADIUS",radius_km,radius_km * 1000)
                    if (distance_from_location <= radius_km * 1000) {
                        var new_marker = new google.maps.Marker({
                            position: marker_lat_lng,
                            map: map,
                            icon:dealers_icon,
                            title: partner.name,
                        });
                        var addr = partner.street + ',' + partner.city + ',' + partner.state + ',' +partner.country + ',' + partner.zip;
                         var contentString = '<div id="gmap-content">'+
                                '<div id="gmap-siteNotice">'+
                                '</div>'+
                                '<h2 id="gmap-firstHeading" class="gmap-firstHeading">'+partner.name+'</h2>'+
                                '<div id="gmap-bodyContent">'+
                                    '<p><b>Address</b>:<br>' + partner.address +
                                        '<br>'+
                                         '<p><b>Phone</b>: ' + partner.phone +
                                        '<br>'+
                                        '<strong><a href="http://maps.google.com/maps/dir/'+ address +'/'+ addr +'" title="Get Directions" target="_blank">Directions</a></strong><br>'+
                                    '</p>'+
                                    '<div class="clear clearfix"></div>'+
                                '</div>'+
                                '</div>';
                        google.maps.event.addListener(new_marker, 'click', function () {
//                            alert(partner.name + " is " + distance_from_location + " meters from my location");
                             infoWindow.setContent(contentString);
                            infoWindow.open( map, new_marker );
                        });
                        markers_on_map.push(new_marker);
                        partner_markers_arr.push({partner: partner.id, marker : new_marker})
                        partners_arr.push(res_partners[j])
                    }
                })(res_partners[j]);
            }
//            console.log("ALL PARTNERS",partners_arr)
            if(partners_arr.length >= 1)
            {
                $('.show_all_dealers ul').empty();
                $.each(partners_arr, function(i){ //Loop the array
                    var partner = partners_arr[i]
                    var html = '<li>'+
                                    '<div class="wpsl-store-location">'+
                                        '<p>'+
                                            '<strong>'+partner.name+'</strong>'+
                                            '<span class="wpsl-street">'+partner.street + '</span>' +
                                            '<span class="wpsl-street">' + partner.city + '</span>' +
                                            '<span class="wpsl-street">' + partner.zip + '</span>' +
                                        '</p>'+
                                        '<p class="wpsl-contact-details">'+
                                               '<span><strong>Phone</strong>: ' + partner.phone + '</span>' +
                                        '</p>'+
                                        '<p>'+
                                            '<a class="wpsl-store-details view_on_map_location" id="view_on_map_location" href="#"'+
                                            'data-partner_id='+partner.id+'>view on map'+
                                            '</a>'+
                                        '</p>'+
                                    '</div>'+
                                '</li>';
//                    var html = '<li data-store-id="'+partner.id+'"><div class="wpsl-store-location"><p>' +partner.address+'</p>'
//                    html += '<p class="wpsl-contact-details"><span><strong>Phone</strong>:'+partner.phone+'/></span></p>'
//                    html += '<p><a class="psl-store-details view_on_map_location" id="view_on_map_location" data-partner_id='+ partner.id +' href="#">view on map</a></p></div></li>'
                    $('.show_all_dealers ul').append(html);
                    $('.show_all_dealers').css('display', 'block')

                })
            }
            else
            {
                $('.show_all_dealers ul').empty();
                $('.no_results').append("<p><strong><center>No Results Found</center></strong></p>");
                $('.show_all_dealers').css('display', 'none')
                $('.no_results').css('display', 'block')

            }

        })
    }

    function draw_map(current_location, zoom) {
        var $def2 = $.Deferred();
        var current_lat = 0.0//40.41729;
        var current_lng = 0.0//-82.90712;
        if (current_location) {
            current_lat = current_location['lat'];
            current_lng = current_location['lng'];
        }
//        alert("IN HEREEEEEEE")
        var region = new google.maps.LatLng(current_lat, current_lng);
        map = new google.maps.Map(document.getElementById("direction-map"), {
            zoom: zoom,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            center: region,
        });
        $def2.resolve(map);
        return $def2;
    }


    function codeLatLng(lat, lng) {
      var latlng = new google.maps.LatLng(lat, lng);
      geocoder.geocode({
        'latLng': latlng
      }, function (results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
          if (results[0])
          {
//            console.log(results[0].formatted_address);
            alert(results[0].formatted_address)
            return results[0].formatted_address
          }
          else {
            console.log('No results found');
            return false
          }
        } else {
          console.log('Geocoder failed due to: ' + status);
          return false
        }
      });
    }

     function get_current_location() {
//        alert("HEREEEEEEEEEEEE")
        var latlng = new google.maps.LatLng(start_lat,start_lng);
         var myOptions = {
            zoom: 2,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
          };
          map = new google.maps.Map(document.getElementById("direction-map"), myOptions);
          infoWindow = new google.maps.InfoWindow();

          if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position){
                const pos = {
                  lat: position.coords.latitude,
                  lng: position.coords.longitude
                };
//                map.setCenter(pos);
                var locations = {'lat':position.coords.latitude,'lng':position.coords.longitude}
//                console.log("LOCATIONS",locations)
                showDealersLocations(locations)
              },
              () => {
                handleLocationError(true, infoWindow, map.getCenter());
              }
            );
          } else {
            // Browser doesn't support Geolocation
            handleLocationError(false, infoWindow, map.getCenter());
          }
     }



     function handleLocationError(browserHasGeolocation,infoWindow,pos) {
      infoWindow.setPosition(pos);
      infoWindow.setContent(
        browserHasGeolocation
          ? "Error: The Geolocation service failed."
          : "Error: Your browser doesn't support geolocation."
      );
      infoWindow.open(map);
    }




});

