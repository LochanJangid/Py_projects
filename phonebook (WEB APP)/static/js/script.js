lucide.createIcons();

async function fetch_data(q, show_here){
              response = await fetch('/show_contacts?q='+q);
              contacts = await response.text();
              show_here.innerHTML = contacts;
            }

function show_error_msg(form_id, route, msg_div){
    document.getElementById(form_id).addEventListener('submit',function(event){
            event.preventDefault();
            const formData = new FormData(this);
            fetch(route, {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (response.redirected) {
                    window.location.href = response.url
                }
                else{
                    return response.json()
                }
            })
            .then(data => {
                if (data.errors){
                    errors = data.errors
                   for (error in errors){
                        const error_msg = document.createElement('p');
                        error_msg.textContent = errors[error];
                        document.getElementById(msg_div).appendChild(error_msg); 
                   }
                }
                else{
                    // Nothing
                    console.log('Hi ')
                }
            });
        });
}