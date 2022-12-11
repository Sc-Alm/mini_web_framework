async function loadIntoTable(url, table) {
    const response = await fetch(url);
    const data = await response.json();
    let jsonData = JSON.parse(data);
    setupTableHeaders(table, jsonData.headers);
    setupTableBody(table, jsonData.data);
}

function setupTableHeaders(table, headers) {
    const tableHead = table.querySelector("thead");
    let html = "<tr>";
    for (let headerText of headers) {
        html += `<th>${headerText}`
    }
    html += "</tr>";
    tableHead.innerHTML = html
}

function setupTableBody(table, data) {
    const tableBody = table.querySelector("tbody");
    let html = ""
    data.forEach(row => {
        html += "<tr>"
        html += setupCellText(row)
        html += "</tr>"
    })
    tableBody.innerHTML = html;
}

function setupCellText(row) {
    let html = ""
    row.forEach(cell=>{
       html+= `<td>${cell}</td>`
    })

    return html
}


function fetchPhoneData() {
    console.log("Getting Car Data")
    loadIntoTable("http://localhost:8000/api/task/1", document.querySelector(".phoneTable"))
}

function fetchCarData() {
    console.log("Getting Car Data")
    let car_rent_from_date = document.getElementById("car_rent_from_date")
    let car_rent_to_date = document.getElementById("car_rent_to_date")
    loadIntoTable(`http://localhost:8000/api/task/2/${car_rent_from_date}-${car_rent_to_date}`,
        document.querySelector(".carTable"))

}