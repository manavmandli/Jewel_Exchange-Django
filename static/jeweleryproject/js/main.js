
  const hamburgerBtn = document.getElementById('hamburger-btn');
  const responsiveMenu = document.getElementById('responsive-menu');

  hamburgerBtn.addEventListener('click', function() {
    responsiveMenu.classList.toggle('hidden');
  });