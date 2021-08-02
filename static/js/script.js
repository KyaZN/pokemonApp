/**
 * Sort pokemon list
 * 
 * @param {HTMLTableElement} table table to sort
 * @param {number} column index of the column to sort
 * @param {boolean} asc determines if the sorting is asc or desc
 */


function sortTableByColumn (table, column, asc = true){
    const ordby = asc ? 1 : -1;
    const tBody = table.tBodies[0];
    const rows = Array.from(tBody.querySelectorAll("tr"));

    // sorting
    const sRows = rows.sort((a , b) =>{
        const aContent = isNaN(a.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim())?a.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim():parseInt(a.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim());
        const bContent = isNaN(b.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim())?b.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim():parseInt(b.querySelector(`td:nth-child(${ column + 1 })`).textContent.trim());

        return aContent > bContent ? (1 * ordby) : (-1 * ordby);
    });  

    // remove rows
    while (tBody.firstChild){
        tBody.removeChild(tBody.firstChild)
    }

    // rearange rows as sort order
    tBody.append(...sRows);

    // add class for type of sorting
    table.querySelectorAll("th").forEach(th => th.classList.remove("th-sort-asc","th-sort-desc"));
    table.querySelector(`th:nth-child(${ column + 1})`).classList.toggle("th-sort-asc", asc);
    table.querySelector(`th:nth-child(${ column + 1})`).classList.toggle("th-sort-desc", !asc);



}

// sortTableByColumn(document.querySelector("table"),1,false);

document.querySelectorAll(".table-sortable th").forEach(headerCell => {
    headerCell.addEventListener("click", () => {
        const tableElement = headerCell.parentElement.parentElement.parentElement;
        const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
        const currentState = headerCell.classList.contains("th-sort-asc");

        sortTableByColumn(tableElement,headerIndex,!currentState); 
    })
})
