document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".lion-option button");
    const result = document.getElementById("vote-result");
  
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        localStorage.setItem("lion_vote", btn.dataset.id);
        result.style.display = "block";
        result.textContent = `투표 감사합니다! (${btn.dataset.id}) 🧡`;
      });
    });
  });
  