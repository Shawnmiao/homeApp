document.addEventListener("DOMContentLoaded", function() {

    const hiringForm = document.getElementById('hiringForm');

    hiringForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(hiringForm);
        const jsonFormData = JSON.stringify(Object.fromEntries(formData));

        fetch('/hire_staff', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Add this if you're using CSRF protection
            },
            body: jsonFormData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').textContent = data.message;
        })
        .catch(error => {
            document.getElementById('result').textContent = 'Error hiring staff.';
        });
    });

    const cancelButton = document.getElementById('cancelButton');
    cancelButton.addEventListener('click', function() {
        hiringForm.reset();
        document.getElementById('result').textContent = '';
    });

});

// Helper function to get the value of a cookie by name
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
