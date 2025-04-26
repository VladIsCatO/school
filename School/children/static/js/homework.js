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

    const subject = document.getElementById(`subject_hidden_${index_f}`).value
    const homework = document.getElementById(`homework_hidden_${index_f}`).value
    const deadline = document.getElementById(`deadline_hidden_${index_f}`).value
    const group_name = document.getElementById(`group_hidden_${index_f}`).value


    document.getElementById("group_homework_popup").innerText  = "group:" + group_name
    document.getElementById("subject_homework_popup").innerText  = "subject:" + subject
    document.getElementById("deadline_homework_popup").innerText  = "deadline:" + deadline
    document.getElementById("dz_homework_popup").innerText  = "homework:" + homework

    document.querySelector(".popup-container2").classList.add("active");
};

function closePopup2() {
    console.log(222)
    document.querySelector(".popup-container2").classList.remove("active");
}

function find_homework(){
    const document.getElementById("homework_find").value
    const document.getElementById("info1").style.display = none;
    const document.getElementById("info2");
    

}