const msg = document.querySelector(".welcome-msg");
const btn1 = document.querySelector("#search-addon");
const btn2 = document.querySelector("#refresh");
const home = document.querySelector("#title");

btn1.addEventListener("click", hide);
btn2.addEventListener("click", hide);
home.addEventListener("click", unhide);

if (localStorage.getItem("hiddenClass") === "hidden") {
  msg.classList.add("hidden");
}

btn1.addEventListener("click", hide);
btn2.addEventListener("click", hide);

function hide() {
  localStorage.setItem("hiddenClass", "hidden");
  location.reload();
}

function unhide() {
  localStorage.clear();
  location.reload();
}
