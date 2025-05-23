import {isEmpty} from "../../helper.js";

export function collectCreatorData(data){
    const container = document.getElementById(`creator-container`);
    const boxes = container.getElementsByClassName(`creator-box`);

    const dataFragments = [];

    for (const box of boxes){
        const inputs = box.getElementsByClassName('input-wrapper');
        const dataFragment = {};

        for (const input of inputs){
            const value = input.children[0].value;

            if(value !== ''){
                dataFragment[input.children[0].id] = value;
            }
        }
        if(!isEmpty(dataFragment)){
            dataFragments.push(dataFragment);
        }
    }
    if(!isEmpty(dataFragments)){
        data["creator"] = dataFragments;
    }
    return data;
}