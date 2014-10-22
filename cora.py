import xml.etree.ElementTree as ET
from lxml import etree

def app(tag, text,ref):
    print ref
    print tag
    print text
    nodo = source.xpath(ref) #Como importamos el xml con lxml podemos usar toda la funcionalidad de XPath
    a = etree.SubElement(nodo[0],tag) #insertamos el nuevo elemento
    a.text = text

def rep(tag, text,ref):
    nodo = source.xpath(ref)
    a = etree.Element(tag)
    a.text = text
    nodo[0].getparent().replace(nodo[0],a) #Reemplazamos el elemento

def ins(tag, text, ref):
    nodo = source.xpath(ref)
    parent = nodo[0].getparent()
    a = etree.Element(tag)
    a.text = text
    parent.insert(parent.index(nodo[0]),a) #Insertamos en la posición deseada
    
# Este script debe estar en una carpeta con los archivos
# decorator.xml y source.xml.


if __name__ == '__main__':
    dec_name = raw_input('Please input decorator file name(with extension): ')
    source_name = raw_input('Please input source file name(with extension): ')
    out_name = raw_input('Please input output file name(with extension): ')
    decorator = ET.parse(dec_name);
    parser = etree.XMLParser(remove_blank_text=True) ##Removemos espacios blancos
    source = etree.parse(source_name,parser)#Parseamos source.xml con lxml
    namespace = '{http://www.xmlstairways.com/cora}' #Declaramos el namespace de CORA
    root_dec = decorator.getroot()
    for cora in root_dec:  #Iteramos por todos los distintos decorators
        ref = cora.attrib['ref']
        for action in cora: #Iteramos por los distintos métodos (append,insert...)
            ac = action.tag
            print ac
            if (ac == namespace + 'append'):  #Llamamos las funciones necesarias según el método
                print 'append'
                for el in action:  
                    tag = el.tag
                    text = el.text
                    app(tag,text,ref)                   
            elif (ac == namespace + 'replace'):
                for el in action:  
                    tag = el.tag
                    text = el.text
                    rep(tag,text,ref)  
            elif (ac == namespace + 'insert'):
                for el in action:  
                    tag = el.tag
                    text = el.text
                    ins(tag,text,ref)  
    source.write(out_name,pretty_print=True)
