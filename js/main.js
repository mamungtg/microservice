// Micro Service (mspointbd.com) — small progressive-enhancement script.
// No dependencies. Safe to defer-load on every page.

document.addEventListener('DOMContentLoaded', function () {
  // --- Mobile nav toggle -----------------------------------------------
  var toggle = document.getElementById('nav-toggle');
  var nav = document.getElementById('nav-links');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close the mobile menu once the viewport grows past the mobile breakpoint
    // (must match the 1000px nav breakpoint in css/style.css).
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1000 && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // --- Contact / repair-request form ------------------------------------
  // The form posts for real to FormSubmit.co (see the form's action= in
  // build.py). We only intercept the submit to run a client-side check
  // (emails must match) — if that check passes, the browser submits the
  // form normally and FormSubmit redirects to contact-thanks.html once it's
  // delivered. Note: the very first submission ever sent to a brand-new
  // destination email goes to FormSubmit's own "confirm this address" page
  // instead of being delivered — that's a one-time step for the site owner,
  // not something repeat visitors will see.
  var form = document.getElementById('repair-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      var confirmEmail = form.querySelector('[name="email"]');
      var confirmField = form.querySelector('[name="email_confirm"]');
      if (confirmEmail && confirmField && confirmEmail.value !== confirmField.value) {
        e.preventDefault();
        showFormMessage(form, 'Your email addresses don’t match — please check and try again.', true);
      }
      // Otherwise: let the native form submission proceed to FormSubmit.co.
    });
  }

  // --- Lead popup ---------------------------------------------------------
  // Shows once per visitor (tracked via localStorage), on any page except
  // the contact form itself. It's docked bottom-left, and on short/mobile
  // viewports a blind timer can land it right on top of the hero's CTA
  // buttons — so it triggers on whichever happens first: the visitor
  // scrolling down a bit (meaning the hero has scrolled out of the way) or
  // an 8s fallback timer for anyone who lands and doesn't scroll at all.
  var popupOverlay = document.getElementById('site-popup-overlay');
  var popupClose = document.getElementById('site-popup-close');
  // The CookieYes "reopen preferences" button shares the bottom-left corner
  // with the lead popup, so it hides whenever that popup is open.
  var cookieBtn = document.getElementById('cookie-revisit-btn');
  function syncCookieBtn() {
    if (!cookieBtn) return;
    var popupIsOpen = popupOverlay && popupOverlay.classList.contains('is-open');
    cookieBtn.classList.toggle('is-hidden', !!popupIsOpen);
  }
  syncCookieBtn();

  if (popupOverlay && popupClose) {
    var onContactPage = window.location.pathname.indexOf('contact') !== -1;
    var alreadySeen = true;
    try {
      alreadySeen = window.localStorage.getItem('msPopupSeen') === '1';
    } catch (err) {
      // localStorage unavailable (privacy mode, etc.) — just skip the popup.
      alreadySeen = true;
    }

    if (!onContactPage && !alreadySeen) {
      var popupShown = false;
      var showPopup = function () {
        if (popupShown) return;
        popupShown = true;
        popupOverlay.classList.add('is-open');
        try { window.localStorage.setItem('msPopupSeen', '1'); } catch (err) { /* ignore */ }
        window.removeEventListener('scroll', onScroll);
        syncCookieBtn();
      };
      var onScroll = function () {
        if (window.scrollY > 300) showPopup();
      };
      window.addEventListener('scroll', onScroll, { passive: true });
      window.setTimeout(showPopup, 8000);
    }

    function closePopup() {
      popupOverlay.classList.remove('is-open');
      syncCookieBtn();
    }
    popupClose.addEventListener('click', closePopup);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closePopup();
    });
  }

  function showFormMessage(form, text, isError) {
    var existing = form.querySelector('.form-submit-message');
    if (existing) existing.remove();

    var box = document.createElement('div');
    box.className = 'form-submit-message';
    box.setAttribute('role', 'status');
    box.style.marginTop = '16px';
    box.style.padding = '14px 16px';
    box.style.borderRadius = '8px';
    box.style.fontSize = '0.9rem';
    box.style.fontWeight = '600';
    if (isError) {
      box.style.background = '#fdecec';
      box.style.color = '#9c2b2b';
    } else {
      box.style.background = '#e9f7ef';
      box.style.color = '#1f6b3f';
    }
    box.textContent = text;
    form.appendChild(box);
    box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
});
