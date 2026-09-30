import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const root = 'C:/Users/willi/OneDrive/Desktop/04. Recoevo';
const project = path.join(root, 'Proyecto_Usme_Analisis');
const sourceCsv = path.join(project, '03_Data_y_Estadistica/unidades_transcripcion_exploratorias.csv');
const outDir = path.join(project, '03_Data_y_Estadistica/outputs/01a0f344-0eed-7df1-8b74-2b04c3208b05');
const outFile = path.join(outDir, 'Hallazgos_Integrados_RECOEVO.xlsx');
await fs.mkdir(outDir, { recursive: true });

// Import via artifact-tool to retain CSV quoting and multiline cells faithfully.
const parsed = await Workbook.fromCSV(await fs.readFile(sourceCsv, 'utf8'), { sheetName: 'Importación temporal' });
const importedRows = parsed.worksheets.getItem('Importación temporal').getUsedRange().values;
const sourceHeaders = importedRows[0].map(String);
const sourceRows = importedRows.slice(1).filter(row => row.some(v => v !== null && v !== ''));

const wb = Workbook.create();
const summary = wb.worksheets.add('Resumen');
const findings = wb.worksheets.add('Hallazgos cruzados');
const phrases = wb.worksheets.add('Frases y turnos');
const visuals = wb.worksheets.add('Fotos y videos');
const audio = wb.worksheets.add('Audios');
const method = wb.worksheets.add('Trazabilidad y método');
for (const sh of [summary, findings, phrases, visuals, audio, method]) sh.showGridLines = false;

const dark = '#153629', green = '#2E6445', lime = '#E6F3D2', pale = '#F3F6F1', ink = '#23332A', muted = '#64756A', amber = '#FFF0CD';
function title(sh, text, note='') {
  sh.getRange('A1').values = [[text]];
  sh.getRange('A1').format = { font: { name: 'Aptos', size: 16, bold: true, color: dark } };
  if (note) { sh.getRange('A2').values = [[note]]; sh.getRange('A2').format = { font: { name: 'Aptos', size: 10, italic: true, color: muted } }; }
}
function makeTable(sh, headers, rows, name) {
  const matrix = [headers, ...rows];
  sh.getRangeByIndexes(3, 0, matrix.length, headers.length).values = matrix;
  const endCol = col(headers.length - 1);
  const last = matrix.length + 3;
  const table = sh.tables.add(`A4:${endCol}${last}`, true, name);
  table.style = 'TableStyleMedium4';
  table.showFilterButton = true;
  sh.getRange(`A4:${endCol}4`).format = { fill: dark, font: { name: 'Aptos', size: 10, bold: true, color: '#FFFFFF' }, horizontalAlignment: 'center', verticalAlignment: 'center', wrapText: true };
  sh.getRange(`A5:${endCol}${last}`).format = { font: { name: 'Aptos', size: 10, color: ink }, verticalAlignment: 'top', wrapText: false };
  sh.getRange(`A4:${endCol}${last}`).format.rowHeight = 28;
  sh.freezePanes.freezeRows(4);
  return last;
}
function col(n) { let s=''; for(n++; n; n=Math.floor((n-1)/26)) s=String.fromCharCode((n-1)%26+65)+s; return s; }

// Full transcript audit trail; the 545 existing units remain intact.
title(phrases, 'Turnos extraídos de las 10 transcripciones', 'Texto preservado tal como aparece en la extracción. Las etiquetas son exploratorias y pueden solaparse; una fila no equivale a una persona.');
const phraseHeaders = [...sourceHeaders, 'Grupo de lectura', 'Uso en el análisis integrado'];
const phraseRows = sourceRows.map(r => {
  const record = Object.fromEntries(sourceHeaders.map((h,i) => [h, r[i] ?? '']));
  let group = 'Revisar con contexto';
  if (/entrevistador/i.test(String(record.rol_probable))) group = 'Pregunta o intervención del equipo';
  else if (record.temas_regla_exploratoria) group = 'Intervención de participante con etiqueta exploratoria';
  return [...sourceHeaders.map(h => record[h] ?? ''), group, 'Se conserva para leer coincidencias y diferencias entre todas las entrevistas; revisar el turno junto con audio y transcripción.'];
});
makeTable(phrases, phraseHeaders, phraseRows, 'TurnosExtraidos');
const phraseWidths = [19,14,22,32,74,36,24,68,42,78];
phraseWidths.forEach((w,i)=>phrases.getRange(`${col(i)}:${col(i)}`).format.columnWidth=w);
phrases.getRange(`E5:E${phraseRows.length+4}`).format.wrapText = true;
phrases.getRange(`E5:E${phraseRows.length+4}`).format.columnWidth = 82;

const findingRows = [
  ['H01','Separación cotidiana','Varias voces cuentan que restos de cocina, cartón y otros residuos terminan en la misma bolsa; separar no aparece como rutina estable.','Audio1-U018; Audio3-U009; Audio3-U010; Audio7.txt (pasaje sobre bolsa común)','Audio1.txt; Audio3.txt; Audio7.txt','Foto: WhatsApp Image 2026-09-20 at 10.45.02 AM (1).jpeg','La frase de Audio1 ilustra una práctica que también aparece en otras entrevistas; la foto muestra residuos distintos juntos.','No convertir recuentos de frases en porcentajes de hogares. Audio7 tiene hablantes poco marcados.','Coincidencia en entrevistas + apoyo visual'],
  ['H02','Punto de depósito y dispersión','Las entrevistas relacionan el desorden con bolsas fuera del punto, bolsas abiertas y residuos que terminan en más de una esquina.','Audio1-U044; Audio6-U035; Audio8-U026; Audio9-U018','Audio1.txt; Audio6.txt; Audio8.txt; Audio9.txt','Fotos: 10.45.01 AM.jpeg; 10.44.52 AM (1).jpeg; 10.44.53 AM.jpeg','El chute y el área circundante muestran residuos; las citas describen cómo se dispersan.','Las imágenes no prueban quién abrió las bolsas ni cuándo.','Coincidencia entre varias entrevistas + observación'],
  ['H03','Perros y restos de comida','Distintas voces mencionan perros que buscan comida o abren bolsas; en un local también se cuenta que se ofrecen sobras a los perros.','Audio3-U010; Audio6-U019; Audio8-U010; Audio8-U026; Audio9-U018','Audio3.txt; Audio6.txt; Audio8.txt; Audio9.txt','Fotos: 10.44.58 AM.jpeg; 10.45.02 AM.jpeg; 10.45.01 AM.jpeg','Las fotos muestran perros cerca de zonas con residuos; las entrevistas describen relación con la comida y las bolsas.','Una foto no permite determinar si un animal está abandonado ni atribuirle una acción.','Coincidencia entre relatos + apoyo visual'],
  ['H04','Recolección y acceso','Aparecen relatos de horarios inciertos, puntos que no reciben el servicio y personas que llevan la basura a un lugar distinto.','Audio1-U044; Audio6-U035; Audio6-U037; Audio9-U014; Audio9-U018','Audio1.txt; Audio6.txt; Audio9.txt','Fotos de bolsas y puntos de disposición (sin geolocalización)','Los problemas de frecuencia y distancia se atribuyen a quienes los cuentan; no hay registro operativo de la empresa recolectora.','No generalizar el horario de una entrevista a todo el barrio.','Coincidencia narrativa; falta validar con datos de ruta'],
  ['H05','Opiniones distintas sobre el chute','Las voces no coinciden en cuánto ayuda el chute: aparece como un recurso útil para algunos y como insuficiente para otros cuando siguen la dispersión y las fallas de servicio.','Audio9-U020; Audio6-U035; Audio7.txt (pasaje sobre llevar la bolsa al punto)','Audio6.txt; Audio7.txt; Audio9.txt','Foto: 10.45.01 AM.jpeg','Las diferencias se mantienen en el análisis; no se promedian ni se ocultan.','Audio7 no tiene atribución uniforme y requiere cotejo fino.','Diferencia explícita entre entrevistas'],
  ['H06','Comercios y manejo de alimentos','Una comerciante describe destinar algunas sobras a los perros; otras voces describen orgánicos mezclados o abandonados junto a otros residuos.','Audio6-U019; Audio1-U018; Audio3-U010','Audio1.txt; Audio3.txt; Audio6.txt','Foto: 10.44.53 AM.jpeg (frente comercial y espacio exterior)','Comercio y hogares se analizan dentro del mismo conjunto, sin asumir una sola práctica para todos.','La foto no identifica el tipo de residuo que genera ese comercio.','Coincidencia parcial; prácticas diferentes'],
 ['H07','Suelo, lluvia y bordes de vía','En el recorrido se fotografían tramos pavimentados junto a bordes de tierra húmeda, charcos y superficies sin pavimentar.','No se atribuye como frase de entrevista; observación del equipo de campo','Recorrido de campo, 20 sep 2026','Foto: 11.13.01 AM.jpeg · video: WhatsApp Video 2026-09-20 at 7.47.32 AM.mp4 (solo como referencia de paso; no se incluye por persona visible)','La evidencia es visual y localizada: describe estas imágenes, no todas las calles de Villarrosita. El video 7.47.02 AM muestra mejor el punto con residuos y perros.','Sin GPS ni mediciones de lluvia, no reconstruir distribución ni frecuencia. No exponer a la persona visible en el clip vial.','Observación visual + clip seleccionado en otra lámina'],
  ['H08','Basura y actividad en la calle','Las fotos incluyen depósitos, bolsas y residuos en espacios abiertos; entrevistas distintas describen presencia de residuos en esquinas y alrededor del punto.','Audio6-U035; Audio8-U026; Audio9-U018','Audio6.txt; Audio8.txt; Audio9.txt','Fotos: 10.44.51 AM (3).jpeg; 10.45.01 AM.jpeg; 10.44.52 AM.jpeg','Se relacionan fuentes para situar el problema en el espacio público.','No inferir causalidad ni asignar el origen de cada residuo a una persona o local.','Coincidencia visual y testimonial'],
];
title(findings, 'Lectura integrada: coincidencias, diferencias y límites', 'Las unidades de análisis son temas que cruzan entrevistas; las citas respaldan el tema y no convierten a una persona en “el hallazgo”.');
const findingView = findingRows.map(r => [r[0],r[1],r[2],r[3],`${r[4]} · ${r[5]}`,r[6],r[7]]);
makeTable(findings, ['ID','Tema común','Hallazgo integrado','Turnos que respaldan','Transcripciones + evidencia visual','Por qué se cruzan','Qué no permite afirmar'], findingView, 'HallazgosIntegrados');
[8,21,47,43,54,58,48].forEach((w,i)=>findings.getRange(`${col(i)}:${col(i)}`).format.columnWidth=w);
findings.getRange(`C5:G${findingView.length+4}`).format.wrapText = true;
findings.getRange(`A5:G${findingView.length+4}`).format.rowHeight = 66;

// Image register and decision notes. Every source photo is present; only selected safe, legible frames enter the deck.
const evidenceDir = path.join(root, 'Entrevistas/Evidencias');
const sourceFiles = (await fs.readdir(evidenceDir)).filter(f => /\.(jpeg|jpg|png|mp4)$/i.test(f));
const chosen = new Map([
 ['WhatsApp Image 2026-09-20 at 10.45.01 AM.jpeg',['Alta','Chute rosado junto a residuos sueltos y aviso visible','Lámina 3','Imagen nítida y evidencia directa del punto; no identifica quién dejó los residuos.']],
 ['WhatsApp Image 2026-09-20 at 10.45.02 AM (1).jpeg',['Alta','Restos de alimentos junto a bolsas y materiales variados en un borde de vegetación','Lámina 6','Muestra mezcla de residuos con lectura clara; no prueba qué material llegó primero.']],
 ['WhatsApp Image 2026-09-20 at 10.44.58 AM.jpeg',['Alta','Dos perros cerca de bolsas/residuos y del chute rosado','Lámina 7','Apoya cercanía entre animales y punto; no determina abandono ni conducta.']],
 ['WhatsApp Image 2026-09-20 at 11.13.01 AM.jpeg',['Alta','Superficie de vía con agua acumulada y borde de tierra húmeda','Lámina 10','Contraste visual claro entre pavimento y terreno; no representa todas las vías.']],
 ['WhatsApp Image 2026-09-20 at 10.44.52 AM (1).jpeg',['Media-alta','Grupo de bolsas cerradas sobre superficie pavimentada','Lámina 5','Contextualiza acopio; no se sabe qué contienen las bolsas.']],
 ['WhatsApp Image 2026-09-20 at 10.45.02 AM.jpeg',['Media','Perro recostado junto a bolsa blanca en un espacio con pasto','Lámina 7 (detalle opcional)','Foto apoya proximidad; no demuestra abandono del animal.']],
 ['WhatsApp Image 2026-09-20 at 10.44.53 AM.jpeg',['Media-alta','Fachada de comercio junto al área abierta con residuos y chute al fondo','Lámina 11','Da contexto comercio-calle; no atribuir los residuos al local.']],
 ['WhatsApp Image 2026-09-20 at 11.13.01 AM (1).jpeg',['Media','Vía pavimentada junto a franja de suelo y vegetación','Lámina 10 (alternativa)','Sirve como contraste; la foto no ubica un recorrido exacto.']],
 ['WhatsApp Image 2026-09-20 at 10.45.00 AM.jpeg',['Baja (duplicada)','Vista casi igual a la foto de perros en el entorno del chute','No usar','Redundante frente a la imagen más nítida 10.44.58 AM.']],
 ['WhatsApp Image 2026-09-20 at 10.45.02 AM (2).jpeg',['No usar','Caneca interior en espacio doméstico','No usar en público','Incluye interior privado; no aporta un resultado común y no debe exponerse sin autorización.']],
]);
const imageDescriptions = new Map([
 ['WhatsApp Image 2026-09-20 at 10.44.51 AM (1).jpeg',['No usar','Dos personas conversando junto a un área verde','No usar en público','Personas identificables; evitar exposición sin confirmar autorización específica.']],
 ['WhatsApp Image 2026-09-20 at 10.44.51 AM (2).jpeg',['No usar','Repetición de la escena de dos personas conversando','No usar en público','Imagen repetida y personas identificables.']],
 ['WhatsApp Image 2026-09-20 at 10.44.51 AM (3).jpeg',['Media','Borde verde con residuos dispersos frente a edificaciones','No usar','Más lejana y menos legible que imágenes escogidas del punto.']],
 ['WhatsApp Image 2026-09-20 at 10.44.51 AM.jpeg',['Media','Bolsas agrupadas sobre pavimento','No usar','Repite acopio de bolsas; la selección 10.44.52 AM (1) es más clara.']],
 ['WhatsApp Image 2026-09-20 at 10.44.52 AM.jpeg',['Media','Perro en área verde con algunos residuos y objetos próximos','No usar','Menos nítida que 10.44.58 AM; no inferir abandono.']],
 ['WhatsApp Image 2026-09-20 at 10.45.01 AM (1).jpeg',['Media','Chute rosado y entorno con residuos vistos desde otro ángulo','Alternativa','La seleccionada 10.45.01 AM es más legible y permite ver el aviso.']],
 ['WhatsApp Image 2026-09-20 at 11.12.54 AM.jpeg',['No usar','Personas en un local comercial','No usar en público','Personas identificables; no es necesaria para mostrar el patrón.']],
 ['WhatsApp Image 2026-09-20 at 11.12.59 AM.jpeg',['No usar','Personas dentro de un comercio','No usar en público','Personas identificables y actividad privada.']],
 ['WhatsApp Image 2026-09-20 at 11.13.00 AM (1).jpeg',['No usar','Persona en primer plano dentro de comercio','No usar en público','Persona identificable; la conclusión de prácticas viene de las entrevistas.']],
 ['WhatsApp Image 2026-09-20 at 11.13.00 AM (2).jpeg',['No usar','Personas junto a un mostrador comercial','No usar en público','Personas identificables.']],
 ['WhatsApp Image 2026-09-20 at 11.13.00 AM.jpeg',['No usar','Persona entrevistada o cliente en comercio','No usar en público','Persona identificable; no publicar sin autorización específica.']],
 ['WhatsApp Image 2026-09-20 at 7.47.18 AM (1).jpeg',['Media','Escena vial con suelo húmedo y vegetación/residuos al borde','Alternativa','Muy similar a 7.47.18 AM; usar una sola toma.']],
 ['WhatsApp Image 2026-09-20 at 7.47.18 AM.jpeg',['Media-alta','Cruce de vía pavimentada y borde de terreno húmedo con residuos','Lámina 10 (alternativa)','Aporta contexto vial, aunque la toma seleccionada 11.13.01 es más legible.']],
]);
for (const [k,v] of chosen) imageDescriptions.set(k,v);
const vidDur = new Map([
 ['WhatsApp Video 2026-09-20 at 11.12.59 AM.mp4','00:18'],
 ['WhatsApp Video 2026-09-20 at 7.47.02 AM.mp4','00:13'],
 ['WhatsApp Video 2026-09-20 at 7.47.11 AM.mp4','00:11'],
 ['WhatsApp Video 2026-09-20 at 7.47.32 AM.mp4','00:10'],
]);
const visualRows = await Promise.all(sourceFiles.map(async file => {
  const full = path.join(evidenceDir,file);
  const stat = await fs.stat(full);
  if (/\.mp4$/i.test(file)) {
    const videoNotes = {
      'WhatsApp Video 2026-09-20 at 7.47.02 AM.mp4':['Alta · seleccionado','Plano en movimiento de varios perros cerca de residuos y bolsas en un borde de vía','Lámina 7','Aporta escena continua y directa, más informativa que los otros clips. El clip no demuestra abandono ni causa; el audio va silenciado.'],
      'WhatsApp Video 2026-09-20 at 7.47.11 AM.mp4':['No usar en público','Vista muy parecida al clip anterior, con una persona parcialmente visible en el cuadro','No usar','Repite la escena y expone a una persona; se elige el clip 7.47.02 AM.'],
      'WhatsApp Video 2026-09-20 at 7.47.32 AM.mp4':['No usar en público','Recorrido por superficie de tierra con una persona visible','No usar','La foto 11.13.01 AM comunica el cambio de superficie sin mostrar a una persona.'],
      'WhatsApp Video 2026-09-20 at 11.12.59 AM.mp4':['No usar','Plano corto del suelo/pies; no muestra un hallazgo de campo legible','No usar','No añade evidencia visual al relato.'],
    };
    const v=videoNotes[file]||['Pendiente','Video sin descripción validada','No usar todavía','Revisar contenido y privacidad antes de mostrar.'];
    return [file,'Video MP4',vidDur.get(file)||'No verificada',stat.size,v[0]+' · '+v[1],v[2]+' · '+v[3], 'Entrevistas/Evidencias/'+file];
  }
  const v=imageDescriptions.get(file) || ['Pendiente','Imagen no descrita con suficiente confianza','No usar todavía','Revisar original y autorización antes de usar.'];
  return [file,'Foto',v[0],stat.size,v[1]+' · '+v[2],v[3], 'Entrevistas/Evidencias/'+file];
}));
title(visuals,'Inventario y selección visual','Se examinaron 22 fotos y los cuatro videos. La selección prioriza escenas legibles sin personas identificables. Un video entra en la presentación; los otros tres se dejan fuera con motivo documentado.');
makeTable(visuals,['Archivo fuente','Tipo','Prioridad','Tamaño (bytes)','Qué se ve / destino','Por qué / cautela','Ruta original'],visualRows,'InventarioVisual');
[52,14,18,16,56,68,62].forEach((w,i)=>visuals.getRange(`${col(i)}:${col(i)}`).format.columnWidth=w);
visuals.getRange(`D5:D${visualRows.length+4}`).format.numberFormat='#,##0';
visuals.getRange(`E5:G${visualRows.length+4}`).format.wrapText=true;
visuals.getRange(`A5:G${visualRows.length+4}`).format.rowHeight=42;

const audioMeta=[
 ['Audio1','Audio1.mp3','00:07:38',457.74,1360,'Entrevista sustantiva','Don José nombrado en la transcripción; verificar repetición de identidad.'],
 ['Audio2','Audio2.mp3','00:00:26',26.15,107,'Fragmento breve','No contar automáticamente como una entrevista completa.'],
 ['Audio3','Audio3.mp3','00:08:40',520.02,1225,'Entrevista sustantiva','Don Álvaro nombrado en transcripción.'],
 ['Audio4','Audio4.mp3','00:08:21',501.21,1247,'Entrevista sustantiva','Don Pérez / Álvaro Pérez según encabezado; verificar identidad repetida con Audio3.'],
 ['Audio5','Audio5.mp3','00:06:00',360.41,934,'Entrevista sustantiva','Juan Sebastián según transcripción.'],
 ['Audio6','Audio6.ogg','00:06:27',387.40,1048,'Entrevista sustantiva','Propietaria de local; identidad no consignada. Duración calculada desde Ogg Opus.'],
 ['Audio7','Audio7.ogg','00:04:17',257.44,570,'Entrevista sustantiva','Hablantes poco marcados; duración calculada desde Ogg Opus.'],
 ['Audio8','Audio8.mp4','00:09:28',568.00,1671,'Entrevista sustantiva','Valentina Rodríguez según transcripción.'],
 ['Audio9','Audio9.mp4','00:13:18',798.00,2551,'Entrevista sustantiva','Isaac según transcripción.'],
 ['Audio10','Audio10.ogg','00:01:30',89.72,163,'Permiso / autorización probable','No contar como entrevista sustantiva sin revisar audio; duración calculada desde Ogg Opus.'],
];
const totalDuration=audioMeta.reduce((a,r)=>a+r[3],0);
const audioRows=audioMeta.map(r=>[...r.slice(0,3),r[4],r[5],r[6],'Entrevistas/'+r[1],'Emparejado por número de archivo con Entrevistas/'+r[0]+'.txt']);
title(audio,'Audios y transcripciones emparejados',`10 pares de archivos · ${Math.floor(totalDuration/3600)} h ${String(Math.floor(totalDuration%3600/60)).padStart(2,'0')} min ${String(Math.round(totalDuration%60)).padStart(2,'0')} s de grabación total, incluyendo un fragmento de 26 s y un archivo de permiso.`);
makeTable(audio,['ID','Archivo de audio','Duración','Palabras transcritas','Lectura del archivo','Identidad / cautela','Ruta del audio','Justificación del emparejamiento'],audioRows,'ArchivosAudio');
[14,22,17,21,26,72,48,70].forEach((w,i)=>audio.getRange(`${col(i)}:${col(i)}`).format.columnWidth=w);
audio.getRange('D5:D14').format.numberFormat='#,##0';
audio.getRange('F5:H14').format.wrapText=true;

const traceRows=[
 ['Cruce texto-audio','AudioN.txt se enlaza con AudioN.<ext> por número de archivo.','Reduce el riesgo de comparar una entrevista con otro audio.','No prueba que todos sean entrevistas completas ni que no existan segmentos repetidos.','Conservar el ID y confirmar escuchando los pasajes citados.'],
 ['Cruce cita-hallazgo','Las citas se incluyen como pasajes verificables; los temas se proponen a partir de recurrencias en varias transcripciones.','Evita que una voz aislada se presente como el resultado entero.','La extracción por turnos no resuelve por sí sola todas las voces/errores de transcripción.','Consultar ID de turno, archivo y párrafo antes de publicar cita textual.'],
 ['Cruce entrevista-foto','Una foto se vincula a un tema sólo si muestra el aspecto visible correspondiente; el audio aporta la explicación atribuida.','Permite contrastar “lo que se ve” con “lo que la gente cuenta”.','Sin GPS, fecha aproximada y ruta, las fotos no pueden localizarse con precisión en el mapa.','No usar fotos como evidencia de causa, autoría o frecuencia.'],
 ['Temas cuantificados','Etiquetas léxicas exploratorias sobre 320 turnos atribuibles a participantes; se mantienen categorías y coincidencias multitema.','Da una primera pista auditable de recurrencia textual.','Una palabra puede aparecer por la pregunta del entrevistador o en distinto sentido; una persona puede producir muchos turnos.','No reportar como prevalencia de personas, emoción clínica ni estadística poblacional.'],
 ['Identidades','Usar nombre sólo si queda consignado con suficiente claridad y para esa cita; de lo contrario, “entrevistado/a”.','Respeta la trazabilidad sin adjudicar identidad por intuición.','Audio3/Audio4 pueden referirse a Álvaro/Pérez; el conteo de personas únicas no está cerrado.','Evitar publicar edades/datos personales salvo necesidad y permiso.'],
 ['Puntaje de sentimiento','No se usa una escala de caritas ni un valor 0–5 como resultado. Se conservan palabras y tono como citas contextuales.','Evita confundir evaluación negativa del problema con estado emocional de quien habla.','Una puntuación automática no se ha validado con hablantes ni codificadores.','Mantener la emoción como tema cualitativo, con cita y contexto.'],
 ['Videos de campo','Se inspeccionaron localmente tres fotogramas por clip. Se eligió WhatsApp Video 2026-09-20 at 7.47.02 AM.mp4 (13 s) para mostrar perros y residuos; los demás se excluyeron por repetición, plano poco informativo o persona visible.','La decisión se apoya en el contenido visto, no en el nombre ni duración del archivo.','Un clip no establece abandono, autoría ni frecuencia; su audio se mantiene silenciado.','Citar la escena como registro de campo y no como prueba de causalidad.'],
 ['Ubicación','Nombre del barrio “Villarrosita” según indicación del equipo; Google Maps provee un punto de referencia en Usme.','Da contexto geográfico sin inventar límite o traza de recorrido.','El enlace no ofrece un polígono validado del barrio ni GPS para cada evidencia.','Mostrar pin referencial y enlace; no dibujar límites.'],
];
title(method,'Cómo se hicieron los cruces y qué permiten decir','Hoja de auditoría: relación entre fuentes, justificación y límites. Distingue observación visible, relato y lectura integrada.');
makeTable(method,['Decisión','Regla aplicada','Por qué se cruza así','Límite','Cuidado al comunicar'],traceRows,'TrazabilidadMetodo');
[24,70,68,74,72].forEach((w,i)=>method.getRange(`${col(i)}:${col(i)}`).format.columnWidth=w);
method.getRange(`B5:E${traceRows.length+4}`).format.wrapText=true;

// Executive first view with formula-linked counts plus exploratory tags.
title(summary,'RECOEVO · Resultados integrados de Villarrosita','Entrevistas + fotografías de campo · corte exploratorio · archivos de salida de campo del 20 sep 2026.');
summary.getRange('A4:C11').values=[
 ['Qué tenemos','Cantidad','Cómo se cuenta'],
 ['Audios emparejados',null,'10 archivos con transcripción del mismo número'],
 ['Intervenciones extraídas',null,'Todas las filas de “Frases y turnos”; 225 preguntas del equipo y 320 turnos de participantes según etiqueta provisional'],
 ['Fotos inventariadas',null,`${sourceFiles.filter(f=>/\.(jpeg|jpg|png)$/i.test(f)).length} archivos; selección basada en claridad, pertinencia y privacidad`],
 ['Videos inventariados',null,`${sourceFiles.filter(f=>/\.mp4$/i.test(f)).length} revisados; 1 seleccionado para la presentación`],
 ['Grabación total',`1:06:06`,'Suma de duraciones por archivo; incluye Audio2 (00:26) y Audio10 (01:30)'],
 ['Personas únicas','Pendiente','Nombres de transcripción no permiten deduplicar con seguridad; Audio3/4 requieren cotejo'],
 ['Citas de audio','Rastreables','Se cita archivo y turno en la hoja de hallazgos y frases'],
];
summary.getRange('B5').formulas=[[`=COUNTA('Audios'!A5:A14)`]];
summary.getRange('B6').formulas=[[`=COUNTA('Frases y turnos'!A5:A${phraseRows.length+4})`]];
summary.getRange('B7').formulas=[[`=COUNTIF('Fotos y videos'!B5:B${visualRows.length+4},"Foto")`]];
summary.getRange('B8').formulas=[[`=COUNTIF('Fotos y videos'!B5:B${visualRows.length+4},"Video MP4")`]];
summary.getRange('A4:C4').format={fill:dark,font:{name:'Aptos',size:10,bold:true,color:'#FFFFFF'},horizontalAlignment:'center',wrapText:true};
summary.getRange('A5:C11').format={font:{name:'Aptos',size:10,color:ink},verticalAlignment:'center',wrapText:true};
summary.getRange('A4:C11').format.rowHeight=33;
[26,21,94].forEach((w,i)=>summary.getRange(`${col(i)}:${col(i)}`).format.columnWidth=w);
summary.getRange('A14:C14').values=[['Etiquetas temáticas preliminares','Turnos marcados','Lectura']];
summary.getRange('A15:C20').values=[
 ['Disposición y recolección',53,'Coincidencias léxicas; categorías pueden solaparse'],
 ['Separación y hábitos',21,'Coincidencias léxicas; categorías pueden solaparse'],
 ['Impactos y salud',16,'No medir prevalencia ni impacto clínico'],
 ['Generación y desperdicio',10,'Coincidencias léxicas; revisar contexto'],
 ['Confianza y gestión',10,'Coincidencias léxicas; revisar contexto'],
 ['Soluciones mencionadas',9,'Incluye respuestas sugeridas por preguntas del equipo'],
];
summary.getRange('A14:C14').format={fill:green,font:{name:'Aptos',size:10,bold:true,color:'#FFFFFF'},horizontalAlignment:'center',wrapText:true};
summary.getRange('A15:C20').format={font:{name:'Aptos',size:10,color:ink},verticalAlignment:'center',wrapText:true};
summary.getRange('A15:C20').format.rowHeight=26;
const chart=summary.charts.add('bar',summary.getRange('A14:B20'));
chart.title='Menciones temáticas por intervención'; chart.hasLegend=false; chart.titleTextStyle.typeface='Aptos'; chart.titleTextStyle.fontSize=12;
chart.xAxis={axisType:'textAxis',textStyle:{typeface:'Aptos',fontSize:10}};
chart.yAxis={numberFormatSourceLinked:false,textStyle:{typeface:'Aptos',fontSize:10}};
chart.setPosition('E4','M20');
summary.getRange('A22').values=[['Nota de uso: los conteos son etiquetas automáticas iniciales, no personas entrevistadas. Las hojas “Hallazgos cruzados” y “Trazabilidad y método” explican cómo se vincula cada evidencia y sus límites.']];
summary.getRange('A22:G23').merge();
summary.getRange('A22:G23').format={fill:lime,font:{name:'Aptos',size:10,color:ink},wrapText:true,verticalAlignment:'center'};
summary.freezePanes.unfreeze();

// Distinguish missing from zero; notes and sources remain adjacent to records.
wb.recalculate();
const inspect=await wb.inspect({kind:'sheet,table',maxChars:4000,tableMaxRows:3,tableMaxCols:6});
await fs.writeFile(path.join(outDir,'workbook_inspect.ndjson'),inspect.ndjson,'utf8');
for (const [sheetName,range] of [['Resumen','A1:M23'],['Hallazgos cruzados','A1:G12'],['Fotos y videos','A1:G20'],['Audios','A1:H15'],['Trazabilidad y método','A1:E13']]) {
  try { const preview=await wb.render({sheetName,range,scale:1,format:'png'}); await fs.writeFile(path.join(outDir,`preview_${sheetName.replaceAll(' ','_')}.png`),new Uint8Array(await preview.arrayBuffer())); }
  catch(e) { console.error('RENDER',sheetName,String(e)); }
}
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},summary:'formula error scan'});
await fs.writeFile(path.join(outDir,'formula_scan.ndjson'),errors.ndjson,'utf8');
const xlsx=await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(outFile);
console.log(JSON.stringify({outFile,phraseRows:phraseRows.length,visualRows:visualRows.length,audioRows:audioRows.length,findings:findingRows.length,errors:errors.ndjson}));
