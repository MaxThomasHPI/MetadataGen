import {buildCreatorUi} from "../inputFormTemplates/creator.js";
import {loadInputWrapper} from "./loaderHelper.js";


export function loadAllCreatorData(inputData) {
    const container = document.getElementById('creator-container');

    for (const box of container.getElementsByClassName('creator-box')){
        box.remove();
    }

    inputData = inputData["creator"];

    for (let i = 0; i < inputData.length; i++){  // for loop with counter because value and index is needed
        if(i === 0){
            buildCreatorUi();
        } else {
            buildCreatorUi(false);
        }

        const boxes = container.getElementsByClassName("creator-box");

        const box = boxes[boxes.length - 1];
        loadInputWrapper(box, inputData[i]);
    }
}