// Lógica interactiva para la Landing Page MUHM Precompra Inteligente

function switchReportTab(tabId) {
  // Desactivar todos los botones
  const buttons = document.querySelectorAll('.tab-btn');
  buttons.forEach(btn => btn.classList.remove('active'));

  // Desactivar todos los contenidos
  const contents = document.querySelectorAll('.report-tab-content');
  contents.forEach(content => content.classList.remove('active'));

  // Activar el seleccionado
  const targetContent = document.getElementById(tabId);
  if (targetContent) {
    targetContent.classList.add('active');
  }

  // Activar botón correspondiente
  event.currentTarget.classList.add('active');
}

function openImageModal(imgSrc) {
  const modal = document.getElementById('imageModal');
  const modalImg = document.getElementById('modalImg');
  modal.style.display = 'block';
  modalImg.src = imgSrc;
}

function closeImageModal() {
  const modal = document.getElementById('imageModal');
  modal.style.display = 'none';
}

function toggleFaq(button) {
  const item = button.parentElement;
  const answer = button.nextElementSibling;
  
  const isOpen = item.classList.contains('open');

  // Cerrar todos los demás
  document.querySelectorAll('.faq-item').forEach(el => {
    el.classList.remove('open');
    el.querySelector('.faq-answer').style.maxHeight = null;
  });

  if (!isOpen) {
    item.classList.add('open');
    answer.style.maxHeight = answer.scrollHeight + 'px';
  }
}

// Cerrar modal con tecla Escape
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeImageModal();
  }
});
