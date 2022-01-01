// import { Modeler } from '../vendor/bpmn-js/dist/bpmn-modeler.development.js';

function fetchDiagram(url) {
    return fetch(url).then(response => response.text());
}

async function run(){
    // the diagram you are going to display
    const url = 'bpmn-sample/sample.bpmn';
    // const bpmnXML = url;
    const bpmnXML = await fetchDiagram(url);
  
    console.log('Hello, BPMN.js modeler!');
    
    // BpmnJS is the BPMN modeler instance
    const modeler = new BpmnJS({
        container: '#canvas',
        keyboard: {
            bindTo: window
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
