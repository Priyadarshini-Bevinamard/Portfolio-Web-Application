const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

if (navToggle) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });
}

const contactForm = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');

if (contactForm) {
  contactForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const payload = {
      name: contactForm.name.value.trim(),
      email: contactForm.email.value.trim(),
      subject: contactForm.subject.value.trim(),
      message: contactForm.message.value.trim(),
    };

    try {
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      const result = await response.json();
      if (response.ok && result.success) {
        formMessage.textContent = result.message;
        formMessage.style.color = '#d1fae5';
        contactForm.reset();
      } else {
        formMessage.textContent = result.message || 'Unable to submit form.';
        formMessage.style.color = '#fecaca';
      }
    } catch (error) {
      formMessage.textContent = 'Network error. Please try again.';
      formMessage.style.color = '#fecaca';
    }
  });
}
