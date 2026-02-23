export function buildInput(type, name = null) {
    const wrapper = document.createElement('div');
    wrapper.className = "input-wrapper";

    let input = null;

    if(type === "tf"){
        input = document.createElement('input');
        input.size = 60;
    } else if(type === "ta") {
        input = document.createElement('textarea');
        input.rows = 10;
        input.cols = 60;
    }

    if(input){
        input.id = name;
    }

    wrapper.appendChild(input);
    return wrapper;
}


export function buildRow(input, labelText, mandatory) {
    const row = document.createElement('div');
    row.className = "row mb-4";

    const label = document.createElement('label');
    label.htmlFor = input.id;
    if(mandatory){
        labelText = labelText + "*";
    }

    label.textContent = labelText;

    const titleCol = document.createElement('div');
    titleCol.className = "col-4 ms-4";
    titleCol.appendChild(label);

    const inputCol = document.createElement('div');
    inputCol.className = `col-6`;
    inputCol.appendChild(input);

    const optionalCol = document.createElement('div');
    optionalCol.className = 'col-2 optional-col';

    row.appendChild(titleCol);
    row.appendChild(inputCol);
    row.appendChild(optionalCol);

    return row;
}


export function buildAddAndDeleteButton(container, box, isFirst, buildFunction, group = null) {
    const buttonRow = document.createElement('div');
    buttonRow.className = "row mb-4";

    const addButton = document.createElement('button');
    addButton.className = "add-button";
    addButton.textContent = "Add new";
    addButton.onclick = function () {
        if(group){
            buildFunction(group, false);
        }else{
            buildFunction(false);  // the next build item is never the first
        }
        addButton.disabled = true;
    }

    box.appendChild(addButton);

    const deleteButton = document.createElement('button');
    deleteButton.textContent = "Delete";
    deleteButton.onclick = function () {
        box.remove();
        if(isFirst){
            if(group){
                buildFunction(group);
            }else{
                buildFunction();  // the build item is always the first
            }
        } else {
            const buttons = container.getElementsByClassName('add-button');
            buttons[buttons.length - 1].disabled = false;
        }
    }
    box.appendChild(deleteButton);
}