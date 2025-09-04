// Simple fade-in animation for page content
document.addEventListener('DOMContentLoaded', () => {
  const content = document.querySelector('main, body');
  if (content) {
    content.style.opacity = 0;
    content.style.transition = 'opacity 0.8s ease-in-out';
    requestAnimationFrame(() => {
      content.style.opacity = 1;
    });
  }
});
