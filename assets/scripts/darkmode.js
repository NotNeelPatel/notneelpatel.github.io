var darkMode;
const root = document.querySelector(":root");

window.addEventListener("load", function () {
    if (darkMode == "dark") {
        document.getElementById("darkModeToggle").textContent = "☀️";
    }
});

if (localStorage.getItem("dark-mode")) {
    darkMode = localStorage.getItem("dark-mode");
    root.classList.toggle(darkMode);
} else {
    darkMode = "light";
}

localStorage.setItem("dark-mode", darkMode);

function toggleDarkMode() {
    const toggle = document.getElementById("darkModeToggle");
    if (toggle.textContent == "🌙") {
        toggle.textContent = "☀️";
        localStorage.setItem("dark-mode", "dark");
        root.classList.remove("light");
        root.classList.add("dark");
    } else {
        toggle.textContent = "🌙";
        localStorage.setItem("dark-mode", "light");
        root.classList.remove("dark");
        root.classList.add("light");
    }
}
