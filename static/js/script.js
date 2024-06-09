// script.js
document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('.page');
    const navLinks = document.querySelectorAll('nav ul li a');

    function activateSection(section) {
        section.classList.add('visible');
    }

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            window.scrollTo({
                top: targetSection.offsetTop - 60, // Adjust for fixed header height
                behavior: 'smooth'
            });
            activateSection(targetSection);
        });
    });

    // Activate all sections initially
    sections.forEach(section => {
        activateSection(section);
    });
});

// Add this at the end of your existing DOMContentLoaded block
const bookingForm = document.getElementById('booking-form');
bookingForm.addEventListener('submit', (e) => {
    e.preventDefault();
    // Extract data from form here and send it to your server via AJAX in a real app
    alert('Ваше бронирование принято!');
});


document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('booking-form').addEventListener('submit', function(event) {
                event.preventDefault();

                const activity = document.getElementById('activity').value;
                const people = document.getElementById('people').value;
                const timeslot = document.getElementById('timeslot').value;

                const bookingData = {
                    activity: activity,
                    people: people,
                    timeslot: timeslot
                };

                fetch('/api/booking', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(bookingData)
                })
                .then(response => response.json())
                .then(data => {
                    alert('Бронирование успешно!');
                })
                .catch((error) => {
                    alert('Ошибка бронирования: ' + error);
                });
            });
        });