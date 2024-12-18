document.querySelectorAll('.approve').forEach(button => {
    button.addEventListener('click', function() {
        var vacationId = this.dataset.vacationId;
        var xhr = new XMLHttpRequest();
        xhr.open('POST', `/approveVacation/${vacationId}/`, true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}'); // Ensure you have CSRF token in your template
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Assuming you want to remove the row upon successful approval
                    var rowToRemove = button.closest('tr');
                    rowToRemove.parentNode.removeChild(rowToRemove);
                } else {
                    console.error('Error occurred while approving vacation');
                }
            }
        };
        xhr.send();
    });
});
