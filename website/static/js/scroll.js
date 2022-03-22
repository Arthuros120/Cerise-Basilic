//Get the button
var ScrollBtn = document.getElementById("ScrollBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    ScrollBtn.style.display = "table";
  } else {
    ScrollBtn.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  $("html, body").animate( { scrollTop: 0 }, 750);
  document.documentElement.scrollTop = 0;
}