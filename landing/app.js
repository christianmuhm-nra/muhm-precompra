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
  if (window.event && window.event.currentTarget) {
    window.event.currentTarget.classList.add('active');
  }
}

function openImageModal(imgSrc) {
  const modal = document.getElementById('imageModal');
  const modalImg = document.getElementById('modalImg');
  modal.style.display = 'block';
  modalImg.src = imgSrc;
}

function closeImageModal() {
  const modal = document.getElementById('imageModal');
  if (modal) modal.style.display = 'none';
}

function toggleFaq(button) {
  const item = button.parentElement;
  const answer = button.nextElementSibling;
  
  const isOpen = item.classList.contains('open');

  // Cerrar todos los demás
  document.querySelectorAll('.faq-item').forEach(el => {
    el.classList.remove('open');
    const a = el.querySelector('.faq-answer');
    if (a) a.style.maxHeight = null;
  });

  if (!isOpen) {
    item.classList.add('open');
    answer.style.maxHeight = answer.scrollHeight + 'px';
  }
}

// Menú Móvil Desplegable
function toggleMobileNav() {
  const drawer = document.getElementById('mobileNavDrawer');
  const btn = document.getElementById('mobileMenuBtn');
  if (drawer && btn) {
    drawer.classList.toggle('open');
    btn.classList.toggle('active');
  }
}

function closeMobileNav() {
  const drawer = document.getElementById('mobileNavDrawer');
  const btn = document.getElementById('mobileMenuBtn');
  if (drawer) {
    drawer.classList.remove('open');
  }
  if (btn) btn.classList.remove('active');
}

// Desplazamiento suave con compensación exacta para el header fijo y la botonera móvil
document.addEventListener('DOMContentLoaded', () => {
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  
  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (!targetId || targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (!targetElement) return;
      
      // Cerrar menú móvil si estuviera abierto
      closeMobileNav();
      
      // Prevenir el salto nativo abrupto que oculta encabezados bajo el header
      e.preventDefault();
      
      // En móvil tenemos el header principal más la barra rápida pinned
      const isMobile = window.innerWidth <= 992;
      const header = document.querySelector('.main-header');
      let offset = 80;
      
      if (isMobile) {
        offset = header ? header.offsetHeight + 14 : 112;
      } else {
        offset = header ? header.offsetHeight + 12 : 76;
      }
      
      const elementTop = targetElement.getBoundingClientRect().top + window.pageYOffset;
      const targetScroll = Math.max(0, elementTop - offset);
      
      window.scrollTo({
        top: targetScroll,
        behavior: 'smooth'
      });
      
      if (history.pushState) {
        history.pushState(null, null, targetId);
      }
    });
  });
});

// Cerrar modal o drawer con tecla Escape
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeImageModal();
    closeMobileNav();
  }
});
