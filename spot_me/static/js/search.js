"use strict";

var map = null;
var infowindow = null;
var markers = [];

var populateMap = function(geoPosition, term) {
  $("#geolocation").hide();

  infowindow = new google.maps.InfoWindow({
    content: "hello"
  });

  var position = geoPosition;
  if (!position) {
    position = defaultPosition;
  }

  map = new google.maps.Map(document.getElementById("map"), {
    center: {
      lat: position.coords.latitude,
      lng: position.coords.longitude
    },
    zoom: 16
  });

  var windowOptions = {
    pixelOffset: {
      height: -32,
      width: 0
    }
  };


var geolocationFail = function() {
  populateMap(defaultPosition);
};

var initMap = function() {
  if (navigator.geolocation) {
    var location_timeout = setTimeout(geolocationFail, 5000);

    navigator.geolocation.getCurrentPosition(
      function(position) {
        clearTimeout(location_timeout);
        populateMap(position);
      },
      function(error) {
        clearTimeout(location_timeout);
        geolocationFail();
      }
    );
  } else {
    // Fallback for no geolocation
    geolocationFail();
  }
};

var clearMarkers = function(markers) {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
  markers = [];
};

