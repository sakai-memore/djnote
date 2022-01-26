{% load static %}

function fetchDiagram(url) {
    return fetch(url).then(response => response.text());
}

async function run(){
    // the diagram you are going to display
    const url = "{% static 'bpmn-sample/sample.bpmn' %}";
    // const bpmnXML = url;
    const bpmnXML = await fetchDiagram(url);
  
    // console.log(bpmnXML);
    console.log('Hello, BPMN.js');
    // BpmnJS is the BPMN viewer instance
    const viewer = new BpmnJS({ container: '#canvas'});

    // import a BPMN 2.0 diagram
    try{
        await viewer.importXML(bpmnXML);
        viewer.get('canvas').zoom('fit-viewport');
    } catch(err) {
        console.error('something went wrong:', err);
    }
}

run();