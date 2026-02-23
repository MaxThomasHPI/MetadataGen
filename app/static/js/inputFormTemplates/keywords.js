import {buildInput, buildRow, buildAddAndDeleteButton} from "../helper.js";


export function buildKeywordsUi(isFirst = true) {
    const container = document.getElementById('keywords-container');

    const box = document.createElement('div');
    box.className = "keywords-box";

    const input = buildInput('tf', "");
    box.appendChild(buildRow(input, "", false));

    container.appendChild(box);

    buildAddAndDeleteButton(container, box, isFirst, buildKeywordsUi);
}