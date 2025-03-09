document.querySelector("#create_room_inp").addEventListener("click", function() {
    document.querySelector(".popup-container").classList.add("active");
    document.querySelector(".popup-overlay").classList.add("active");
});
document.querySelector(".popup-close-btn").addEventListener("click", function() {
    document.querySelector(".popup-container").classList.remove("active");
    document.querySelector(".popup-overlay").classList.remove("active");
});
