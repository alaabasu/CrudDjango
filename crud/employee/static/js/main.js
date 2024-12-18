
document.getElementById("mainpage").addEventListener("click", function redirectToAnotherPage() {
    window.location.href = "index.html";
});

function validateForm() {
    const name = document.getElementById("name").value;
    const salary = document.getElementById("Salary").value;
    const dateOfBirth = document.getElementById("date").value;
  
    let isValid = true;
    let errorMessage = "";
  
    // Validate name
    if (!/^[a-zA-Z ]+$/.test(name)) {
      errorMessage += "Name should only contain letters and spaces.<br>";
      isValid = false;
    }
  
    // Validate salary
    if (salary < 3000) {
      errorMessage += "Salary should be at least 3000.<br>";
      isValid = false;
    }
  
    // Validate date
    // Assuming a specific format like YYYY-MM-DD:
    const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
    if (!dateRegex.test(dateOfBirth)) {
      errorMessage += "Date of birth should be in the format YYYY-MM-DD.<br>";
      isValid = false;
    }
  
    // Display error message if any
    const errorContainer = document.getElementById("error-message");
    errorContainer.innerHTML = errorMessage;
    errorContainer.style.color = isValid ? "green" : "red";
  
    return isValid;
  }
  
  // Attach the validation function to the form's submit event
  const form = document.getElementById("your-form-id"); // Replace with your form's ID
  form.addEventListener("submit", function(event) {
    if (!validateForm()) {
      event.preventDefault(); // Prevent form submission if validation fails
    }
  });

// Function To Confirm  deleteion

function confirmDelete(employeeId) {
    var response = confirm("Are you sure you want to delete this employee?");

    if (response == true) {
        // Construct the delete URL
        var deleteUrl = "/delete/" + employeeId;

        // Redirect to the delete URL
        window.location.href = deleteUrl;
    } else {
        // Deletion canceled, do nothing
        console.log("Deletion canceled. Nothing deleted.");
    }
}



