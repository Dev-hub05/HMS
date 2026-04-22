/* ═══════════════════════════════════════════════════════════
   Hospital Management System — Core JavaScript
   ═══════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

    // ── Auto-dismiss messages ──
    document.querySelectorAll('.message[data-auto-dismiss]').forEach(msg => {
        setTimeout(() => {
            msg.style.opacity = '0';
            msg.style.transform = 'translateX(100px)';
            setTimeout(() => msg.remove(), 400);
        }, 4000);
    });

    // ── Close message buttons ──
    document.querySelectorAll('.message-close').forEach(btn => {
        btn.addEventListener('click', () => {
            const msg = btn.closest('.message');
            msg.style.opacity = '0';
            msg.style.transform = 'translateX(100px)';
            setTimeout(() => msg.remove(), 300);
        });
    });

    // ── Admin sidebar toggle (mobile) ──
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    const sidebarOverlay = document.getElementById('sidebarOverlay');

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', () => {
            sidebar.classList.toggle('open');
            if (sidebarOverlay) sidebarOverlay.classList.toggle('active');
        });
    }

    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', () => {
            sidebar.classList.remove('open');
            sidebarOverlay.classList.remove('active');
        });
    }

    // ── Public nav toggle (mobile) ──
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', () => {
            navLinks.classList.toggle('open');
        });
    }

    // ── Delete confirmation ──
    document.querySelectorAll('.delete-form').forEach(form => {
        form.addEventListener('submit', e => {
            if (!confirm('Are you sure you want to delete this record? This action cannot be undone.')) {
                e.preventDefault();
            }
        });
    });

    // ── Number counting animation (for public stats) ──
    const animateCounters = () => {
        document.querySelectorAll('[data-count]').forEach(el => {
            const target = parseInt(el.dataset.count, 10);
            const duration = 1500;
            const step = Math.max(1, Math.floor(target / (duration / 16)));
            let current = 0;

            const timer = setInterval(() => {
                current += step;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                el.textContent = current.toLocaleString();
            }, 16);
        });
    };

    // Run counter animation when elements are in view
    const counters = document.querySelectorAll('[data-count]');
    if (counters.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounters();
                    observer.disconnect();
                }
            });
        }, { threshold: 0.3 });

        counters.forEach(c => observer.observe(c));
    }

    // ── Fade-in animation on scroll ──
    const animateOnScroll = document.querySelectorAll('.animate-on-scroll');
    if (animateOnScroll.length > 0) {
        const scrollObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                    scrollObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        animateOnScroll.forEach(el => scrollObserver.observe(el));
    }

});
