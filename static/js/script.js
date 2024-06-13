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

document.addEventListener('DOMContentLoaded', function() {
            const activitySelect = document.getElementById('activity');
            const timeslotSelect = document.getElementById('timeslot');

            // Function to fetch and populate available timeslots
            function updateTimeslots(activity) {
                fetch(`/api/availability?activity=${activity}`)
                    .then(response => response.json())
                    .then(data => {
                        // Clear existing options
                        timeslotSelect.innerHTML = '';
                        console.log(data)
                        // Populate timeslot options
                        data.forEach(slot => {
                            const option = document.createElement('option');
                            option.value = slot.time;
                            option.textContent = `${slot.time} - ${slot.available ? 'Доступно' : 'Недоступно'}`;
                            console.log(slot.available)
                            if (!slot.available) {
                                option.disabled = true;
                            }
                            timeslotSelect.appendChild(option);
                        });
                    })
                    .catch(error => {
                        alert('Ошибка получения доступности времени: ' + error);
                    });
            }

            // Initial load of timeslots for the default activity
            updateTimeslots(activitySelect.value);

            // Update timeslots when the activity changes
            activitySelect.addEventListener('change', function() {
                updateTimeslots(activitySelect.value);
            });

            document.getElementById('booking-form').addEventListener('submit', function(event) {
                event.preventDefault();

                const activity = document.getElementById('activity').value;
                const people = document.getElementById('people').value;
                const timeslot = document.getElementById('timeslot').value;
                const customer_name = document.getElementById('customer_name').value;

                const bookingData = {
                    activity: activity,
                    people: people,
                    timeslot: timeslot,
                    customer_name: customer_name
                };

                console.log(bookingData)

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
                    location.reload();
                })
                .catch((error) => {
                    alert('Ошибка бронирования: ' + error);
                });
            });
        });