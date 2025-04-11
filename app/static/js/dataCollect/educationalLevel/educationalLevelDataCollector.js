export function collectEducationalLevel(data) {
    const selectedFramework = document.getElementById('educationalLevelFramework-select').textContent;
    const selectedEducationalLevel = document.getElementById('educationalLevel-select');

    if(selectedEducationalLevel.value !== ""){
        data["educationalLevel"] = {
            "name": selectedEducationalLevel.value,
            "educationalFramework": selectedFramework
        }
    }

    return data;
}