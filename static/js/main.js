document.addEventListener('DOMContentLoaded', () => {
    let receiver_div = document.querySelector('#div_id_entire_team');
    receiver_div.classList.add('mt-2');

    let check_box = document.querySelector('#id_entire_team');
    let receiver = document.querySelector('#div_id_receiver');


    check_box.addEventListener('change',()=>{
        if(check_box.checked){
            receiver.style.display = 'none';
        }
        else{
            receiver.style.display = 'block';
        }
    })
    
});