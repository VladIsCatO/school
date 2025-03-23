var lesson_c = 0
document.getElementById("add_lesson").addEventListener("click", function() {
    lesson_id = document.getElementById("lesson_number").value;
    if (lesson_id){
        lesson_c2 = lesson_id
    }
    else{
    lesson_c2 =  lesson_c + 1;
    lesson_c = lesson_c2; 
    }

    const input1 = document.createElement("input") ;
    input1.placeholder = "enter lesson name" ;
    input1.type = "text" ;
    input1.id = "inp" + lesson_c2 ;
    input1.name = "inp_l";
    
    const label1 = document.createElement("label") ;
    label1.for = "inp" + lesson_c2;
    label1.id = "labl" + lesson_c2 ;
    label1.name = "labl";
    const node = document.createTextNode("Lesson" + lesson_c2);
    label1.appendChild(node);

    const button1 = document.createElement("button") ;
    button1.id = lesson_c2;
    button1.setAttribute("onclick", 'delete_lesson(id)')    
    button1.name = "btns";
    const node1 = document.createTextNode("Delete lesson" + lesson_c2);
    button1.appendChild(node1);


    const element = document.getElementById("lessons");
    element.appendChild(button1);
    element.appendChild(label1);
    element.appendChild(input1);

});

function delete_lesson(lessonc2){
    event.preventDefault()
    console.log(lessonc2)
    const element = document.getElementById("inp" + lessonc2);  element.remove();
    const element1 = document.getElementById("labl" + lessonc2); element1.remove();
    const element2 = document.getElementById(lessonc2); element2.remove();
}