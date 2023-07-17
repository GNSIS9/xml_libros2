

from lxml import etree

def validar_xml_con_esquema(xml_file, xsd_file):
    try:
        # Cargar el archivo XML
        xml_doc = etree.parse(xml_file)

        # Cargar el archivo XSD
        xsd_doc = etree.parse(xsd_file)
        xsd = etree.XMLSchema(xsd_doc)

        # Validar el XML contra el XSD
        xsd.validate(xml_doc)

        # Comprobar si hay errores de validación
        if xsd.error_log:
            for error in xsd.error_log:
                print("Error de validación XML:", error)
        else:
            print("El XML es válido según el esquema.")
    except etree.XMLSyntaxError as e:
        print("Error al analizar el XML:", e)
    except etree.XMLSchemaParseError as e:
        print("Error al analizar el esquema XSD:", e)

# Ruta del archivo XML a validar
xml_file = "archivo.xml"

# Ruta del archivo XSD (esquema XML)
xsd_file = "schema.xsd"

# Llamar a la función para validar el XML
validar_xml_con_esquema(xml_file, xsd_file)