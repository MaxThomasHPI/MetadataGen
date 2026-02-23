export function loadLicenseData(inputData) {
    const container = document.getElementById('license-container');
    const input = container.querySelector(`#identifier`);

    input.value = inputData["license"][0]["url"];
}