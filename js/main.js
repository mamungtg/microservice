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
  // The form posts for real to our own mail-relay Worker (see the form's
  // action= in build.py / ms-mail-worker/), which logs into the Zoho
  // mailbox over SMTP and sends the message on so it arrives
  // From: mominul@mspointbd.com. We intercept the submit only to run a
  // client-side check (emails must match) as a fast fail before the round
  // trip; the same check also happens server-side in the Worker. On
  // success the Worker redirects to contact-thanks.html; on a validation
  // or delivery problem it redirects back here with ?error=... , which we
  // pick up below and show inline.
  var form = document.getElementById('repair-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      var confirmEmail = form.querySelector('[name="email"]');
      var confirmField = form.querySelector('[name="email_confirm"]');
      if (confirmEmail && confirmField && confirmEmail.value !== confirmField.value) {
        e.preventDefault();
        showFormMessage(form, 'Your email addresses don’t match — please check and try again.', true);
      }
      // Otherwise: let the native form submission proceed to the Worker.
    });

    // Surface a server-side error (bad input, or the mail relay failed)
    // that the Worker passed back via ?error=... on its redirect here.
    var params = new URLSearchParams(window.location.search);
    var serverError = params.get('error');
    if (serverError) {
      showFormMessage(form, serverError, true);
      params.delete('error');
      var cleanUrl = window.location.pathname + (params.toString() ? '?' + params.toString() : '') + window.location.hash;
      window.history.replaceState({}, document.title, cleanUrl);
    }
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
