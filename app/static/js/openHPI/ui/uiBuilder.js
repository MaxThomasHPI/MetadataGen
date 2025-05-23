import {buildCourseInfo} from "./courseInfo/courseInfoBuilder.js";
import {buildEducationalAlignmentUi} from "./educationaAlignment/educationalAlignmentUiBuilder.js";
import {buildTeachesUi} from "./teaches/teachesUiBuilder.js";
import {build_metadata} from "../dataExchange/dataSender.js";

const containers = {
    "edAlign-container": buildEducationalAlignmentUi,
    "teaches-container": buildTeachesUi
}


export async function buildUI(shortCode) {
    const container = document.getElementById('main-window');

    while (container.children.length > 0){
        container.children[0].remove();
    }

    const foundCourse = await buildCourseInfo(container, shortCode);

    if(!foundCourse){
        return
    }
    for(const key of Object.keys(containers)){
        const subContainer = document.createElement('div');
        subContainer.id = key;

        const headline = document.createElement('h2');
        headline.textContent = key.replace("-container", "");
        subContainer.appendChild(headline);

        container.appendChild(subContainer);
        containers[key](foundCourse);
    }

    const sendBtn = document.createElement('button');
    sendBtn.textContent = "Generate Fragments";
    sendBtn.onclick = function () {
        build_metadata();
    }
    container.appendChild(sendBtn);
}