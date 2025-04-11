export function loadEducationalAlignmentData(inputData) {
    const frameworkSelector = document.getElementById('educationalAlignment-select-0');
    const selectedLabel = document.getElementById('selected-educationalAlignment-0');

    inputData = inputData["educationalAlignment"][0];

    const framework = inputData["educationalFramework"];
    const name = `${inputData["name"][0]["name"]}@${inputData["educationalFramework"]}`;

    frameworkSelector.value = framework;
    frameworkSelector.onchange();
    selectedLabel.textContent = name;
}