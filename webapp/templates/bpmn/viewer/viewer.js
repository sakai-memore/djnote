function fetchDiagram(url) {
    return fetch(url).then(response => response.text());
}

async function run(){
    // the diagram you are going to display
    const url = "../../media/xml/" + "{{file_name}}";
    // const bpmnXML = url;
    const bpmnXML = await fetchDiagram(url);
  
    console.log('Hello, BPMN.js');
    console.log(url);

    // BpmnJS is the BPMN viewer instance
    const viewer = new BpmnJS({ container: '#js-canvas'});

    // import a BPMN 2.0 diagram
    try{
        await viewer.importXML(bpmnXML);
        //viewer.get('js-canvas').zoom('fit-viewport');
    } catch(err) {
        console.error('something went wrong:', err);
    }
}

run();