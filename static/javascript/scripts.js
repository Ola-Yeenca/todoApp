
document.addEventListener('DOMContentLoaded', function() {
    // Handle task completion toggle
    document.querySelectorAll('.task').forEach(function(task) {
        task.addEventListener('click', function() {
            this.classList.toggle('completed');
        });
    });

    // Handle task deletion
    document.querySelectorAll('.delete-btn').forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            this.parentElement.remove();
        });
    });
});
