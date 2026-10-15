(function () {
  'use strict';

  // Header shadow on scroll
  var header = document.querySelector('.site-header');
  var toTop = document.querySelector('[data-to-top]');
  var onScroll = function () {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 8);
    if (toTop) toTop.classList.toggle('is-visible', window.scrollY > 600);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
  // Anchor jumps (/#contacts) and scroll restoration can land after init
  window.addEventListener('load', onScroll);
  window.addEventListener('hashchange', onScroll);
  setTimeout(onScroll, 300);
  if (toTop) toTop.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });

  // Mobile menu
  var menu = document.querySelector('.mobile-menu');
  var openBtn = document.querySelector('[data-menu-open]');
  var closeBtn = document.querySelector('[data-menu-close]');
  var setMenu = function (open) {
    if (!menu) return;
    menu.classList.toggle('is-open', open);
    menu.setAttribute('aria-hidden', String(!open));
    document.body.style.overflow = open ? 'hidden' : '';
    if (openBtn) openBtn.setAttribute('aria-expanded', String(open));
  };
  if (openBtn) openBtn.addEventListener('click', function () { setMenu(true); });
  if (closeBtn) closeBtn.addEventListener('click', function () { setMenu(false); });
  if (menu) {
    menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });

  // Active nav link by current page
  var page = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  document.querySelectorAll('.nav-link, .m-link').forEach(function (a) {
    var href = (a.getAttribute('href') || '').split('#')[0].split('?')[0].toLowerCase();
    if (href === page) a.classList.add('is-active');
  });

  // Placeholder links (PDF catalogues etc.): no target yet
  document.querySelectorAll('[data-placeholder]').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); });
  });

  // Objects: filter by direction (buttons + ?dir= in the URL)
  var filterBar = document.querySelector('[data-filter-bar]');
  if (filterBar) {
    var cards = document.querySelectorAll('[data-dir]');
    var applyFilter = function (dir) {
      filterBar.querySelectorAll('[data-filter]').forEach(function (b) {
        var on = b.getAttribute('data-filter') === dir;
        b.classList.toggle('is-active', on); b.setAttribute('aria-pressed', String(on));
      });
      cards.forEach(function (c) { c.hidden = dir !== 'all' && c.getAttribute('data-dir') !== dir; });
    };
    filterBar.addEventListener('click', function (e) {
      var b = e.target.closest('[data-filter]'); if (b) applyFilter(b.getAttribute('data-filter'));
    });
    var initial = new URLSearchParams(location.search).get('dir');
    applyFilter(initial === 'espa' || initial === 'hidrostal' ? initial : 'all');
  }

  // Video modal (YouTube embed by data-video id; empty id shows a note)
  var modal = document.querySelector('[data-video-modal]');
  if (modal) {
    var frame = modal.querySelector('iframe');
    var note = modal.querySelector('[data-video-note]');
    var openVideo = function (id, title) {
      modal.classList.add('is-open'); modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      if (id) { frame.src = 'https://www.youtube.com/embed/' + id + '?autoplay=1&rel=0'; frame.hidden = false; note.hidden = true; }
      else { frame.hidden = true; note.hidden = false; }
      modal.querySelector('[data-video-title]').textContent = title || '';
    };
    var closeVideo = function () {
      modal.classList.remove('is-open'); modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = ''; frame.src = '';
    };
    document.querySelectorAll('[data-video]').forEach(function (card) {
      card.addEventListener('click', function (e) { e.preventDefault(); openVideo(card.getAttribute('data-video'), card.getAttribute('data-title')); });
    });
    modal.querySelectorAll('[data-video-close]').forEach(function (b) { b.addEventListener('click', closeVideo); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeVideo(); });
  }

  // Current year in footer
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = String(new Date().getFullYear());

  // Form: mockup only, no backend yet
  var form = document.querySelector('[data-lead-form]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = form.querySelector('[data-form-note]');
      if (note) { note.hidden = false; }
      form.reset();
    });
  }

  // Scroll reveal with GSAP (static HTML → GSAP + ScrollTrigger)
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduced && window.gsap && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);

    document.querySelectorAll('.rv').forEach(function (el) {
      gsap.from(el, {
        y: 28, opacity: 0, duration: .8, ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 88%', once: true }
      });
    });

    // Direction blocks slide in from their side
    document.querySelectorAll('[data-slide]').forEach(function (el) {
      var fromX = el.getAttribute('data-slide') === 'left' ? -60 : 60;
      gsap.from(el.querySelector('.dir2-body'), {
        x: fromX, opacity: 0, duration: .9, ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 80%', once: true }
      });
      gsap.from(el.querySelector('.dir2-bg'), {
        scale: 1.08, duration: 1.4, ease: 'power2.out',
        scrollTrigger: { trigger: el, start: 'top 80%', once: true }
      });
    });

    // Hero: soft parallax of the photo while scrolling away
    var heroImg = document.querySelector('.hero-img');
    if (heroImg) {
      gsap.to(heroImg, {
        yPercent: 14, ease: 'none',
        scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true }
      });
    }

    document.querySelectorAll('.rv-group').forEach(function (group) {
      var items = group.children;
      gsap.from(items, {
        y: 28, opacity: 0, duration: .7, ease: 'power3.out', stagger: .09,
        scrollTrigger: { trigger: group, start: 'top 85%', once: true }
      });
    });
  }
})();
