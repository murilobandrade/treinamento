const btn = document.querySelector(".js-active-menu");
const sidbar = document.querySelector(".sidebar");

if (btn) {
  btn.addEventListener("click", function(e) {
    sidbar.classList.toggle("__active");
    console.log(sidbar.classList)
  })
}

/* Set the width of the sidebar to 250px (show it) */
function openNav() {
  document.getElementById("mainSidepanel").style.width = "250px";
}

/* Set the width of the sidebar to 0 (hide it) */
function closeNav() {
  document.getElementById("mainSidepanel").style.width = "0";
} 