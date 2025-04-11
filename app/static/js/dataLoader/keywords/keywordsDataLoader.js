import {buildKeywordsUi} from "../../ui/keywords/keywordsUiBuilder.js";

export function loadKeywordsData(inputData) {
    const container = document.getElementById('keywords-container');

    for(const box of container.getElementsByClassName('keywords-box')){
        box.remove();
    }

    inputData = inputData["keywords"];

    for(let i = 0; i < inputData.length; i++){
        buildKeywordsUi(i);
        const subContainer = container.querySelector(`#keywords-${i}`);

        const input = subContainer.getElementsByClassName('input-wrapper')[0].children[0];

        input.value = inputData[i];
    }
}