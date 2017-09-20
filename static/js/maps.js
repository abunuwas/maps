function initMap() {
var map = new google.maps.Map(document.getElementById('map'), {
  zoom: 1,
  center: center
});
var bounds = new google.maps.LatLngBounds();
var infowindow = new google.maps.InfoWindow();
for (var i=0, l=markers.length; i<l; i++) {
  var pos = markers[i];
  console.log(pos);
  var marker = new google.maps.Marker({
    position: new google.maps.LatLng(markers[i][1], markers[i][2]),
    map: map,
    title: 'Hello, Venice!'
  });
  bounds.extend(marker.position);
  google.maps.event.addListener(marker, 'click', (function(marker, i) {
    return function() {
    infowindow.setContent(locations[i][0]);
    infowindow.open(map, marker);
  })(marker, i));
}
}
map.fitBounds(bounds);

