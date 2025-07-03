document.addEventListener('DOMContentLoaded', function () {
    // Mobile menu toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('nav ul');

    hamburger.addEventListener('click', function () {
        this.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
                if (hamburger.classList.contains('active')) {
                    hamburger.classList.remove('active');
                    navLinks.classList.remove('active');
                }
            }
        });
    });

    // Portfolio Modal Functionality
    window.openModal = function (imageSrc, location, description) {
        const modal = document.getElementById('imageModal');
        const modalImg = document.getElementById('expandedImage');
        const caption = document.getElementById('caption');

        modalImg.src = imageSrc;
        caption.innerHTML = `<h3>${location}</h3><p>${description}</p>`;
        modal.classList.add('show');
        document.body.style.overflow = 'hidden';

        modalImg.onclick = function (e) {
            e.stopPropagation();
        }
    };

    window.closeModal = function () {
        const modal = document.getElementById('imageModal');
        modal.classList.remove('show');
        document.body.style.overflow = '';
    };

    // Close modal when clicking outside or pressing ESC
    document.addEventListener('click', function (event) {
        if (event.target.classList.contains('modal')) {
            closeModal();
        }
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === "Escape") {
            closeModal();
        }
    });

    // Animation on scroll
    const animateOnScroll = function () {
        const elements = document.querySelectorAll('.feature-card, .system-card, .gallery-square, .review-card');
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            if (elementPosition < windowHeight - 100) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };

    // Initialize animations
    const animatedElements = document.querySelectorAll('.feature-card, .system-card, .gallery-square, .review-card');
    animatedElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    });

    animateOnScroll();
    window.addEventListener('scroll', animateOnScroll);

    // Brand filtering functionality - corrected version
    document.querySelectorAll('.brand-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            // Get all elements
            const buttons = document.querySelectorAll('.brand-btn');
            const cards = document.querySelectorAll('.system-card');
            const selectedBrand = this.dataset.brand;

            // Update active button
            buttons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // Filter cards
            cards.forEach(card => {
                const cardBrand = card.dataset.brand;
                const shouldShow = selectedBrand === 'all' || cardBrand === selectedBrand;

                if (shouldShow) {
                    card.style.display = 'block';
                    // Force reflow to enable animation
                    void card.offsetWidth;
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    // Hide after animation completes
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });
});