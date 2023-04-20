const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const form = document.getElementById('my-form');
const csrfToken = form.querySelector('input[name="csrfmiddlewaretoken"]').value;

// Get access to the user's webcam

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  });
  const rd=document.getElementById("response");
  const user1x='<h2 class=\"card-title\"> Thank You ';
  const user1e='<h2 class=\"card-title\"> Proceed ';
  const user2x='</h2><h2 class=\"card-title\">Visit Again</h2>';
  const user2e='</h2><h5>Enjoy the ride and cherish the memories</h5>';
  const spinning='<h1>Capturing...</h1><div class=\"spinner-border\" role=\"status\"><span class=\"sr-only\">Loading...</span></div> ';
  const unknown='<h2 class=\"card-title\">Unknown User</h2> <p> Please Register At your nearest Registration Desk.</p>';
  const nobal1='<h2 class=\"card-title\"> ';
  const nobal='</h2><h2 class=\"card-title\">Insufficient Balance Please Recharge</h2>';
  // Take a photo when the capture button is clicked
function upload(){
  const context = canvas.getContext('2d');
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  const imageData = canvas.toDataURL('image/png');
  const blob = dataURItoBlob(imageData);
  const formData = new FormData();
  formData.append('image', blob, 'myimage.png');
  // Send the photo to the server using a POST request
  fetch('', {
    method: 'POST',
    body: formData ,
    headers: {
      'X-CSRFToken': csrfToken
    }
  })
  .then(response=>{
      response.json().then(result=>{
        if(result.name=="capturing"){
          rd.classList.remove("bg-success");
          rd.classList.remove("bg-danger");
          rd.classList.remove("bg-warning");
          rd.classList.add("bg-secondary");
          rd.innerHTML=spinning;
        }else if(result.name=="unknown"){
          rd.classList.remove("bg-secondary");
          rd.classList.remove("bg-success");
          rd.classList.remove("bg-danger");
          rd.classList.add("bg-warning");
          rd.innerHTML=unknown;
        }else if(result.name=="nobal"){
          rd.classList.remove("bg-secondary");
          rd.classList.remove("bg-success");
          rd.classList.remove("bg-warning");
          rd.classList.add("bg-danger");
          rd.innerHTML=nobal1+result.sec+nobal
        }else{
          rd.classList.remove("bg-secondary");
          rd.classList.remove("bg-danger");          
          rd.classList.remove("bg-warning");
          rd.classList.add("bg-success");
          if(result.stat=='e'){  
            rd.innerHTML=user1e+result.name+user2e;
          }else{
            rd.innerHTML=user1x+result.name+user2x;
          }
        }
      })
  })
  .catch(error => {
    console.error(error);
  });
  
};

function dataURItoBlob(dataURI) {
    const byteString = atob(dataURI.split(',')[1]);
    const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
    }
    return new Blob([ab], { type: mimeString });
  }

setInterval( upload,2000);