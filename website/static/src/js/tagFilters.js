const tagArray = [];
const selectedArray = [];

const clickedClass = "flex items-center rounded-2xl border-2 border-gray-700 bg-gray-700 dark:border-slate-200 dark:bg-slate-200 w-fit h-full px-2"
const clickedClass_text = "text-sm text-gray-100 dark:text-gray-700 "
const emptyClass = "flex items-center rounded-2xl border-2 border-gray-700 dark:border-slate-200 w-fit h-full px-2"
const emptyClass_text = "text-sm text-gray-700 dark:text-gray-100"


// Creates the HTML snippets for the tags
function tagCreator(tagName) {
    snippet = 
        `<a id="filter_${tagName}" href="javascript:toggleFilter('${tagName}')"><div class="${emptyClass}">
            <p class="text-sm">${tagName}</p>
        </div></a>`;

    return snippet
}

function toggleFilter(tag) {
    console.log("Toggling");
    selectedArray[tagArray.indexOf(tag)] = !selectedArray[tagArray.indexOf(tag)];

    if (selectedArray[tagArray.indexOf(tag)]) {
        document.getElementById(`filter_${tag}`).children[0].className = clickedClass
        document.getElementById(`filter_${tag}`).children[0].children[0].className = clickedClass_text
    } else {
        document.getElementById(`filter_${tag}`).children[0].className = emptyClass
        document.getElementById(`filter_${tag}`).children[0].children[0].className = emptyClass_text
    }

    updateCards();
}

// Function called from HTML to register the tag names with this code
function registerTags(tag) {
    tagArray[tagArray.length] = tag;
    selectedArray[selectedArray.length] = false;
}

// Function that creates the HTML elements that are clicked on to filter
function createFilters() {
    for (let i=0; i<tagArray.length; i++) {
        document.getElementById("filterContainer").innerHTML += tagCreator(tagArray[i])
    }

}

// Function that updates the list of cards (called when filters clicked)
function updateCards() {
    console.log(tagArray);
    console.log(selectedArray);

    cards = document.getElementById("cardContainer").children

}