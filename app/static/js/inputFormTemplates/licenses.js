import {buildRow} from "../helper.js";

const licenses = {
    "proprietary": null,
    "CC0-1.0": "https://spdx.org/licenses/CC0-1.0.html",
    "CC-BY-4.0": "https://spdx.org/licenses/CC-BY-4.0.html",
    "CC-BY-NC-4.0": "https://spdx.org/licenses/CC-BY-NC-4.0.html",
    "CC-BY-SA-4.0": "https://spdx.org/licenses/CC-BY-SA-4.0.html",
    "CC-BY-NC-SA-4.0": "https://spdx.org/licenses/CC-BY-NC-SA-4.0.html",
    "CC-BY-NC-ND-4.0": "https://spdx.org/licenses/CC-BY-NC-ND-4.0.html"
};


export function buildLicenseUi() {
    const container = document.getElementById("license-container");

    const label = "license";
    const input_id = "identifier";

    const wrapper = document.createElement('div');
    wrapper.className = "input-wrapper";

    const input = document.createElement('select');
    input.className = "form-select-lg mb-3";

    for(const name in licenses){
        const option = document.createElement('option');
        option.textContent = name;
        option.value = licenses[name];
        input.appendChild(option);
    }

    if(input){
        input.id = input_id;
    }

    wrapper.appendChild(input);

    container.appendChild(buildRow(wrapper, label, true));
}