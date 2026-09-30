# RECOEVO* · Metodología y reporte del análisis de campo (Fase 1 urbana)

**Percepciones, dinámicas y problemáticas frente al manejo de residuos orgánicos en las calles de Usme**
Politécnico Grancolombiano · Asignatura Proceso Administrativo · Docente: Ingrid Zoraida Sandoval Pérez · Acompañamiento en campo: Willington Javier Ortiz Amador (Centro de Emprendimiento).
Estudiantes (orden por apellido): Ricardo Beltrán, William Fonseca, Samuel Medina, Faber Ortiz, Camila Riaño.
\* Nombre provisional: el proyecto cambiará de nombre.

**Lugar:** barrio Villa Rosita, sector Tihuaque, Usme, Bogotá. El punto de referencia es 4.500941, -74.085905, entregado por el equipo (Cra. 15 Este #89C-31).
**Trabajo de campo:** sábado 19 de septiembre de 2026. Entrevistas de 2:30 a 5:00 p. m.
**Análisis:** 30 de septiembre de 2026 (versión 2, auditada).

> **Correcciones de ubicación.** El mapa de la presentación anterior apuntaba a Engativá (4.6989, -74.1081). En una primera corrección se usó el salón comunal de OpenStreetMap, 480 m al nororiente del punto real. Ahora se usa el punto que entregó el equipo.

## 1. Diseño
Estudio **cualitativo exploratorio**: entrevista semiestructurada más observación no participante. Su objetivo es validar el problema. Las cifras significan "cuántas de las 8 personas" y no describen a todo el barrio.

## 2. Corpus y participantes
- Hay 10 grabaciones que suman 66 min y corresponden a **8 personas únicas**.
  - Audio2 y Audio3 son la misma persona (E02).
  - Audio10 es muy probablemente el cierre de Audio6 (E05).
  - Audio3 y Audio4 son personas distintas: 36 años frente a 50 años en el barrio, y nombres distintos.
- Material visual:
  - 22 fotos y 4 videos del equipo.
  - 1 imagen de Google Street View (`Basuras.png`) de la parte alta del barrio. Se cita la fuente y se aclara que no es del día del campo.
- Las horas de los archivos de WhatsApp son horas de **envío** (20 de septiembre), no de captura. Por eso no se usan para afirmar horarios.

## 3. Validación de transcripciones
Whisper large-v3 se ejecutó localmente en GPU con configuración anti-alucinación. Cada transcripción se comparó palabra por palabra con esa re-transcripción:
- Similitud media del 92 % en los 8 audios validados.
- Audio6 se revisó bloque por bloque.
- Audio7 y Audio10 se reemplazaron por versiones revisadas con hablantes asignados.

Además, cada frase se ubicó en su minuto del audio: **212 de 220** (confianza media 0,88). Desde la presentación se puede escuchar el audio original de cada frase.

## 4. Edición gramatical de las frases (para mostrarlas)
1. El modelo local Qwen2.5 14B propuso una versión corregida de cada frase.
2. Un filtro automático **rechazó toda edición que agregara palabras con contenido** que no estuvieran en el original: 91 de 175. Por ejemplo, el modelo cambió "pienso yo" por "piensa" e inventó "cosas bonitas".
3. Las 91 rechazadas se editaron a mano, con criterio conservador: puntuación, repeticiones, "chux/Chuck" → "shut", y [corchetes] para las aclaraciones.
4. El texto literal se conserva siempre junto al editado.

## 5. Análisis: Framework Method
Se siguieron las cinco etapas de Gale et al. (2013).
- Hay **220 unidades de significado**, de las cuales **169 tienen contenido**.
- Se usan **17 códigos en 5 dimensiones** (`codebook.json`).
- Cada frase puede tener varios códigos.

### Reglas estrictas (auditoría v2)
La primera versión mezclaba dos cosas en la escala de satisfacción: la opinión sobre el barrio y la descripción de prácticas propias. Por ejemplo, la única frase "muy satisfecho" era "mi casa vive muy limpia". Se re-auditaron las 220 frases con estas reglas:
- **Satisfacción (1–5):** solo cuando la persona evalúa la situación del barrio o el servicio. Las prácticas propias quedan en "no aplica". Resultado: 86 frases.
- **Disposición (1–5):** solo cuando la persona opina sobre participar en una solución. Resultado: 43 frases.
- **"Ya aprovechan lo orgánico":** solo prácticas actuales. No cuentan los recuerdos del campo ni las ideas futuras.
- **Condiciones para participar:** etiqueta propia (pedagogía, líderes, recolección, incentivo, ejemplo, práctico, costo).
- Las cifras se reportan **por persona** (promedio de cada una), no por frase.

### Cambios que produjo la auditoría
| Afirmación | Versión 1 | Versión 2 (auditada) |
|---|---|---|
| Ya aprovechan lo orgánico | 5 de 8 | **3 de 8** (E04, E05, E08) |
| Mezclan todo en casa | 6 de 8 | **5 de 8** |
| Cultura y hábito | 8 de 8 | **7 de 8** |
| Se quejan de la recolección | 6 de 8 | **5 de 8** (E07 dice que cumple) |
| Viento y lluvia | 5 de 8 | **3 de 8** |
| "Que alguien recoja" | 6 de 8 | **2 de 8** |
| Satisfacción | 2,05 · 1 "muy satisfecho" | **1,76 · 0 "muy satisfecho"** · 7 de 8 insatisfechas |
| Disposición | 69 % de las frases | **4 de 7 personas a favor, 3 con condiciones, 0 rechazos** |

En la presentación, **cada cifra se calcula en el navegador a partir de las mismas frases que se muestran al hacer clic**.

## 6. Confiabilidad
- **Doble codificación:** investigador frente a Qwen2.5 14B, que codificó por separado.
  - κ = 0,70, acuerdo sustancial; coincidencia del 96,9 %.
  - Los códigos con menor acuerdo son "¿Y si los demás no?" y "Líderes y comunidad", que son los más interpretativos.
- **Saturación** (promedio de 1.000 órdenes aleatorios): con 4 entrevistas ya aparece el 97 % de los temas.
- **Caso discrepante:** E06, adulto mayor que casi no sale de casa, tiene satisfacción de 2,8. Se reporta como tal.

## 7. Hallazgos

### De las entrevistas
1. **8 de 8** señalan el shut y las esquinas como el foco del problema.
2. La cadena falla en tres puntos:
   - Mezcla en la cocina: 5 de 8.
   - Bolsas rotas por perros y recicladores: 6 de 8.
   - Recolección: 5 de 8 se quejan.
3. **6 de 8** mencionan perros, ratas o plagas.
4. **Servicio:** quejas por horario y frecuencia.
   - Costos mencionados: $40.000 al mes (E05) y entre $130.000 y $160.000 por piso (E06).
   - Diferencia entre la zona comercial y la residencial (E08).
5. **7 de 8** personas están insatisfechas con el barrio. La satisfacción media es de 1,76 sobre 5.
6. **Barreras:**
   - Hábito: 7 de 8.
   - "¿Y si los demás no?": 5 de 8.
   - Estado ausente: 4 de 8.
7. **3 de 8** ya reutilizan sobras. **Insight:** el hábito de reutilizar existe; falta un sistema que lo organice.
8. **Disposición:** 4 de 7 a favor, 3 con condiciones y ningún rechazo.
9. **Condiciones:**
   - Pedagogía: 5.
   - Líderes o Junta: 3.
   - Recolección: 2.
   - Incentivo: 2.
   - Ver que funciona: 2.
   - Que sea práctico: 2.
   - E01 acepta aportar a cambio del beneficio.
10. **4 de 8** relacionan los residuos con el abono y critican los químicos.

### De la observación
- **O1.** El shut está desbordado y abierto, a pesar del aviso de multa. Loma arriba, las esquinas se vuelven botaderos (Street View).
- **O2.** Perros y palomas comen de lo expuesto; se vio un perro comiendo de un recipiente de icopor.
- **O3.** El botadero es un lugar activo: unos llegan a dejar bolsas y otros a buscar reciclables.
- **O4.** Hay grandes generadores que no se entrevistaron: vendedores ambulantes y fruvers.
- **O5.** Las vías destapadas y las pendientes complican la recolección; las bolsas quedan en los andenes.
- **O6.** En los locales ya se usan canecas de pedal.

## 8. Límites
- Muestra intencional y pequeña.
- No incluye agricultores, que quedan para la fase 2.
- El codificador B es una IA, no un segundo investigador.
- Las fotos solo prueban lo que muestran.
- El reporte sigue la lista COREQ.

## Referencias
- Gale, N. K., et al. (2013). Using the framework method for the analysis of qualitative data. *BMC Medical Research Methodology*, 13, 117.
- Graneheim, U. H., & Lundman, B. (2004). Qualitative content analysis in nursing research. *Nurse Education Today*, 24(2), 105–112.
- Guest, G., Bunce, A., & Johnson, L. (2006). How many interviews are enough? *Field Methods*, 18(1), 59–82.
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174.
- Sandelowski, M., Voils, C. I., & Knafl, G. (2009). On quantitizing. *Journal of Mixed Methods Research*, 3(3), 208–222.
- Tong, A., Sainsbury, P., & Craig, J. (2007). COREQ. *International Journal for Quality in Health Care*, 19(6), 349–357.
