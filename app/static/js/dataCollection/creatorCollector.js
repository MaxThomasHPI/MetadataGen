//import {isEmpty} from "../dataCheck/checkHelper.js";
import {collectInputWrapper} from "./collectorHelper.js";


export function collectCreatorData(data){
    const container = document.getElementById(`creator-container`);
    const boxes = container.getElementsByClassName(`creator-box`);

    //const dataFragments = [];
    data["creator"] = [];
    for (const box of boxes){
        const dataFragment = {};
        collectInputWrapper(box, dataFragment);
        data["creator"].push(dataFragment);
        /**
        const inputs = box.getElementsByClassName('input-wrapper');
        const dataFragment = {};

        for (const input of inputs){
            const value = input.children[0].value;

            if(value !== ''){
                dataFragment[input.children[0].id] = value;
            }
        }**/
        //if(!isEmpty(dataFragment)){
        //    dataFragments.push(dataFragment);
        //}
    }
    //if(!isEmpty(dataFragments)){
    //    data["creator"] = dataFragments;
    //}
}