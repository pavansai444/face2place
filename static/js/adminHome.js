function toggleDarkMode() {
    var element = document.body;
    element.classList.toggle("dark-mode");
    var thbtn= document.querySelector("#dark-button");
    var regbtn=document.querySelector("#register-button");
    thbtn.classList.toggle("fa-light");
    thbtn.classList.toggle("fa-moon");
    thbtn.classList.toggle("fa-adjust");
}
// Password validator
var password = document.getElementById("password")
  , confirm_password = document.getElementById("confirm-password");

function validatePassword(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'Passwords don\'t match';
  } else {
    confirm_password.setCustomValidity('');
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'Passwords match';
  }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;

// Password Strength
function checkPasswordStrength() {
    var password = document.getElementById("password").value;
    var strength = document.getElementById("password-strength");
  
    // Check the password strength
    var regex = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])/;
    if (password.length < 8) {
      strength.innerHTML = 'Password must be at least 8 characters long';
      strength.style.color = 'red';
    } else if (!regex.test(password)) {
      strength.innerHTML = 'Password must contain at least one lowercase letter, one uppercase letter, one number, and one special character';
      strength.style.color = 'red';
    } else {
      strength.innerHTML = 'Password strength: strong';
      strength.style.color = 'green';
    }
  }

//   phone validator 
const phoneInput = document.getElementById("phone");

phoneInput.addEventListener("input", () => {
  const phoneNumber = phoneInput.value;
  const phoneRegex = /^[0-9]{10}$/;

  if (phoneRegex.test(phoneNumber)) {
    phoneInput.setCustomValidity("");
  } else {
    phoneInput.setCustomValidity("Please enter a valid 10-digit phone number");
  }
});

phoneInput.addEventListener("invalid", () => {
  phoneInput.setCustomValidity("Please enter a valid 10-digit phone number");
});
// Photo Capture
