(function(){

// initialize on document ready
$(document).ready(function() {
      //const URL_GETALL = '../api/json/p/xml_file/all/';
      const URL_GETALL = '../api/json/t/xml_file/';
      const table = $('#tbl').DataTable({
          'dom': "<'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'<'float-md-right ml-2'B>f>>" +
            "<'row'<'col-sm-12'tr>>" +
            "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
          'ajax': URL_GETALL,
          'buttons': ['csv', {
            'text': '<i class="bi bi-card-text" aria-hidden="true"></i>',
            'action': function(e, dt, node) {

              $(dt.table().node()).toggleClass('cards');
              $('.bi', node).toggleClass(['bi-table', 'bi-card-text']);
              dt.draw('page');
            },
            'className': 'btn-sm',
            'attr': {
              'title': 'Change views',
            }
          }],
          'select': 'single',
          'scrollx': true,
          'autoWidth': false,
          'table-layout': 'fixed',
          'word-wrap': 'break-word',
          'columnDefs': [{
              targets: 0,
              width: '10px'
            },
            {
              targets: 1,
              width: '30px'
            },
            {
              targets: 2,
              width: '30px'
            },
            {
              targets: 3,
              width: '30px'
            },
            {
              targets: 4,
              width: '40px',
              className: "truncate"
            },
            {
              targets: 5,
              width: '30px'
            },
            {
              targets: 6,
              width: '30px'
            },
          ],
          'columns': [{
              'data': 'id',
              'class': 'text-right'
            },
            {
              'data': 'file_name'
            },
            {
              'data': 'business_pattern_id',
              "visible": false
            },
            {
              'data': 'process_pattern_name',
            },
            {
              'data': 'description',
            },
            {
              'data': 'updated_by',
              'className': 'text-center',
              'render': function(data, type, full, meta) {
                if (type === 'display') {
                  //var token = (Math.random()*3*1e38).toString(16);
                  const token = hashCode(data)
                  //console.log(data)
                  //console.log(token)
                  const img_link = '<img src="https://www.gravatar.com/avatar/' + token + '.png?d=robohash" class="avatar border rounded-circle">';
                  data = img_link + " " + data
                }

                return data;
              }
            },
            {
              'data': 'update_at'
            }
          ],
          'drawCallback': function(settings) {
            const api = this.api();
            const $table = $(api.table().node());

            if ($table.hasClass('cards')) {
              // Create an array of labels containing all table headers
              let labels = [];
              $('thead th', $table).each(function() {
                labels.push($(this).text());
              });

              // Add data-label attribute to each cell
              $('tbody tr', $table).each(function() {
                $(this).find('td').each(function(column) {
                  $(this).attr('data-label', labels[column]);
                });
              });

              let max = 0;
              $('tbody tr', $table).each(function() {
                max = Math.max($(this).height(), max);
              }).height(max);

            } else {
              // Remove data-label attribute from each cell
              $('tbody td', $table).each(function() {
                $(this).removeAttr('data-label');
              });

              $('tbody tr', $table).each(function() {
                $(this).height('auto');
              });
            }
          }
        })
        .on('select', function(e, dt, type, indexes) {
          const rowData = table.rows(indexes).data().toArray()
          setCard(rowData[0])
        })
        .on('deselect', function() {
          $('#row-data').empty();
        })
    }
);

// -------------------------------------------------------------------
// local functions
function setCard(rowObj) {
     $('#id').text(rowObj['id']);
     $('#file_name').val(rowObj['file_name']);
     $('#description').val(rowObj['description']);
     $('#updated_by').text(rowObj['updated_by']);
     $('#update_at').text(rowObj['update_at']);
     let img_name = "";
     if(rowObj['file_name'].substr(0,3) == "PDM") {
         img_name = rowObj['file_name'] + '.svg';
     } else {
         img_name = 'e99d70d12692e73fcee73ad21cf30b1a.png';
     }
     //console.log(rowObj['file_name'].substr(0,3));
     $('#bpmn_img').attr('src', '../media/images/' + img_name);
     $('#bpmn_img_link').attr('href', '../bpmn/viewer/' + rowObj['id']);
     $('#bpmn_img_link').attr('target', '_blank');
     $('#description').focus()
     
     // $('#row-data').html(JSON.stringify(rowObj));
};


const hashCode = str => {
  return str.split('').reduce((prevHash, currVal) =>
    (((prevHash << 5) - prevHash) + currVal.charCodeAt(0))|0, 0);
}


// button event  
const deleteBpmnFile = ()=>{
    console.log('click btn_delete');
    const URL = "../api/json/tinydb/xml_file/" + $('#id').text();
    let result_y = confirm('Delete a file');
    
    // do not implement : 403 Forbidden error
    if (result_y) {
      return axios
        .delete(URL)
        .then(function(res){
          console.log(res);
        })
    } else {
      console.log("Cancel!!!!!")
      return ""
    }
}
$("#btn_delete").bind("click", deleteBpmnFile)

const copyBpmnFile = ()=>{
    console.log('click btn_copy');
    let id = 1;
    if ($('#id').text() !== "") {
      id = $('#id').text();
    }
    location.href = "../bpmn/modeler/copy/" + id;
}
$("#btn_copy").bind("click", copyBpmnFile)

const editBpmnFile = ()=>{
    console.log('click btn_edit');
    let id = 1;
    if ($('#id').text() !== "") {
      id = $('#id').text();
    }
    location.href = "../bpmn/modeler/" + id;
}
$("#btn_edit").bind("click", editBpmnFile)

const createBpmnFile = ()=>{
    console.log('click btn_new');
    location.href = "../bpmn/modeler/new";
}
$("#btn_new").bind("click", createBpmnFile)

const saveBpmnFile = ()=>{
    console.log('click btn_save');
}
$("#btn_save").bind("click", saveBpmnFile)


/*
// event container
const eventContract = new jsaction.EventContract();
//eventContract.addContainer(document.getElementById('container'));
eventContract.addContainer($('#container')[0]);

// Register the event types we care about.
console.log("line 09");
eventContract.addEvent('click');
//eventContract.addEvent('dblclick');

// Set jsaction.dispatcher

const dispatcher = new jsaction.Dispatcher();
eventContract.dispatchTo(dispatcher.dispatch.bind(dispatcher));

dispatcher.registerHandlers(
    'bpmnlist',                      // the namespace
    null,                            // handler object
    {                                // action map
      'delete' : deleteBpmnFile,
      'copy' : copyBpmnFile,
      'edit' : editBpmnFile,
      'new' : createBpmnFile,
      'save' : saveBpmnFile
    }
);
*/

})();
