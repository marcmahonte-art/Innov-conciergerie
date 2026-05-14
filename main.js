// Navbar scroll effect
        const navbar = document.getElementById('navbar');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Mobile menu toggle
        const hamburger = document.getElementById('hamburger');
        const navLinks = document.getElementById('nav-links');
        const navLinksItems = document.querySelectorAll('.nav-link');

        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = navLinks.classList.contains('active') 
                ? '<line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line>'
                : '<line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line>';
            hamburger.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${icon}</svg>`;
        });

        navLinksItems.forEach(item => {
            item.addEventListener('click', () => {
                navLinks.classList.remove('active');
                hamburger.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
            });
        });

        // Scroll Reveal animations
        const revealElements = document.querySelectorAll('.reveal');
        
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            root: null,
            threshold: 0.15,
            rootMargin: "0px 0px -50px 0px"
        });

        revealElements.forEach(el => {
            revealObserver.observe(el);
        });

        // Animated Counters
        const counters = document.querySelectorAll('.counter');
        const speed = 200; // The lower the slower

        const counterObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = +counter.getAttribute('data-target');
                    
                    const updateCount = () => {
                        const count = +counter.innerText;
                        const inc = target / speed;

                        if (count < target) {
                            counter.innerText = Math.ceil(count + inc);
                            setTimeout(updateCount, 10);
                        } else {
                            counter.innerText = target;
                        }
                    };
                    
                    updateCount();
                    observer.unobserve(counter);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(counter => {
            counterObserver.observe(counter);
        });

        // Form Validation
        const contactForm = document.getElementById('contact-form');
        const formSuccess = document.getElementById('form-success');

        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            let isValid = true;
            const name = document.getElementById('name');
            const phone = document.getElementById('phone');
            const email = document.getElementById('email');
            const subscription = document.getElementById('subscription');

            // Simple validation
            if (!name.value.trim()) {
                name.parentElement.classList.add('error');
                isValid = false;
            } else {
                name.parentElement.classList.remove('error');
            }

            if (!phone.value.trim()) {
                phone.parentElement.classList.add('error');
                isValid = false;
            } else {
                phone.parentElement.classList.remove('error');
            }

            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email.value)) {
                email.parentElement.classList.add('error');
                isValid = false;
            } else {
                email.parentElement.classList.remove('error');
            }

            if (!subscription.value) {
                subscription.parentElement.classList.add('error');
                isValid = false;
            } else {
                subscription.parentElement.classList.remove('error');
            }

            // Clean inputs on input
            const inputs = [name, phone, email, subscription];
            inputs.forEach(input => {
                input.addEventListener('input', () => {
                    input.parentElement.classList.remove('error');
                });
            });

            if (isValid) {
                // Simulate API call
                const submitBtn = contactForm.querySelector('button[type="submit"]');
                const originalText = submitBtn.innerText;
                submitBtn.innerText = 'Envoi en cours...';
                submitBtn.disabled = true;

                setTimeout(() => {
                    contactForm.reset();
                    formSuccess.style.display = 'block';
                    submitBtn.innerText = originalText;
                    submitBtn.disabled = false;
                    
                    setTimeout(() => {
                        formSuccess.style.display = 'none';
                    }, 5000);
                }, 1500);
            }
        });