function fetchDiagram(url) {
    return fetch(url).then(response => response.text());
}

async function run(){
    // the diagram you are going to display
    const url = "../../media/xml/" + "{{file_name}}";
    // const bpmnXML = url;
    const bpmnXML = await fetchDiagram(url);
  
    console.log('Hello, BPMN.js modeler!');
    console.log(url);
    
    // BpmnJS is the BPMN modeler instance
    const modeler = new BpmnJS({
        container: '#js-canvas',
        keyboard: {
            bindTo: window
        }
    });

    // import a BPMN 2.0 diagram
    try{
        await modeler.importXML(bpmnXML);
        // modeler.get('js-canvas').zoom('fit-viewport');
    } catch(err) {
        console.error('something went wrong:', err);
    }
}

run();

{% include "bpmn/modeler/components/io-import-export.js" %}
{% include "bpmn/modeler/components/io-zoom-controls.js" %}
{% include "bpmn/modeler/components/io-editing-tools.js" %}

