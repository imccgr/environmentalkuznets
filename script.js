//Code for slideshow
let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls (switch to diff slides)
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

//function show slides to be able to skip through slides
function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none"; //display correct slide
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

// Code for sidebar
function w3_open() {
  document.getElementById("mySidebar").style.display = "block";
}
 //code to close the sidebar
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
}