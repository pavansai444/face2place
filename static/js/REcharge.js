
// const form = document.querySelector('form');
// const btn= document.querySelector("#recharge-button");
// btn.addEventListener('click', function() {
//   const mobile = form.elements.mobile.value;
//   const amount = form.elements.amount.value;
//   if (amount <= 0) {
//       document.getElementById('result').textContent = `Recharge amount must be a positive number.`;
//       return;
//   }   
//   const message = `Successfully recharged ${mobile} with ${amount} credits.`;
//   document.getElementById('result').textContent = message;
//   form.reset(); // Reset form
// });
const form = document.querySelector('#myForm');
const csrfToken = form.querySelector('input[name="csrfmiddlewaretoken"]').value;
form.addEventListener('submit', (event) => {
  event.preventDefault(); // prevent the form from submitting normally
  const formData = new FormData(form);
  fetch('', {
    method: 'POST',
    body: formData ,
    headers: {
      'X-CSRFToken' : csrfToken
    }
  })
  .then(response =>{
    response.json().then(result=>{
      alert(result.message);
    })
  })
  .catch(error => {
    console.error('Error:', error);
  });
  form.reset();
});