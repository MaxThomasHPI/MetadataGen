import {buildRow} from "./helper.js";
import {getESCOFragment} from "../../dataExchange/templateFrameworkDownloader.js";

export function buildFrameworkSelect(frameworks, container, purpose, number) {
    const frameworkSelect = document.createElement('select');
    frameworkSelect.id = `${purpose}-select-${number}`;

    for (const key of Object.keys(frameworks)){
        const option = document.createElement('option');
        option.textContent = key;
        option.value = key;

        frameworkSelect.appendChild(option);
    }

    container.appendChild(buildRow(frameworkSelect, "framework", false));

    let frameworkName = frameworkSelect.value;
    let selectedFramework = frameworks[frameworkName];
    const accordionContainer = document.createElement('div');

    buildTree(accordionContainer, selectedFramework, 0, purpose, number);

    frameworkSelect.onchange = function () {
        for (const c of accordionContainer.children) {
            c.remove();
        }
        frameworkName = frameworkSelect.value;
        selectedFramework = frameworks[frameworkName];
        if(frameworkName === "ESCO"){
            buildESCOTree(accordionContainer, selectedFramework, 0, purpose, number);
        }else{
            buildTree(accordionContainer, selectedFramework, 0, purpose, number);
        }
    }

    const row = buildRow(accordionContainer, `Select ${purpose}`,false, 6);
    container.appendChild(row);

    const selected = document.createElement('p');
    selected.id = `selected-${purpose}-${number}`;
    selected.className = `selected-${purpose}`;
    selected.textContent = "None selected";
    container.appendChild(buildRow(selected, "Selected", false));
}


function buildTree(container, entries, level, purpose, number) {
    const subContainer = document.createElement('div');
    subContainer.className = 'accordion';
    subContainer.id = `accordion-${purpose}-${number}`;
    level++;

    for (const entry of Object.keys(entries)){
        if(Object.keys(entries[entry])[0] !== "shortCode"){
            const name = entry.replace(/(\s|\(|\)|\/|;|,)/g, '_');

            const item = document.createElement('div');
            item.className = 'accordion-item';

            const header = document.createElement('h2');
            header.className = 'accordion-header';

            const btn = document.createElement('button');
            btn.className = "accordion-button collapsed";
            btn.textContent = entry;

            btn.setAttribute("data-bs-toggle", "collapse");

            header.appendChild(btn);
            item.appendChild(header);

            const collapse = document.createElement('div');
            collapse.className = "accordion-collapse collapse";
            collapse.id = `collapse-${name}-${level}-${number}`;
            btn.setAttribute("data-bs-target", `#${collapse.id}`);
            btn.setAttribute("aria-expanded", "false");
            btn.setAttribute("aria-controls", collapse.id);

            collapse.setAttribute("aria-labelledby", collapse.id);
            collapse.setAttribute("data-bs-parent", subContainer.id);

            const body = document.createElement('div');
            body.className = "accordion-body";
            buildTree(body, entries[entry], level, purpose, number);

            collapse.appendChild(body);
            item.appendChild(collapse);

            subContainer.appendChild(item);
        } else {
            const btn = document.createElement('button');
            btn.textContent = 'Select';
            btn.onclick = function () {
                const selected = document.getElementById(`selected-${purpose}-${number}`);
                const framework = document.getElementById(`${purpose}-select-${number}`).value;

                selected.textContent = `${entry}@${framework}`;
            }

            const row = buildRow(btn, entry, false);
            subContainer.appendChild(row);
        }
    }
    container.appendChild(subContainer);
}


function buildESCOTree(container, entries, level, purpose, number) {
    const subContainer = document.createElement('div');
    subContainer.className = 'accordion';
    subContainer.id = `accordion-${purpose}-${number}`;
    level++;

    for(const entry of Object.keys(entries)){
        if(entries[entry]['hasNarrower']){
            const name = entry.replace(/\s/g, '_');
            const item = document.createElement('div');
            item.className = 'accordion-item';

            const header = document.createElement('h2');
            header.className = 'accordion-header';

            const btn = document.createElement('button');
            btn.className = 'accordion-button collapsed';
            btn.textContent = entry;
            btn.setAttribute('data-bs-toggle', 'collapse');

            header.appendChild(btn);
            item.appendChild(header);

            const collapse = document.createElement('div');
            collapse.className = 'accordion-collapse collapse';
            collapse.id = `collapse-${name}-${level}-${number}`;

            btn.setAttribute('data-bs-target', `#${collapse.id}`);
            btn.setAttribute('aria-expended', 'false');
            btn.setAttribute('aria-controls', collapse.id);

            collapse.setAttribute('aria-labelledby', collapse.id);
            collapse.setAttribute('data-bs-parent', subContainer.id);

            const body = document.createElement('div');
            body.className = 'accordion-body';

            btn.onclick = async function () {
                if(body.children.length === 0){
                    const fragment = await getESCOFragment(entries[entry]['uri']);

                    buildESCOTree(body, fragment, level, purpose, number);
                }
            }

            const selectBtn = buildSelectButton(purpose, number, entry, entries[entry]['uri']);

            collapse.appendChild(body);
            item.appendChild(collapse);

            subContainer.appendChild(item);

            const p = document.createElement('p');
            p.setAttribute('align', 'right');
            p.appendChild(selectBtn);

            item.appendChild(p);
            collapse.addEventListener('show.bs.collapse', () => {
                selectBtn.style.display = 'none';
            });
            collapse.addEventListener('hidden.bs.collapse', () => {
                selectBtn.style.display = 'block';
            });
        } else {
            const btn = buildSelectButton(purpose, number, entry, entries[entry]['uri']);

            const row = buildRow(btn, entry, false);
            subContainer.appendChild(row);
        }
    }
    container.appendChild(subContainer);
}


function buildSelectButton(purpose, number, entry, uri) {
    const selectBtn = document.createElement('button');
    selectBtn.textContent = 'Select';
    selectBtn.setAttribute('style', "float:right;");
    selectBtn.onclick = function () {
        const selected = document.getElementById(`selected-${purpose}-${number}`);
        const framework = document.getElementById(`${purpose}-select-${number}`).value;

        selected.textContent = `${entry}@${framework}`;
        selected.setAttribute('conceptUrl', uri);
    }
    return selectBtn
}