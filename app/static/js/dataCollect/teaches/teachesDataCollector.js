import {isEmpty} from "../../helper.js";

export function collectTeachesData(data) {
    const container = document.getElementById(`teaches-container`);
    const boxes = container.getElementsByClassName(`teaches-box`);

    const dataFragments = [];

    for (const box of boxes){
        const inputs = box.getElementsByClassName(`selected-teaches`);
        let dataFragment = {};

        for (const input of inputs){
            const selected = input.textContent;
            const name = selected.split("@")[0];

            if(name === "None selected"){
                continue;
            }

            const framework = selected.split("@")[1];
            let uri = input.getAttribute('conceptUrl');

            dataFragment = {
                "name": name,
                "educationalFramework": framework
            }
            if(uri){
                dataFragment["conceptUrl"] = uri;
            }
        }
        if(!isEmpty(dataFragment)){
            dataFragments.push(dataFragment);
        }
    }
    if(!isEmpty(dataFragments)){
        data["teaches"] = dataFragments;
    }
    return data;
}