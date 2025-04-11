export function loadEducationalLevelData(inputData) {
    const frameworkSelector = document.getElementById('educationalLevelFramework-select');

    inputData = inputData["educationalLevel"][0];

    const framework = inputData["educationalFramework"];
    const level = inputData["name"][0]["name"];

    frameworkSelector.value = framework;
    frameworkSelector.onchange();

    const selectedLevel = document.getElementById('educationalLevel-select');
    selectedLevel.value = level;
}