# **Levantamiento de requerimientos de la lógica de decisión**

### **¿Cuáles son los estados posibles reales del dato que van a evaluar?**

1. **`invalid_data`** (`data invalida`): Estado de excepción para manejar datos de entrada incorrectos o perfiles no reconocidos en el sistema.
2. **`not_started`** (`no comenzado`): El expediente está en cero; no se ha marcado ningún documento en el sistema (`uploaded_documents == 0`).
3. **`incomplete`** (`incompleto`): El expediente ya tiene archivos cargados (`uploaded_documents > 0`), pero aún no alcanza la totalidad de documentos requeridos por el checklist del perfil o falta algún documento obligatorio.
4. **`expired_license`**: Estado aplicable cuando la licencia/carnet de la Junta de Vigilancia del perfil médico se encuentra vencida (`days_to_expire <= 0`).
5. **`complete`** (`completo`): Se entregaron los documentos requeridos según la plantilla del perfil y las validaciones requeridas están al día.
6. **`over_completed`** (`cantidad de archivos excedida`): Estado para clasificar escenarios donde la cantidad de documentos cargados supera el número de requerimientos solicitados por la plantilla del perfil.

---

### **¿Qué valor o condición de la ficha define cada estado?**

* **`profile`** (`perfil`): Define la plantilla de evaluación según el puesto del empleado (en el formulario actual, `medical`).
* **`uploaded_documents`**: Suma total de documentos marcados en el formulario (`dui`, `antecedentes`, `carnet`).
* **`dui`**, **`antecedentes`**, **`carnet`**: Indicadores individuales (booleanos/flags) que determinan si cada documento del checklist fue presentado o está pendiente.
* **`days_to_expire`**: Días restantes de vigencia de la licencia/carnet de la Junta de Vigilancia (`days_to_expire <= 0` indica carnet vencido).

---

### **¿Hay reglas de negocio confirmadas en la ficha que aún no están reflejadas en la lógica de la Semana 6?**

Sí. La lógica de la Semana 6 solo manejaba validaciones booleanas básicas. Para esta entrega se integran formalmente los estados requeridos por la vista y plantilla Jinja2 (`completo`, `incompleto`, `no comenzado`, `data invalida` y `cantidad de archivos excedida`), permitiendo evaluar dinámicamente el checklist del expediente según el perfil seleccionado y el desglose de documentos (DUI, Antecedentes y Carnet de junta).

---

### **¿Qué pasa si el dato no encaja en ningún estado esperado?**

Se evalúa como **`invalid_data`** (`data invalida`) en el bloque `else` o de validación inicial, por ejemplo, si se recibe un perfil no autorizado en la opción del formulario o si los parámetros de entrada no corresponden a los formatos aceptados.


---
### **Pruebas:** https://docs.google.com/document/d/1WTyAk5acbiVEJr7ffShtyHQ_9iPPE6a1NYvNKZ2jGeM/edit?usp=sharing
