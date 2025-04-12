var lesson_c = 0;

function deleteLesson(lessonId) {
    document.getElementById("row" + lessonId).remove();
}

document.getElementById("add_lesson").addEventListener("click", function() {
    let lesson_id = document.getElementById("lesson_number").value;
    if (lesson_id) {
        lesson_c2 = lesson_id;
    } else {
        lesson_c2 = lesson_c + 1;
        lesson_c = lesson_c2;
    }

    const tableRow = document.createElement("tr");
    tableRow.id = "row" + lesson_c2;

    const lessonNumberCell = document.createElement("td");
    const lessonNumberInput = document.createElement("input");
    lessonNumberInput.type = "number";
    lessonNumberInput.name = "lesson_number";
    lessonNumberInput.value = lesson_c2;
    lessonNumberCell.appendChild(lessonNumberInput);

    const lessonNameCell = document.createElement("td");
    const input = document.createElement("input");
    input.type = "text";
    input.name = "lesson_name";
    input.placeholder = "Введіть назву уроку";
    lessonNameCell.appendChild(input);

    const actionCell = document.createElement("td");
    const deleteButton = document.createElement("button");
    deleteButton.classList.add("delete-btn");
    deleteButton.textContent = "Видалити";
    deleteButton.onclick = function() {
        deleteLesson(lesson_c2);
    };
    actionCell.appendChild(deleteButton);

    tableRow.appendChild(lessonNumberCell);
    tableRow.appendChild(lessonNameCell);
    tableRow.appendChild(actionCell);

    document.getElementById("lessons").appendChild(tableRow);
});