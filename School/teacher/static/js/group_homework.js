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


// document.querySelector("#send_homework").addEventListener("click", function(e) {
//     e.preventDefault();
//     const form = document.querySelector("#pop_up_homework_f")
//     console.log(211)
//     RequestToServer( form, "/teacher/group/").then(data => {
//         console.log(332211)
//         if (data.res == "Щось пішло не так") {
//             console.log(data)
//         } else {
//             document.querySelector(".popup-container").classList.remove("active");
//             alert("домашнє було успішго додано")
//         }
//     }).catch(error => console.error(error));
// });



function homework_pop_up() {
    console.log(111)
    document.querySelector(".popup-container").classList.add("active");
};
function closePopup() {
    console.log(222)
    document.querySelector(".popup-container").classList.remove("active");
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