import {buildRow} from "../helper.js";
import {findDataSet} from "../../interactionAPI/APIInteractor.js";

export async function buildCourseInfo(container, shortCode) {
    let courseData = await findDataSet(shortCode);

    if(Object.keys(courseData).length === 0){
        alert("No course with this short code!");
        return null;
    }

    courseData = courseData["attributes"];

    const titleLabel = document.createElement('label');
    titleLabel.textContent = "Course Title";
    titleLabel.htmlFor = "titlePres";

    const titlePresentation = document.createElement('p');
    titlePresentation.id = "titlePres";
    titlePresentation.innerText = courseData["name"];

    container.appendChild(buildRow(titleLabel, titlePresentation));

    const descriptionLabel = document.createElement('label');
    descriptionLabel.textContent = "Course Description";
    descriptionLabel.htmlFor = "descPres";

    const descriptionPresentation = document.createElement('p');
    descriptionPresentation.id = "descPres";
    descriptionPresentation.innerText = courseData["description"];

    container.appendChild(buildRow(descriptionLabel, descriptionPresentation));

    return courseData;
}