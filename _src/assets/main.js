(function () {
  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var menu = document.getElementById('menu');
  if (btn && menu) {
    btn.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    var closeMenu = function () { if (menu.classList.contains('open')) { menu.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); } };
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeMenu(); } });
    document.addEventListener('click', function (e) { if (!menu.contains(e.target) && !btn.contains(e.target)) closeMenu(); });
    window.addEventListener('resize', function () { if (window.innerWidth > 1060) closeMenu(); });
  }

  // "View me as" lens on the home page
  var lensOut = document.getElementById('lensText');
  if (lensOut) {
    var texts = {
      scientist: 'Trained in biotechnology and drawn to cancer genomics and precision medicine — curious about what our genes can tell medicine next.',
      analyst: 'Three-plus years turning medical-device and healthcare market data into clean, decision-ready intelligence.',
      author: 'Three books and counting — a healthcare consulting handbook, a mythic techno-thriller, and a journey through Alzheimer’s disease.',
      legal: 'An LL.B. student studying the rules that will govern biology, data and AI — with a focus on healthcare law and IP.'
    };
    var lenses = document.querySelectorAll('[data-lens]');
    lenses.forEach(function (b) {
      b.addEventListener('click', function () {
        lenses.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        lensOut.textContent = texts[b.dataset.lens];
      });
    });
  }

  // Generic filter: buttons [data-filter] inside [data-filter-group] toggle items [data-group] in the target
  document.querySelectorAll('[data-filter-group]').forEach(function (group) {
    var target = document.getElementById(group.dataset.filterGroup);
    var buttons = group.querySelectorAll('[data-filter]');
    buttons.forEach(function (b) {
      b.addEventListener('click', function () {
        buttons.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        var f = b.dataset.filter;
        var shown = 0;
        target.querySelectorAll('[data-group]').forEach(function (item) {
          item.hidden = !(f === 'All' || item.dataset.group === f);
          if (!item.hidden) shown++;
        });
        target.setAttribute('aria-label', shown + ' shown');
      });
    });
  });

  // Year in footer
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();

// Dark / light mode toggle
(function () {
  var root = document.documentElement;
  var btn = document.querySelector('.theme-btn');
  var meta = document.querySelector('meta[name="theme-color"]');
  function apply(t) {
    root.setAttribute('data-theme', t);
    var next = t === 'light' ? 'dark' : 'light';
    if (btn) {
      btn.setAttribute('aria-label', 'Switch to ' + next + ' mode');
      btn.setAttribute('title', 'Switch to ' + next + ' mode');
      var l = btn.querySelector('.theme-label'); if (l) l.textContent = next === 'light' ? 'Light' : 'Dark';
    }
    if (meta) meta.setAttribute('content', t === 'light' ? '#F7F4EE' : '#0D0F12');
  }
  apply(root.getAttribute('data-theme') === 'light' ? 'light' : 'dark');
  // Follow the device setting live, until the visitor picks a mode themselves
  try {
    var mq = window.matchMedia('(prefers-color-scheme: light)');
    var onChange = function (e) { var saved = null; try { saved = localStorage.getItem('theme'); } catch (x) {} if (!saved) apply(e.matches ? 'light' : 'dark'); };
    if (mq.addEventListener) mq.addEventListener('change', onChange); else if (mq.addListener) mq.addListener(onChange);
  } catch (e) {}
  if (btn) btn.addEventListener('click', function () {
    var t = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    apply(t);
    try { localStorage.setItem('theme', t); } catch (e) {}
  });
})();

// ChobiGhor lightbox
(function () {
  var data = window.CHOBI, lb = document.getElementById('lb');
  if (!data || !lb) return;
  var img = document.getElementById('lb-img'), title = document.getElementById('lb-title'),
      cap = document.getElementById('lb-cap'), count = document.getElementById('lb-count'), i = 0, opener = null;
  function visible() { return [].slice.call(document.querySelectorAll('.ph')).filter(function (f) { return !f.hidden; }).map(function (f) { return +f.querySelector('.ph-open').dataset.i; }); }
  function show(n) {
    var v = visible(); if (!v.length) return;
    var pos = v.indexOf(n); if (pos < 0) pos = 0; i = v[pos];
    var d = data[i]; img.src = d.src; img.alt = d.t + ' — ' + d.c; title.textContent = d.t; cap.textContent = d.c;
    count.textContent = (pos + 1) + ' / ' + v.length;
  }
  function step(k) { var v = visible(), pos = v.indexOf(i); show(v[(pos + k + v.length) % v.length]); }
  document.querySelectorAll('.ph-open').forEach(function (b) {
    b.addEventListener('click', function () { opener = b; show(+b.dataset.i); if (lb.showModal) lb.showModal(); else lb.setAttribute('open', ''); });
  });
  document.getElementById('lb-prev').addEventListener('click', function () { step(-1); });
  document.getElementById('lb-next').addEventListener('click', function () { step(1); });
  document.getElementById('lb-close').addEventListener('click', function () { lb.close(); });
  lb.addEventListener('close', function () { if (opener) opener.focus(); });
  lb.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') step(1); if (e.key === 'ArrowLeft') step(-1); });
  lb.addEventListener('click', function (e) { if (e.target === lb || e.target.classList.contains('lb-inner')) lb.close(); });
  var x0 = null;
  lb.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener('touchend', function (e) { if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 50) step(dx < 0 ? 1 : -1); x0 = null; });
  // discourage casual saving of copyrighted photos
  document.querySelectorAll('.ph img, #lb-img, .strip-ph img').forEach(function (el) { el.addEventListener('contextmenu', function (e) { e.preventDefault(); }); el.setAttribute('draggable', 'false'); });
})();
