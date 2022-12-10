async function loadIntoTable(url, table) {
    const response = await fetch(url);
    const data = await response.json();
    let jsonData = JSON.parse(data);
    setupTableHeaders(table, jsonData.headers);
    setupTableBody(table, jsonData.data);
}

function setupTableHeaders(table, headers) {
    const tableHead = table.querySelector("thead");
    tableHead.innerHTML = "<tr></tr>";
    for (let headerText of headers) {
        const headerElement = document.createElement("th");
        headerElement.textContent = headerText;
        tableHead.querySelector("tr").appendChild(headerElement);
    }
}

function setupTableBody(table, data) {
    const tableBody = table.querySelector("tbody");
    tableBody.innerHTML = "";
    const rowElement = document.createElement("tr");
    setupCellText(rowElement, data)
    tableBody.appendChild(rowElement);
}

function setupCellText(rowElement, data) {
    for (let cellText of data) {
        const cellElement = document.createElement("td");
        cellElement.textContent = cellText
        rowElement.appendChild(cellElement);
    }
}


function fetchPhoneData() {
    console.log("Getting Car Data")
    loadIntoTable("http://localhost:8000/api/task/1",
        document.querySelector(".phoneTable"))
}

function fetchCarData() {
    console.log("Getting Car Data")
    loadIntoTable("http://localhost:8000/api/task/2",
        document.querySelector(".carTable"))

}