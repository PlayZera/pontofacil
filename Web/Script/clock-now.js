function updateClock() {
    const now = new Date();
    const timeElement = document.getElementById('time');
    const dateElement = document.getElementById('date');
  
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    const date = now.toLocaleDateString();
  
    const timeString = `${hours}:${minutes}:${seconds}`;
    timeElement.textContent = timeString;
    dateElement.textContent = date;
  }
  
  // Atualizar o relógio a cada segundo
  setInterval(updateClock, 1000);
  
  // Iniciar o relógio ao carregar a página
  updateClock();
  
  