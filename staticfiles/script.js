function exportData(type, table_id) {
  // Format date as YYYY-MM-DD
  const now = new Date();
  const yyyy = now.getFullYear();
  const mm = String(now.getMonth() + 1).padStart(2, '0');
  const dd = String(now.getDate()).padStart(2, '0');
  const dateStr = `${yyyy}-${mm}-${dd}`;

  const fileName = `${table_id}_${dateStr}.${type}`;

  // Clone the data table
  const tableClone = document.getElementById(table_id).cloneNode(true);

  // Remove hyperlinks from cloned table
  const links = tableClone.querySelectorAll('a');
  links.forEach(link => {
    const textNode = document.createTextNode(link.textContent);
    link.parentNode.replaceChild(textNode, link);
  });

  // Convert table to workbook
  const wb = XLSX.utils.table_to_book(tableClone);

  // Save workbook to file
  XLSX.writeFile(wb, fileName);
}

function exportAllTablesToSingleSheet(type, weekNumber) {
    // List the IDs of all tables you want to export.
    const tableIds = ['weekly_summary','members_report', 'plans_next_week', 'tracking_issues'];

    // Create a new workbook and a single worksheet.
    const wb = XLSX.utils.book_new();
    const ws = XLSX.utils.aoa_to_sheet([]); // Create a new, empty sheet.

    // Format date as YYYY-MM-DD for the final filename.
    const now = new Date();
    const yyyy = now.getFullYear();
    const mm = String(now.getMonth() + 1).padStart(2, '0');
    const dd = String(now.getDate()).padStart(2, '0');
    const dateStr = `${yyyy}-${mm}-${dd}`;
    
    // Construct the filename using the week number and date.
    const fileName = `Weekly_Report_Week_${weekNumber}_${dateStr}.${type}`;

    tableIds.forEach(id => {
        const table = document.getElementById(id);
        if (table) {
            // Add a header to the sheet for each table to separate the data.
            XLSX.utils.sheet_add_aoa(ws, [[`--- Data from Table: ${id} ---`]], { origin: -1 });

            // Append the data from the HTML table to the main worksheet.
            // origin: -1 tells it to append to the next available row.
            // raw: true preserves the original cell formatting.
            XLSX.utils.sheet_add_dom(ws, table, { origin: -1, raw: true });
        }
    });

    // Append the final single worksheet to the workbook.
    XLSX.utils.book_append_sheet(wb, ws, "Weekly_Report");

    // Save the single workbook to a file.
    XLSX.writeFile(wb, fileName);
}