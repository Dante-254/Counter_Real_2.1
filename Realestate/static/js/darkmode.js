document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("darkModeToggle");
    const body = document.body;

    if (!toggleButton) return;

    function updateButtonIcon() {
        const icon = toggleButton.querySelector('.dark-mode-icon');
        if (icon) {
            if (body.classList.contains("dark-mode")) {
                icon.textContent = "☀️";
            } else {
                icon.textContent = "🌙";
            }
        }
    }

    // Load dark mode setting from local storage
    const savedMode = localStorage.getItem("darkMode");
    if (savedMode === "enabled") {
        body.classList.add("dark-mode");
    } else if (savedMode === null) {
        // Check system preference if no saved preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            body.classList.add("dark-mode");
            localStorage.setItem("darkMode", "enabled");
        } else {
            localStorage.setItem("darkMode", "disabled");
        }
    }
    
    updateButtonIcon();

    toggleButton.addEventListener("click", function () {
        body.classList.toggle("dark-mode");

        if (body.classList.contains("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
        } else {
            localStorage.setItem("darkMode", "disabled");
        }

        updateButtonIcon();
    });
});
