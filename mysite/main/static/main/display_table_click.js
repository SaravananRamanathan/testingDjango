//$('#summaryTable').on('click-cell.bs.table', function (field, value, row, $el) {
 	  
//$(document).ready(function() {	

   /* $('#display_table > tbody > tr').click(function(field, value, row, $el) {
    // row was clicked
    //alert($el.Name);
    //console.log($el.Name);
    
    window.location.replace('http://www.google.com/');//testing 
    });*/

//});
$(document).ready(function() {

$('#display_table > tbody > tr').on('click', function(row,$element,field){
        // row was clicked on bootstrap table
        //how to get the row data now?
        alert("testing");
        //window.location.replace('http://www.google.com/');//testing 
});

});
/*$('#display_table').on('click-cell.bs.table', function (field, value, row, $element) {
      alert("testing");
});*/

/*$('#display_table').on('click-row.bs.table', function (e, row, $element) {
    alert("testing")
});*/

/*$("table").on("click-cell.bs.table", function (field, value, row, $el) {
    alert("testing");
 });*/

/*$('#display_table').bootstrapTable({
    onClickRow: function (row, $element, field) {
      alert("testing");
    }
})*/