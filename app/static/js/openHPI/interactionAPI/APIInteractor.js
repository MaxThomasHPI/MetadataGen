export async function findDataSet(shortCode) {
    const url = `/get_course_by_short_code?shortCode=${shortCode}`;

    return await fetch(url)
        .then(response => {
            if(!response.ok){
                throw new Error('Error while getting course by short code!');
            }
            return response.json();
        })
        .catch(error => {
            console.error(error);
    });
}





/*
export function findDataSet(shortCode) {
    let url = "https://open.hpi.de/bridges/moochub/courses";

    let data = loadDataSet(url);

    let currentPage = parseInt(data["links"]["self"].split("=")[1]);
    const maxPage = parseInt(data["links"]["last"].split("=")[1]);

    let course = extractCourse(data, shortCode);

    while (!course && currentPage <= maxPage){
        url = data["links"]["next"];

        data = loadDataSet(url);
        course = extractCourse(data, shortCode);

        currentPage = parseInt(data["links"]["self"].split("=")[1]);
    }

    return course;
}


async function loadDataSet(url) {

    return await fetch(url)
        .then(response => {
            if(!response.ok){
                throw new Error('Error while loading openHPI courses!');
            }
            return response.json();
        })
        .catch(e => {
            console.error(e);
        });

}

function extractCourse(data, shortCode) {
    const courses = data["data"];

    for (const course of courses){
        if(course["attributes"]["courseCode"] === shortCode){
            return course
        }
    }

    return null;
}
*/


