import {buildAddAndDeleteButton, buildInput, buildRow} from "../helper/helper.js";
import {collectGeneralData} from "../../dataCollect/general/generalDataCollector.js";
import {askForKeywordsSuggestion} from "../../dataExchange/aiInteraction/keywordsAiInteracter.js";
import {loadKeywordsData} from "../../dataLoader/keywords/keywordsDataLoader.js";

export function buildKeywordsUi(number) {
    const container = document.getElementById('keywords-container');

    const box = document.createElement('div');
    box.className = "keywords-box";
    box.id = `keywords-${number}`;

    const keywordLabel = `keyword ${number+1}`;
    const input = buildInput('tf', keywordLabel);
    box.appendChild(buildRow(input, keywordLabel, false));

    container.appendChild(box);

    buildAddAndDeleteButton(container, box, number, buildKeywordsUi);

    if(number === 0){
        buildSuggestionButton(container);
    }

}


function buildSuggestionButton(container) {  // add this at the top: 10 suggestions will be made, all 10 shall be shown
                                            // separate boxes!
    const optCol = container.getElementsByClassName('optional-col')[0];

    const btn = document.createElement('button');
    btn.textContent = "Get Suggestion";

    btn.onclick = async function () {
        const generalData = collectGeneralData({});
        const suggestion = await askForKeywordsSuggestion(generalData["name"], generalData["description"]);

        loadKeywordsData(suggestion);
    }

    optCol.appendChild(btn);
}
