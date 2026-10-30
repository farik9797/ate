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
  var page = (document.body.getAttribute('data-nav') || location.pathname.split('/').pop() || 'index.html').toLowerCase();
  document.querySelectorAll('.nav-link, .m-link, .sub-link').forEach(function (a) {
    var href = (a.getAttribute('href') || '').split('#')[0].split('?')[0].toLowerCase();
    if (href === page) {
      a.classList.add('is-active');
      var parent = a.closest('.nav-item'); if (parent) { var top = parent.querySelector('.nav-link'); if (top) top.classList.add('is-active'); }
    }
  });

  // Catalogue: category tiles + sidebar filters + series grid (katalog.html).
  // Hash keeps old links working: #espa-stancii opens the category, #espa / #hidrostal filters by brand.
  var cat = document.querySelector('[data-catalog]');
  if (cat) {
    var form = cat.querySelector('[data-flt-form]');
    var cards = [].slice.call(cat.querySelectorAll('[data-res-grid] .pcard'));
    var tiles = [].slice.call(document.querySelectorAll('[data-cat-tile]'));
    var chipsEl = cat.querySelector('[data-res-chips]');
    var badge = cat.querySelector('[data-flt-badge]');
    var toggle = cat.querySelector('[data-flt-toggle]');
    var panel = document.getElementById('flt');
    var brands = { espa: 'ESPA', hidrostal: 'Hidrostal' };
    var catTitle = {};
    form.querySelectorAll('input[name="cat"]').forEach(function (i) {
      catTitle[i.value] = i.closest('label').querySelector('.fchk-t').textContent;
    });
    var plural = function (n, one, few, many) {
      var a = n % 10, b = n % 100;
      return a === 1 && b !== 11 ? one : (a >= 2 && a <= 4 && (b < 12 || b > 14) ? few : many);
    };
    var num = function (v) { v = parseFloat(String(v).replace(',', '.')); return isNaN(v) ? null : v; };
    var state = function () {
      return {
        q: form.q.value.trim().toLowerCase(),
        brand: form.querySelector('input[name="brand"]:checked').value,
        cats: [].slice.call(form.querySelectorAll('input[name="cat"]:checked')).map(function (i) { return i.value; }),
        qmin: num(form.qmin.value),
        hmin: num(form.hmin.value)
      };
    };
    var chip = function (label, k, v, extra) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'res-chip' + (extra || '');
      b.dataset.k = k;
      if (v) b.dataset.v = v;
      b.textContent = label;
      if (k !== 'all') b.insertAdjacentHTML('beforeend', '<svg class="ic" aria-hidden="true"><use href="#i-x"/></svg>');
      b.setAttribute('aria-label', k === 'all' ? label : 'Убрать фильтр: ' + label);
      return b;
    };

    var apply = function () {
      var s = state(), shown = 0;
      form.querySelectorAll('[data-brand-group]').forEach(function (g) {
        g.hidden = !!s.brand && g.getAttribute('data-brand-group') !== s.brand;
      });
      cards.forEach(function (c) {
        var q = num(c.dataset.q), h = num(c.dataset.h);
        var ok = (!s.brand || c.dataset.brand === s.brand) &&
          (!s.cats.length || s.cats.indexOf(c.dataset.cat) > -1) &&
          (!s.q || c.textContent.toLowerCase().indexOf(s.q) > -1) &&
          (s.qmin === null || (q !== null && q >= s.qmin)) &&
          (s.hmin === null || (h !== null && h >= s.hmin));
        c.hidden = !ok;
        if (ok) shown++;
      });

      cat.querySelector('[data-res-title]').textContent =
        s.cats.length === 1 ? catTitle[s.cats[0]] : (s.brand ? 'Серии ' + brands[s.brand] : 'Все серии');
      cat.querySelector('[data-res-count]').innerHTML = 'Показано <b>' + shown + '</b> ' + plural(shown, 'серия', 'серии', 'серий') +
        (shown < cards.length ? ' из ' + cards.length : '');
      cat.querySelector('[data-res-empty]').hidden = shown > 0;
      tiles.forEach(function (t) { t.classList.toggle('is-active', s.cats.length === 1 && s.cats[0] === t.dataset.catTile); });

      chipsEl.textContent = '';
      if (s.brand) chipsEl.appendChild(chip(brands[s.brand], 'brand'));
      s.cats.forEach(function (c) { chipsEl.appendChild(chip(catTitle[c], 'cat', c)); });
      if (s.q) chipsEl.appendChild(chip('Поиск: ' + form.q.value.trim(), 'q'));
      if (s.qmin !== null) chipsEl.appendChild(chip('Q от ' + s.qmin + ' м³/ч', 'qmin'));
      if (s.hmin !== null) chipsEl.appendChild(chip('H от ' + s.hmin + ' м', 'hmin'));
      var n = chipsEl.children.length;
      if (n > 1) chipsEl.appendChild(chip('Сбросить всё', 'all', '', ' res-chip-clear'));
      chipsEl.hidden = !n;
      badge.hidden = !n;
      badge.textContent = n;

      // shareable URL: one category or one brand -> hash, nothing -> clean URL
      var only = !s.q && s.qmin === null && s.hmin === null;
      var hash = only && s.cats.length === 1 && !s.brand ? '#' + s.cats[0] : (only && !s.cats.length && s.brand ? '#' + s.brand : (n ? null : ''));
      if (hash !== null && hash !== location.hash) history.replaceState(null, '', location.pathname + location.search + hash);
    };

    var scrollToResults = function () {
      setTimeout(function () { cat.querySelector('.wrap').scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 40);
    };
    var selectCat = function (id) {
      form.reset();
      form.querySelector('input[name="cat"][value="' + id + '"]').checked = true;
      apply();
      scrollToResults();
    };

    form.addEventListener('input', apply);
    form.addEventListener('change', function (e) {
      if (e.target.name === 'brand' && e.target.value) {   // brand switch drops categories of the other brand
        form.querySelectorAll('input[name="cat"]:checked').forEach(function (i) {
          if (i.value.indexOf(e.target.value + '-') !== 0) i.checked = false;
        });
      }
      apply();
    });
    form.addEventListener('reset', function () { setTimeout(apply, 0); });
    cat.querySelectorAll('[data-flt-reset]').forEach(function (b) {
      if (b.type !== 'reset') b.addEventListener('click', function () { form.reset(); });
    });
    chipsEl.addEventListener('click', function (e) {
      var b = e.target.closest('[data-k]');
      if (!b) return;
      var k = b.dataset.k;
      if (k === 'all') { form.reset(); return; }
      if (k === 'brand') form.querySelector('input[name="brand"][value=""]').checked = true;
      else if (k === 'cat') form.querySelector('input[name="cat"][value="' + b.dataset.v + '"]').checked = false;
      else form[k].value = '';
      apply();
    });
    tiles.forEach(function (t) {
      t.addEventListener('click', function (e) { e.preventDefault(); selectCat(t.dataset.catTile); });
    });
    toggle.addEventListener('click', function () {
      var open = panel.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    var fromHash = function () {
      var id = decodeURIComponent((location.hash || '').slice(1));
      if (catTitle[id]) { selectCat(id); }
      else if (brands[id]) {
        form.reset();
        form.querySelector('input[name="brand"][value="' + id + '"]').checked = true;
        apply();
      }
    };
    fromHash();
    window.addEventListener('hashchange', fromHash);
  }

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

  // Forms: mockup only, no backend yet
  document.querySelectorAll('[data-lead-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = form.querySelector('[data-form-note]');
      if (note) { note.hidden = false; }
      form.reset();
    });
  });

  // Lead popup: any CTA with data-popup="lead" opens the request form
  var leadModal = document.querySelector('[data-lead-modal]');
  if (leadModal) {
    var leadTitle = leadModal.querySelector('[data-lead-title]');
    var openLead = function (title, dir, note) {
      if (title && leadTitle) leadTitle.textContent = title;
      var sel = leadModal.querySelector('select[name="direction"]');
      if (sel) sel.value = dir || '';
      var comment = leadModal.querySelector('textarea[name="comment"]');
      if (comment) comment.value = note || '';
      leadModal.classList.add('is-open'); leadModal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      var first = leadModal.querySelector('input'); if (first) setTimeout(function () { first.focus(); }, 250);
    };
    var closeLead = function () {
      if (!leadModal.classList.contains('is-open')) return;
      leadModal.classList.remove('is-open'); leadModal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      var note = leadModal.querySelector('[data-form-note]'); if (note) note.hidden = true;
    };
    document.querySelectorAll('[data-popup="lead"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        setMenu(false);
        openLead(a.getAttribute('data-popup-title') || a.textContent.trim(), a.getAttribute('data-popup-dir'), a.getAttribute('data-popup-note'));
      });
    });
    leadModal.querySelectorAll('[data-lead-close]').forEach(function (b) { b.addEventListener('click', closeLead); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeLead(); });
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
        y: 28, opacity: 0, duration: .7, ease: 'power3.out', stagger: .09, clearProps: 'transform,opacity',
        scrollTrigger: { trigger: group, start: 'top 85%', once: true }
      });
    });
  }
})();
