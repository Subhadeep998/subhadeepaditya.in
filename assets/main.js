(function () {
  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var menu = document.getElementById('menu');
  if (btn && menu) {
    btn.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
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
        target.querySelectorAll('[data-group]').forEach(function (item) {
          item.hidden = !(f === 'All' || item.dataset.group === f);
        });
      });
    });
  });

  // Year in footer
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
