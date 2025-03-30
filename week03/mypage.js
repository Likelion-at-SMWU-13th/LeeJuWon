function saveOneliner() {
    const input = document.getElementById('onelinerInput').value.trim();
    if (!input) return;
  
    const today = new Date();
    const dateStr = `${today.getMonth() + 1}월 ${today.getDate()}일`;
  
    const data = {
      text: input,
      date: dateStr
    };
  
    localStorage.setItem('oneliner', JSON.stringify(data));
    updateOnelinerDisplay(data);
    document.getElementById('onelinerInput').value = "";
  }
  
  function updateOnelinerDisplay(data) {
    document.getElementById('onelinerDate').textContent = `💬 ${data.date}`;
    document.getElementById('onelinerText').textContent = data.text;
  }
  
  window.onload = function () {
    const saved = localStorage.getItem('oneliner');
    if (saved) {
      const data = JSON.parse(saved);
      updateOnelinerDisplay(data);
    }
  };
  