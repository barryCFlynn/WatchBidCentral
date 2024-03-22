document.addEventListener("DOMContentLoaded", function() {
    var likeButtons = document.querySelectorAll(".like-btn");

    likeButtons.forEach(button => button.addEventListener("click", function() {
        var listingId = this.getAttribute("data-listing-id");
        fetch("/like_listing/" + listingId)
        .then(response => response.json())
        .then(data => {
            document.querySelector("#likes-count-" + listingId).textContent = data.likes;
        })
        .catch(error => console.error("Error:", error));
    }));
});