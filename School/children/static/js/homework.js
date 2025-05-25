console.log("start")
function RequestToServer(form, url) {
    const formData = new FormData(form);
    console.log('Я RequestToServer');
    formData.append('key1', 'value1');

    return new Promise((resolve, reject) => {
        fetch(url, {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            resolve(data);
        });
    });
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function homework_pop_up2(index_f) {
    console.log(111, index_f)

    const subject = document.getElementById(`subject_hidden_${index_f}`).value;
    const homework = document.getElementById(`homework_hidden_${index_f}`).value;
    const deadline = document.getElementById(`deadline_hidden_${index_f}`).value;
    const group_name = document.getElementById(`group_hidden_${index_f}`).value;


    document.getElementById("group_homework_popup").innerText  = "group:" + group_name;
    document.getElementById("subject_homework_popup").innerText  = "subject:" + subject;
    document.getElementById("deadline_homework_popup").innerText  = "deadline:" + deadline;
    document.getElementById("dz_homework_popup").innerText  = "homework:" + homework;

    document.querySelector("#homework_send_id").value = index_f;

    document.querySelector(".popup-container2").classList.add("active");
};

function closePopup2() {
    console.log(222)
    document.querySelector(".popup-container2").classList.remove("active");
}

function find_js(){
    console.log("322222222222222223", document.getElementById('homework_info_all').value)
    const request_sub = document.getElementById("homework_find").value
    document.getElementById("info1").style.display = 'none';
    document.getElementById("info2").style.display = 'block';
    const homework_info_all = JSON.parse(document.getElementById('homework_info_all').value);
    const last_div = document.getElementById("info2");
    if (homework_info_all.length == 0) {
        clear_find()}
    for (const dz of homework_info_all) {
        console.log(dz.subject, request_sub, 212)
         if(dz.subject.includes(request_sub)){// dz.subject.toUpperCase().includes(request_sub.toUpperCase())
            console.log(dz.subject, request_sub, 212)

    last_div.innerHTML = `
                        <div id="homework_infos">
                                
                                    <div class="homework_info">
                                        <div id="lesson_data" class="lesson_data">
                                            <p>Lesson:</p>
                                            <p id="subject" >${dz.subject}</p>
                                        </div>
                                        
                                        <div id="homework_data" class="homework_data">
                                            <p>homework:</p>
                                            <p class="homework_text" >${dz.text}</p>
                                        </div>
    
                                        <div id="deadline_data" class="deadline_data">
                                            <p style="color: red;">deadline:</p>
                                            <p id="deadline_display">${dz.deadline}</p>
                                        </div>
                                        <button type="button" onclick="homework_pop_up2('${dz.id}')">details</button>
                                    </div>
                                    
    
    
                            </div>    
    
    `;break
}}

};

function clear_find(){
    // console.log(clear)
    document.getElementById("info1").style.display = 'block';
    document.getElementById("info2").style.display = 'none';
    document.getElementById("homework_find").value = ""
}


function log_out_pop_up(index_f) {
    document.getElementById("log_out").style.display = "block"
    console.log(333)
};

function closePopup_logout() {
    console.log(222)
    document.getElementById("log_out").style.display = "none"
}