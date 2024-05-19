document.getElementById('form').addEventListener('submit', (event) => {
    event.preventDefault();
    const form = event.target;
    const isValid = formValidator.validateForm(form);
    if (isValid) {
        alert('Form is valid!');
        form.submit();
    } else {
        alert('Please correct the errors in the form');
    }
});
