{% load static %}

function fetchDiagram(url) {
    return fetch(url).then(response => response.text());
}

async function run(){
    // the diagram you are going to display
    const url = "{% static 'bpmn-sample/sample.bpmn' %}";
    // const bpmnXML = url;
    const bpmnXML = await fetchDiagram(url);
  
    console.log('Hello, BPMN.js modeler 2!');
    
    // BpmnJS is the BPMN modeler instance
    const modeler = new BpmnJS({
        container: '#js-canvas',
        keyboard: {
            bindTo: window
        },
        additionalModules: [PropertiesPanel, CamundaPropertiesProvider],
        propertiesPanel: {
            parent: "#properties-panel-parent"
        }
    });

    // import a BPMN 2.0 diagram
    try{
        await modeler.importXML(bpmnXML);
        // modeler.get('canvas').zoom('fit-viewport');
    } catch(err) {
        console.error('something went wrong:', err);
    }
}

run();
