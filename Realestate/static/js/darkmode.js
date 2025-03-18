document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("darkModeToggle");
    const body = document.body;

    function updateButtonText() {
        if (body.classList.contains("dark-mode")) {
            toggleButton.textContent = "☀️ Light Mode";
        } else {
            toggleButton.textContent = "🌙 Dark Mode";
        }
    }

    // Load dark mode setting from local storage
    if (localStorage.getItem("darkMode") === "enabled") {
        body.classList.add("dark-mode");
    }
    updateButtonText(); // Set the initial button text

    toggleButton.addEventListener("click", function () {
        body.classList.toggle("dark-mode");

        if (body.classList.contains("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
        } else {
            localStorage.setItem("darkMode", "disabled");
        }

        updateButtonText(); // Update button text after toggling
    });
});
