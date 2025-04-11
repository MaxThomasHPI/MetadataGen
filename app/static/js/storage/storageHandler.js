const templates = {};
const frameworks = {};

const licenses = new Map();
licenses.set("proprietary", null);
licenses.set("CC0-1.0", "https://spdx.org/licenses/CC0-1.0.html");
licenses.set("CC-BY-4.0", "https://spdx.org/licenses/CC-BY-4.0.html");
licenses.set("CC-BY-NC-4.0", "https://spdx.org/licenses/CC-BY-NC-4.0.html");
licenses.set("CC-BY-SA-4.0", "https://spdx.org/licenses/CC-BY-SA-4.0.html");
licenses.set("CC-BY-NC-SA-4.0", "https://spdx.org/licenses/CC-BY-NC-SA-4.0.html");
licenses.set("CC-BY-NC-ND-4.0", "https://spdx.org/licenses/CC-BY-NC-ND-4.0.html");


export function storeData(dataTemplates, dataFrameworks) {
    for(const key of Object.keys(dataTemplates)){
        templates[key] = dataTemplates[key];
    }

    for(const key of Object.keys(dataFrameworks)){
        frameworks[key] = dataFrameworks[key];
    }
}

export function getTemplates() {
    return templates;
}

export function getFrameworks() {
    return frameworks;
}


export function getLicenses() {
    return licenses;
}