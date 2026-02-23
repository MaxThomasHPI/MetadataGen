import {buildInput, buildRow} from "../helper";


export function buildBaseInput(container, template){
    for (const field of template){
        const id = field["id"];
        const label = field["label"];
        const type = field["type"];
        const mandatory = field["mandatory"];

        const input = buildInput(type, id);
        container.appendChild(buildRow(input, label, mandatory));
    }
}
