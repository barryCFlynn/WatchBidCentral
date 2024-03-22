document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("show-bid-form").addEventListener(
        "click", function() {
        var bidForm = document.getElementById("bid-form");
        if (bidForm.style.display === "none") {
            bidForm.style.display = "block";
        } else {
            bidForm.style.display = "none";
        }
    });
});