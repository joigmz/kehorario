$(function(){
    $( 'input[type="checkbox"]' ).prop('checked', false);
});

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("wrapper").style.width = "100vw";
}
  
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("wrapper").style.width = "0vw";
    document.body.style.backgroundColor = "white";
}