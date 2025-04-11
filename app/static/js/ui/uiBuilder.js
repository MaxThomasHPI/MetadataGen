import {buildGeneralUi} from "./general/generalUiBuilder.js";
import {buildLicenseUi} from "./general/licenseUiBuilder.js";
import {buildPublisherUi} from "./publisher/publisherUiBuilder.js";
import {buildCreatorUi} from "./creator/creatorUiBuilder.js";
import {buildEducationalAlignmentUi} from "./educationaAlignment/educationalAlignmentUiBuilder.js";
import {buildTeachesUi} from "./teaches/teachesUiBuilder.js";
import {buildKeywordsUi} from "./keywords/keywordsUiBuilder.js";
import {buildEducationalLevelUi} from "./educationalLevel/educationalLevelUiBuilder.js";

import {submitData} from "../dataExchange/dataSender.js";
import {isInputDataValid} from "../dataCheck/dataChecker.js";


const headlineAssignment = {
    "general-container": "General Information",
    "license-container": null,
    "publisher-container": "Publisher",
    "creator-container": "Creator",
    "edAlign-container": "Educational Alignment",
    "teaches-container": "Competencies & Skills (teaches)",
    "keywords-container": "Keywords",
    "educationalLevel-container": "educational Level"
};

export function buildUI() {
    const container = document.getElementById('main_window');
    buildUIContainer(container);

    buildGeneralUi();
    buildLicenseUi();
    buildPublisherUi();
    buildCreatorUi(0);
    buildEducationalAlignmentUi();
    buildTeachesUi(0);
    buildKeywordsUi(0);
    buildEducationalLevelUi();

    buildSubmitButton(container);
}

function buildUIContainer(container) {
    for (const key in headlineAssignment){
        const subContainer = document.createElement('div');
        subContainer.id = key;

        if(headlineAssignment[key]){
            const headline = document.createElement('h2');
            headline.textContent = headlineAssignment[key];
            subContainer.appendChild(headline);
        }
        container.appendChild(subContainer);
    }
}


function buildSubmitButton(container){
    const row = document.createElement('div');
    row.className = "row";

    const submitButton = document.createElement('button');
    submitButton.textContent = "Generate Metadata";
    submitButton.onclick = function () {
        if(isInputDataValid()) {
            const submitted = submitData();

            if(submitted){
                console.log("Metadata submitted");

            }
        } else {
            alert("Invalid input data! Please check!");
        }

    }

    row.appendChild(submitButton);

    container.appendChild(row);
}