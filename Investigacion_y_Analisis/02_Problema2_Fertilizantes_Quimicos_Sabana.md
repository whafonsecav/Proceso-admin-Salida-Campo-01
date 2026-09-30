# PROBLEMA 2 — LOS FERTILIZANTES QUÍMICOS DE SÍNTESIS EN BOGOTÁ Y LA SABANA DE BOGOTÁ

### Diagnóstico económico, ambiental y de mercado

**Fecha de elaboración:** 10 de septiembre de 2026
**Ámbito geográfico:** Bogotá D.C. y Sabana de Bogotá (Cundinamarca)
**Objeto de estudio:** fertilizantes de síntesis química — urea, DAP, MAP, KCl, NPK compuestos, nitratos y sulfato de amonio
**Ventana temporal:** 2021–2026, con prioridad en 2025–2026

---

## NOTA METODOLÓGICA Y SISTEMA DE ETIQUETADO

Toda cifra de este informe está etiquetada según su grado de confianza:

| Etiqueta | Significado |
|---|---|
| **(a) Oficial verificada** | Proviene de una fuente estadística oficial (DANE, MADR, IDEAM, MinAmbiente, Banco Mundial, Superintendencia Financiera) y fue extraída directamente del documento o microdato fuente. |
| **(b) Prensa / gremio** | Proviene de medios económicos o de gremios (Portafolio, La República, Fedepapa, Asocolflores, Bolsa Mercantil). Verificada contra al menos una segunda fuente cuando fue posible. |
| **(c) Estimación propia** | Cálculo derivado del autor a partir de datos (a) y/o (b). Se explicita la fórmula y los supuestos. |
| **NO ENCONTRADO** | El dato fue buscado y no se halló fuente verificable. No se inventa. |

**Sobre los precios.** La columna vertebral de precios de este informe **no proviene de titulares de prensa sino del microdato oficial del DANE**: los anexos estadísticos municipales del Sistema de Información de Precios y Abastecimiento del Sector Agropecuario – Componente Insumos (SIPSA-I). Se descargaron y procesaron directamente:

- `anex-SIPSAinsumosmunicipio-jul2026.xlsx` (1.527 registros de precios de fertilizantes por municipio, julio 2026)
- `anex-SIPSAInsumos-SeriesHistoricasMun-2021-2026.xlsx` (112.978 registros; se filtraron 20.981 registros de los cinco fertilizantes de síntesis principales en presentación de bulto de 50 kg)

De este universo se aislaron los **283 registros de precios correspondientes a Bogotá D.C. y a 22 municipios de Cundinamarca**, lo que permite reportar precios *regionales* y no solo promedios nacionales. Los precios internacionales se tomaron del *Pink Sheet* del Banco Mundial (ediciones de junio y septiembre de 2026) y de la serie histórica anual `CMO-Historical-Data-Annual.xlsx`, descargadas y procesadas directamente.

**Advertencia sobre 2026.** El año 2026 es un año **atípico y de crisis** en el mercado mundial de fertilizantes, por la disrupción del Estrecho de Ormuz. Cualquier modelo financiero construido sobre precios de 2026 debe incorporar explícitamente esta volatilidad. El informe documenta tanto el pico como la corrección posterior.

---

## 1. RESUMEN EJECUTIVO

1. **Colombia importa prácticamente todo el fertilizante que consume.** El consumo nacional se ubica entre **2,4 y 2,5 millones de toneladas/año** y en 2025 se importaron **2,3 millones de toneladas**, es decir, cerca del **90 % de la demanda**. *(b) — La República / Portafolio, 2026, con datos DANE.*

2. **Más del 90 % de las materias primas** empleadas incluso por las plantas mezcladoras que operan en el país proviene del exterior; la producción nacional cubre apenas **5 %–10 %** de la demanda doméstica. *(b) — Agronegocios, 2025.*

3. **No existe base geológica para la autosuficiencia.** El país no tiene reservas de potasio, sus depósitos de fosfatos (Huila) están sin explotar y no dispone de gas natural excedentario para producir amoníaco y urea. *(b) — Portafolio, 5 abril 2026, citando a Jorge Bedoya (SAC) y Andrés Valencia (exministro de Agricultura).*

4. **La factura de importación fue de USD CIF 1.469 millones en 2023**, para un volumen cercano a 2,1 millones de toneladas — un valor unitario implícito de **USD 700/t**. *(b) — Fedepapa con datos Legiscomex, boletín 190, marzo 2024.*

5. **El precio de la urea en Cundinamarca y Bogotá subió 36,2 % en un año**: de $136.766 por bulto de 50 kg en julio de 2025 a **$186.235 en julio de 2026**. *(a) — DANE SIPSA-I, microdato municipal, cálculo propio sobre 8 municipios.*

6. **Dentro de 2026 el alza fue aún más violenta:** la urea pasó de $139.049/bulto en enero a un pico de **$197.075 en mayo (+41,7 % en cinco meses)** en Cundinamarca/Bogotá. *(a) — DANE SIPSA-I.*

7. **El detonante fue geopolítico.** El Estrecho de Ormuz —por donde transita cerca de un tercio del comercio marítimo mundial de fertilizantes, unos 16 millones de toneladas anuales— sufrió disrupciones que llevaron la urea internacional a **USD 856,9/t en abril de 2026**, su nivel más alto en cuatro años. *(a) — Banco Mundial, Pink Sheet, y (b) blog de datos del Banco Mundial, 14 mayo 2026.*

8. **El mercado internacional ya corrigió, pero el fósforo no.** La urea FOB cayó a **USD 390/t en agosto de 2026** (–54 % desde el pico de abril), mientras el **DAP alcanzó USD 793,5/t en agosto de 2026**, su máximo del ciclo. *(a) — Banco Mundial, Pink Sheet, septiembre 2026.*

9. **El precedente de 2021–2022 fue peor.** La urea nacional pasó de **$78.567/bulto en enero de 2021 a $260.562 en mayo de 2022: un alza de 231,6 %**. El KCl subió 229,7 % y el sulfato de amonio 211,8 % en el mismo lapso. *(a) — DANE SIPSA-I, cálculo propio sobre 67 meses de serie.*

10. **La volatilidad es estructural, no excepcional.** En 67 meses (ene-2021 a jul-2026) el precio mensual de la urea osciló entre $78.567 y $260.562 — un **rango de 3,32 veces**, con un coeficiente de variación de **30,9 %**. El KCl osciló 3,30x (CV 37,9 %). *(a)+(c) — cálculo propio sobre microdato DANE.*

11. **Los fertilizantes pesan entre 17 % y 19 % del costo total por hectárea de papa de variedades blancas**, y específicamente en Cundinamarca **18,5 % (variedad Superior) y 19,1 % (Diacol Capiro)**. *(b) — Fedepapa, Boletín Regional Cundinamarca, 2023 y boletines 2026.*

12. **A escala nacional los fertilizantes representan entre 12 % y 30 % de los costos de producción agrícola**, y pueden llegar hasta **un tercio** en algunos cultivos. *(b) — La República, abril 2026.*

13. **La Sabana de Bogotá sembró 76.626 hectáreas en 2025**, de las cuales **58.087 ha (75,8 %) son papa** — el cultivo más intensivo en fertilización de la región. *(a) — Evaluaciones Agropecuarias Municipales (EVA), MADR, microdato procesado para 31 municipios sabaneros.*

14. **Cundinamarca concentra el 71 % de las hectáreas de flores de Colombia**, con Madrid (18 %), Facatativá (9 %), El Rosal (8 %), Funza (5 %) y Tocancipá (5 %) a la cabeza; el sector genera **115.500 empleos directos**. *(b) — Alcaldía Mayor de Bogotá / Asocolflores, 2025-2026.*

15. **El gasto anual en fertilizantes solo del cultivo de papa en la Sabana se estima en $368.256 millones COP (USD 118,8 millones)** a precios de julio de 2026 y para un ciclo de siembra. *(c) — estimación propia; ver §5.4 para la fórmula.*

16. **El 80,3 % de los suelos de Cundinamarca están afectados por algún grado de erosión, y 5 % por erosión severa**, frente a 40 % en el promedio nacional. En las áreas de uso exclusivamente agrícola del país (2.078.094 ha), **el 93 % presenta erosión** por manejo inadecuado. *(a) — IDEAM/MADS/UDCA, Estudio Nacional de Degradación de Suelos por Erosión; difundido por MinAmbiente y Agrosavia.*

17. **El sector agricultura aporta el 20,69 % de las emisiones netas de GEI de Colombia.** Dentro de ese sector, las **emisiones directas e indirectas de N₂O de suelos agrícolas representan el 16,61 %** y la aplicación de urea otro 0,38 %. *(a) — Inventario Nacional de Emisiones y Absorciones Atmosféricas de Colombia, MinAmbiente/IDEAM, datos 2021, publicado 2025.*

18. **En 2021 se aplicaron 370.357 toneladas de nitrógeno provenientes de fertilizantes inorgánicos** a los suelos colombianos. *(a) — Inventario Nacional de Emisiones, MinAmbiente, 2025.*

19. **La eficiencia agronómica del nitrógeno es baja: menos del 50 % del N aplicado es aprovechado por el cultivo**; el resto se pierde por lixiviación (como nitrato), volatilización (amoníaco, N₂O, NOx) y escorrentía. *(b) — literatura agronómica revisada; ver §10.*

20. **El límite sanitario de nitratos en agua potable es de 10 mg/L**; por encima de ese valor, los lactantes menores de seis meses pueden desarrollar metahemoglobinemia ("síndrome del bebé azul"), potencialmente mortal. La escorrentía de fertilizantes es una de las tres fuentes reconocidas de esta contaminación. *(a) — US EPA, National Primary Drinking Water Regulations.*

21. **El abono orgánico es 8 veces más barato por bulto pero 3,9 veces más caro por kilogramo de nitrógeno.** Bulto de 50 kg: $23.616 (orgánico) vs $188.053 (urea). Por kg de N: **$31.488 (orgánico, al 1,5 % N) vs $8.176 (urea)**. *(a)+(c) — DANE SIPSA-I jul-2026 y cálculo propio.*

22. **Pero el abono orgánico es la mitad de volátil.** En 67 meses su rango máximo/mínimo fue de **1,64x (CV 15,8 %)** frente a **3,32x (CV 30,9 %)** de la urea. *(a)+(c).*

23. **Existe una brecha enorme entre el precio internacional y el precio de finca.** En julio de 2026 la urea FOB costaba USD 400/t y en el mostrador de Cundinamarca **USD 1.138/t: un múltiplo de 2,85 veces**. *(a)+(c) — Banco Mundial y DANE SIPSA-I, TRM jul-2026.*

24. **La política pública existe en el papel pero no en la industria.** El Gobierno propuso en mayo de 2026 un acuerdo Ecopetrol–Monómeros con una inversión de **$1 billón COP (USD 274 millones)** para subsidiar fertilizantes en 2026; la compra de Monómeros nunca se materializó y no hubo inversiones concretas en minería de fosfatos. *(b) — El Heraldo, Infobae, Portafolio, 2026.*

25. **TRM de referencia:** **$3.099,48 COP/USD** (vigencia 10 de septiembre de 2026) y **$3.101,00** (11 de septiembre de 2026). El promedio de julio de 2026 —mes de los precios de este informe— fue **$3.272,01**. *(a) — Superintendencia Financiera de Colombia vía datos.gov.co.*

---

## 2. EL MERCADO COLOMBIANO DE FERTILIZANTES: DEPENDENCIA DE IMPORTACIONES Y VULNERABILIDAD

### 2.1. La magnitud de la dependencia

Colombia es un país **estructuralmente importador** de fertilizantes de síntesis. Las cifras convergentes de distintas fuentes dibujan el siguiente cuadro:

| Indicador | Valor | Año | Fuente | Confianza |
|---|---|---|---|---|
| Consumo aparente nacional | 2,4 – 2,5 millones t | 2025-2026 | La República / Portafolio | (b) |
| Importaciones | 2,3 millones t | 2025 | DANE vía prensa | (b) |
| Importaciones (ene–oct) | 1,94 millones t (+10 % a/a) | 2025 | DANE vía Portafolio | (b) |
| Importaciones | 2,13 millones t | 2024 | DANE vía Portafolio | (b) |
| Dependencia de importaciones | ~90 % de las necesidades | 2026 | La República | (b) |
| Materias primas importadas | >90 % | 2025 | Agronegocios | (b) |
| Cobertura de producción nacional | 5 %–10 % de la demanda | 2025 | Agronegocios | (b) |
| Volumen transado en mercado interno | 1,5 millones t / ~$2 billones COP | — | Bolsa Mercantil de Colombia | (b) |
| Crecimiento del consumo aparente 2012–2022 | +78 % (5,9 % anual promedio) | 2022 | Bolsa Mercantil de Colombia | (b) |
| Exportaciones (ene–nov) | 160.000 t (+18 %) | 2025 | Portafolio | (b) |

> **Lectura clave:** el país exporta 160.000 t e importa 2.300.000 t. La balanza física es de aproximadamente **14 toneladas importadas por cada tonelada exportada**. *(c) — cálculo propio.*

### 2.2. ¿Por qué Colombia no produce sus fertilizantes?

La razón no es de voluntad política sino **geológica y energética**. Según Portafolio (5 de abril de 2026), recogiendo declaraciones de Jorge Bedoya, presidente de la SAC:

- **No hay potasio.** Colombia carece de reservas de potasio explotables, insumo del que no existe sustituto agronómico directo.
- **Los fosfatos están sin explotar.** Existen depósitos en el departamento del Huila, pero nunca se desarrolló la minería de roca fosfórica. El desafío técnico pendiente, según fuentes del sector, es "mejorar la solubilidad del fósforo nacional mediante procesos térmicos, acidulación o microorganismos eficientes".
- **No hay gas suficiente.** La producción de amoníaco —precursor de la urea— exige gas natural barato y abundante. Colombia es actualmente **importador neto de gas**.

Andrés Valencia, exministro de Agricultura, resumió la situación: el país *"no es un productor de fertilizantes, ni lo será en el corto plazo"*. Las instalaciones domésticas actuales **solo mezclan** componentes nitrogenados, fosfatados y potásicos importados; no producen las materias primas.

La Bolsa Mercantil de Colombia es igualmente categórica: *"En Colombia no existe potencial para su producción nacional"* de amoníaco y urea, por insuficiencia de reservas de gas bajo contrato y altos costos de extracción comparados con otros países.

### 2.3. Concentración y riesgo de origen

La estructura de proveedores se reconfiguró tras la guerra Rusia-Ucrania:

| Grupo de fertilizante | Proveedor líder 2025 | Observación |
|---|---|---|
| Nitrogenados | **China** (desplazó a Rusia) | China representó **18,3 %** del total importado en 2025 |
| Fosfatados | **Estados Unidos**, seguido de Rusia | — |
| Potásicos | **Canadá** | Volúmenes decrecientes |
| Compuestos (NPK) | **Rusia, Finlandia, Noruega** | — |

*(b) — Portafolio, con datos DANE, 2026.*

**Los cinco fertilizantes más importados (12 meses a abril de 2026):** *(b) — La República, 2026*

| Producto | Volumen | Valor | Participación |
|---|---|---|---|
| Urea | 665.780 t | USD 295 millones | 27,8 % del total |
| Cloruro de potasio | 622.550 t | USD 217 millones | — |
| NPK compuesto | 269.460 t | USD 138 millones | — |
| MAP (fosfato monoamónico) | 155.720 t | — | — |
| DAP (fosfato diamónico) | 141.590 t | — | — |

**Composición por grupo en 2023** *(b) — Fedepapa/Legiscomex, boletín 190*:

- Nitrogenados: **46 %** del volumen (964.000 t), de las cuales **dos terceras partes fueron urea**
- Potásicos: **26 %** (577.000 t)
- Compuestos: **27 %** (556.000 t)
- Orgánicos y fosfatados: apenas **1 %** del total importado

> **Riesgo identificado:** la dependencia de proveedores asiáticos —particularmente China— expone al país a controles ambientales, cambios en licencias de exportación o disrupciones logísticas fuera de su control. Portafolio (2026) lo señala explícitamente. A abril de 2026 los **inventarios nacionales cubrían apenas 2 a 3 meses** de consumo *(b) — La República*.

### 2.4. El eslabón perdido: de FOB a finca

Un hallazgo central de este informe es la **brecha entre el precio internacional y el precio que paga el agricultor de la Sabana**:

| Producto | Precio FOB internacional (jul-2026) | Precio minorista Cundinamarca (jul-2026) | Múltiplo |
|---|---|---|---|
| Urea 46 % | USD 400,0/t | **USD 1.138,4/t** | **2,85x** |
| DAP 18-46-0 | USD 781,3/t | **USD 1.428,3/t** | **1,83x** |
| KCl (MOP) 0-0-60 | USD 396,5/t | **USD 781,3/t** | **1,97x** |

*(a) Precios FOB: Banco Mundial, Pink Sheet, septiembre 2026 (urea prill spot FOB Middle East; KCl granular spot CFR Brasil; DAP spot FOB US Gulf). (a) Precios minoristas: DANE SIPSA-I, promedio Cundinamarca+Bogotá, julio 2026. TRM julio 2026: $3.272,01. (c) Múltiplo: cálculo propio.*

Esta brecha incorpora flete marítimo, nacionalización, transporte interno, almacenamiento, márgenes de mayorista y minorista, y costos financieros. **Para el modelo financiero es crítico usar el precio minorista, no el FOB.** La cifra relevante para un productor de la Sabana es la de la columna central.

---

## 3. PRECIOS: SERIE 2021–2026 Y PRECIOS VIGENTES

### 3.1. Precios internacionales — Banco Mundial (USD por tonelada métrica)

**Serie anual nominal** *(a) — Banco Mundial, CMO Historical Data Annual*

| Producto | 2018 | 2019 | 2020 | **2021** | **2022** | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Urea (E. Europa) | 249,4 | 245,3 | 229,1 | **483,2** | **700,0** | 358,0 | 338,3 | 422,7 |
| DAP | 393,4 | 306,4 | 312,4 | **601,0** | **772,2** | 550,0 | 563,7 | 685,2 |
| TSP | 346,7 | 294,5 | 265,0 | **538,2** | **716,1** | 480,2 | 474,6 | 577,6 |
| Cloruro de potasio | 215,5 | 255,5 | 241,1 | **542,8** | **863,4** | 383,2 | 295,1 | 347,5 |
| Roca fosfórica | 87,9 | 88,0 | 76,1 | **123,2** | **266,2** | 321,7 | 152,5 | 152,5 |

**El choque de 2021–2022 en detalle (serie mensual)** *(a) — Banco Mundial, CMO Historical Data Monthly*

| Mes | Urea | DAP | KCl | TSP | Roca fosfórica |
|---|---|---|---|---|---|
| ene-2021 | 265,0 | 421,3 | 255,5 | 337,6 | 85,0 |
| nov-2021 | **900,5** | 726,7 | 806,9 | 665,0 | 153,1 |
| mar-2022 | 872,5 | 938,1 | 977,5 | 792,5 | 178,8 |
| **abr-2022** | **925,0** | **954,0** | **1.202,0** | **856,0** | 249,5 |
| jun-2022 | 690,0 | 783,8 | 1.101,9 | 730,1 | 287,5 |
| dic-2022 | 519,4 | 625,0 | 513,8 | 584,4 | 300,0 |

> **Choque Rusia-Ucrania cuantificado:** de enero de 2021 a abril de 2022 la urea internacional subió **+249 %** (USD 265 → 925/t) y el cloruro de potasio **+370 %** (USD 255,5 → 1.202/t). *(c) — cálculo propio sobre datos (a).*

**El choque de 2026 — Estrecho de Ormuz** *(a) — Banco Mundial, Pink Sheet, ediciones junio y septiembre 2026*

| Producto | 2025 (anual) | 2026 Q1 | mar-26 | abr-26 | may-26 | jun-26 | jul-26 | ago-26 |
|---|---|---|---|---|---|---|---|---|
| Urea (E. Europa) | 422,7 | 537,7 | 725,6 | **856,9** | 770,5 | 453,1 | 400,0 | **390,0** |
| DAP | 685,2 | 634,7 | 658,3 | 725,3 | 769,5 | 783,8 | 781,3 | **793,5** |
| Cloruro de potasio | 347,5 | 373,0 | 380,6 | 401,3 | 405,0 | 402,5 | 396,5 | 386,9 |
| TSP | 577,6 | 541,2 | 558,1 | 658,1 | 713,5 | 735,6 | 719,5 | 704,4 |
| Roca fosfórica | 152,5 | 152,5 | 152,5 | 152,5 | 152,5 | 156,9 | 170,0 | 170,0 |

> **Dos dinámicas divergentes en 2026.** El nitrógeno (urea) tuvo un pico agudo y una corrección brutal: **+59 % de enero a abril y –54 % de abril a agosto**. El fósforo (DAP, TSP, roca fosfórica) mantiene una tendencia alcista sostenida: el DAP cerró agosto de 2026 en **USD 793,5/t, el nivel más alto de toda la serie 2023-2026**. *(c) — cálculo propio.*

**Causa documentada:** *"Desde que comenzó el conflicto hace dos meses, las disrupciones en el Estrecho de Ormuz han tensionado el mercado global de fertilizantes. Esa vía marítima maneja cerca de un tercio del comercio marítimo mundial de fertilizantes, unos 16 millones de toneladas anuales."* El Banco Mundial precisó que Medio Oriente representa *"casi una cuarta parte de las exportaciones mundiales de urea"*. *(b) — Blog de datos abiertos del Banco Mundial, 14 de mayo de 2026.* La prensa colombiana reportó la cifra de **45 % del comercio mundial de fertilizantes** transitando por Ormuz *(b) — La República, 2026*; este informe **prefiere la cifra del Banco Mundial (un tercio / ~16 Mt)** por ser la fuente primaria.

**Proyecciones del Banco Mundial para 2026-2027** *(b)*:

| Producto | Variación esperada 2026 | Variación esperada 2027 |
|---|---|---|
| Urea | **+60 %** promedio anual | A la baja |
| DAP | +6 % | –10 % |
| MOP (KCl) | +12 % | –6 % |
| Índice general de fertilizantes | **+30 % o más** | — |

### 3.2. Precios en Colombia — DANE SIPSA-I (COP por bulto de 50 kg)

#### 3.2.1. Promedio anual nacional

*(a) — DANE SIPSA-I, serie histórica municipal 2021-2026; cálculo propio de promedios sobre 20.981 registros. Nota: 2026 comprende enero–julio.*

| Producto | 2021 | **2022** | 2023 | 2024 | 2025 | **2026 (ene-jul)** |
|---|---|---|---|---|---|---|
| Urea 46 % | 116.294 | **225.843** | 156.278 | 112.781 | 132.501 | **162.449** |
| DAP 18-46-0 | 139.309 | **241.589** | 210.928 | 169.261 | 202.231 | **222.856** |
| Cloruro de potasio 0-0-60 | 106.449 | **230.777** | 183.921 | 107.795 | 110.526 | **121.640** |
| NPK 15-15-15 | 119.263 | **209.230** | 182.257 | 137.775 | 151.731 | **167.334** |
| Sulfato de amonio 21-0-0-24(S) | 71.973 | **145.513** | 104.431 | 72.911 | 83.880 | **89.959** |

#### 3.2.2. Promedio anual — Cundinamarca + Bogotá D.C.

*(a) — DANE SIPSA-I, filtrado a Bogotá D.C. y municipios de Cundinamarca; cálculo propio.*

| Producto | 2021 | **2022** | 2023 | 2024 | 2025 | **2026 (ene-jul)** |
|---|---|---|---|---|---|---|
| Urea 46 % | 116.511 | **220.093** | 154.859 | 114.685 | 134.152 | **163.554** |
| DAP 18-46-0 | 142.052 | **235.458** | 210.085 | 171.378 | 203.967 | **222.527** |
| Cloruro de potasio 0-0-60 | 107.616 | **240.307** | 168.138 | 107.519 | 113.341 | **121.805** |
| NPK 15-15-15 | 119.220 | **205.450** | 179.356 | 137.212 | 150.831 | **166.745** |
| Sulfato de amonio 21-0-0-24(S) | 72.740 | **142.000** | 106.786 | 75.250 | 91.406 | **90.859** |

> Los precios de la Sabana **siguen de cerca al promedio nacional** (desviaciones inferiores al 5 % en la mayoría de productos y años), lo que valida el uso de cualquiera de las dos series. Para el modelo financiero se recomienda usar la serie de Cundinamarca/Bogotá.

#### 3.2.3. El choque de 2021–2022 en el mercado colombiano

*(a) DANE SIPSA-I + (c) cálculo propio. Promedio mensual nacional.*

| Producto | ene-2021 | Pico 2022 (mes) | Variación |
|---|---|---|---|
| Urea 46 % | 78.567 | **260.562** (may-22) | **+231,6 %** |
| DAP 18-46-0 | 97.006 | **268.529** (jun-22) | **+176,8 %** |
| Cloruro de potasio | 77.426 | **255.290** (jun-22) | **+229,7 %** |
| NPK 15-15-15 | 92.283 | **228.029** (may-22) | **+147,1 %** |
| Sulfato de amonio | 50.690 | **158.072** (may-22) | **+211,8 %** |

**Trayectoria mensual de la urea (nacional, COP/bulto 50 kg)** *(a)*:

| 2021 | Ene | Feb | Mar | Abr | May | Jun | Jul | Ago | Sep | Oct | Nov | Dic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | 78.567 | 80.860 | 90.164 | 98.357 | 101.192 | 104.574 | 111.875 | 121.290 | 129.211 | 139.244 | 169.531 | 194.907 |
| **2022** | 205.582 | 210.461 | 213.087 | 242.097 | **260.562** | 255.276 | 237.000 | 225.039 | 219.106 | 214.054 | 216.964 | 216.712 |

#### 3.2.4. El repunte de 2026 en Cundinamarca y Bogotá

*(a) — DANE SIPSA-I, promedio mensual Cundinamarca+Bogotá, COP/bulto 50 kg.*

| Producto | Ene-26 | Feb-26 | Mar-26 | Abr-26 | May-26 | Jun-26 | **Jul-26** | Δ ene→máx |
|---|---|---|---|---|---|---|---|---|
| Urea 46 % | 139.049 | 138.499 | 142.554 | 179.575 | **197.075** | 192.107 | **186.235** | **+41,7 %** |
| DAP 18-46-0 | 213.885 | 214.153 | 216.375 | 227.569 | **235.808** | 235.445 | **233.669** | +10,3 % |
| KCl 0-0-60 | 115.913 | 116.753 | 117.977 | 122.570 | 127.288 | **127.886** | **127.821** | +10,3 % |
| NPK 15-15-15 | 146.316 | 146.831 | 152.697 | 169.462 | **180.193** | 179.620 | **178.059** | +23,2 % |
| Sulfato de amonio | 88.000 | 87.750 | 85.583 | 85.000 | **105.500** | 95.667 | **90.500** | +19,9 % |

**Variación interanual julio 2025 → julio 2026 (Cundinamarca + Bogotá)** *(a)+(c)*:

| Producto | jul-2025 | jul-2026 | Variación |
|---|---|---|---|
| Urea 46 % | 136.766 | 186.235 | **+36,2 %** |
| DAP 18-46-0 | 207.549 | 233.669 | **+12,6 %** |
| NPK 15-15-15 | 151.832 | 178.059 | **+17,3 %** |
| KCl 0-0-60 | 114.951 | 127.821 | **+11,2 %** |
| Sulfato de amonio | 92.900 | 90.500 | –2,6 % |

> Nota de coherencia: La República reportó un alza del **51,5 %** en el índice norteamericano Green Markets entre abril de 2025 y abril de 2026, y **+78 % para la urea internacional**. El dato de este informe (**+36,2 % para la urea en Cundinamarca**) es *menor* y *no lo contradice*: el precio doméstico minorista amortigua el choque internacional gracias a inventarios, contratos previos y a la **apreciación del peso** (la TRM pasó de $4.052 promedio en 2025 a $3.518 promedio en 2026, es decir, **–13,2 %**), que abarata las importaciones en pesos. Portafolio reportó exactamente este fenómeno: precios internacionales +25 % (urea), +22 % (DAP), +18 % (KCl) frente a **+14 % promedio doméstico** en 2025. *(b)+(c).*

### 3.3. Volatilidad medida (2021–2026, 67 meses)

*(a) DANE SIPSA-I + (c) cálculo propio. Promedio mensual nacional, bulto de 50 kg.*

| Producto | Mínimo | Máximo | Promedio | **Coef. variación** | **Máx/Mín** |
|---|---|---|---|---|---|
| Cloruro de potasio 0-0-60 | 77.426 | 255.290 | 146.233 | **37,9 %** | **3,30x** |
| Urea 46 % | 78.567 | 260.562 | 151.110 | **30,9 %** | **3,32x** |
| Sulfato de amonio | 50.690 | 158.072 | 95.386 | **30,3 %** | **3,12x** |
| NPK 15-15-15 | 92.283 | 228.029 | 161.034 | 21,7 % | 2,47x |
| DAP 18-46-0 | 97.006 | 268.529 | 196.951 | 20,5 % | 2,77x |
| *Cal dolomita (referencia)* | 10.240 | 18.733 | 14.839 | 17,4 % | 1,83x |
| *Abono orgánico (referencia)* | 14.557 | 23.932 | 19.953 | **15,8 %** | **1,64x** |

> **Hallazgo central para el análisis de riesgo:** el productor de la Sabana enfrenta, en el insumo que representa ~19 % de su costo, una **volatilidad de precio del orden de 2 veces la de los insumos no sintéticos**. Un fertilizante nitrogenado puede triplicar su precio en 16 meses (ene-2021 → may-2022) sin que el precio de venta de la papa se ajuste en igual proporción.

---

## 4. CARACTERIZACIÓN AGRÍCOLA DE LA SABANA DE BOGOTÁ

### 4.1. Área sembrada por municipio (2025)

*(a) — Evaluaciones Agropecuarias Municipales (EVA), Ministerio de Agricultura y Desarrollo Rural, dataset `uejq-wxrr`, datos.gov.co. Procesamiento propio sobre 15.584 registros de Cundinamarca; se seleccionaron 30 municipios sabaneros.*

| Municipio | Área sembrada total (ha) | Papa (ha) |
|---|---|---|
| Villapinzón | 17.424,7 | 17.075,0 |
| Tausa | 15.875,0 | 15.090,0 |
| Mosquera | 3.672,3 | 480,0 |
| Sibaté | 3.582,9 | 2.728,0 |
| Madrid | 3.490,4 | 1.156,0 |
| Tenjo | 3.158,6 | 1.050,0 |
| Guatavita | 3.073,5 | 2.945,0 |
| La Calera | 2.755,0 | 2.345,0 |
| Chocontá | 2.610,0 | 2.268,0 |
| Zipaquirá | 2.572,8 | 2.440,0 |
| Facatativá | 2.363,2 | 943,0 |
| Sesquilé | 2.160,4 | 2.080,0 |
| Bojacá | 1.898,0 | 670,0 |
| Suesca | 1.607,0 | 1.536,0 |
| Funza | 1.566,0 | 525,0 |
| Soacha | 1.413,7 | 885,5 |
| Subachoque | 1.287,0 | 765,0 |
| Zipacón | 948,5 | 430,0 |
| Cota | 895,6 | 160,8 |
| Cogua | 795,5 | 700,0 |
| El Rosal | 716,0 | 420,0 |
| Guasca | 505,0 | 323,0 |
| Sopó | 442,0 | 185,0 |
| Chía | 398,7 | 130,0 |
| Cucunubá | 389,8 | 351,0 |
| Tabio | 375,1 | 209,0 |
| Cajicá | 294,0 | 59,5 |
| Tocancipá | 167,9 | 60,0 |
| Nemocón | 151,0 | 61,0 |
| Gachancipá | 36,6 | 16,0 |
| **TOTAL SABANA** | **76.626,3** | **58.086,9** |

### 4.2. Composición por grupo de cultivo — Sabana de Bogotá, 2025

*(a) — EVA/MADR, procesamiento propio.*

| Grupo de cultivo | Hectáreas | Participación |
|---|---|---|
| Raíces y tubérculos (papa) | 58.086,9 | **75,8 %** |
| Hortalizas | 8.771,3 | 11,4 % |
| Cereales | 3.741,3 | 4,9 % |
| Leguminosas | 3.332,7 | 4,3 % |
| Frutales | 2.361,9 | 3,1 % |
| Condimentos, bebidas, aromáticas | 242,1 | 0,3 % |
| Cultivos tropicales tradicionales | 90,2 | 0,1 % |
| **TOTAL** | **76.626,3** | **100 %** |

**Principales cultivos individuales (ha, 2025):** Papa 58.086,9 · Maíz 3.576,3 · Arveja 3.199,0 · Zanahoria 2.504,7 · Lechuga 1.969,8 · Fresa 1.530,6 · Otras hortalizas 1.474,2 · Espinaca 532,5 · Cebolla de bulbo 489,8 · Arándano 389,9 · Apio 357,8 · Brócoli 328,9 · Cilantro 237,7 · Repollo 201,0 · Acelga 193,9.

### 4.3. Evolución del área sembrada — Sabana de Bogotá

*(a) — EVA/MADR.*

| Año | Papa (ha) | Total Sabana (ha) |
|---|---|---|
| 2019 | 52.897,6 | 73.442,1 |
| 2020 | 51.806,4 | 72.039,8 |
| 2021 | 53.522,3 | 73.278,7 |
| 2022 | 53.152,1 | 71.381,2 |
| 2023 | 57.831,9 | 75.297,8 |
| 2024 | 56.573,5 | 74.206,7 |
| **2025** | **58.086,9** | **76.626,3** |

> El área sembrada se **contrajo en 2022** (el año del choque de precios de fertilizantes, –2,6 % frente a 2021) y se recuperó a partir de 2023 cuando los precios cedieron. La correlación es consistente con el diagnóstico de Fedepapa: *"las fluctuaciones en los costos de producción durante los últimos dos años han impactado significativamente en la producción nacional de papa, incidiendo en la reducción de las áreas sembradas"*.

### 4.4. Contexto departamental

| Indicador | Valor | Año | Fuente | Confianza |
|---|---|---|---|---|
| Área sembrada total Cundinamarca | 267.061,1 ha | 2025 | EVA/MADR | (a) |
| Área sembrada de papa, Cundinamarca | 73.884,9 ha | 2025 | EVA/MADR | (a) |
| Área sembrada hortalizas, Cundinamarca | 16.749,7 ha | 2025 | EVA/MADR | (a) |
| Superficie con aptitud para papa | 473.675 ha | 2023 | Fedepapa | (b) |
| Aptitud alta / media / baja para papa | 52,1 % / 43,9 % / 3,8 % | 2023 | Fedepapa | (b) |
| Frontera agrícola de Cundinamarca | 62,3 % del territorio | 2023 | Fedepapa | (b) |
| Municipios de Cundinamarca con reporte agrícola | 60 de 116 reportaron papa en 2022 | 2022 | Fedepapa | (b) |
| Rendimiento promedio de papa, Cundinamarca | 24,16 t/ha | 2023 | Fedepapa | (b) |
| Producción de papa, Cundinamarca | >1.799.000 t/año (71.450 ha cosechadas) | 2025 | Prensa/Gobernación | (b) |

### 4.5. Floricultura de la Sabana

La floricultura es el segundo gran consumidor de fertilizantes de síntesis de la región y **no aparece en las EVA** porque se reporta por canales gremiales y de comercio exterior.

| Indicador | Valor | Año | Fuente | Confianza |
|---|---|---|---|---|
| Participación de Cundinamarca en hectáreas de flores del país | **71 %** | 2025-2026 | Alcaldía de Bogotá / Asocolflores | (b) |
| Participación de la Sabana en área nacional de flores y follajes de corte | **75 %** | — | Prensa sectorial | (b) |
| Empleos directos generados | **115.500** | 2025-2026 | Alcaldía de Bogotá | (b) |
| Participación femenina en el empleo | ~60 % | 2025-2026 | Alcaldía de Bogotá | (b) |
| Exportaciones aéreas desde Cundinamarca | 60.000 t | 2025 | Alcaldía de Bogotá | (b) |
| Exportaciones marítimas | >5.000 t | 2025 | Alcaldía de Bogotá | (b) |
| Principal destino | EE. UU. (80 % del valor exportado en temporada de San Valentín 2025) | 2025 | Alcaldía de Bogotá | (b) |

**Distribución municipal de la floricultura de la Sabana** *(b)*: Madrid **18 %** · Facatativá **9 %** · El Rosal **8 %** · Funza **5 %** · Tocancipá **5 %**. Especies principales: rosas, claveles y crisantemos (también alstroemerias).

**Hectáreas absolutas de flores en la Sabana de Bogotá: NO ENCONTRADO** en fuente oficial actualizada. El portal de cifras de Asocolflores consultado el 10 de septiembre de 2026 devolvió los indicadores sin poblar (valores en cero), y la información detallada está restringida al portal de afiliados. **Recomendación:** solicitar la cifra directamente a Asocolflores antes de usarla en el modelo financiero.

### 4.6. Estructura de la propiedad

| Indicador | Valor | Año | Fuente | Confianza |
|---|---|---|---|---|
| Empresas activas en municipios paperos de Cundinamarca | 69.272 | sep-2023 | Fedepapa | (b) |
| De ellas, microempresas | **95 %** | 2023 | Fedepapa | (b) |
| Pequeñas | 3 % | 2023 | Fedepapa | (b) |
| Medianas | 1 % | 2023 | Fedepapa | (b) |
| Municipios con más empresas | Sibaté (938), Cogua (803), Villapinzón (562) | 2023 | Fedepapa | (b) |
| Población rural de Cundinamarca | 22 % del total (48 % mujeres / 52 % hombres) | 2023 | Fedepapa | (b) |

> **Predominio de pequeños productores confirmado:** el 95 % de las unidades empresariales de los municipios paperos son microempresas. Fedepapa documenta además *"la salida de una porción de pequeños productores de la actividad"*, con concentración progresiva en grandes productores *"los cuales en su mayoría se encuentran en la sabana de Cundinamarca"*. Esto implica que el choque de precios de fertilizantes **opera como un mecanismo de exclusión de los productores más pequeños**.

**Número exacto de productores agrícolas de la Sabana de Bogotá y distribución por tamaño de predio: NO ENCONTRADO** en fuente oficial desagregada actualizada. Se recomienda consultar los microdatos del Censo Nacional Agropecuario o solicitar el dato a la Secretaría de Agricultura de Cundinamarca.

---

## 5. PESO DE LOS FERTILIZANTES EN LA ESTRUCTURA DE COSTOS

### 5.1. Tabla consolidada por cultivo

| Cultivo | Participación de fertilizantes en el costo total | Ámbito | Año | Fuente | Confianza |
|---|---|---|---|---|---|
| **Papa var. Superior** | **18,5 %** | Cundinamarca | 2023 | Fedepapa, Boletín Regional Cundinamarca | (b) |
| **Papa var. Diacol Capiro** | **19,1 %** | Cundinamarca | 2023 | Fedepapa, Boletín Regional Cundinamarca | (b) |
| **Papa, variedades blancas** | **17 % – 19 %** | Nacional (por departamento) | 2026 | Fedepapa, Boletín 240 | (b) |
| **Papa, variedades amarillas (criolla)** | **9 % – 13 %** | Nacional | 2026 | Fedepapa, Boletín 240 | (b) |
| **Flores (finca florícola)** | Mano de obra ≈ **60 %** del costo; fertilizantes dentro del bloque de insumos (participación específica **NO ENCONTRADA**) | Sabana de Bogotá | 2022-2026 | Prensa sectorial / Asocolflores | (b) |
| **Promedio agrícola nacional** | **12 % – 30 %**, hasta **un tercio** en algunos cultivos | Colombia | 2026 | La República | (b) |
| **Hortalizas de la Sabana** | **NO ENCONTRADO** con desagregación específica | — | — | — | — |
| **Pastos / lechería especializada** | **NO ENCONTRADO** con desagregación específica para la Sabana | — | — | — | — |

> **Advertencia importante para el modelo financiero:** no se localizó una estructura de costos oficial y desagregada por rubro para **hortalizas de la Sabana**, para **lechería especializada** ni una cifra publicada de participación de fertilizantes en el costo florícola. Usar el rango general 12 %–30 % como aproximación, o solicitar los estudios de costos directamente a Fedegán (lechería), Asohofrucol (hortalizas) y Asocolflores (flores). **No se debe inventar un porcentaje.**

### 5.2. Costo de fertilización por hectárea — papa

*(b) — Fedepapa. Promedio de Antioquia, Nariño, Cundinamarca y Boyacá.*

| Momento | Costo de fertilización por hectárea (papa Diacol Capiro) |
|---|---|
| Enero 2023 | $7.136.280 |
| **Junio 2023** | **$6.482.773** (–9,2 % frente a enero) |
| Mayo 2022 (pico) | Valor máximo registrado del periodo; la caída a 2023 fue de **–12,8 % en Cundinamarca** |

### 5.3. Precios de insumos usados por Fedepapa (contraste histórico)

*(b) — Fedepapa, boletines 190 y 211, con datos SIPSA-DANE. Bulto de 50 kg.*

| Fecha | NPK 15-15-15 | Agrimins 8-5-0-6 |
|---|---|---|
| Junio 2022 (pico) | **$226.283** | — |
| Junio 2023 | $191.034 | — |
| Diciembre 2023 | $148.437 | — |
| Febrero 2024 | $140.613 | — |
| Febrero 2025 | **$139.837** (–24 %) | $126.755 (–14 %) |
| **Julio 2026 (Cund/Bog, DANE)** | **$178.059** | — |

### 5.4. Estimación del gasto regional en fertilizantes

**(c) — ESTIMACIÓN PROPIA.** Fórmula y supuestos explícitos:

```
Gasto = Área de papa en la Sabana (ha) × Costo de fertilización por ha ajustado a precios de jul-2026

Área de papa Sabana 2025 ................ 58.086,9 ha        [ (a) EVA/MADR ]
Costo fertilización/ha, junio 2023 ...... $6.482.773         [ (b) Fedepapa ]
Factor de ajuste de precios 2023→jul-2026:
   NPK 15-15-15 nacional prom. 2023 ..... $182.257           [ (a) DANE ]
   NPK 15-15-15 nacional jul-2026 ....... $178.236           [ (a) DANE ]
   Factor = 178.236 / 182.257 = 0,9779
Costo fertilización/ha, jul-2026 (est.) . $6.339.748
```

| Escenario de precios | Gasto anual en fertilizantes — papa, Sabana de Bogotá |
|---|---|
| Precios mínimos de 2024 | **$284.700 millones COP** (USD 91,8 M) |
| **Precios julio 2026 (base)** | **$368.256 millones COP** (USD 118,8 M) |
| Precios del pico de mayo 2022 | **$471.100 millones COP** (USD 152,0 M) |

*Conversión a USD con TRM de julio 2026 ($3.272,01). Cifra para **un ciclo de siembra**; si se asume 1,5 ciclos anuales en la Sabana, el escenario base asciende a ~$552.000 millones COP.*

> **Limitación declarada:** esta estimación aplica un costo de fertilización derivado del cultivo de papa a la totalidad del área de papa de la Sabana, sin diferenciar variedades ni niveles tecnológicos, y **no incluye** hortalizas, flores ni pastos. Es un **piso**, no un total regional.

---

## 6. IMPACTO HÍDRICO: RÍO BOGOTÁ, HUMEDALES, EUTROFIZACIÓN Y NITRATOS

### 6.1. Marco del problema

El nitrógeno y el fósforo aplicados como fertilizantes de síntesis y no absorbidos por el cultivo migran hacia los cuerpos de agua por tres vías: **lixiviación** (nitrato, muy soluble, hacia el acuífero), **escorrentía superficial** (arrastre de partículas fertilizantes y suelo) y **flujo subsuperficial**. Su llegada a ríos y humedales produce **eutrofización**: enriquecimiento de nutrientes que dispara el crecimiento de algas y macrófitas, consume el oxígeno disuelto y degrada el ecosistema.

La Secretaría Distrital de Ambiente lo define así: *"La eutrofización es causada por exceso de nutrientes en el agua, principalmente nitrógeno y fósforo, permitiendo el crecimiento excesivo de especies vegetales."* *(a)*

### 6.2. Estado del río Bogotá

| Indicador | Valor | Año | Fuente | Confianza |
|---|---|---|---|---|
| Contaminantes principales de la cuenca | Materia orgánica, materia en suspensión, **nitrógeno, fósforo**, metales pesados, contaminantes orgánicos traza | — | Literatura / CAR | (b) |
| Manifestaciones de contaminación | **Eutrofización** y sustancias altamente tóxicas | — | Literatura | (b) |
| Origen del río | Páramo de Guacheneque, Villapinzón, 3.300 m s. n. m. | — | CAR | (a) |
| Desembocadura | Río Magdalena, Girardot, 280 m s. n. m. | — | CAR | (a) |
| Aporte de carga contaminante concentrado en Bogotá | **84 %** de la carga | — | Literatura | (b) |
| Puntos de monitoreo, cuenca alta del río Bogotá | 40 puntos (río y afluentes), campaña I-2024 | 2024 | CAR | (b) |
| Red de Calidad Hídrica de Bogotá (SDA) | **66 puntos**; mide ICA como instrumento regional desde 2022 | 2022-2024 | SDA | (a) |
| Red Hidrológica Tradicional (RCHB-T) | 30 estaciones en ríos Torca, Fucha, Salitre y Tunjuelo | 2023-2024 | SDA | (a) |
| Categoría de calidad | *"En los últimos periodos ningún río presentó una categoría de calidad de agua Pobre (WQI<45), situación que no había ocurrido históricamente"* | 2023-2024 | SDA, Observatorio Ambiental de Bogotá | (a) |
| Mejor calidad entre ríos urbanos | Río Torca | 2023-2024 | SDA | (a) |

**Parámetros medidos en la cuenca media del río Bogotá, 2007–2019** *(b) — Escalante Castro & Fajardo Pineda, Universidad Libre, revista INVENTUM 17(33), 2022*:

| Parámetro | Comportamiento documentado |
|---|---|
| DBO₅ | En ascenso desde 2014; valores máximos en 2019 |
| Oxígeno disuelto | Llegó a **0 mg/L en 2014**; mejoró a 0,8 mg/L en 2019 tras el fallo judicial |
| Sólidos suspendidos totales | 500–1.000 mg/L (2007-2017); pico de **1.300 mg/L en 2012**; deterioro en 2018-2019 |
| Coliformes totales | Máximos entre 2007-2011; descenso hasta 2015; nuevo ascenso posterior |

Fuentes de contaminación identificadas por ese estudio: vertimientos industriales (curtiembres, alimentos, textiles), aguas residuales domésticas (que aportan el 84 % de la contaminación que entra a Bogotá), **escorrentía agrícola y sedimentos**, y conexiones erradas de alcantarillado.

> **Carga de nutrientes (nitrógeno total y fósforo total) del río Bogotá en toneladas/año, desagregada por tramo y por origen agrícola: NO ENCONTRADO.** La CAR Cundinamarca publica inventarios de vertimientos que incluyen nitrógeno orgánico, N-amoniacal, N-nitratos, N-nitritos, fósforo orgánico y fósforo inorgánico para el horizonte 2025–2029, pero **su servidor bloqueó sistemáticamente el acceso automatizado** durante esta investigación (10 de septiembre de 2026), tanto por WebFetch como por descarga directa. **Recomendación:** solicitar el dato mediante derecho de petición a la CAR o consultar presencialmente el POMCA del río Bogotá y el "Estado del recurso hídrico en la cuenca del río Bogotá en jurisdicción CAR".

### 6.3. Humedales de la Sabana

| Indicador | Valor | Año | Fuente | Confianza |
|---|---|---|---|---|
| Humedales en proceso de restauración/gestión | La Isla, Capellanía, Juan Amarillo, Salitre, El Burro | 2024-2025 | SDA / Alcaldía de Bogotá | (a) |
| Restauración y mantenimiento ejecutados | Humedal La Conejera y Humedal Torca-Guaymaral | 2024 | SDA | (a) |
| Proyecto en estructuración | Fondo Verde para el Clima | 2025 | SDA | (a) |

> **Mediciones de concentración de nitrógeno y fósforo y grado de eutrofización de los humedales de la Sabana: NO ENCONTRADO** en fuente oficial pública con cifras. Los Planes de Manejo Ambiental de cada humedal contendrían el dato; requieren consulta directa a la SDA.

### 6.4. Aguas subterráneas

El acuífero de la Sabana de Bogotá es especialmente vulnerable por dos razones: es un acuífero **somero** y está **sobreexplotado**, en buena medida por el sector florícola.

| Indicador | Valor | Año | Fuente | Confianza |
|---|---|---|---|---|
| Explotación intensiva del agua subterránea | Se intensificó desde los años 80 | — | Literatura (Geología Colombiana, UNAL) | (b) |
| Agotamiento del acuífero cuaternario (somero) | Documentado, **por sobreexplotación, particularmente del sector florícola** | — | Literatura | (b) |
| Contaminantes con movilidad identificada hacia el acuífero | Ingredientes activos de plaguicidas (Epingle®, Roxion®, Furadan®) hacia los sectores noroeste y norte según las líneas de flujo subterráneo | — | Estudio hidrogeológico | (b) |
| Calidad del agua en pozos concesionados | Evaluación 2016 – 30 jun 2023: flujo local en el acuífero Formación Sabana; medidas de manejo requeridas en pozos con coliformes fecales y grasas/aceites | 2023 | Acuíferos en Bogotá y su estado ambiental (OAB) | (b) |

> **Concentraciones de nitratos en el agua subterránea de la Sabana de Bogotá: NO ENCONTRADO.** Los estudios hidrogeológicos localizados documentan la movilidad de plaguicidas y la contaminación microbiológica, pero **no reportan series de nitratos**. Este es un vacío de información relevante y debe declararse como tal.

### 6.5. Norma sanitaria aplicable

| Parámetro | Valor máximo | Fuente | Confianza |
|---|---|---|---|
| Nitrato (NO₃⁻) en agua potable | **10 mg/L** | US EPA, National Primary Drinking Water Regulations | (a) |
| Nitrito (NO₂⁻) en agua potable | **1 mg/L** | US EPA | (a) |
| Fuentes de contaminación reconocidas | **Escorrentía por uso de fertilizantes**, fugas de tanques sépticos y alcantarillado, erosión de depósitos naturales | US EPA | (a) |

*La norma colombiana equivalente es la **Resolución 2115 de 2007** (MinSalud/MinAmbiente), que fija los valores máximos aceptables de características químicas del agua para consumo humano. **El valor exacto de nitratos de esa resolución no pudo verificarse directamente** durante esta investigación por límite de tamaño del documento; debe confirmarse antes de citarlo.*

---

## 7. DEGRADACIÓN DE SUELOS

### 7.1. Cifras nacionales

*(a) — IDEAM, MADS, U.D.C.A, SINA: Estudio Nacional de la Degradación de Suelos por Erosión en Colombia (2015), escala 1:100.000. Difundido por MinAmbiente (2016) y Agrosavia. Se cita este estudio por ser la línea base oficial vigente; no se encontró una actualización posterior.*

| Indicador | Valor |
|---|---|
| Superficie continental e insular afectada por erosión | **40 %** |
| — Erosión ligera | 20 % |
| — Erosión moderada | 17 % |
| — Erosión severa | 3 % |
| — Erosión muy severa | 0,2 % |
| Tierras susceptibles de degradación por aridez | 24 % |
| País con salinización de suelos | **5 %** |
| Región Caribe con procesos de salinización y sodificación | 53.237 km² |
| Áreas deforestadas 1990-2010 con algún grado de erosión | >60 % (≈4 millones de ha) |
| **Áreas de uso exclusivamente agrícola** | **2.078.094 ha, de las cuales el 93 % presenta erosión** por manejo inadecuado en las labores agrícolas |

### 7.2. Cundinamarca

| Indicador | Valor | Fuente | Confianza |
|---|---|---|---|
| **Suelos de Cundinamarca afectados por algún grado de erosión** | **80,3 %** | IDEAM/Agrosavia | (a) |
| **Suelos de Cundinamarca con erosión severa** | **5 %** | IDEAM/Agrosavia | (a) |
| Comparación: Boyacá | 72,1 % con erosión; 6,8 % severa | IDEAM/Agrosavia | (a) |
| Comparación: promedio nacional | 40 % | IDEAM/Agrosavia | (a) |

> **Cundinamarca duplica el promedio nacional de erosión.** El 80,3 % de sus suelos está afectado frente al 40 % nacional. La causa identificada por el estudio es el **manejo inadecuado en las labores agrícolas**, no el fertilizante químico *per se*; sin embargo, el paquete tecnológico de alta intensidad —laboreo mecánico intensivo, monocultivo de papa, fertilización mineral y baja reposición de materia orgánica— es el patrón dominante en la Sabana.

### 7.3. Mecanismos de degradación asociados a la fertilización mineral

Los mecanismos que la literatura agronómica asocia a la fertilización de síntesis sostenida son:

- **Acidificación:** la nitrificación del amonio (urea, sulfato de amonio, DAP) libera protones y acidifica el suelo, obligando a encalar. La presencia de cal dolomita y cal agrícola como productos de alta rotación en el mercado de la Sabana es evidencia indirecta de este fenómeno: **30 municipios reportaron precio de cal dolomita** y 14 de cal agrícola en el relevamiento DANE de julio de 2026, incluidos 8 municipios de Cundinamarca. *(a) DANE SIPSA-I + (c) interpretación propia.*
- **Pérdida de materia orgánica:** la fertilización mineral no repone carbono orgánico; en sistemas de laboreo intensivo el balance de materia orgánica es negativo.
- **Salinización:** el 5 % del país presenta salinización *(a)*. Cifra específica para la Sabana de Bogotá: **NO ENCONTRADO**.
- **Compactación:** asociada al laboreo mecánico. Cifra específica para la Sabana: **NO ENCONTRADO**.

**Soluciones planteadas por AGROSAVIA** (Centro de Investigación Tibaitatá, ubicado en Mosquera, Sabana de Bogotá) *(b)*: bacterias promotoras del crecimiento vegetal, sistemas de labranza apropiados, abonos verdes y cultivos asociados (gramíneas-leguminosas), **compost a partir de residuos agrícolas** y manejo adecuado del agua.

---

## 8. EMISIONES DE GASES DE EFECTO INVERNADERO (N₂O)

*(a) — Inventario Nacional de Emisiones y Absorciones Atmosféricas de Colombia, MinAmbiente / IDEAM, publicado en 2025 con datos del año 2021.*

### 8.1. Cifras nacionales

| Indicador | Valor |
|---|---|
| Emisiones **netas** de Colombia, 2021 | **280.101,98 kt CO₂eq** |
| Emisiones **totales (brutas)**, 2021 | **302.934,03 kt CO₂eq** |
| Absorciones | 22.832,04 kt CO₂eq |
| Participación del sector **agricultura** en emisiones netas | **20,69 %** |
| Participación de LULUCF | 34,49 % |
| Participación de energía | 32,71 % |
| Participación de residuos | 7,93 % |
| Participación de IPPU | 4,18 % |

### 8.2. Desglose del módulo agricultura (2021)

| Categoría | kt CO₂eq | Participación en el sector |
|---|---|---|
| **Total sector agricultura** | **57.957,85** | 100 % |
| 3.A. Fermentación entérica | 44.504,73 | 76,79 % |
| **3.D. Emisiones directas e indirectas de N₂O de suelos agrícolas** | **≈9.627** | **16,61 %** |
| 3.B. Gestión del estiércol | — | 5,24 % |
| 3.C. Cultivo de arroz | — | 0,90 % |
| **3.H. Aplicación de urea** | — | **0,38 %** |
| 3.G. Encalado | — | 0,09 % |

**Participación por gas dentro del módulo agricultura:**

| Gas | kt CO₂eq | Participación |
|---|---|---|
| CH₄ (fermentación entérica y estiércol) | 46.963,33 | 81,03 % |
| **N₂O (nitrógeno incorporado a suelos agrícolas)** | **10.722,78** | **18,50 %** |
| CO₂ (aplicación de cal dolomita y urea) | 271,73 | 0,47 % |

**Peso del N₂O agrícola sobre el total nacional** *(a)*:

- Emisiones directas de N₂O de suelos gestionados: **2,06 %** de las emisiones totales del país
- Emisiones indirectas de N₂O de suelos gestionados: **1,12 %** de las emisiones totales del país
- **Total: 3,18 % de las emisiones brutas nacionales** — equivalente a ≈9.633 kt CO₂eq *(c) cálculo propio.*

### 8.3. Nitrógeno aplicado a los suelos colombianos

| Fuente de nitrógeno | Toneladas de N, 2021 | Fuente | Confianza |
|---|---|---|---|
| **Fertilizantes inorgánicos** | **370.357 t N** | MinAmbiente/IDEAM, con datos de MinAgricultura y consulta nacional de expertos | (a) |
| Orina y estiércol de animales en pasturas | 1.063.119 t N | MinAmbiente/IDEAM, con datos del inventario animal ICA 2021 | (a) |

El inventario es explícito sobre la causa del aumento de emisiones: *"el aumento de las emisiones por la gestión de los suelos se atribuye a la cantidad de nitrógeno aplicado al suelo por las diferentes fuentes, **principalmente los fertilizantes nitrogenados inorgánicos** y la deposición de orina y estiércol de los animales en pasturas."*

### 8.4. Potencial de calentamiento global del N₂O

El inventario nacional define el potencial de calentamiento global como *"una medida que establece la capacidad que tiene un gas de efecto invernadero para absorber energía o calentar la atmósfera en comparación con el CO₂ durante un periodo específico (IPCC, 2013)"*, pero **no explicita el valor numérico del PCG del N₂O en la sección consultada**.

El valor de referencia de **265 a 273 veces el CO₂ en horizonte de 100 años** corresponde a los informes AR5 (265) y AR6 (273) del IPCC. **(b) — no verificado en fuente primaria del IPCC durante esta investigación; debe confirmarse antes de citarlo como dato duro.**

---

## 9. IMPACTOS EN SALUD

### 9.1. Nitratos en agua de consumo y metahemoglobinemia

*(a) — US EPA, National Primary Drinking Water Regulations.*

| Aspecto | Contenido |
|---|---|
| **Límite máximo de nitrato (MCL)** | **10 mg/L** |
| **Límite máximo de nitrito (MCL)** | **1 mg/L** |
| **Población de riesgo** | Lactantes menores de seis meses |
| **Efecto documentado** | *"Los lactantes menores de seis meses que beban agua con nitrato por encima del MCL pueden enfermar gravemente y, si no reciben tratamiento, pueden morir. Los síntomas incluyen dificultad respiratoria y síndrome del bebé azul."* |
| **Nombre clínico** | Metahemoglobinemia (*blue-baby syndrome*) |
| **Fuentes de contaminación reconocidas** | **Escorrentía por uso de fertilizantes**; fugas de tanques sépticos y alcantarillado; erosión de depósitos naturales |

El mecanismo fisiopatológico es la conversión de nitrato a nitrito en el tracto digestivo del lactante y la posterior oxidación del hierro de la hemoglobina, que pierde su capacidad de transportar oxígeno.

### 9.2. Exposición de trabajadores agrícolas

**NO ENCONTRADO.** No se localizaron estudios epidemiológicos publicados sobre exposición ocupacional específicamente a **fertilizantes de síntesis** (a diferencia de plaguicidas, que sí están ampliamente documentados) en trabajadores agrícolas o florícolas de la Sabana de Bogotá. La literatura consultada sobre el sector florícola de la Sabana se concentra en plaguicidas y en condiciones laborales generales.

**Recomendación:** no atribuir al fertilizante químico efectos de salud ocupacional sin evidencia. El riesgo ocupacional documentado en la floricultura de la Sabana corresponde principalmente a **plaguicidas**, que son una categoría distinta de insumo.

### 9.3. Casos de metahemoglobinemia en Colombia asociados a nitratos

**NO ENCONTRADO.** No se localizó registro epidemiológico público del INS o MinSalud que cuantifique casos de metahemoglobinemia por nitratos en agua en Colombia o en Cundinamarca.

---

## 10. INEFICIENCIA AGRONÓMICA: CUÁNTO NITRÓGENO SE PIERDE

### 10.1. Eficiencia de uso del nitrógeno

| Afirmación | Valor | Fuente | Confianza |
|---|---|---|---|
| Eficiencia de aprovechamiento del N aplicado | **Generalmente inferior al 50 %** | Literatura agronómica (SciELO México, CIMMYT) | (b) |
| En maíz | 35 % – 75 % según condiciones | SciELO México | (b) |
| Estimación frecuente en la literatura | Solo ≈ **40 %** del N aplicado es utilizado por el cultivo | Literatura agronómica | (b) |

### 10.2. Vías de pérdida

La literatura identifica las siguientes rutas para el nitrógeno no absorbido:

1. **Lixiviación**, principalmente como **nitrato (NO₃⁻)** — muy soluble, migra al agua subterránea
2. **Volatilización**, como **amoníaco (NH₃)**
3. **Emisión gaseosa** como **óxido nitroso (N₂O)**, **óxido nítrico (NO)** y **dióxido de nitrógeno (NO₂)**
4. **Inmovilización** por microorganismos del suelo
5. **Erosión y escorrentía**

*(b) — literatura agronómica (Agroes, Intagri, SciELO).*

> **Implicación económica directa:** si menos del 50 % del nitrógeno aplicado llega a la planta, entonces **más de la mitad del gasto en fertilizante nitrogenado no genera producto**. Aplicado al gasto estimado de fertilización de la papa en la Sabana (§5.4), **más de $184.000 millones COP al año (≈USD 56 millones) corresponderían a nutriente perdido** — y ese nutriente perdido es exactamente el que termina en el río Bogotá, en el acuífero y en la atmósfera. *(c) — estimación propia, ilustrativa; el porcentaje de pérdida aplica estrictamente al nitrógeno, no a la totalidad del gasto en fertilizantes.*

### 10.3. Costo por kilogramo de nutriente — julio 2026

*(a) precios DANE SIPSA-I nacional jul-2026 + (c) cálculo propio. Se asume la concentración nominal declarada en la fórmula comercial.*

| Producto | Precio bulto 50 kg | Nutriente por bulto | **Costo por kg de nutriente** |
|---|---|---|---|
| Urea 46 % | $188.053 | 23,00 kg N | **$8.176 / kg N** |
| Sulfato de amonio 21-0-0-24(S) | $94.224 | 10,50 kg N | **$8.974 / kg N** |
| DAP 18-46-0 (fracción P₂O₅) | $238.805 | 23,00 kg P₂O₅ | **$10.383 / kg P₂O₅** |
| DAP 18-46-0 (fracción N) | $238.805 | 9,00 kg N | $26.534 / kg N |
| Cloruro de potasio 0-0-60 | $130.323 | 30,00 kg K₂O | **$4.344 / kg K₂O** |
| NPK 15-15-15 (suma NPK = 45 %) | $178.236 | 22,50 kg NPK | **$7.922 / kg NPK** |
| Abono orgánico (supuesto 1,5 % N) | $23.616 | 0,75 kg N | **$31.488 / kg N** |

> **Ajustado por eficiencia:** si solo el 40 %–50 % del N se aprovecha, el **costo efectivo del nitrógeno útil de la urea sube a $16.352–$20.440 por kg de N absorbido**. *(c) — cálculo propio.*

---

## 11. EL MERCADO DE FERTILIZANTES ORGÁNICOS COMO ALTERNATIVA

### 11.1. Precios oficiales de productos orgánicos y enmiendas — DANE SIPSA-I, julio 2026

*(a) — DANE SIPSA-I, anexo municipal julio 2026. Promedios propios.*

| Producto | Presentación | Municipios que reportan | Promedio nacional | Mín. | Máx. | Cundinamarca / Bogotá |
|---|---|---|---|---|---|---|
| **Abono Orgánico** | 50 kg | 9 | **$23.616** | $20.333 | $28.950 | Villapinzón **$20.333** |
| Fertilizante Orgánico de Lombriz San Rafael | 1 litro | 2 | $18.417 | $17.500 | $19.333 | Bogotá D.C. $19.333 |
| Geoplant Humus | 1 litro | 1 | $18.000 | — | — | Facatativá $18.000 |
| Humus 15 | 1 litro | 6 | $26.817 | $25.850 | $27.617 | Choachí $26.000; Fómeque $27.500 |
| Humus 15 | 4 litros | 1 | $101.500 | — | — | Fómeque $101.500 |
| Humus 500 | 1 litro | 1 | $42.700 | — | — | Subachoque $42.700 |
| **Sáfer Micorrizas MA** (bioinsumo) | 50 kg | 3 | **$93.925** | $89.800 | $99.000 | Bogotá D.C. $92.975; El Rosal $89.800 |
| Sáfer Micorrizas MA | 10 kg | 1 | $29.100 | — | — | Bogotá D.C. $29.100 |
| **Cal Dolomita** (enmienda) | 50 kg | 30 | **$18.733** | $14.000 | $22.000 | 8 municipios; promedio Cund. $16.112 |
| **Cal Agrícola** (enmienda) | 50 kg | 14 | **$19.129** | — | — | Pasca $26.000 |

> **Precios de compost a granel, humus de lombriz por bulto y gallinaza compostada por bulto en la Sabana de Bogotá: NO ENCONTRADOS en fuente oficial.** Los precios hallados en avisos comerciales en línea (humus de lombriz 50 kg ≈ $45.000; tonelada de compost en 20 bultos de 50 kg ≈ $340.000; gallinaza compostada 50 kg ≈ $10.000 en planta, Garagoa-Boyacá) son **(b) precios de anuncio no verificados**, no series oficiales, y **no deben usarse en un modelo financiero sin cotización directa**. La única referencia oficial y auditable disponible es la del DANE: **"Abono Orgánico", bulto de 50 kg, $20.333 en Villapinzón (Cundinamarca) y $23.616 promedio nacional, julio de 2026.**

### 11.2. Evolución del precio del abono orgánico (2021–2026)

*(a) — DANE SIPSA-I, promedio anual nacional, bulto de 50 kg.*

| Año | Precio | Variación anual | n (observaciones) |
|---|---|---|---|
| 2021 | $14.945 | — | 148 |
| 2022 | $17.509 | +17,2 % | 131 |
| 2023 | $20.176 | +15,2 % | 101 |
| 2024 | $21.947 | +8,8 % | 102 |
| 2025 | $23.098 | +5,2 % | 108 |
| **2026 (ene-jul)** | **$23.655** | **+2,4 %** | 59 |
| **Variación 2021→2026** | | **+58,3 %** | |

### 11.3. Comparación estructural: sintético vs. orgánico

| Dimensión | Fertilizante de síntesis (urea) | Abono orgánico | Fuente |
|---|---|---|---|
| Precio por bulto de 50 kg (jul-2026) | $188.053 | **$23.616** (8,0x más barato) | (a) DANE |
| Costo por kg de N | **$8.176** | $31.488 (3,9x más caro) | (a)+(c) |
| Volatilidad (CV, 67 meses) | 30,9 % | **15,8 %** | (a)+(c) |
| Rango máx/mín (67 meses) | 3,32x | **1,64x** | (a)+(c) |
| Variación acumulada 2021→2026 | +39,7 % (con pico intermedio de +231,6 %) | **+58,3 % monotónica y suave** | (a)+(c) |
| Dependencia de importaciones | ~90 % | Producción local | (b) |
| Aporte de materia orgánica al suelo | Nulo | Sí | (b) |

> **Conclusión honesta del análisis comparativo:** el abono orgánico **no es competitivo por unidad de nitrógeno** a precios de mercado actuales —cuesta casi cuatro veces más por kilogramo de N—. Su ventaja es **triple y distinta**: (i) un precio **la mitad de volátil**, que reduce el riesgo del flujo de caja; (ii) **aporte de materia orgánica**, que ataca directamente la causa de la degradación del 80,3 % de los suelos de Cundinamarca; y (iii) **independencia de la cadena de importación** y de disrupciones geopolíticas como la del Estrecho de Ormuz. Cualquier modelo financiero que compare ambos debe hacerlo **por unidad de nutriente y con una prima de riesgo por volatilidad**, no por precio de bulto.

### 11.4. Tamaño del mercado y actores

| Indicador | Valor | Año | Fuente | Confianza |
|---|---|---|---|---|
| Cobertura de los abonos orgánicos sobre las necesidades nacionales | **<25 %** | — | Bolsa Mercantil de Colombia | (b) |
| Participación de fertilizantes orgánicos + fosfatados en el volumen importado | ~1 % del total | 2023 | Fedepapa/Legiscomex | (b) |
| Participación de "fertilizantes total (incluye orgánicos y fosfatados)" en compras por volumen | 0,43 % | 2023 | Fedepapa/Legiscomex | (b) |
| Capacidad de producción, Molienda de la Sabana | 1.000 t/día de acondicionadores de suelo | 2025 | Agronegocios | (b) |
| Proyecto Opex y Hevolución | 45.000 t/año de nitrato de amonio; hasta 70.000 t/año de fertilizantes verdes; inicio previsto **2029** | 2025 | Agronegocios | (b) |
| Actores en amoníaco verde | Celsia (a partir de hidroelectricidad) | 2025 | Agronegocios | (b) |
| Actores en I+D de biofertilizantes | Universidad Nacional, Universidad de Antioquia, **AGROSAVIA** | 2025 | Agronegocios | (b) |
| Exploración mineral | Agencia Nacional de Minería (ANM) | 2025 | Agronegocios | (b) |

> **Tamaño del mercado de fertilizantes orgánicos en Colombia expresado en toneladas o en valor (COP/USD): NO ENCONTRADO** en fuente oficial. El único indicador cuantitativo localizado es el de cobertura (<25 % de las necesidades nacionales, Bolsa Mercantil).

### 11.5. Requisitos normativos ICA para producir y vender un fertilizante orgánico

**Resolución ICA 00150 de 2003** — *"Por la cual se adopta el Reglamento Técnico de Fertilizantes y Acondicionadores de Suelos para Colombia"*:

- **Ámbito:** aplica en todo el territorio nacional a toda persona natural o jurídica que **fabrique, formule, envase, empaque o importe** fertilizantes y acondicionadores de suelos y sus materias primas.
- **Registro obligatorio:** *"Toda persona natural o jurídica que desee fabricar, formular, envasar o empacar fertilizantes y acondicionadores de suelos, deberá registrarse ante el Instituto Colombiano Agropecuario ICA, mediante el diligenciamiento y presentación de la Forma ICA 3-894."*
- **Doble registro:** se requiere registro **de productor** (o importador) y registro **de producto**.
- **Definiciones que incorpora:** fertilizante, **fertilizante orgánico** (material derivado de residuos biológicos que mejora la nutrición y las propiedades del suelo) y **acondicionador de suelo**.
- **Cumplimiento de normas técnicas:** exige el cumplimiento de las normas NTC, en particular la **NTC 5167** — *Productos para la industria agrícola. Productos orgánicos usados como abonos o fertilizantes y enmiendas o acondicionadores de suelo* —, que fija las especificaciones técnicas (contenido de materia orgánica, humedad, pH, capacidad de intercambio catiónico, relación C/N, metales pesados, ausencia de patógenos).
- **Etiquetado:** información clara sobre contenido nutricional, instrucciones de uso e identificación del fabricante o importador.
- **Sanciones:** multas y restricciones comerciales por incumplimiento de registro, etiquetado o especificaciones técnicas.

*(a) — Resolución ICA 150 de 2003, texto consultado.*

> **Implicación operativa para cualquier emprendimiento de fertilizante orgánico en la Sabana:** no basta con producir compost. Se requiere (i) registro de productor ante el ICA, (ii) registro del producto, (iii) análisis de laboratorio que acrediten el cumplimiento de la NTC 5167, y (iv) etiquetado conforme. **Es una barrera de entrada regulatoria real y debe presupuestarse.** El costo y los tiempos del trámite **NO FUERON ENCONTRADOS** y deben consultarse directamente en el tarifario vigente del ICA.

### 11.6. Política pública de bioinsumos

Existe un marco de política explícito, en construcción:

- **Documento "Lineamientos de política pública de bioinsumos, fertilizantes orgánicos y acondicionadores de suelos: una apuesta para el logro de las agriculturas para la vida"** — Ministerio de Agricultura y Desarrollo Rural. *"Define y establece la promoción de la producción y el uso eficiente de bioinsumos en el marco de la política de insumos agropecuarios y del programa de agroecología."* *(a)*
- **Plan Estratégico Institucional del ICA 2023–2026 "ICA más cerca del campo"** — articula la política de bioinsumos. *(a)*
- **CONPES 4129 de 2023** (Política Nacional de Reindustrialización) — línea 5.2 asigna al ICA la tarea de *"facilitar la eficiencia y calidad normativa para la actividad productiva"* y el compromiso de actualizar documentos normativos y medidas sanitarias y fitosanitarias orientados a mejorar los procesos de registro, inspección, vigilancia y control de insumos agropecuarios. *(a)*
- **Plan Nacional de Desarrollo 2022–2026 "Colombia Potencia Mundial de la Vida"** — establece como prioridad *"la producción nacional de insumos y transición de insumo de origen químico al biológico"*, en el marco del Sistema Nacional de Reforma Agraria reactivado. *(a)*
- **Proyecto de resolución ICA sobre biopreparados** — *"Por la cual se establecen los requisitos para el registro de producto, productor y comercializador de biopreparados para uso agrícola elaborados en biofábricas familiares y comunitarias"*. Crea una figura simplificada de registro para **biofábricas familiares y comunitarias**, incluyendo registro voluntario de productor de biopreparados para autoconsumo. *(a) — documento en consulta pública, portal SUCOP.*

> **"Ley de bioinsumos": NO ENCONTRADA.** No se localizó una ley de la República específica sobre bioinsumos. El marco vigente es de **rango reglamentario** (resoluciones del ICA) y de **política pública** (CONPES, PND, lineamientos MADR). No debe citarse una "ley de bioinsumos" sin verificación.

---

## 12. MARCO NORMATIVO Y POLÍTICA PÚBLICA

| Norma / política | Año | Contenido | Implicación |
|---|---|---|---|
| **Resolución ICA 00150** | 2003 | Reglamento Técnico de Fertilizantes y Acondicionadores de Suelos. Registro obligatorio de productor y de producto (Forma ICA 3-894); etiquetado; cumplimiento de NTC; sanciones. | Norma marco vigente. **Barrera de entrada regulatoria** para cualquier producto fertilizante, sintético u orgánico. |
| **NTC 5167** | Vigente | Especificaciones técnicas de productos orgánicos usados como abonos, fertilizantes, enmiendas y acondicionadores de suelo. | Define los parámetros de laboratorio que un compost debe cumplir para ser comercializable. |
| **Resolución 2115** (MinSalud/MinAmbiente) | 2007 | Características, instrumentos básicos y frecuencias del sistema de control y vigilancia de la calidad del agua para consumo humano. Fija valores máximos aceptables de parámetros químicos, incluidos nitratos y nitritos. | Norma sanitaria que determina cuándo el nitrato en agua se vuelve un problema legal. *Valor exacto pendiente de verificación directa.* |
| **Decreto 1071** (art. 2.13.1.6.1) | 2015 | Decreto Único Reglamentario del Sector Agropecuario; base de competencia del ICA en insumos. | Sustento legal del control técnico del ICA. |
| **Decretos 4765 de 2008 y 3761 de 2009** | 2008-2009 | Estructura y funciones del ICA; facultad de conceder, suspender o cancelar registros y licencias de insumos agropecuarios. | Sustento legal de la función de registro. |
| **CONPES 4129** | 2023 | Política Nacional de Reindustrialización. Línea 5.2: mejora regulatoria del ICA en registro, inspección, vigilancia y control de insumos agropecuarios. | Mandato de simplificación de trámites para insumos, incluidos bioinsumos. |
| **PND 2022–2026 "Colombia Potencia Mundial de la Vida"** | 2023 | Política de reindustrialización; soberanía alimentaria y agroindustrial; **"transición de insumo de origen químico al biológico"** como prioridad. | Marco político que respalda alternativas al fertilizante de síntesis. |
| **Lineamientos de política pública de bioinsumos, fertilizantes orgánicos y acondicionadores de suelos (MADR)** | 2023-2026 | Promoción de la producción y uso eficiente de bioinsumos en el marco del programa de agroecología. | Documento de política sectorial de referencia. |
| **Plan Estratégico Institucional ICA 2023–2026 "ICA más cerca del campo"** | 2023 | Articula la política de bioinsumos en la gestión del ICA. | — |
| **Proyecto de Resolución ICA sobre biopreparados en biofábricas familiares y comunitarias** | En trámite (consulta pública) | Requisitos simplificados de registro de producto, productor y comercializador de biopreparados agrícolas; registro voluntario para autoconsumo. | **Reduciría la barrera de entrada** para iniciativas comunitarias de bioinsumos. |
| **Acuerdo Ecopetrol – Monómeros (propuesta)** | may-2026 | Memorando de entendimiento con Venezuela; venta directa de azufre de Ecopetrol a Monómeros para reducir ~35 % los costos de intermediación; inversión de **$1 billón COP (USD 274 millones)** de anticipos de dividendos para **subsidiar fertilizantes durante 2026**. | **Estado: anunciado, no ejecutado.** |
| **Compra estatal de Monómeros** | 2025-2026 | El ministro Edwin Palma afirmó en enero de 2026 que avanzaba la posible compra nacional de la empresa. | **Estado: no materializada** (Portafolio, abril 2026). |
| **Estudio de factibilidad planta de fertilizantes en Huila** | 2025-2026 | MADR y Gobernación del Huila avanzan estudio para producción nacional a partir de roca fosfórica. | **Estado: estudio de factibilidad.** Sin inversión ejecutada. |

> **Balance de política pública 2022–2026:** existe una **arquitectura política robusta** (PND, CONPES, lineamientos MADR, plan estratégico ICA) que apunta explícitamente a la transición del insumo químico al biológico y a la soberanía de fertilizantes. Pero, como concluye Portafolio el 5 de abril de 2026, la idea de la producción nacional **"se quedó en el papel"**: no se compró Monómeros, no se desarrolló la minería de fosfatos y no hubo inversiones concretas ejecutadas. La única política con recursos asignados es un **subsidio coyuntural** ($1 billón COP), no una solución estructural.

---

## 13. TABLA MAESTRA DE CIFRAS

| # | Indicador | Valor | Unidad | Año | Fuente | URL | Confianza |
|---|---|---|---|---|---|---|---|
| 1 | Consumo aparente de fertilizantes, Colombia | 2,4 – 2,5 | millones t/año | 2026 | La República | https://www.larepublica.co/economia/precio-de-los-fertilizantes-entre-abril-de-2025-y-abril-de-2026-4364877 | (b) |
| 2 | Importaciones de fertilizantes | 2,3 | millones t | 2025 | DANE vía La República | https://www.larepublica.co/economia/precio-de-los-fertilizantes-entre-abril-de-2025-y-abril-de-2026-4364877 | (b) |
| 3 | Importaciones ene–oct | 1,94 | millones t (+10 % a/a) | 2025 | DANE vía Portafolio | https://www.portafolio.co/economia/agro/colombia-importo-1-94-millones-de-toneladas-de-fertilizantes-y-diversifico-proveedores-en-488304 | (b) |
| 4 | Importaciones año completo | 2,13 | millones t | 2024 | DANE vía Portafolio | https://www.portafolio.co/economia/agro/colombia-importo-1-94-millones-de-toneladas-de-fertilizantes-y-diversifico-proveedores-en-488304 | (b) |
| 5 | Dependencia de importaciones | ~90 | % de la demanda | 2026 | La República | https://www.larepublica.co/economia/precio-de-los-fertilizantes-entre-abril-de-2025-y-abril-de-2026-4364877 | (b) |
| 6 | Materias primas importadas | >90 | % | 2025 | Agronegocios | https://www.agronegocios.co/comentarios/cesar-palacio-3680916/fertilizantes-nacionales-en-colombia-hemos-avanzado-en-2024-2025-4265492 | (b) |
| 7 | Cobertura de la producción nacional | 5 – 10 | % de la demanda | 2025 | Agronegocios | (misma que #6) | (b) |
| 8 | Factura de importación CIF | 1.469 | millones USD | 2023 | Fedepapa/Legiscomex, Boletín 190 | https://fedepapa.com/home/wp-content/uploads/2024/10/Boletin-190.pdf | (b) |
| 9 | Participación de China en importaciones | 18,3 | % | 2025 | Portafolio/La República | (ver #3) | (b) |
| 10 | Importación de urea (12 meses a abr-2026) | 665.780 t / USD 295 M | t y USD | 2026 | La República | https://www.larepublica.co/economia/precio-de-los-fertilizantes-en-abril-de-2026-versus-abril-de-2025-4374825 | (b) |
| 11 | Importación de KCl (12 meses a abr-2026) | 622.550 t / USD 217 M | t y USD | 2026 | La República | (misma que #10) | (b) |
| 12 | Inventarios nacionales de fertilizante | 2 – 3 | meses de consumo | abr-2026 | La República | (misma que #10) | (b) |
| 13 | **Urea 46 %, Cundinamarca/Bogotá** | **186.235** | COP/bulto 50 kg | jul-2026 | DANE SIPSA-I (microdato) | https://www.dane.gov.co/files/operaciones/SIPSA/anex-SIPSAinsumosmunicipio-jul2026.xlsx | **(a)** |
| 14 | **DAP 18-46-0, Cundinamarca/Bogotá** | **233.669** | COP/bulto 50 kg | jul-2026 | DANE SIPSA-I | (misma que #13) | **(a)** |
| 15 | **KCl 0-0-60, Cundinamarca/Bogotá** | **127.821** | COP/bulto 50 kg | jul-2026 | DANE SIPSA-I | (misma que #13) | **(a)** |
| 16 | **NPK 15-15-15, Cundinamarca/Bogotá** | **178.059** | COP/bulto 50 kg | jul-2026 | DANE SIPSA-I | (misma que #13) | **(a)** |
| 17 | **Sulfato de amonio, Cundinamarca/Bogotá** | **90.500** | COP/bulto 50 kg | jul-2026 | DANE SIPSA-I | (misma que #13) | **(a)** |
| 18 | Urea 46 %, promedio nacional | 188.053 | COP/bulto 50 kg | jul-2026 | DANE SIPSA-I | (misma que #13) | (a) |
| 19 | Urea 46 %, precio más alto del país | 222.400 (Santa Marta) | COP/bulto 50 kg | jul-2026 | DANE, Boletín técnico 169 | https://www.dane.gov.co/files/operaciones/SIPSA/bol-SIPSAinsumos-jul2026.pdf | (a) |
| 20 | Urea 46 %, precio más bajo del país | 155.767 (Garzón, Huila) | COP/bulto 50 kg | jul-2026 | DANE, Boletín técnico 169 | (misma que #19) | (a) |
| 21 | Urea 46 %, precio pico histórico nacional | 260.562 | COP/bulto 50 kg | may-2022 | DANE SIPSA-I | https://www.dane.gov.co/files/operaciones/SIPSA/anex-SIPSAInsumos-SeriesHistoricasMun-2021-2026.xlsx | (a) |
| 22 | Urea 46 %, mínimo histórico de la serie | 78.567 | COP/bulto 50 kg | ene-2021 | DANE SIPSA-I | (misma que #21) | (a) |
| 23 | **Alza de la urea ene-2021 → may-2022** | **+231,6** | % | 2021-22 | Cálculo sobre DANE SIPSA-I | (misma que #21) | (c) |
| 24 | **Alza de la urea jul-2025 → jul-2026 (Cund/Bog)** | **+36,2** | % | 2026 | Cálculo sobre DANE SIPSA-I | (misma que #21) | (c) |
| 25 | Volatilidad de la urea (CV mensual, 67 meses) | 30,9 | % | 2021-26 | Cálculo sobre DANE SIPSA-I | (misma que #21) | (c) |
| 26 | Rango máx/mín de la urea (67 meses) | 3,32 | veces | 2021-26 | Cálculo sobre DANE SIPSA-I | (misma que #21) | (c) |
| 27 | Urea internacional, pico 2026 | 856,9 | USD/t (FOB) | abr-2026 | Banco Mundial, Pink Sheet | https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Pink-Sheet-June-2026.pdf | (a) |
| 28 | Urea internacional, agosto 2026 | 390,0 | USD/t (FOB) | ago-2026 | Banco Mundial, Pink Sheet | https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Pink-Sheet-September-2026.pdf | (a) |
| 29 | DAP internacional, agosto 2026 (máx. del ciclo) | 793,5 | USD/t (FOB) | ago-2026 | Banco Mundial, Pink Sheet | (misma que #28) | (a) |
| 30 | Urea internacional, pico 2022 | 925,0 | USD/t | abr-2022 | Banco Mundial, CMO Monthly | https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/related/CMO-Historical-Data-Monthly.xlsx | (a) |
| 31 | KCl internacional, pico 2022 | 1.202,0 | USD/t | abr-2022 | Banco Mundial, CMO Monthly | (misma que #30) | (a) |
| 32 | Comercio de fertilizantes por el Estrecho de Ormuz | ~1/3 del total marítimo (~16 Mt/año) | — | 2026 | Banco Mundial | https://blogs.worldbank.org/en/opendata/fertilizer-prices-surge-as-strait-of-hormuz-disruptions-tighten- | (b) |
| 33 | Proyección de alza de fertilizantes 2026 | >30 | % | 2026 | Banco Mundial | (misma que #32) | (b) |
| 34 | **Brecha precio FOB vs. minorista (urea)** | **2,85** | veces | jul-2026 | Cálculo sobre B. Mundial + DANE | — | (c) |
| 35 | **Fertilizantes en costo de papa var. Superior, Cundinamarca** | **18,5** | % del costo total | 2023 | Fedepapa, Boletín Regional Cundinamarca | https://fedepapa.com/home/wp-content/uploads/2024/10/Regional-Cundinamarca.pdf | (b) |
| 36 | **Fertilizantes en costo de papa var. Diacol, Cundinamarca** | **19,1** | % del costo total | 2023 | Fedepapa | (misma que #35) | (b) |
| 37 | Fertilizantes en costo de papa, variedades blancas | 17 – 19 | % | 2026 | Fedepapa, Boletín 240 | https://repositorio.fedepapa.com/items/9d98bb6c-26be-4c84-8a4a-7634fe0bbe15 | (b) |
| 38 | Fertilizantes en costo de papa criolla | 9 – 13 | % | 2026 | Fedepapa, Boletín 240 | (misma que #37) | (b) |
| 39 | Fertilizantes en costos agrícolas, Colombia | 12 – 30 (hasta 33) | % | 2026 | La República | (ver #10) | (b) |
| 40 | Costo de fertilización por hectárea de papa | 6.482.773 | COP/ha | jun-2023 | Fedepapa | (ver #35) | (b) |
| 41 | **Área sembrada total, Sabana de Bogotá** | **76.626,3** | ha | 2025 | EVA – MADR | https://www.datos.gov.co/resource/uejq-wxrr.json | **(a)** |
| 42 | **Área de papa, Sabana de Bogotá** | **58.086,9** | ha (75,8 % del total) | 2025 | EVA – MADR | (misma que #41) | **(a)** |
| 43 | Área de hortalizas, Sabana de Bogotá | 8.771,3 | ha (11,4 %) | 2025 | EVA – MADR | (misma que #41) | (a) |
| 44 | Área sembrada total, Cundinamarca | 267.061,1 | ha | 2025 | EVA – MADR | (misma que #41) | (a) |
| 45 | Área de papa, Cundinamarca | 73.884,9 | ha | 2025 | EVA – MADR | (misma que #41) | (a) |
| 46 | Municipio con mayor área sembrada de la Sabana | Villapinzón (17.424,7 ha) | ha | 2025 | EVA – MADR | (misma que #41) | (a) |
| 47 | Segundo municipio de la Sabana | Tausa (15.875,0 ha) | ha | 2025 | EVA – MADR | (misma que #41) | (a) |
| 48 | **Gasto anual en fertilizantes, papa de la Sabana** | **368.256** | millones COP (USD 118,8 M) | 2026 | Estimación propia | — | **(c)** |
| 49 | Participación de Cundinamarca en hectáreas de flores del país | 71 | % | 2025-26 | Alcaldía de Bogotá / Asocolflores | https://bogota.gov.co/cundinamarca/cundinamarca-se-consolida-como-corazon-de-la-floricultura-colombiana | (b) |
| 50 | Empleos directos de la floricultura de Cundinamarca | 115.500 | empleos | 2025-26 | Alcaldía de Bogotá | (misma que #49) | (b) |
| 51 | Microempresas entre las unidades de municipios paperos | 95 | % | 2023 | Fedepapa | (ver #35) | (b) |
| 52 | **Suelos de Cundinamarca con algún grado de erosión** | **80,3** | % | 2015 | IDEAM/MADS/UDCA vía Agrosavia | https://www.agrosavia.co/noticias/impactos-y-posibles-soluciones-a-la-degradaci%C3%B3n-de-suelos-en-colombia | **(a)** |
| 53 | Suelos de Cundinamarca con erosión severa | 5 | % | 2015 | IDEAM vía Agrosavia | (misma que #52) | (a) |
| 54 | Territorio nacional con erosión | 40 | % | 2015 | IDEAM vía MinAmbiente | https://www.minambiente.gov.co/40-del-territorio-colombiano-presenta-algun-grado-de-degradacion-de-suelos-por-erosion/ | (a) |
| 55 | Áreas de uso exclusivamente agrícola con erosión | 93 | % (de 2.078.094 ha) | 2015 | IDEAM vía Agrosavia | (misma que #52) | (a) |
| 56 | Territorio nacional con salinización | 5 | % | 2015 | IDEAM vía MinAmbiente | (misma que #54) | (a) |
| 57 | **Participación de agricultura en emisiones netas de GEI** | **20,69** | % | 2021 | MinAmbiente/IDEAM, INEAA | https://www.minambiente.gov.co/wp-content/uploads/2025/05/Inventario_Nacional_de_Emisiones_y_Absorciones_Atmosfericas_de_Colombia.pdf | **(a)** |
| 58 | Emisiones netas nacionales | 280.101,98 | kt CO₂eq | 2021 | MinAmbiente/IDEAM | (misma que #57) | (a) |
| 59 | Emisiones del sector agricultura | 57.957,85 | kt CO₂eq | 2021 | MinAmbiente/IDEAM | (misma que #57) | (a) |
| 60 | **N₂O de suelos agrícolas dentro del sector agricultura** | **16,61** | % | 2021 | MinAmbiente/IDEAM | (misma que #57) | (a) |
| 61 | N₂O como % del módulo agricultura | 18,50 (10.722,78 kt CO₂eq) | % | 2021 | MinAmbiente/IDEAM | (misma que #57) | (a) |
| 62 | N₂O de suelos gestionados sobre el total nacional | 3,18 (2,06 directas + 1,12 indirectas) | % | 2021 | MinAmbiente/IDEAM | (misma que #57) | (a) |
| 63 | **Nitrógeno aplicado vía fertilizantes inorgánicos** | **370.357** | t de N | 2021 | MinAmbiente/IDEAM | (misma que #57) | **(a)** |
| 64 | Aplicación de urea como categoría de emisión | 0,38 | % del sector agricultura | 2021 | MinAmbiente/IDEAM | (misma que #57) | (a) |
| 65 | Eficiencia de uso del nitrógeno aplicado | <50 (frecuentemente ~40) | % absorbido por el cultivo | — | Literatura agronómica | https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0187-73802024000200099 | (b) |
| 66 | Límite máximo de nitrato en agua potable | 10 | mg/L | Vigente | US EPA | https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations | (a) |
| 67 | Límite máximo de nitrito en agua potable | 1 | mg/L | Vigente | US EPA | (misma que #66) | (a) |
| 68 | **Abono orgánico, promedio nacional** | **23.616** | COP/bulto 50 kg | jul-2026 | DANE SIPSA-I | (ver #13) | **(a)** |
| 69 | **Abono orgánico, Villapinzón (Cundinamarca)** | **20.333** | COP/bulto 50 kg | jul-2026 | DANE SIPSA-I | (ver #13) | **(a)** |
| 70 | Variación del abono orgánico 2021→2026 | +58,3 | % | 2021-26 | Cálculo sobre DANE SIPSA-I | (ver #21) | (c) |
| 71 | Volatilidad del abono orgánico (CV mensual) | 15,8 | % | 2021-26 | Cálculo sobre DANE SIPSA-I | (ver #21) | (c) |
| 72 | Cal dolomita | 18.733 | COP/bulto 50 kg | jul-2026 | DANE SIPSA-I | (ver #13) | (a) |
| 73 | Micorrizas (Sáfer MA) | 93.925 | COP/bulto 50 kg | jul-2026 | DANE SIPSA-I | (ver #13) | (a) |
| 74 | Cobertura de abonos orgánicos sobre necesidades nacionales | <25 | % | — | Bolsa Mercantil de Colombia | https://www.bolsamercantil.com.co/desafio-abastecimiento-abonos-y-fertilizantes-producci%C3%B3n-agr%C3%ADcola | (b) |
| 75 | Crecimiento del consumo aparente de fertilizantes 2012-2022 | +78 (5,9 % anual) | % | 2022 | Bolsa Mercantil de Colombia | (misma que #74) | (b) |
| 76 | Inversión anunciada Ecopetrol para subsidio de fertilizantes | 1 billón COP (USD 274 M) | COP/USD | 2026 | El Heraldo / Diario Financiero | https://www.elheraldo.co/colombia/2026/05/23/gobierno-colombiano-busca-acuerdo-entre-ecopetrol-y-monomeros-para-tratar-de-estabilizar-precio-de-fertilizantes/ | (b) |
| 77 | **TRM vigente** | **3.099,48** | COP/USD (10-sep-2026) | 2026 | Superintendencia Financiera vía datos.gov.co | https://www.datos.gov.co/resource/32sa-8pi3.json | **(a)** |
| 78 | TRM promedio julio 2026 | 3.272,01 | COP/USD | 2026 | Superintendencia Financiera | (misma que #77) | (a) |
| 79 | TRM promedio 2025 | 4.052,27 | COP/USD | 2025 | Superintendencia Financiera | (misma que #77) | (a) |
| 80 | **Costo por kg de N vía urea** | **8.176** | COP/kg N | jul-2026 | Cálculo sobre DANE SIPSA-I | — | **(c)** |
| 81 | Costo por kg de N vía abono orgánico (1,5 % N) | 31.488 | COP/kg N | jul-2026 | Cálculo sobre DANE SIPSA-I | — | (c) |
| 82 | Costo por kg de K₂O vía KCl | 4.344 | COP/kg K₂O | jul-2026 | Cálculo sobre DANE SIPSA-I | — | (c) |

---

## 14. TABLA DE PRECIOS DE REFERENCIA 2026 (PARA EL MODELO FINANCIERO)

> **Esta es la tabla operativa.** Todos los precios provienen del microdato oficial del DANE SIPSA-I, anexo municipal de julio de 2026 — el dato más reciente publicado a la fecha de este informe (10 de septiembre de 2026; el boletín de agosto aún no estaba disponible). Se ofrecen dos series: **promedio nacional** y **promedio Cundinamarca + Bogotá D.C.** Para modelar operaciones en la Sabana de Bogotá, **usar la columna de Cundinamarca/Bogotá**.

### 14.1. Fertilizantes de síntesis química

| Producto | Presentación | Precio COP (nacional) | **Precio COP (Cund/Bogotá)** | USD (TRM jul-26) | USD (TRM 10-sep-26) | COP/tonelada (Cund) | Fuente | Fecha |
|---|---|---|---|---|---|---|---|---|
| **Urea 46 %** | Bulto 50 kg | 188.053 | **186.235** | 56,92 | 60,09 | 3.724.700 | DANE SIPSA-I | jul-2026 |
| **Fosfato Diamónico (DAP) 18-46-0** | Bulto 50 kg | 238.805 | **233.669** | 71,41 | 75,39 | 4.673.380 | DANE SIPSA-I | jul-2026 |
| **Cloruro de Potasio (KCl) 0-0-60** | Bulto 50 kg | 130.323 | **127.821** | 39,06 | 41,24 | 2.556.420 | DANE SIPSA-I | jul-2026 |
| **NPK 15-15-15** | Bulto 50 kg | 178.236 | **178.059** | 54,42 | 57,45 | 3.561.180 | DANE SIPSA-I | jul-2026 |
| **Sulfato de Amonio (SAM) 21-0-0-24(S)** | Bulto 50 kg | 94.224 | **90.500** | 27,66 | 29,20 | 1.810.000 | DANE SIPSA-I | jul-2026 |
| NPK 10-30-10 | Bulto 50 kg | 228.937 | 213.200 | 65,16 | 68,79 | 4.264.000 | DANE SIPSA-I | jul-2026 |
| NPK 18-18-18 | Bulto 50 kg | 172.560 | 185.050 | 56,56 | 59,70 | 3.701.000 | DANE SIPSA-I | jul-2026 |
| NPK 18-18-18-1(Mg) | Bulto 50 kg | 182.335 | 185.450 | 56,68 | 59,83 | 3.709.000 | DANE SIPSA-I | jul-2026 |
| NPK 31-8-8-2 | Bulto 50 kg | 183.321 | 178.013 | 54,40 | 57,43 | 3.560.260 | DANE SIPSA-I | jul-2026 |
| NPK 10-20-20 | Bulto 50 kg | — | 182.486 | 55,77 | 58,88 | 3.649.720 | DANE SIPSA-I | jul-2026 |
| NPK 13-40-13 | Bulto 25 kg | — | 337.525 | 103,15 | 108,90 | 13.501.000 | DANE SIPSA-I | jul-2026 |
| NPK 20-20-20 | Bulto 25 kg | — | 345.000 | 105,44 | 111,31 | 13.800.000 | DANE SIPSA-I | jul-2026 |

### 14.2. Alternativas orgánicas y enmiendas

| Producto | Presentación | Precio COP (nacional) | **Precio COP (Cund/Bogotá)** | USD (TRM jul-26) | COP/tonelada | Fuente | Fecha |
|---|---|---|---|---|---|---|---|
| **Abono Orgánico** | Bulto 50 kg | 23.616 | **20.333** (Villapinzón) | 6,21 | 406.660 | DANE SIPSA-I | jul-2026 |
| Sáfer Micorrizas MA | Bulto 50 kg | 93.925 | 92.975 (Bogotá) / 89.800 (El Rosal) | 28,42 | 1.859.500 | DANE SIPSA-I | jul-2026 |
| Sáfer Micorrizas MA | Bolsa 10 kg | 29.100 | 29.100 (Bogotá) | 8,89 | 2.910.000 | DANE SIPSA-I | jul-2026 |
| Humus 500 | 1 litro | 42.700 | 42.700 (Subachoque) | 13,05 | — | DANE SIPSA-I | jul-2026 |
| Humus 15 | 1 litro | 26.817 | 26.000 – 27.500 | 8,20 | — | DANE SIPSA-I | jul-2026 |
| Humus 15 | 4 litros | 101.500 | 101.500 (Fómeque) | 31,02 | — | DANE SIPSA-I | jul-2026 |
| Fertilizante Orgánico de Lombriz San Rafael | 1 litro | 18.417 | 19.333 (Bogotá) | 5,91 | — | DANE SIPSA-I | jul-2026 |
| Geoplant Humus | 1 litro | 18.000 | 18.000 (Facatativá) | 5,50 | — | DANE SIPSA-I | jul-2026 |
| **Cal Dolomita** | Bulto 50 kg | 18.733 | **16.112** | 4,92 | 322.240 | DANE SIPSA-I | jul-2026 |
| Cal Dolomita 65-33 | Bulto 50 kg | 17.267 | 17.267 | 5,28 | 345.340 | DANE SIPSA-I | jul-2026 |
| Cal Dolomita 70-25 | Bulto 50 kg | 16.993 | 14.067 (Sibaté) | 4,30 | 281.340 | DANE SIPSA-I | jul-2026 |
| **Cal Agrícola** | Bulto 50 kg | 19.129 | 26.000 (Pasca) | 7,95 | 520.000 | DANE SIPSA-I | jul-2026 |

### 14.3. Precios internacionales de referencia (USD/tonelada, FOB)

| Producto | jun-2026 | jul-2026 | **ago-2026** | Fuente | Fecha de consulta |
|---|---|---|---|---|---|
| Urea (E. Europa, prill spot FOB Medio Oriente) | 453,1 | 400,0 | **390,0** | Banco Mundial, Pink Sheet | 10-sep-2026 |
| DAP (spot FOB US Gulf) | 783,8 | 781,3 | **793,5** | Banco Mundial, Pink Sheet | 10-sep-2026 |
| Cloruro de potasio (granular spot CFR Brasil) | 402,5 | 396,5 | **386,9** | Banco Mundial, Pink Sheet | 10-sep-2026 |
| TSP (spot import US Gulf) | 735,6 | 719,5 | **704,4** | Banco Mundial, Pink Sheet | 10-sep-2026 |
| Roca fosfórica (FOB Norte de África) | 156,9 | 170,0 | **170,0** | Banco Mundial, Pink Sheet | 10-sep-2026 |

### 14.4. Tasa de cambio para conversiones

| Concepto | Valor COP/USD | Fecha / periodo | Fuente |
|---|---|---|---|
| **TRM vigente (usar para valoración corriente)** | **3.099,48** | 10 de septiembre de 2026 | Superintendencia Financiera de Colombia |
| TRM siguiente día hábil | 3.101,00 | 11 de septiembre de 2026 | Superintendencia Financiera |
| **TRM promedio julio 2026 (usar con precios de julio)** | **3.272,01** | julio 2026 | Superintendencia Financiera |
| TRM promedio agosto 2026 | 3.126,78 | agosto 2026 | Superintendencia Financiera |
| TRM promedio 2026 (ene-sep) | 3.518,43 | 2026 | Superintendencia Financiera |
| TRM promedio 2025 | 4.052,27 | 2025 | Superintendencia Financiera |
| TRM promedio 2024 | 4.075,04 | 2024 | Superintendencia Financiera |
| TRM promedio 2023 | 4.323,97 | 2023 | Superintendencia Financiera |
| TRM promedio 2022 | 4.251,47 | 2022 | Superintendencia Financiera |
| TRM promedio 2021 | 3.749,12 | 2021 | Superintendencia Financiera |

### 14.5. Advertencias de uso para el modelo financiero

1. **Los precios de julio de 2026 están por encima de la mediana histórica pero por debajo del pico.** Modelar con escenarios: pesimista (pico may-2022 escalado), base (jul-2026), optimista (mínimos de 2024).
2. **El nitrógeno y el fósforo se mueven en direcciones opuestas en 2026.** No aplicar un único factor de inflación a toda la canasta de fertilizantes.
3. **La apreciación del peso amortiguó el choque.** Si la TRM regresa a niveles de 2025 ($4.052), el precio en pesos de un fertilizante importado subiría ~30 % *ceteris paribus*. Incorporar la TRM como variable, no como constante.
4. **Usar precio minorista, no FOB.** El múltiplo observado es de 1,83x a 2,85x.
5. **Comparar orgánico y sintético por unidad de nutriente**, no por bulto (§10.3 y §11.3).

---

## 15. BIBLIOGRAFÍA (APA 7)

Agencia Ecofin. (2026). *World Bank warns fertilizer prices could rise more than 30% in 2026*. https://www.ecofinagency.com/news-industry/3004-55146-world-bank-warns-fertilizer-prices-could-rise-more-than-30-in-2026 (Consultado el 10 de septiembre de 2026)

Agrosavia. (s. f.). *Impactos y posibles soluciones a la degradación de suelos en Colombia*. Corporación Colombiana de Investigación Agropecuaria. https://www.agrosavia.co/noticias/impactos-y-posibles-soluciones-a-la-degradaci%C3%B3n-de-suelos-en-colombia (Consultado el 10 de septiembre de 2026)

Alcaldía Mayor de Bogotá. (2026). *Cundinamarca se consolida como corazón de la floricultura colombiana*. https://bogota.gov.co/cundinamarca/cundinamarca-se-consolida-como-corazon-de-la-floricultura-colombiana (Consultado el 10 de septiembre de 2026)

Banco Mundial. (2026a). *Commodity markets outlook: Pink Sheet — June 2026*. https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Pink-Sheet-June-2026.pdf (Consultado el 10 de septiembre de 2026)

Banco Mundial. (2026b). *Commodity markets outlook: Pink Sheet — September 2026*. https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Pink-Sheet-September-2026.pdf (Consultado el 10 de septiembre de 2026)

Banco Mundial. (2026c). *CMO historical data: Annual prices (nominal), 1960–2025* [Conjunto de datos]. https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/related/CMO-Historical-Data-Annual.xlsx (Consultado el 10 de septiembre de 2026)

Banco Mundial. (2026d). *CMO historical data: Monthly prices* [Conjunto de datos]. https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/related/CMO-Historical-Data-Monthly.xlsx (Consultado el 10 de septiembre de 2026)

Banco Mundial. (2026e, 14 de mayo). *Fertilizer prices surge as Strait of Hormuz disruptions tighten supplies*. World Bank Data Blog. https://blogs.worldbank.org/en/opendata/fertilizer-prices-surge-as-strait-of-hormuz-disruptions-tighten- (Consultado el 10 de septiembre de 2026)

Bolsa Mercantil de Colombia. (s. f.). *Alta dependencia a las importaciones de abonos y fertilizantes impacta producción agrícola*. https://www.bolsamercantil.com.co/desafio-abastecimiento-abonos-y-fertilizantes-producci%C3%B3n-agr%C3%ADcola (Consultado el 10 de septiembre de 2026)

Departamento Administrativo Nacional de Estadística. (2026a). *Boletín técnico 166: Insumos y factores asociados a la producción agropecuaria (SIPSA-I), abril de 2026*. https://www.dane.gov.co/files/operaciones/SIPSA/bol-SIPSAinsumos-abr2026.pdf (Consultado el 10 de septiembre de 2026)

Departamento Administrativo Nacional de Estadística. (2026b). *Boletín técnico 169: Insumos y factores asociados a la producción agropecuaria (SIPSA-I), julio de 2026*. https://www.dane.gov.co/files/operaciones/SIPSA/bol-SIPSAinsumos-jul2026.pdf (Consultado el 10 de septiembre de 2026)

Departamento Administrativo Nacional de Estadística. (2026c). *SIPSA-I: Precio promedio de mercado por municipio, julio de 2026* [Anexo estadístico]. https://www.dane.gov.co/files/operaciones/SIPSA/anex-SIPSAinsumosmunicipio-jul2026.xlsx (Consultado el 10 de septiembre de 2026)

Departamento Administrativo Nacional de Estadística. (2026d). *SIPSA-I: Serie histórica de precio promedio de mercado por municipio, 2021–2026* [Anexo estadístico]. https://www.dane.gov.co/files/operaciones/SIPSA/anex-SIPSAInsumos-SeriesHistoricasMun-2021-2026.xlsx (Consultado el 10 de septiembre de 2026)

Departamento Administrativo Nacional de Estadística. (2026e). *SIPSA-I: Serie histórica de precio promedio de mercado por departamento, 2018–2026* [Anexo estadístico]. https://www.dane.gov.co/files/operaciones/SIPSA/anex-SIPSAInsumos-SeriesHistoricasDep-2018-2026.xlsx (Consultado el 10 de septiembre de 2026)

Escalante Castro, S., & Fajardo Pineda, J. A. (2022). Evaluación de la descontaminación de la cuenca media del río Bogotá y alternativas de solución con humedales artificiales. *INVENTUM, 17*(33). https://portal.amelica.org/ameli/journal/671/6713614003/html/ (Consultado el 10 de septiembre de 2026)

Federación Colombiana de Productores de Papa. (2024a). *Boletín 190: Importaciones de fertilizantes en Colombia aumentan un 22% en 2023*. Fondo Nacional de Fomento de la Papa. https://fedepapa.com/home/wp-content/uploads/2024/10/Boletin-190.pdf (Consultado el 10 de septiembre de 2026)

Federación Colombiana de Productores de Papa. (2024b). *Boletín regional Cundinamarca, Vol. 7 – 2023*. https://fedepapa.com/home/wp-content/uploads/2024/10/Regional-Cundinamarca.pdf (Consultado el 10 de septiembre de 2026)

Federación Colombiana de Productores de Papa. (2025). *Boletín 211*. https://fedepapa.com/home/wp-content/uploads/2025/02/Boletin-211.pdf (Consultado el 10 de septiembre de 2026)

Federación Colombiana de Productores de Papa. (2026). *Boletín No. 240*. Repositorio Fedepapa. https://repositorio.fedepapa.com/items/9d98bb6c-26be-4c84-8a4a-7634fe0bbe15 (Consultado el 10 de septiembre de 2026)

Instituto Colombiano Agropecuario. (2003). *Resolución 00150 de 2003, por la cual se adopta el Reglamento Técnico de Fertilizantes y Acondicionadores de Suelos para Colombia*. https://www.suin-juriscol.gov.co/viewDocument.asp?ruta=Resolucion/30042205 (Consultado el 10 de septiembre de 2026)

Instituto Colombiano Agropecuario. (s. f.). *Proyecto de resolución: Requisitos para el registro de producto, productor y comercializador de biopreparados para uso agrícola elaborados en biofábricas familiares y comunitarias*. Sistema Único de Consulta Pública. https://www.sucop.gov.co/entidades/ica/Anexos%20comentarios/ICA%20bio%20insumos%20AT%20-%2086c54614.pdf (Consultado el 10 de septiembre de 2026)

Ministerio de Agricultura y Desarrollo Rural. (2026). *Evaluaciones Agropecuarias Municipales – EVA, 2019–2025. Base agrícola* [Conjunto de datos]. Datos Abiertos Colombia. https://www.datos.gov.co/resource/uejq-wxrr.json (Consultado el 10 de septiembre de 2026)

Ministerio de Ambiente y Desarrollo Sostenible. (2016). *40% del territorio colombiano presenta algún grado de degradación de suelos por erosión*. https://www.minambiente.gov.co/40-del-territorio-colombiano-presenta-algun-grado-de-degradacion-de-suelos-por-erosion/ (Consultado el 10 de septiembre de 2026)

Ministerio de Ambiente y Desarrollo Sostenible & IDEAM. (2025). *Inventario Nacional de Emisiones y Absorciones Atmosféricas de Colombia*. https://www.minambiente.gov.co/wp-content/uploads/2025/05/Inventario_Nacional_de_Emisiones_y_Absorciones_Atmosfe%CC%81ricas_de_Colombia.pdf (Consultado el 10 de septiembre de 2026)

Palacio, C. (2025). Fertilizantes nacionales en Colombia: ¿hemos avanzado en 2024-2025? *Agronegocios*. https://www.agronegocios.co/comentarios/cesar-palacio-3680916/fertilizantes-nacionales-en-colombia-hemos-avanzado-en-2024-2025-4265492 (Consultado el 10 de septiembre de 2026)

Portafolio. (2026a, 5 de abril). *Producción de fertilizantes en Colombia: ¿por qué esta idea se quedó en el papel?* https://www.portafolio.co/negocios/industrias/produccion-de-fertilizantes-en-colombia-por-que-esta-idea-se-quedo-en-el-papel-491333 (Consultado el 10 de septiembre de 2026)

Portafolio. (2026b). *Colombia importó 1,94 millones de toneladas de fertilizantes y diversificó proveedores en 2025*. https://www.portafolio.co/economia/agro/colombia-importo-1-94-millones-de-toneladas-de-fertilizantes-y-diversifico-proveedores-en-488304 (Consultado el 10 de septiembre de 2026)

La República. (2026a). *Los precios de los fertilizantes se han incrementado más de 50% durante el último año*. https://www.larepublica.co/economia/precio-de-los-fertilizantes-entre-abril-de-2025-y-abril-de-2026-4364877 (Consultado el 10 de septiembre de 2026)

La República. (2026b). *Precio de los fertilizantes subió 51,5% en el último año por la guerra en Medio Oriente*. https://www.larepublica.co/economia/precio-de-los-fertilizantes-en-abril-de-2026-versus-abril-de-2025-4374825 (Consultado el 10 de septiembre de 2026)

Secretaría Distrital de Ambiente. (2024). *Índice de calidad del agua Bogotá 2023–2024*. Observatorio Ambiental de Bogotá. https://oab.ambientebogota.gov.co/?post_type=dlm_download&p=33990 (Consultado el 10 de septiembre de 2026)

Superintendencia Financiera de Colombia. (2026). *Tasa de Cambio Representativa del Mercado – TRM* [Conjunto de datos]. Datos Abiertos Colombia. https://www.datos.gov.co/resource/32sa-8pi3.json (Consultado el 10 de septiembre de 2026)

United States Environmental Protection Agency. (s. f.). *National Primary Drinking Water Regulations*. https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations (Consultado el 10 de septiembre de 2026)

Unidad de Planificación Rural Agropecuaria. (2022). *Plan de Ordenamiento Productivo para la cadena de la papa en Colombia*. https://upra.gov.co/sites/default/files/2025-07/202201_POP_Cadena_Papa.pdf (Consultado el 10 de septiembre de 2026)

---

## ANEXO A — VACÍOS DE INFORMACIÓN DECLARADOS

En cumplimiento del principio de no inventar cifras, se declaran los siguientes datos **NO ENCONTRADOS** tras búsqueda sistemática:

| Dato buscado | Estado | Vía de obtención sugerida |
|---|---|---|
| Carga de nitrógeno y fósforo del río Bogotá (t/año) por tramo | NO ENCONTRADO | Derecho de petición a la CAR Cundinamarca; POMCA del río Bogotá. El servidor de la CAR bloqueó el acceso automatizado el 10-sep-2026. |
| Índice de Calidad del Agua (ICA) del río Bogotá por tramo con valores numéricos | NO ENCONTRADO (solo categorías cualitativas) | CAR Cundinamarca; Observatorio ORARBO (servidor con certificado no verificable). |
| Concentración de nitratos en el acuífero de la Sabana de Bogotá | NO ENCONTRADO | CAR; Plan de Manejo Ambiental de agua subterránea de la Sabana. |
| Concentraciones de N y P en humedales de Bogotá | NO ENCONTRADO | Planes de Manejo Ambiental por humedal, Secretaría Distrital de Ambiente. |
| Hectáreas absolutas de flores en la Sabana de Bogotá | NO ENCONTRADO | Asocolflores (portal de cifras sin poblar en la consulta pública). |
| Participación de fertilizantes en el costo de producción de flores | NO ENCONTRADO | Asocolflores; estudios de costos gremiales. |
| Participación de fertilizantes en el costo de hortalizas de la Sabana | NO ENCONTRADO | Asohofrucol; Agrosavia. |
| Participación de fertilizantes en el costo de pastos / lechería especializada | NO ENCONTRADO | Fedegán, estudios de costos de producción de leche. |
| Número de productores agrícolas de la Sabana y distribución por tamaño de predio | NO ENCONTRADO (solo proxy de microempresas 95 %) | Censo Nacional Agropecuario; Secretaría de Agricultura de Cundinamarca. |
| Tamaño del mercado de fertilizantes orgánicos en Colombia (t o COP) | NO ENCONTRADO | Encuesta Anual Manufacturera DANE; ICA (registros vigentes). |
| Costo y tiempo del trámite de registro ICA para un fertilizante orgánico | NO ENCONTRADO | Tarifario vigente del ICA. |
| Valor exacto de nitratos en la Resolución 2115 de 2007 | NO VERIFICADO directamente | Texto oficial de la resolución (MinSalud). |
| Casos de metahemoglobinemia por nitratos registrados en Colombia | NO ENCONTRADO | Instituto Nacional de Salud (SIVIGILA). |
| Estudios de exposición ocupacional a fertilizantes (no plaguicidas) en la Sabana | NO ENCONTRADO | Literatura de salud ocupacional. |
| Valor numérico del PCG del N₂O en el inventario nacional colombiano | NO EXPLICITADO en el documento | IPCC AR5/AR6 como fuente primaria. |
| Ley de la República sobre bioinsumos | NO EXISTE / NO ENCONTRADA | El marco es reglamentario (resoluciones ICA) y de política (CONPES, PND). |

---

## ANEXO B — TRAZABILIDAD DEL PROCESAMIENTO DE DATOS

Para garantizar la replicabilidad del análisis de precios, se documenta el procesamiento realizado:

| Archivo fuente | Registros | Procesamiento |
|---|---|---|
| `anex-SIPSAinsumosmunicipio-jul2026.xlsx`, hoja «1.3» | 1.527 filas de precios de fertilizantes por municipio | Filtrado por departamento (Cundinamarca + Bogotá D.C.) → 283 registros; agregación por producto y presentación |
| `anex-SIPSAinsumosmunicipio-jul2026.xlsx`, hoja «1.1» | Bioinsumos | Filtrado por palabras clave de productos orgánicos |
| `anex-SIPSAInsumos-SeriesHistoricasMun-2021-2026.xlsx`, hoja «1.3» | 112.978 filas | Filtrado a 5 fertilizantes de síntesis en presentación de 50 kg → 20.981 registros; promedios anuales y mensuales, nacionales y de Cundinamarca/Bogotá; cálculo de coeficiente de variación sobre 67 promedios mensuales |
| `CMO-Historical-Data-Annual.xlsx`, hoja «Annual Prices (Nominal)» | Serie 1960–2025 | Extracción de columnas Phosphate rock, DAP, TSP, Urea, Potassium chloride para 2018–2025 |
| `CMO-Historical-Data-Monthly.xlsx`, hoja «Monthly Prices» | Serie mensual | Extracción de 2021M01–2022M12 y 2025M10–2025M12 |
| `CMO-Pink-Sheet-June-2026.pdf` y `CMO-Pink-Sheet-September-2026.pdf` | Tabla de fertilizantes | Extracción de valores mensuales mar-2026 a ago-2026 |
| `uejq-wxrr.json` (EVA-MADR, API Socrata) | 15.584 registros de Cundinamarca (2019–2025) | Filtrado a 30 municipios sabaneros; agregación de área sembrada por cultivo, grupo, municipio y año |
| `32sa-8pi3.json` (TRM, API Socrata) | Serie diaria desde 2021 | Promedios anuales y mensuales; TRM vigente al 10-sep-2026 |

**Nota sobre el boletín DANE de agosto de 2026:** no estaba publicado al 10 de septiembre de 2026 (se verificó que la URL `bol-SIPSAinsumos-ago2026.pdf` devuelve HTTP 404). El dato más reciente disponible es el de **julio de 2026**, publicado en el Boletín técnico 169.

---

*Documento elaborado el 10 de septiembre de 2026. Todas las URLs fueron consultadas y verificadas en esa fecha. Los precios de fertilizantes corresponden a julio de 2026, último periodo publicado por el DANE.*
