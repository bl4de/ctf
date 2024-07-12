from flask import Flask, request, render_template_string, render_template
from lxml import etree

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        xml_data = request.data
        try:
            parser = etree.XMLParser(resolve_entities=True)
            root = etree.fromstring(xml_data, parser=parser)
        except etree.XMLSyntaxError as e:
            return render_template_string('<div style="color:red;">Error parsing XML: {{ error }}</div>', error=str(e))
        feedback_element = root.find('feedback')
        if feedback_element is not None:
            feedback = feedback_element.text
            return render_template_string('<div style="color:green;">Feedback sent to the Emus: {{ feedback }}</div>', feedback=feedback)
        else:
            return render_template_string('<div style="color:red;">Invalid XML format: feedback element not found</div>')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
