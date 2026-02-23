import {buildKeywordsUi} from "../inputFormTemplates/keywords.js";


export function loadKeywordsData(inputData) {
    const container = document.getElementById('keywords-container');

    for(const box of container.getElementsByClassName('keywords-box')){
        box.remove();
    }

    inputData = inputData["keywords"];

    for(let i = 0; i < inputData.length; i++){
        if (i === 0){
            buildKeywordsUi();
        }else {
            buildKeywordsUi(false);
        }

        //const subContainer = container.querySelector(`#keywords-${i}`);
        const boxes = container.getElementsByClassName('keywords-box');
        const subContainer = boxes[boxes.length - 1];

        const input = subContainer.getElementsByClassName('input-wrapper')[0].children[0];

        input.value = inputData[i];
    }
}