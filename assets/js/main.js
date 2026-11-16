if (window.lucide) lucide.createIcons();
function openLightbox(src, caption) {
    document.getElementById('lightbox-img').src = src;
    document.getElementById('lightbox-caption').textContent = caption;
    document.getElementById('lightbox').classList.remove('hidden');
}
function closeLightbox() {
    document.getElementById('lightbox').classList.add('hidden');
}
document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeLightbox();
});
document.addEventListener('click', (event) => {
    const photo = event.target.closest('[data-lightbox]');
    if (photo) openLightbox(photo.src, photo.alt);
});
