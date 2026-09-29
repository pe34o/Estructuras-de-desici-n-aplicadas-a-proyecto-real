# **Levantamiento de requerimientos de la logica de decision**

### **¿Cuales son los estados posibles reales del dato que van a evaluar?**

1. **`invalid_data`**: Estado de excepcion para manejar datos de entrada incorrectos, como registrar un numero negativo de documentos subidos(`uploaded_documents<0`) o ingresar un perfil que no existe en el sistema.
2. **`not_started`**: El expediente esta en cero; no se h subido ningun documento al sistema(`uploaded_documents == 0`).
3. **`incomplete`**: El expediente ya tiene archivos cargados, pero aun no alcanza la cantidad total requerida por el checklist del perfil, o le falta la licencia requerida al perfil médico (`medical`).
4. **`expired_license`**: El checklist de documentos ya se completó o se superó, pero el carnet de la Junta de Vigilancia se encuentra vencido (`days_to_expire <= 0`).
5. **`complete`**: Se entregó exactamente la cantidad de documentos solicitados según la plantilla del perfil y la licencia del profesional está al día.
6. **`over_completed`**: Se han subido más documentos de los requeridos por el perfil y la licencia está vigente.

---

### **¿Qué valor o condición de la ficha define cada estado?**

* **`profile`**: Define la plantilla de evaluación según el puesto del empleado. Si es `medical` se exigen 6 documentos más la validación de su licencia; si es `administrative` se requieren 4 documentos.
* **`uploaded_documents`**: Variable entera que representa el total de documentos adjuntados en el sistema.
* **`has_license`**: Indicador de si el personal médico presentó su licencia de la Junta de Vigilancia.
* **`days_to_expire`**: Días restantes de vigencia del carnet (`days_to_expire <= 0` implica que el carnet está vencido).

---

### **¿Hay reglas de negocio confirmadas en la ficha que aún no están reflejadas en la lógica de la Semana 6?**

Sí, la lógica que implementamos en la Semana 6 solo manejaba validaciones booleanas sencillas de incompletitud y vencimiento de carnet. Para esta entrega estamos integrando el checklist dinámico de la ficha de RRHH que varía la cuota de documentos según el perfil (`medical` con 6 vs. `administrative` con 4), además de clasificar los casos donde hay exceso de documentos (`over_completed`) o error en los datos (`invalid_data`).

---

### **¿Qué pasa si el dato no encaja en ningún estado esperado?**

Se maneja como **`invalid_data`** en el bloque `else` final o de validación de entrada, en caso de recibir valores negativos en la cantidad de documentos o cuando el parámetro de `profile` no coincida con los roles autorizados (`medical` o `administrative`).

---
### **Pruebas:**
