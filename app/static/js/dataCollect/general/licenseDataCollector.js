export function collectLicenseData(data) {
    const container = document.getElementById('license-container');
    const inputs = container.getElementsByClassName('input-wrapper')[0];

    const dropdown = inputs.children[0];

    data["license"] = {
        "identifier": dropdown.options[dropdown.selectedIndex].text,
        "url": dropdown.value
    };
    return data;
}