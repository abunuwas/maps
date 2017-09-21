function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
    });
    var bounds = new google.maps.LatLngBounds();
    var infowindow = new google.maps.InfoWindow();
      for (let pos of markers) {
        var marker = new google.maps.Marker({
        position: new google.maps.LatLng(pos),
        map: map,
        title: 'Hello, Venice!'
      });
      bounds.extend(marker.position);
    }
    google.maps.event.addListenerOnce(map, 'idle', function() {
      map.fitBounds(bounds);
      //map.setZoom(13);
    });
}

// https://stackoverflow.com/questions/15719951/google-maps-api-v3-auto-center-map-with-multiple-markers

