export function buildRow(element1, element2){
    const row = document.createElement('div');
    row.className = "row mb-4";
    row.id = "title-row";

    const col1 = document.createElement('div');
    col1.className = "col-4 ms-4";

    const col2 = document.createElement('div');
    col2.className = "col-6";

    col1.appendChild(element1);
    col2.appendChild(element2);

    row.appendChild(col1);
    row.appendChild(col2);

    return row;
}