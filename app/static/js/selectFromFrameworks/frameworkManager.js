import {getAllToplevel} from "./frameworkDataHandler.js";

let frameworks = null;


export async function storeAllToplevel() {
    frameworks = await getAllToplevel();
}


export function getFrameworks(group) {
    return frameworks[group]
}