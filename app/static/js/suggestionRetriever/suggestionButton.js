import {buildRow} from "../helper.js";
import {collectData} from "../dataCollection/dataCollector.js";
import {retrieveSuggestion} from "./SuggestionAPIConnector.js";
import {loadData} from "../metadataLoader/loadingManager.js";


export function buildSuggestionButton() {
    const container = document.getElementById('suggestionButton-container');
    const button = document.createElement('button');
    button.textContent = "Generate suggestion";
    button.id = "suggest-btn";

    button.onclick = async function () {
        const data = collectData();
        if(data){
            if(!data.hasOwnProperty("keywords")){
                data["keywords"] = null;
            }

            const suggestion = await retrieveSuggestion(data);
            await loadData(suggestion);
        }
    }
    container.appendChild(buildRow(button, "", false));
}
