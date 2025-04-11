import {isEmpty} from "../../helper.js";

export function collectKeywordsData(data) {
    const container = document.getElementById(`keywords-container`);
    const boxes = container.getElementsByClassName(`keywords-box`);

    const dataFragments = [];

    for (const box of boxes){
        const inputs = box.getElementsByClassName('input-wrapper');
        const keyword = inputs[0].children[0].value;

        if(!(keyword === '')){
            dataFragments.push(keyword);
        }

    }

    if(!isEmpty(dataFragments)){
        data["keywords"] = dataFragments;
    }

    return data;
}