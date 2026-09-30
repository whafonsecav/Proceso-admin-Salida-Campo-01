# RECOEVO* · Estudio de campo en Villa Rosita, Usme (Fase 1 urbana)
\* Nombre provisional.

## Cómo presentar
**Doble clic en `05_Presentacion/Presentar.bat`.** Se abre el navegador con la presentación servida desde un servidor local, que es la forma recomendada: el mapa funciona sin internet y los audios saltan al minuto exacto.
- **F**: pantalla completa. **Flechas o espacio**: avanzar. **Esc**: vista general.
- **Cifras y citas con subrayado punteado**: al hacer clic se abre un modal con todas las frases que las sustentan. En el modal se puede filtrar por persona, ver el texto literal y escuchar el audio original.
- **Fotos y videos**: al hacer clic se abren en grande. Se amplían con + / −, con la rueda del ratón o con doble clic, y se mueven arrastrando con la mano.
- **Celular**: si se abre en vertical, las láminas se reorganizan en formato vertical y avanzan hacia abajo. En horizontal se ve la versión de pantalla grande.
- Si se abre `index.html` directamente, sin el servidor, todo funciona, pero el mapa necesita internet y el audio puede no saltar al minuto exacto.

## Carpetas
| Carpeta | Contenido |
|---|---|
| `01_Validacion_Transcripciones/` | Re-transcripción Whisper, versiones revisadas de Audio7 y Audio10, métricas de validación |
| `02_Metodologia/` | `Metodologia_y_Reporte.md` (método, auditoría, hallazgos, límites) y `codebook.json` |
| `03_Base_de_Datos/` | **`RECOEVO_Base_de_Datos_Campo.xlsx`**, `codificacion_A.txt` (codificación auditada), `frases_finales.json`, ediciones y tiempos |
| `04_Scripts/` | Pipeline reproducible (01 → 10) |
| `05_Presentacion/` | `index.html`, `Presentar.bat`, `servidor.py`, `media/` (fotos, videos, audios, teselas del mapa) y `lib/` |

## Reproducir después de editar la codificación
Editar `03_Base_de_Datos/codificacion_A.txt` y luego ejecutar:
```
python 04_Scripts/05_analizar.py
python 04_Scripts/06_datos_presentacion.py
python 04_Scripts/07_excel.py
```
La presentación y el Excel se actualizan solos. Las cifras de las láminas se recalculan a partir de las frases.
