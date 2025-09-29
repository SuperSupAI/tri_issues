function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    document.getElementById('latitude').value = position.coords.latitude;
    document.getElementById('longitude').value = position.coords.longitude;
    document.getElementById('latitude_out').value = position.coords.latitude;
    document.getElementById('longitude_out').value = position.coords.longitude;

}

window.onload = getLocation;  // Call getLocation when the page loads