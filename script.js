document.getElementById("searchBtn").addEventListener("click", () => {
  showToast("Search triggered");
});

document.querySelectorAll(".accept").forEach((btn) => {
  btn.addEventListener("click", () => showToast("Accepted successfully!"));
});

document.querySelectorAll(".reject").forEach((btn) => {
  btn.addEventListener("click", () => showToast("Rejected!"));
});

function showToast(message) {
  const toast = document.getElementById("toast");
  toast.textContent = message;
  toast.classList.remove("hidden");

  setTimeout(() => {
    toast.classList.add("hidden");
  }, 3000);
}

// Theme toggle
const toggle = document.getElementById("themeToggle");
toggle.addEventListener("click", () => {
  document.body.classList.toggle("light");
  localStorage.setItem(
    "theme",
    document.body.classList.contains("light") ? "light" : "dark"
  );
});

// Load theme
window.addEventListener("DOMContentLoaded", () => {
  const saved = localStorage.getItem("theme");
  if (saved === "light") {
    document.body.classList.add("light");
  }
});
