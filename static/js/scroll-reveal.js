(function () {
  'use strict';

  var REVEAL_THRESHOLD = 0.01;
  var REVEAL_ROOT_MARGIN = '0px 0px -40px 0px';
  var STAGGER_DELAY = 80;

  function initScrollReveal() {
    var els = document.querySelectorAll('[data-reveal]');
    if (!els.length) return;

    if (!('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('revealed'); });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;

        if (el.getAttribute('data-reveal') === 'stagger') {
          var children = el.querySelectorAll('[data-reveal-child]');
          children.forEach(function (child, i) {
            child.style.transitionDelay = (i * STAGGER_DELAY) + 'ms';
            child.classList.add('revealed');
          });
        }

        el.classList.add('revealed');
        observer.unobserve(el);
      });
    }, {
      threshold: REVEAL_THRESHOLD,
      rootMargin: REVEAL_ROOT_MARGIN,
    });

    els.forEach(function (el) { observer.observe(el); });
  }

  function initImageReveal() {
    var imgs = document.querySelectorAll('img[data-img-reveal]');
    if (!imgs.length) {
      imgs = document.querySelectorAll(
        '.cms-post-cover img, .cms-post-card-img img, .cms-gallery-item img'
      );
    }

    imgs.forEach(function (img) {
      if (img.complete && img.naturalWidth > 0) {
        img.classList.add('img-revealed');
        return;
      }

      img.classList.add('img-loading');

      img.addEventListener('load', function () {
        requestAnimationFrame(function () {
          img.classList.remove('img-loading');
          img.classList.add('img-revealed');
        });
      });

      img.addEventListener('error', function () {
        img.classList.remove('img-loading');
        img.classList.add('img-revealed');
      });
    });
  }

  function autoMarkRevealTargets() {
    var selectors = [
      '.cms-prose', '.cms-callout', '.cms-cta', '.cms-feature-grid',
      '.cms-comparison', '.cms-table', '.cms-faq', '.cms-quote',
      '.cms-logo-cloud', '.cms-pricing', '.cms-gallery-wrap',
      '.cms-post-cover', '.cms-blog-hero',
    ];

    var all = document.querySelectorAll(selectors.join(','));
    all.forEach(function (el) {
      if (!el.hasAttribute('data-reveal')) {
        el.setAttribute('data-reveal', '');
      }
    });

    var grids = document.querySelectorAll('.cms-feature-grid, .cms-pricing, .cms-post-grid');
    grids.forEach(function (grid) {
      grid.setAttribute('data-reveal', 'stagger');
      Array.prototype.forEach.call(grid.children, function (child) {
        child.setAttribute('data-reveal-child', '');
      });
    });
  }

  function initPageEntrance() {
    document.documentElement.classList.add('page-ready');
  }

  function init() {
    autoMarkRevealTargets();
    initScrollReveal();
    initImageReveal();
    requestAnimationFrame(function () {
      requestAnimationFrame(initPageEntrance);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
