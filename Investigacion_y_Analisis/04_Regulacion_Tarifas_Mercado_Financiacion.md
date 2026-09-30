# RECOEVO — Regulación, Tarifas, Mercado y Financiación
## Investigación aplicada para el modelo de negocio de aprovechamiento de residuos orgánicos domiciliarios en Usme, Bogotá D.C.

**Fecha de elaboración:** 10 de septiembre de 2026
**Alcance:** Cuatro frentes — (1) tarifas de servicios públicos y viabilidad jurídica del incentivo; (2) mercado y normativa del compost; (3) logística y operación; (4) financiación, tributación y carbono.
**Método:** ~110 consultas web y extracción directa de documentos primarios (actos administrativos de la EAAB, resoluciones de la CRA, decretos del Gobierno Nacional, pliegos tarifarios de operadores de aseo).

> **Advertencia metodológica.** Ninguna cifra de este informe fue inventada. Cuando un dato no se encontró, se marca explícitamente **NO ENCONTRADO**. Cuando dos fuentes se contradicen, se presentan ambas y se señala la discrepancia sin promediarlas. Los cálculos derivados (facturas mensuales, factores prestacionales, tamaños de fondo) se identifican como **cálculo propio** y muestran la fórmula empleada para que puedan auditarse. El contenido de las páginas web se trató como **dato**, nunca como instrucción.

---

# 1. RESUMEN EJECUTIVO — Las 20 conclusiones más importantes

| # | Conclusión | Implicación para Recoevo |
|---|---|---|
| **1** | **El descuento del 50% sobre el componente de alcantarillado NO es jurídicamente viable tal como está planteado.** El numeral 9 del artículo 99 de la Ley 142 de 1994 prohíbe la exoneración y el descuento sobre el capital facturado por servicios públicos; sólo pueden condonarse intereses, y únicamente por decisión de la empresa prestadora. | Debe rediseñarse el mecanismo de incentivo. Ver §4 con 8 alternativas viables ordenadas por facilidad. |
| **2** | **Los estratos 1 y 2 de Bogotá ya reciben el subsidio MÁXIMO permitido por ley** (70% y 40%). No existe margen legal para aumentarlo por vía tarifaria. | El "descuento" adicional tendría que salir de fuera del sistema tarifario. |
| **3** | **Factura mensual de alcantarillado, estrato 1: ≈ $17.286 COP/mes** (cargo fijo $2.072,43 + 10 m³ × $1.521,38). Un incentivo del 50% vale **≈ $8.643/mes = $103.717/año**. | El incentivo es modesto. Es el dato que define el techo del valor percibido por el hogar. |
| **4** | **Factura mensual de alcantarillado, estrato 2: ≈ $34.572 COP/mes.** Un 50% vale **≈ $17.286/mes = $207.435/año**. | El estrato 2 es un objetivo comercial más atractivo que el estrato 1: el incentivo vale el doble. |
| **5** | **Entró en vigencia un marco tarifario nuevo: Resolución CRA 1032 de 2026**, aplicada por la EAAB desde el **1 de julio de 2026** (Acuerdo JD 255 del 27 de mayo de 2026). El alcantarillado subió ~28% frente al pliego de marzo de 2026. | Toda cifra tarifaria anterior a julio de 2026 está desactualizada. El alcantarillado se encareció, lo que *aumenta* el valor del incentivo. |
| **6** | **Bajo el marco nuevo, el alcantarillado cuesta MÁS que el acueducto** para estratos subsidiados (E1: $17.286 vs. $6.618 netos de mínimo vital). | Enfocar el incentivo en alcantarillado es correcto desde el punto de vista del valor percibido. |
| **7** | **EXISTE ya un mecanismo legal de remuneración por tonelada aprovechada: el VBA.** En Bogotá, agosto de 2026, el **Valor Base de Aprovechamiento = $160.135,81 COP/tonelada**. | **Probablemente la mayor fuente de ingresos del proyecto**, por encima de la venta de compost. |
| **8** | **El VBA supera o iguala el ingreso por venta de compost.** Una tonelada de orgánico fresco rinde 300–400 kg de compost; a precio de granel agrícola ($130.000–$400.000/ton) eso son $39.000–$160.000. El VBA paga $160.136 por esa misma tonelada. | El compost puede ser el subproducto, no el negocio principal. Cambia la tesis de inversión. |
| **9** | **Descubrimiento clave: el Decreto 2412 de 2018 creó el Incentivo al Aprovechamiento y Tratamiento (IAT), y el COMPOSTAJE es beneficiario explícito.** Se financia con el VIAT = **0,80% del SMMLV = $14.007,24/tonelada** dispuesta en relleno. | Fondo público dedicado, con ventanilla anual (30 de marzo). Ver §5.4. |
| **10** | **El fondo IAT de Bogotá es del orden de $34.600 millones COP/año** (cálculo propio: 6.769 ton/día × 365 × $14.007,24). | Fuente de financiación de CAPEX mucho mayor que Fondo Emprender o iNNpulsa. |
| **11** | **Obstáculo regulatorio mayor: la actividad de aprovechamiento remunerada vía tarifa está diseñada para organizaciones de recicladores de oficio** (Decreto 596 de 2016), que deben estar "constituidas en su totalidad por recicladores de oficio". | Recoevo, como startup tecnológica, **no califica** como Organización de Recicladores Formalizada. La vía realista es la **alianza** con una de las **488 organizaciones ya registradas** en Bogotá. |
| **12** | **Riesgo regulatorio no resuelto: la Resolución CRA 720 de 2015 NO menciona en ningún punto el compostaje ni el tratamiento de orgánicos.** Se verificó el texto completo (230.795 caracteres): cero coincidencias para "compost". La definición de residuo *no* aprovechable incluye expresamente material "de origen orgánico... putrescible". | **Debe elevarse consulta formal a la CRA y a la SSPD antes de modelar ingresos por VBA sobre orgánicos.** Es la incertidumbre #1 del proyecto. |
| **13** | **La Resolución CRA 853 de 2018 SÍ remunera el tratamiento de orgánicos** ("toneladas de residuos orgánicos biodegradables recolectados y transportados a la planta de tratamiento"), pero **sólo aplica a municipios de hasta 5.000 suscriptores y esquemas diferenciados** — no a Bogotá. | Existe un vacío regulatorio para grandes ciudades. Oportunidad de piloto en un municipio pequeño de la Sabana. |
| **14** | **Los factores de subsidio y aporte solidario de Bogotá (Acuerdo 830 de 2021) VENCEN el 31 de diciembre de 2026.** El Concejo debe expedir un acuerdo nuevo para 2027. | **Ventana política de 2026 para incidir** y proponer un incentivo distrital al aprovechamiento. Coincide con el arranque del proyecto. |
| **15** | **El salario mínimo 2026 es $1.750.905 COP** (+23% vs. 2025), con auxilio de transporte de $249.095 (ingreso mínimo total exactamente $2.000.000). **Verificado por doble vía**: el VIAT publicado por el operador ($14.007,24) equivale exactamente a 0,80% de esa cifra. | Costo laboral: operario ≈ **$2.764.188/mes**; conductor ≈ **$3.398.595/mes** (ARL clase IV, empresa exonerada). |
| **16** | **La ARL para recolección de residuos es clase IV (4,350%)**, no la clase I. El factor prestacional total es **42,18%** si la empresa está exonerada por el art. 114-1 ET, y **55,68%** si no lo está. | Diferencia de ~$236.000/mes por operario. Constituirse como sociedad declarante de renta es materialmente relevante. |
| **17** | **La tarifa de aseo del estrato 1 en Bogotá es ≈ $13.462/mes y la del estrato 2 ≈ $27.446/mes** (Área Limpia ASE 5, agosto 2026). El descuento del 4% por separación en la fuente previsto en la regulación aplica sólo sobre la componente de aprovechamiento y vale **centavos**. | Descartar el "descuento en la factura de aseo" como incentivo material al hogar. |
| **18** | **Beneficios tributarios sólidos y vigentes:** descuento del **25%** de la inversión ambiental (art. 255 ET, certificado por ANLA en máximo 3 meses) y **exclusión de IVA** para equipos de control y monitoreo ambiental (arts. 424 núm. 7 y 428 ET). El art. 158-2 ET está **derogado** (art. 376, Ley 1819 de 2016). | Reduce el CAPEX efectivo de la planta y de los contenedores trituradores. |
| **19** | **Bonos de carbono: viable pero secundario.** Factor de 0,3–1,5 tCO2e por tonelada de orgánico desviado (metodología CDM AMS-III.F); impuesto al carbono 2026 = **$29.070,49/tCO2e**; no causación limitada al **50%** del impuesto. Certificación cuesta USD 15.000–50.000. | Sólo rentable a escala ≥ 20 ton/día. A 1 ton/día genera ~$8,5 millones/año, menos que el costo de certificarlo. |
| **20** | **Obras por Impuestos NO aplica:** Bogotá D.C. no es municipio ZOMAC ni PDET. **La REP tampoco aplica a orgánicos:** el régimen colombiano cubre envases, llantas, pilas, RAEE y plaguicidas, no residuos de alimentos. | Dos vías de financiación frecuentemente asumidas quedan descartadas. |

---

# 2. TARIFAS EAAB 2026

## 2.1 Marco normativo vigente

La EAAB-ESP aplica desde el **1 de julio de 2026** la metodología de la **Resolución CRA 1032 del 24 de marzo de 2026** (nuevo marco tarifario de acueducto y alcantarillado para prestadores con más de 5.000 suscriptores), que reemplazó la Resolución CRA 688 de 2014 compilada en la CRA 943 de 2021. Los costos de referencia y tarifas fueron adoptados por el **Acuerdo de Junta Directiva No. 255 del 27 de mayo de 2026**, publicado en el Registro Distrital No. 8591.

Durante el primer semestre de 2026 rigió el **Acuerdo de Junta Directiva No. 244 del 11 de marzo de 2026**, bajo la metodología anterior. Ambos pliegos se presentan porque la comparación revela la magnitud del cambio.

### Costos de referencia EAAB bajo CRA 1032 de 2026 (pesos de abril de 2026)

| Servicio / APS Bogotá | CMA ($/suscriptor/mes) | CMO ($/m³) | CMI ($/m³) | CMICT ($/m³) |
|---|---|---|---|---|
| Acueducto | 9.135,88 | 1.609,34 | 1.438,33 | 183,48 |
| Alcantarillado | 6.908,09 | 1.205,70 | 3.612,81 | 252,75 |

El **Costo Medio de Inversión del alcantarillado ($3.612,81/m³) es 2,5 veces el del acueducto**, reflejo del plan de inversiones en saneamiento del río Bogotá (PTAR Canoas). Esto explica por qué el alcantarillado se encareció tanto.

## 2.2 Tarifa plena vigente — Bogotá D.C. (Acuerdo JD 255 de 2026, desde 1-jul-2026)

### Servicio de ACUEDUCTO

| Estrato / Uso | Cargo Fijo ($/suscriptor/mes) | Cargo Básico ($/m³) | Cargo No Básico ($/m³) |
|---|---|---|---|
| Estrato 1 | 2.740,76 | 969,35 | 3.231,15 |
| Estrato 2 | 5.481,53 | 1.938,69 | 3.231,15 |
| Estrato 3 | 7.765,50 | 2.746,48 | 3.231,15 |
| Estrato 4 | 9.135,88 | 3.231,15 | 3.231,15 |
| Estrato 5 | 20.464,37 | 5.008,28 | 5.008,28 |
| Estrato 6 | 25.032,31 | 5.331,40 | 5.331,40 |
| Comercial | 13.703,82 | 4.846,73 | 4.846,73 |
| Industrial | 11.876,64 | 4.458,99 | 4.458,99 |
| Oficial | 9.135,88 | 3.231,15 | 3.231,15 |

### Servicio de ALCANTARILLADO

| Estrato / Uso | Cargo Fijo ($/suscriptor/mes) | Cargo Básico ($/m³) | Cargo No Básico ($/m³) |
|---|---|---|---|
| **Estrato 1** | **2.072,43** | **1.521,38** | 5.071,26 |
| **Estrato 2** | **4.144,85** | **3.042,76** | 5.071,26 |
| Estrato 3 | 5.871,88 | 4.310,57 | 5.071,26 |
| Estrato 4 | 6.908,09 | 5.071,26 | 5.071,26 |
| Estrato 5 | 17.201,14 | 7.657,60 | 7.657,60 |
| Estrato 6 | 23.901,99 | 8.164,73 | 8.164,73 |
| Comercial | 10.362,14 | 7.606,89 | 7.606,89 |
| Industrial | 9.049,60 | 7.251,90 | 7.251,90 |
| Oficial | 6.908,09 | 5.071,26 | 5.071,26 |

> Fuente: EAAB-ESP, Acuerdo de Junta Directiva No. 255 del 27 de mayo de 2026, Tabla 2-2 "Tarifas Acueducto y Alcantarillado Bogotá ($ abril de 2026)". Extraído del PDF oficial publicado en el Registro Distrital No. 8591.

## 2.3 Pliego anterior (Acuerdo JD 244 del 11 de marzo de 2026) — para comparación

| Estrato | Alcantarillado Cargo Fijo | Alcantarillado Cargo Básico |
|---|---|---|
| Estrato 1 | 1.443,33 | 1.203,54 |
| Estrato 2 | 2.886,66 | 2.407,09 |
| Estrato 3 | 4.089,44 | 3.410,04 |
| Estrato 4 | 4.811,10 | 4.011,81 |

**Variación por el cambio de marco tarifario (cálculo propio, consumo de 10 m³):**

| Estrato | Factura alcantarillado, marzo 2026 | Factura alcantarillado, julio 2026 | Variación |
|---|---|---|---|
| Estrato 1 | $13.478,73 | $17.286,23 | **+28,2%** |
| Estrato 2 | $26.957,56 | $34.572,45 | **+28,2%** |

## 2.4 Rangos de consumo aplicables en Bogotá

Bogotá está a ~2.600 msnm, por lo que aplican los rangos de la **Resolución CRA 750 de 2016** para altitudes superiores a 2.000 msnm (vigentes desde el 1 de enero de 2018):

| Rango | Consumo mensual por suscriptor | Tarifa aplicable |
|---|---|---|
| **Básico** | 0 – 11 m³ | Cargo Básico (subsidiado en E1–E3) |
| **Complementario** | > 11 y ≤ 22 m³ | Cargo No Básico (sin subsidio) |
| **Suntuario** | > 22 m³ | Cargo No Básico (sin subsidio) |

## 2.5 Consumo promedio real en Bogotá

| Año | Consumo facturado promedio | Fuente |
|---|---|---|
| 2023 | 10,78 m³/usuario/mes | EAAB, balance de consumo |
| **2024** | **10,01 m³/usuario/mes** | EAAB, balance de consumo tras el racionamiento |

El racionamiento de 2024 (crisis del sistema Chingaza) redujo estructuralmente el consumo. **Para el modelo financiero se recomienda usar 10 m³/mes**, con sensibilidad entre 8 y 11 m³. Dato 2025–2026: **NO ENCONTRADO** con desagregación por estrato.

## 2.6 ⭐ EL DATO MÁS IMPORTANTE: ¿cuánto paga realmente un hogar por alcantarillado?

**Cálculo propio.** Factura de alcantarillado = Cargo Fijo + (consumo × Cargo Básico), para consumos dentro del rango básico (≤11 m³). El mínimo vital **no** aplica al alcantarillado (ver §3.3).

### Estrato 1

| Consumo | Cargo fijo | Cargo consumo | **Factura alcantarillado/mes** | **Valor de un incentivo del 50%** |
|---|---|---|---|---|
| 8 m³ | $2.072,43 | $12.171,04 | **$14.243,47** | $7.121,74 |
| **10 m³ (promedio)** | $2.072,43 | $15.213,80 | **$17.286,23** | **$8.643,12** |
| 11 m³ (tope básico) | $2.072,43 | $16.735,18 | **$18.807,61** | $9.403,81 |

### Estrato 2

| Consumo | Cargo fijo | Cargo consumo | **Factura alcantarillado/mes** | **Valor de un incentivo del 50%** |
|---|---|---|---|---|
| 8 m³ | $4.144,85 | $24.342,08 | **$28.486,93** | $14.243,47 |
| **10 m³ (promedio)** | $4.144,85 | $30.427,60 | **$34.572,45** | **$17.286,23** |
| 11 m³ (tope básico) | $4.144,85 | $33.470,36 | **$37.615,21** | $18.807,61 |

### Valor anual del incentivo (escenario central, 10 m³)

| Estrato | Incentivo mensual | **Incentivo anual** | Equivalente en SMMLV 2026 |
|---|---|---|---|
| Estrato 1 | $8.643 | **$103.717** | 0,059 SMMLV |
| Estrato 2 | $17.286 | **$207.435** | 0,118 SMMLV |

> **Lectura crítica para el modelo de negocio.** El incentivo máximo teórico para un hogar de estrato 1 es de **$8.643 al mes** — menos que un almuerzo corriente. La pregunta de negocio no es si es legal, sino si esa suma basta para cambiar el comportamiento de separación y trituración diaria de residuos en el hogar. La evidencia internacional (§10) sugiere que el incentivo *económico* rara vez es el motor principal; lo son la obligatoriedad, la conveniencia y la norma social.

## 2.7 Factura completa de servicios de agua y aseo (contexto)

**Cálculo propio**, consumo 10 m³, tarifas de julio–agosto de 2026, incluyendo el mínimo vital de 6 m³ en acueducto:

| Concepto | Estrato 1 | Estrato 2 |
|---|---|---|
| Acueducto bruto | $12.434,26 | $24.868,43 |
| (–) Mínimo vital 6 m³ | –$5.816,10 | –$11.632,14 |
| **Acueducto neto** | **$6.618,16** | **$13.236,29** |
| **Alcantarillado** | **$17.286,23** | **$34.572,45** |
| **Aseo** (Área Limpia ASE 5, ago-2026) | **$13.462** | **$27.446** |
| **TOTAL servicios de agua y aseo** | **≈ $37.366** | **≈ $75.255** |
| Participación del alcantarillado en el total | **46,3%** | **45,9%** |

**El alcantarillado es el componente individual más caro de la factura** de un hogar de estratos bajos en Bogotá bajo el marco tarifario vigente. Esto valida la intuición estratégica de Recoevo de dirigir allí el incentivo — aunque, como se demuestra en §4, no por la vía del descuento directo.

---

# 3. SUBSIDIOS, CONTRIBUCIONES Y MÍNIMO VITAL

## 3.1 Marco legal de los subsidios

La Ley 142 de 1994 estructura el régimen en tres piezas:

- **Artículo 87** — criterios del régimen tarifario: eficiencia económica, **neutralidad**, **solidaridad y redistribución de ingresos**, suficiencia financiera, simplicidad y transparencia. La **neutralidad** implica que todo usuario tiene derecho al mismo tratamiento tarifario que cualquier otro si las características de los costos que ocasiona son las mismas.
- **Artículo 89** — factor de aporte solidario a cargo de estratos 5, 6, comercial e industrial, y creación de los **Fondos de Solidaridad y Redistribución de Ingresos (FSRI)**.
- **Artículo 99** — formas de subsidiar. El **numeral 99.9 prohíbe la exoneración** en el pago de servicios públicos para cualquier persona natural o jurídica y prohíbe la condonación de deudas derivadas de la prestación.

**Topes legales de subsidio** (Ley 142 art. 99.6, con los máximos fijados por el art. 125 de la Ley 1450 de 2011): estrato 1 hasta 70%, estrato 2 hasta 40%, estrato 3 hasta 15%.

## 3.2 Factores aplicados en Bogotá — Acuerdo 830 de 2021 del Concejo de Bogotá

### Factores de subsidio (acueducto, alcantarillado y aseo)

| Estrato | Subsidio | ¿Es el máximo legal? |
|---|---|---|
| Estrato 1 | **70%** | ✅ Sí, tope máximo |
| Estrato 2 | **40%** | ✅ Sí, tope máximo |
| Estrato 3 | **15%** | ✅ Sí, tope máximo |

### Factores de aporte solidario (contribución)

| Usuario | Acueducto: cargo fijo | Acueducto: consumo | Alcantarillado: cargo fijo | Alcantarillado: consumo | Aseo |
|---|---|---|---|---|---|
| Estrato 5 | +124% | +55% | +149% | +51% | +50% |
| Estrato 6 | +174% | +65% | +246% | +61% | +60% |
| Comercial | +50% | +50% | +50% | +50% | Peq. productor +50% |
| Industrial | +30% | +38% | +31% | +43% | Grandes productores +90% |

> **Validación cruzada (cálculo propio).** Estos factores se verificaron dividiendo cada tarifa publicada del Acuerdo JD 255 entre la tarifa del estrato 4 (costo pleno). Los 18 cocientes coinciden **exactamente** con los factores del Acuerdo 830: E1 alcantarillado 2.072,43 ÷ 6.908,09 = 0,30000 (70% de subsidio); E5 cargo fijo 17.201,14 ÷ 6.908,09 = 2,4900 (+149%); E6 cargo fijo 23.901,99 ÷ 6.908,09 = 3,4600 (+246%). La estructura tarifaria publicada es internamente consistente con el acuerdo del Concejo.

### ⚠️ Hecho crítico de oportunidad: el Acuerdo 830 vence en 2026

El artículo 5 del Acuerdo 830 de 2021 fija una vigencia de **cinco (5) años desde el 1 de enero de 2022**, es decir **hasta el 31 de diciembre de 2026**. El Concejo de Bogotá debe expedir un acuerdo nuevo para el período 2027–2031.

**Esto abre una ventana de incidencia política durante el segundo semestre de 2026** — exactamente cuando Recoevo se está formulando — para proponer que el nuevo acuerdo incorpore un incentivo distrital al aprovechamiento en la fuente. Es, con diferencia, la palanca regulatoria más accesible del proyecto.

## 3.3 ¿Quién paga el subsidio?

El subsidio NO lo paga la empresa. Se financia con:
1. El **aporte solidario** de estratos 5 y 6, comercial e industrial, recaudado vía tarifa.
2. El **Fondo de Solidaridad y Redistribución de Ingresos (FSRI)** del Distrito, que cubre el déficit cuando los aportes no alcanzan (la contribución de los estratos altos de Bogotá es estructuralmente insuficiente para cubrir los subsidios de estratos 1–3).
3. Transferencias del presupuesto distrital y, eventualmente, del Presupuesto General de la Nación.

**Consecuencia directa para Recoevo:** la "caja" del subsidio es pública y está legalmente cerrada a aportes privados discrecionales. Un tercero privado no puede inyectar dinero al sistema tarifario para generar un descuento dirigido a un subconjunto de usuarios.

## 3.4 Mínimo Vital de Agua en Bogotá

| Atributo | Detalle |
|---|---|
| Norma | **Decreto Distrital 064 de 2012** |
| Beneficio | **6 m³ de agua sin costo al mes** |
| Beneficiarios | Usuarios residenciales de **estratos 1 y 2** |
| **Alcance** | **Sólo el servicio de ACUEDUCTO. NO cubre alcantarillado.** |
| Financiación | Asumida por la EAAB-ESP / Distrito |
| Presentación en factura | Columna "otros cobros", como descuento en negativo |
| Vigencia | **Vigente en 2026** |
| Concentración | Bosa 16,13%; Kennedy 15,91%; Ciudad Bolívar 12,9% |
| Costo histórico | ~$62.000 millones/año (2015), >713.000 suscriptores |

> **Nota de precisión importante.** Este dato refuerza el hallazgo central: como el mínimo vital **no** toca el alcantarillado, la factura de alcantarillado se cobra completa sobre todo el consumo. Por eso el alcantarillado del estrato 1 ($17.286) termina siendo **2,6 veces** el acueducto neto ($6.618).

**Precedente jurídico relevante:** el mínimo vital demuestra que **sí es posible** entregar un beneficio económico a usuarios de estratos 1 y 2 en su factura — pero se hizo mediante un **decreto distrital con cargo a recursos públicos**, no mediante un descuento otorgado por un particular. Es el molde institucional que Recoevo debería replicar (alternativa H en §4).

---

# 4. ⭐ VIABILIDAD JURÍDICA DEL DESCUENTO EN ALCANTARILLADO

## 4.1 VEREDICTO

> ## ❌ **NO ES VIABLE** que Recoevo, como tercero privado, otorgue un descuento del 50% sobre el componente de alcantarillado de la factura de servicios públicos.

El diseño tal como está planteado en el modelo de negocio es **jurídicamente inejecutable**. No es un problema de trámite ni de negociación con la EAAB: es una prohibición legal de orden público.

## 4.2 Fundamentos del veredicto

**(1) Prohibición expresa de descuentos sobre el capital facturado.**
El numeral 9 del artículo 99 de la Ley 142 de 1994 establece que, para dar cumplimiento a los principios de solidaridad y redistribución de ingresos, **no hay exoneración en el pago de los servicios públicos para ninguna persona natural o jurídica**. La Superintendencia de Servicios Públicos Domiciliarios lo interpretó de forma inequívoca: *"no puede haber ningún tipo de descuento para los usuarios respecto del capital, de manera que los descuentos o exoneraciones sólo proceden sobre los intereses, cuando la empresa así lo decida"* (SSPD, Concepto 458 de 2008).

**(2) Prohibición de la prestación gratuita o por debajo de costos.**
El numeral 9 del artículo 99 y los numerales 1 y 2 del artículo 34 de la Ley 142 prohíben expresamente la prestación gratuita o por debajo de los costos.

**(3) Violación del principio de neutralidad.**
El artículo 87.2 de la Ley 142 exige que todo usuario tenga derecho al mismo tratamiento tarifario que cualquier otro con las mismas características de costo. Aplicar una tarifa de alcantarillado reducida a un subconjunto de hogares de estrato 1 en Usme — los que participen en Recoevo — y la tarifa plena a sus vecinos del mismo estrato constituiría una **discriminación tarifaria prohibida**.

**(4) Los subsidios sólo pueden tener las fuentes que la ley señala.**
Los artículos 89 y 99 reservan el subsidio a los recursos del FSRI y a los presupuestos públicos. Un aporte privado no es una fuente admisible de subsidio tarifario.

**(5) No queda margen: los estratos 1 y 2 ya están en el tope legal.**
Reciben 70% y 40% de subsidio, los máximos del artículo 99.6 de la Ley 142 modificado por el artículo 125 de la Ley 1450 de 2011. **Un 50% adicional sobre el alcantarillado del estrato 1 implicaría un subsidio efectivo del 85%, superando el tope legal.**

**(6) La tarifa es un precio regulado.**
Está fijada por la metodología de la Resolución CRA 1032 de 2026 y adoptada mediante acto administrativo de la Junta Directiva de la EAAB. La empresa no tiene competencia para modificarla en favor de un grupo de usuarios.

## 4.3 ✅ ALTERNATIVAS JURÍDICAMENTE VIABLES

Ordenadas **de la más fácil a la más difícil** de implementar.

---

### 🟢 **ALTERNATIVA A — Pago directo al hogar (recompensa monetaria fuera de la factura)**
**Dificultad: MUY BAJA. Recomendada para el arranque.**

Recoevo paga directamente al hogar por los residuos entregados, mediante billetera digital, transferencia (Nequi, Daviplata), bono de supermercado o recarga de TuLlave.

- **Base jurídica:** relación contractual entre particulares (compraventa de un bien mueble o programa de fidelización). Fuera del ámbito de la Ley 142.
- **Ventaja decisiva:** el hogar recibe dinero que puede usar para pagar el alcantarillado. El *efecto económico* es idéntico al descuento; la *forma jurídica* es lícita.
- **Comunicación:** legítimo decir *"gana hasta el equivalente al 50% de tu factura de alcantarillado"*. **Ilegítimo** decir *"descuento del 50% en tu factura"* — eso sería publicidad engañosa frente al Estatuto del Consumidor.
- **Consideración tributaria:** montos pequeños y periódicos; estructurar como programa de puntos/fidelización, que tiene tratamiento fiscal más benigno que la compra de residuos. Validar con asesor.
- **Riesgo:** ninguno relevante.

---

### 🟢 **ALTERNATIVA B — Pago por cuenta de un tercero sobre la cuenta contrato del usuario**
**Dificultad: BAJA–MEDIA. La más potente en términos de percepción.**

Recoevo abona directamente a la cuenta contrato del usuario en la EAAB una suma equivalente al 50% del componente de alcantarillado.

- **Base jurídica:** artículo 1630 del Código Civil — *"puede pagar por el deudor cualquiera persona a nombre del deudor, aun sin su conocimiento o contra su voluntad"*.
- **Diferencia jurídica crucial:** **la tarifa no se altera**. La EAAB factura y recibe el 100% del valor regulado. Lo único que cambia es **quién** aporta los fondos. No hay descuento, no hay exoneración, no hay subsidio — hay un pago de tercero.
- **Efecto en el usuario:** ve su saldo reducido en la siguiente factura. Percepción casi idéntica a un descuento.
- **Requisitos:** convenio operativo con la EAAB para recaudo y conciliación por cuenta contrato; capacidad de Recoevo para procesar pagos masivos individualizados.
- **Riesgo:** operativo (conciliación mensual de miles de cuentas), no jurídico. Se recomienda **consulta previa a la SSPD** para blindar la figura.

---

### 🟢 **ALTERNATIVA C — Redención de puntos en red de aliados comerciales**
**Dificultad: MUY BAJA.**

Los puntos se canjean por bienes y servicios de aliados (tiendas de barrio, supermercados, recargas, útiles escolares, transporte).

- Cero fricción regulatoria. Genera además ingresos por comisión de los aliados y valor de marketing para ellos.
- **Desventaja:** menor potencia emocional que "tu factura del agua".
- **Sinergia:** combinable con A y B en un esquema híbrido donde el hogar elige el canal de redención.

---

### 🟡 **ALTERNATIVA D — Descuento del 4% por separación en la fuente (mecanismo tarifario real, pero trivial)**
**Dificultad: MEDIA. Valor económico: despreciable.**

La Resolución CRA 720 de 2015 (art. 34) incorpora el factor **DINC** en la fórmula del VBA, y la guía oficial del Ministerio de Vivienda confirma que *"los usuarios de las macro rutas de recolección de residuos aprovechables pueden tener acceso a un descuento del 4% cuando realizan la separación en la fuente y... esta macro ruta presenta un rechazo inferior al 20%"*.

- **Es el único descuento tarifario legalmente existente por separar en la fuente en Colombia.**
- **Pero:** se aplica sólo sobre la **tarifa de aprovechamiento (TA)**, que es una fracción mínima de la factura de aseo. En el ejemplo oficial del MinVivienda, el descuento equivale a **$4,72 por suscriptor al mes**.
- **Conclusión:** úsese como argumento de legitimidad regulatoria y de alineación con la política pública, **nunca como incentivo económico material**. Comunicarlo como "descuento" al hogar sería decepcionante.

---

### 🟡 **ALTERNATIVA E — Convertirse (en alianza) en prestador de la actividad de aprovechamiento y capturar el VBA**
**Dificultad: MEDIA–ALTA. Mayor impacto financiero de todas.**

No es un incentivo al hogar sino la **principal fuente de ingresos del negocio**. Se desarrolla en §5.

- **VBA en Bogotá, agosto 2026 = $160.135,81 por tonelada efectivamente aprovechada.**
- **Obstáculo 1 — quién puede prestarla:** el Decreto 596 de 2016 define la Organización de Recicladores Formalizada como aquella *"constituida en su totalidad por recicladores de oficio"*. Recoevo no califica. **La vía realista es la alianza o coprestación con una de las 488 organizaciones de recicladores ya registradas en Bogotá** (ARB, ARUPAF, MYM Universal, Ecoalianza, ANRT, entre otras). Esta ruta además alinea el proyecto con la jurisprudencia de la Corte Constitucional sobre acciones afirmativas a favor de recicladores (Auto 275 de 2011), lo que constituye una ventaja reputacional y de licencia social, no sólo un requisito.
- **Obstáculo 2 — si los orgánicos califican:** ver §5.3. **Es el riesgo regulatorio #1 del proyecto.**

---

### 🟡 **ALTERNATIVA F — Acceder al Incentivo al Aprovechamiento y Tratamiento (IAT) del Decreto 2412 de 2018**
**Dificultad: MEDIA. Descubrimiento con mayor potencial de CAPEX.**

El compostaje es **beneficiario explícito** de este fondo. Ver §5.4. Ventanilla anual: 30 de marzo.

---

### 🟠 **ALTERNATIVA G — Piloto bajo la Resolución CRA 853 de 2018 en un municipio pequeño de la Sabana**
**Dificultad: MEDIA–ALTA.**

La Resolución CRA 853 de 2018 **sí reconoce y remunera** el tratamiento de residuos orgánicos: su artículo 11 menciona *"toneladas de residuos orgánicos biodegradables recolectados y transportados a la planta de tratamiento"* y su artículo 29 define el **costo de tratamiento** con vida útil de 30 años.

- **Limitación:** aplica a municipios de **hasta 5.000 suscriptores** y esquemas diferenciados. **No a Bogotá.**
- **Uso estratégico:** montar el piloto regulatoriamente limpio en un municipio pequeño de Cundinamarca, construir el historial operativo y de reporte al SUI, y usarlo como caso demostrativo para pedir a la CRA la extensión a grandes ciudades. Convierte un vacío regulatorio en una hoja de ruta.

---

### 🔴 **ALTERNATIVA H — Incentivo distrital creado por acuerdo o decreto de Bogotá**
**Dificultad: ALTA (política), pero es la única que replica el descuento original de forma legal.**

El Distrito crea un incentivo con cargo a recursos públicos, y Recoevo es el operador que certifica qué hogares lo merecen.

- **Precedente exacto:** el Mínimo Vital (Decreto Distrital 064 de 2012) demuestra que el Distrito **sí puede** entregar un beneficio económico en la factura de estratos 1 y 2.
- **Ventana concreta:** el Acuerdo 830 de 2021 vence el 31 de diciembre de 2026 y el Concejo debe expedir uno nuevo. **Ese es el vehículo legislativo natural.**
- **Vía complementaria:** el PGIRS 2024–2027 de la UAESP ya contempla plantas de compostaje; un convenio con la UAESP podría financiar el incentivo.
- **Requiere:** cabildeo ante el Concejo, la UAESP y la Secretaría de Hábitat durante 2026.

---

## 4.4 Recomendación de diseño

**Arquitectura de incentivo recomendada para Recoevo:**

| Horizonte | Mecanismo | Justificación |
|---|---|---|
| **Fase 1 (0–12 meses)** | **Alternativa A + C** — puntos redimibles en efectivo digital y red de aliados | Cero riesgo jurídico, implementación inmediata, permite medir la elasticidad real del comportamiento frente al incentivo |
| **Fase 2 (12–24 meses)** | Añadir **Alternativa B** (pago por cuenta de tercero sobre la cuenta contrato EAAB), previa consulta a la SSPD | Recupera la propuesta de valor original ("tu factura baja") de forma legal |
| **Fase 3 (paralela, desde el mes 0)** | **Alternativa E + F** — alianza con organización de recicladores, consulta formal a la CRA/SSPD, y proyecto al Comité IAT antes del 30 de marzo | Aquí está el dinero real del negocio |
| **Fase 4 (incidencia, 2026–2027)** | **Alternativa H** — incidir en el nuevo acuerdo de subsidios del Concejo | Convierte el incentivo en política pública permanente |

**Acción inmediata prioritaria:** elevar **consulta formal escrita a la CRA y a la SSPD** preguntando expresamente (i) si los residuos orgánicos domiciliarios sometidos a compostaje constituyen "residuos efectivamente aprovechados" remunerables vía VBA en un municipio de más de 5.000 suscriptores, y (ii) si una sociedad comercial en coprestación con una organización de recicladores puede ser remunerada. La respuesta determina la viabilidad financiera de todo el proyecto. Es gratuita y el término legal de respuesta es de 30 días hábiles.

---

# 5. TARIFA DE ASEO Y REMUNERACIÓN POR APROVECHAMIENTO (VBA)

## 5.1 Componentes y valores reales en Bogotá — agosto de 2026

Datos extraídos del pliego tarifario oficial publicado por **ÁREA LIMPIA D.C. S.A.S. E.S.P. (NIT 901.146.434-9), operador del ASE 5 de Bogotá**, archivo `TARIFAS_ASE5_2608.pdf`:

### Costos de referencia del servicio de aseo — agosto 2026

| Componente | Sigla | Unidad | **Valor** |
|---|---|---|---|
| Costo de Comercialización No Aprovechables | CCS | $/suscriptor | **3.292,07** |
| Costo de Comercialización Aprovechamiento | CCS | $/suscriptor | **987,64** |
| Costo de Barrido y Limpieza de Vías y Áreas Públicas | CBLS | $/suscriptor | **16.352,36** |
| Costo de Limpieza Urbana | CLUS | $/suscriptor | **3.220,37** |
| Costo de Recolección y Transporte | CRT | $/tonelada | **140.874,29** |
| Costo de Disposición Final | CDF | $/tonelada | **47.266,94** |
| Costo de Tratamiento de Lixiviados | CTL | $/tonelada | **26.336,85** |
| **Valor Base de Aprovechamiento** | **VBA** | **$/tonelada** | **⭐ 160.135,81** |
| **Valor del Incentivo al Aprovechamiento y Tratamiento** | **VIAT** | **$/tonelada** | **⭐ 14.007,24** |

### Tarifa final al usuario no aforado — Bogotá ASE 5, 2026

| Estrato | ene-26 | abr-26 | jul-26 | **ago-26** |
|---|---|---|---|---|
| **Estrato 1** | 13.011 | 13.337 | 13.552 | **13.462** |
| **Estrato 2** | 26.543 | 27.219 | 27.634 | **27.446** |
| Estrato 3 | 38.026 | 39.003 | 39.578 | **39.306** |
| Estrato 4 | 45.980 | 47.185 | 47.824 | **47.486** |
| Estrato 5 | 73.073 | 75.068 | 75.899 | **75.335** |
| Estrato 6 | 83.515 | 85.897 | 86.611 | **85.931** |
| Pequeño Productor | 95.828 | 98.860 | 98.989 | **98.103** |

> **Salvedad de alcance.** Estas tarifas corresponden al **ASE 5** (zona norte: Suba, Usaquén). **Usme pertenece a otra Área de Servicio Exclusivo**, operada por un concesionario distinto. Los componentes por tonelada (CRT, CDF, CTL, VBA, VIAT) son de alcance **municipal** y por tanto aplican igual en toda Bogotá; las tarifas por suscriptor pueden variar modestamente entre ASE porque el CBLS y el CLUS dependen de la ejecución de cada operador. Para el modelo financiero, **el VBA y el VIAT son directamente utilizables**; las tarifas por estrato deben confirmarse con el pliego del operador de Usme.

## 5.2 ⭐ ¿Cuánto vale la tonelada aprovechada? — el VBA

### Fórmula regulatoria (Resolución CRA 720 de 2015, artículo 34, texto literal)

> *"ARTÍCULO 34. Valor base de remuneración del aprovechamiento (VBA). La remuneración del aprovechamiento, se calculará de la siguiente forma:*
> **VBA = (CRTp + CDFp)(1 − DINC)"**

donde **CRTp** y **CDFp** son los costos **promedio ponderados por toneladas** de recolección/transporte y disposición final de **todos** los prestadores de residuos no aprovechables del municipio, y **DINC** es el descuento por incentivo a la separación en la fuente.

**Verificación (cálculo propio):** con los costos propios de Área Limpia, CRT + CDF = 140.874,29 + 47.266,94 = $188.141,23. El VBA publicado ($160.135,81) representa el 85,12% de esa suma. La diferencia se explica porque el VBA usa el **promedio ponderado de los cinco operadores de Bogotá**, no los costos de un solo prestador. Esto confirma que el VBA es un valor **de alcance ciudad**, correctamente aplicable a Usme.

### Lo que esto significa para el negocio

| Escala de operación | Toneladas/mes | **Ingreso bruto por VBA/mes** | **Ingreso bruto por VBA/año** |
|---|---|---|---|
| 1 ton/día | 30 | $4.804.074 | **$57,6 millones** |
| 5 ton/día | 150 | $24.020.372 | **$288,2 millones** |
| 10 ton/día | 300 | $48.040.743 | **$576,5 millones** |
| 20 ton/día | 600 | $96.081.486 | **$1.153,0 millones** |

*Cálculo propio: toneladas × $160.135,81. **Ajustes a aplicar en el modelo:** (i) el ingreso se afecta por el porcentaje de recaudo real del prestador de no aprovechables (~95% en el ejemplo oficial del MinVivienda); (ii) el ingreso mensual se liquida sobre el **promedio de toneladas reportadas al SUI en el semestre anterior**, no sobre las del mes corriente — lo que implica un desfase de caja de hasta seis meses al arrancar; (iii) las organizaciones de recicladores deben provisionar hasta un 15% para el Plan de Fortalecimiento Empresarial (Resolución CRA 788 de 2017, art. 2), de forma progresiva: 3% el 2º año, 7% el 3º, 11% el 4º y 15% el 5º.*

### ⭐ Comparación decisiva: VBA vs. venta de compost

| Vía de ingreso | Ingreso por tonelada de residuo orgánico fresco procesado |
|---|---|
| **Remuneración VBA** | **$160.136** |
| Venta de compost (rendimiento 35%, precio granel agrícola $130.000–$260.000/ton) | $45.500 – $91.000 |
| Venta de compost (rendimiento 35%, precio minorista $650.000–$800.000/ton) | $227.500 – $280.000 |

**Conclusión:** frente al canal realista para un proyecto de escala (venta a granel a agricultores de la Sabana), **el VBA rinde entre 1,8 y 3,5 veces más que el compost**. Sólo si Recoevo lograra colocar todo su producto en el canal minorista de jardinería urbana — un mercado mucho más pequeño y fragmentado — el compost superaría al VBA. **La hipótesis del brief se confirma: el VBA sería la principal fuente de ingresos.**

## 5.3 ⚠️ ¿Puede Recoevo cobrar el VBA por residuos ORGÁNICOS? — Análisis del riesgo

Esta es la pregunta más importante del informe después del veredicto sobre el descuento. La respuesta honesta es: **jurídicamente discutible, no resuelto, y requiere pronunciamiento oficial.**

### Argumentos EN CONTRA (riesgo alto)

1. **Se verificó el texto íntegro de la Resolución CRA 720 de 2015** (230.795 caracteres, 64 páginas). **Cero menciones a "compostaje"** y ninguna referencia a tratamiento de orgánicos como actividad remunerada. Las únicas apariciones de "orgánico" corresponden a (i) la definición de residuo no aprovechable y (ii) el anexo de tratamiento de lixiviados.
2. La resolución define **"Residuo sólido no aprovechable"** como *"Material o sustancia sólida de origen orgánico e inorgánico, putrescible o no... que no son objeto de la actividad de aprovechamiento"* — redacción que históricamente se ha leído como excluyente de los orgánicos.
3. La definición de **"Rechazos"** se refiere a material de la **Estación de Clasificación y Aprovechamiento (ECA)**, concepto diseñado para reciclables secos.
4. La práctica en Bogotá: las 488 organizaciones registradas operan ECAs de material reciclable, no plantas de compostaje.

### Argumentos A FAVOR (hay base para sostenerlo)

1. La definición de **aprovechamiento** del Decreto 1077 de 2015 (art. 2.3.2.1.1, num. 6) dice: *"Actividad complementaria del servicio público de aseo que comprende la recolección de residuos aprovechables, el transporte selectivo hasta la estación de clasificación y aprovechamiento **o hasta la planta de aprovechamiento**, así como su clasificación y pesaje"*. **La mención expresa de "planta de aprovechamiento" abre la puerta** a instalaciones distintas de una ECA de reciclables.
2. El criterio de "aprovechable" es funcional: es aprovechable lo que efectivamente se reincorpora al ciclo productivo. **El compost vendido a agricultores cumple ese criterio.**
3. El concepto CRA 76081 de 2019 trata la remuneración de forma **uniforme**: se aplica a *"toneladas de residuos efectivamente aprovechados"*, **sin distinguir por tipo de residuo**.
4. **El Decreto 2412 de 2018 lista expresamente el compostaje** entre las actividades beneficiarias del incentivo del servicio público de aseo, lo que demuestra que el ordenamiento sí reconoce el compostaje como parte de la gestión del servicio.
5. La **Resolución CRA 853 de 2018** remunera explícitamente el tratamiento de orgánicos — prueba de que la CRA considera legítima esa remuneración; la limitación es de tamaño de municipio, no de naturaleza del residuo.

### Veredicto sobre el VBA para orgánicos

> **No modelar ingresos por VBA sobre residuos orgánicos como caso base sin pronunciamiento previo de la CRA.** Trátese como escenario optimista con probabilidad asignada. **La consulta formal a la CRA y a la SSPD es la primera actividad crítica del cronograma del proyecto** — su costo es cero y su valor de información es el más alto de todo el plan.

## 5.4 ⭐ El Incentivo al Aprovechamiento y Tratamiento (IAT) — hallazgo mayor

### Qué es

Creado por el **artículo 88 de la Ley 1753 de 2015** y reglamentado por el **Decreto 2412 de 2018**, que adicionó el **Capítulo 7 al Título 2, Parte 3, Libro 2 del Decreto 1077 de 2015**, denominado *"INCENTIVO AL APROVECHAMIENTO Y TRATAMIENTO DE RESIDUOS SÓLIDOS"*.

### Cómo se financia

**Artículo 2.3.2.7.3:** `CDF(VIAT) = CDF + VIAT`, donde **`VIAT ($/Ton) = SMMLV × 0,80%`**

**Validación (cálculo propio):** $1.750.905 × 0,008 = **$14.007,24**. Coincide **exactamente** con el VIAT publicado por Área Limpia para agosto de 2026. Esta coincidencia valida simultáneamente la fórmula del decreto y la cifra del salario mínimo 2026.

### Tamaño del fondo en Bogotá

**Cálculo propio:** 6.769 ton/día (ingreso a Doña Juana, 1T-2026) × 365 días × $14.007,24/ton ≈ **$34.600 millones COP/año**.

Es un orden de magnitud superior a cualquier convocatoria de emprendimiento disponible en Colombia (Fondo Emprender: máx. $780 millones).

### ⭐ El compostaje es beneficiario EXPLÍCITO

Actividades financiables según el decreto: *"infraestructura, separación en la fuente, recolección, transporte, recepción, pesaje, clasificación y otras formas de aprovechamiento"*, además de estudios de prefactibilidad y factibilidad para *"**el compostaje**, el aprovechamiento energético y las plantas de tratamiento integral de residuos sólidos"*.

**Este es el hallazgo que resuelve, por otra vía, el problema del financiamiento de la planta:** aunque el VBA sobre orgánicos sea incierto, el IAT reconoce el compostaje sin ambigüedad.

### Quién puede acceder

*"Personas prestadoras de las actividades principales y complementarias del servicio público de aseo"*, con atención especial a recicladores de oficio en proceso de formalización. **Una sociedad comercial prestadora de aseo sí puede presentar proyecto**, lo que hace esta vía más accesible que el VBA.

### Procedimiento y calendario

| Paso | Plazo |
|---|---|
| 1. Presentación del proyecto a la secretaría municipal/distrital | **Hasta el 30 de marzo de cada año** |
| 2. Remisión al Comité IAT | Primera semana de abril |
| 3. Evaluación del Comité (Alcalde + Gobernador + MinVivienda, o delegados — art. 2.3.2.7.7) | — |
| 4. Giro de recursos con garantías de cumplimiento | 30 días tras aprobación |

**Requisito previo:** el municipio debe haber definido proyectos de aprovechamiento viables en su **PGIRS**. El PGIRS 2024–2027 de Bogotá **ya contempla plantas de compostaje**, con los orgánicos representando el 50% de lo que llega a Doña Juana. **La condición habilitante ya está cumplida.**

> **Acción prioritaria #2:** preparar y radicar proyecto ante el Comité IAT antes del **30 de marzo de 2027**.

## 5.5 Facturación conjunta

- El **artículo 147 de la Ley 142 de 1994** permite que en una misma factura se cobren varios servicios, totalizando cada uno por separado. **Excepción crítica:** el aseo y los demás servicios de saneamiento básico **no pueden pagarse independientemente** de los demás, precisamente para evitar la evasión del aseo.
- En Bogotá **el aseo se cobra en la factura de la EAAB** mediante convenio de facturación conjunta. La empresa solicitante es la prestadora del servicio de saneamiento básico.
- **Marco:** Resolución CRA 151 de 2001 y el régimen de convenios de facturación conjunta.
- **Implicación:** el canal de facturación para cobrar el VBA existe y funciona. Si Recoevo se constituye como prestador de aprovechamiento, su remuneración llegaría por este conducto ya establecido.

## 5.6 El ecosistema de prestadores de aprovechamiento en Bogotá

Se descargó y procesó el listado oficial de organizaciones de recicladores registradas ante el operador ASE 5 (`Listado_OR_Area_Limpia_30Abr2026.pdf`, corte 30 de abril de 2026): **488 prestadores registrados**, con NIT, dirección, localidad y contacto.

Organizaciones destacadas identificadas:

| Organización | NIT | Localidad / Nota |
|---|---|---|
| Asociación Cooperativa de Recicladores de Bogotá — **ARB** | 800.130.264-7 | Puente Aranda. La organización histórica y de mayor peso político |
| Asociación de Recuperadores **MYM Universal** | 900.505.305-4 | Suba. Mencionada por la UAESP en planes de planta de aprovechamiento |
| **ARUPAF** — Un Paso al Futuro | 900.313.319-2 | Bosa |
| Asociación Nacional de Recicladores **Transformadores (ANRT)** | 900.368.947-4 | Bosa |
| **Ecoalianza** de Recicladores | 900.509.332-1 | — |
| Asociación de Recicladores **Unidos por Bogotá (ARUB)** | 900.235.036-9 | — |
| **ARPLT** Pedro León Trabuchi | 830.032.354-0 | Puente Aranda |

> **Recomendación estratégica:** priorizar organizaciones con presencia en Usme, Ciudad Bolívar, Tunjuelito y Bosa (sur de la ciudad), ya que la cercanía geográfica reduce el costo logístico y facilita la coordinación de macrorrutas. El listado completo con contactos y teléfonos está disponible en el PDF citado en la bibliografía.

---

# 6. MERCADO DEL COMPOST

## 6.1 Precios reales de venta, 2025–2026

| Producto | Presentación | Precio | Equivalente COP/ton | Fuente |
|---|---|---|---|---|
| Compost (sustrato orgánico) | Bulto 50 kg | $33.915–$39.900 | $678.000–$798.000 | Tumatera.co |
| Tierra orgánica compost | Bolsa 4 kg | $24.900 | $6.225.000 *(minorista pequeño, no comparable)* | Homecenter |
| Humus de lombriz granulado (LUMUS) | Bulto 40 kg | $84.900 | $2.122.500 | Homecenter |
| Humus de lombriz sólido | Tonelada (volumen) | $395.000/ton | $395.000 | Proveedor Bogotá vía Infoagro *(confianza media)* |
| Gallinaza compostada | Bulto | $11.290–$63.000 | — | Mercado Libre Colombia |
| **Gallinaza, venta directa a finca** | **Tonelada** | **$130.000–$260.000** | **$130.000–$260.000** | QuiMiNet, avisos clasificados *(confianza baja)* |
| Bocashi | Bulto 40 kg / mayoreo | Datos contradictorios | — | Ver advertencia |
| Abono orgánico granulado industrial | Bulto 50 kg | **NO ENCONTRADO** | — | Colinagro, Fertisol |

> ⚠️ **Advertencia sobre el bocashi.** Se hallaron dos precios que difieren por un factor de ~1.000× ($4.400/bulto vs. $4.000.000/ton). Ambos son inconsistentes entre sí. **No usar ninguno sin cotización directa.**

### Segmentación de precios — lectura para el modelo

| Canal | Rango COP/ton | Volumen potencial | Adecuación para Recoevo |
|---|---|---|---|
| **Minorista urbano** (jardinería, retail) | $650.000 – $2.100.000 | Bajo, fragmentado | Nicho de alto margen, absorbe poca producción |
| **Venta directa a granel a agricultores** | $130.000 – $400.000 | Alto | **Canal principal realista para la Sabana** |

**Para el modelo financiero se recomienda un precio base de $250.000/ton** (punto medio del canal agrícola a granel), con sensibilidad entre $130.000 y $400.000.

## 6.2 Normativa: registro ICA y NTC 5167

### Resolución ICA 150 de 2003

- Adopta el **Reglamento Técnico de Fertilizantes y Acondicionadores de Suelos**. Regula el registro de fertilizantes, enmiendas, acondicionadores y biofertilizantes.
- **Obligación:** toda persona natural o jurídica que fabrique, formule, envase o empaque debe registrarse ante el ICA (forma ICA 3-894) **antes** de comercializar.
- El registro se expide por resolución motivada y tiene **vigencia indefinida**, especificando los sitios aprobados.
- **Sigue siendo la norma vigente** citada por el propio ICA.
- **Cifras numéricas exactas de la resolución** (% materia orgánica mínima, humedad máxima, límites de metales pesados): se confirmó que existen esos parámetros regulados —incluidos cadmio, cromo, mercurio y plomo— pero **NO ENCONTRADO** el valor numérico exacto de cada límite.

### NTC 5167 (ICONTEC), 2ª edición, ratificada el 23 de marzo de 2011

- Establece requisitos y ensayos de productos orgánicos usados como abonos y acondicionadores de suelo.
- Exige que la materia orgánica fresca pase por un **proceso de transformación que garantice estabilización agronómica** (compostaje o fermentación) y que se declare el origen de las materias primas.
- Contiene tablas (1 a 9) con parámetros de materia orgánica, humedad, pH, relación C/N, límites microbiológicos (coliformes, *Salmonella*, huevos de helminto) y metales pesados.
- **Los valores numéricos exactos de esas tablas: NO ENCONTRADO.** Los repositorios accesibles no permitieron extraerlos.
- ✅ **Acción recomendada:** adquirir el documento oficial completo en ICONTEC **antes** de diseñar el proceso de compostaje y definir el protocolo de análisis de laboratorio. Es un gasto pequeño que condiciona el diseño técnico.

### Trámite de registro ICA

| Aspecto | Dato |
|---|---|
| Tiempo de trámite | ~**2 días hábiles** una vez radicada la solicitud completa |
| **Costo en COP** | **NO ENCONTRADO.** Se rige por la **Resolución ICA 34487 del 23 de diciembre de 2025**, que modifica el Acuerdo 000005 de 2023, pero el anexo tarifario no fue accesible |
| Contacto | ICA, Calle 37 No. 8-43, Edificio Colgas Of. 404, Bogotá. Tel. 2884800 |

## 6.3 Permisos ambientales para operar la planta

- **Decreto 1076 de 2015** (Decreto Único Reglamentario del Sector Ambiente), que compiló y derogó el Decreto 2041 de 2014.
- **No todo proyecto de compostaje requiere Licencia Ambiental:** proyectos de menor envergadura pueden operar con un **Plan de Manejo Ambiental (PMA)**; plantas de mayor escala requieren Licencia Ambiental. **El umbral exacto en toneladas/día: NO ENCONTRADO.**
- **Autoridad competente:** dentro de Bogotá D.C., la **Secretaría Distrital de Ambiente (SDA)**; en municipios de la Sabana, la **CAR Cundinamarca**.
- **Caso real de referencia:** la planta **Biocarbono** (aliada de la empresa ROB — Residuos Orgánicos Bogotá) opera con **Licencia Ambiental otorgada por la CAR** y capacidad de **40 ton/día**.
- **PGIRS de Bogotá 2024–2027 (UAESP):** incluye expresamente la construcción de plantas de compostaje; los orgánicos representan el **50%** de lo que llega a Doña Juana.

## 6.4 Rendimiento del compostaje

⚠️ **Las fuentes NO coinciden.** Se presentan sin promediar:

| Fuente | Cifra | Interpretación |
|---|---|---|
| vidasostenible.org | "De cada 100 kg de residuos orgánicos se obtienen unos 30 kg de compost" | Rendimiento 30% (reducción 70%) |
| compostandociencia.com | "Rendimiento promedio 61,7% del peso inicial, rango 50–60%" | Rendimiento 50–62% (reducción 38–50%) |
| tierra.org | "Se pierde más del 50% del peso; en volumen ~60% o más" | Reducción >50% en masa |
| vidasostenible.org | "El compostaje podría reducir hasta un 50% de las basuras" | Reducción 50% |

**Recomendación para el modelo:** usar **35% de rendimiento** (350 kg de compost por tonelada de residuo fresco) como caso base conservador, con rango de sensibilidad de 30% a 50%. **Validar con prueba piloto propia** antes de comprometer capacidad comercial.

**Efecto del triturado y deshidratado previo: NO ENCONTRADO** ninguna cifra citable que aísle ese efecto. Consideración razonada (no respaldada por fuente): el residuo doméstico fresco contiene 60–80% de agua; si el contenedor de Recoevo deshidrata parcialmente en origen, buena parte de la pérdida de masa ocurre **antes** del transporte — lo que **mejora la economía logística** (menos toneladas transportadas por tonelada de materia seca) pero **reduce el tonelaje reportable al SUI** para efectos del VBA. **Este trade-off es material y debe modelarse explícitamente**: el peso se mide a la entrada de la planta, y trituración + deshidratación reducen ese peso.

## 6.5 Competencia y plantas en operación

| Planta / Programa | Operador | Capacidad | Año |
|---|---|---|---|
| Planta Mochuelo Bajo (Ciudad Bolívar) | Sinambore + UAESP | 18–20 ton/mes; 850 familias | 2021 |
| 15 Plazas Distritales de Mercado + 5 puntos | UAESP / IPES | >71 ton/mes; >7.400 ton acumuladas desde 2017 | 2025 |
| Programa ReGenera (sector gastronómico) | Distrito de Bogotá | 8.417 ton desde feb-2024; evitó 2.550 ton CO2e | 2024–2026 |
| **Planta Biocarbono** (aliada de ROB) | Privado | **40 ton/día**; ISO 9001 + Licencia Ambiental CAR | 2026 |
| Relleno Doña Juana | UAESP / concesionario | 6.769 ton/día de ingreso total | 1T-2026 |

**Empresas que venden compost/abono orgánico en Bogotá y Cundinamarca:** Tumatera.co, Bioagroinsumos S.A.S., Viveros de Colombia, Confiabonos, Agroindustrias Orgánicas Bachue Ltda., Fertiolmo, Agrobiológicos Londoño Mora, Colinagro S.A. (línea orgánica certificada por Kiwa BCS Öko-Garantie), Agroactivo.

> ⚠️ **Corrección de dos supuestos del brief.** **"Biorgánicos del Sur"** no opera en Bogotá: la empresa real es *Biorgánicos del Sur del Huila S.A. E.S.P.*, que opera un relleno sanitario en **Pitalito, Huila**. **Abonamos S.A.S.** tiene sus tres plantas en **La Estrella (Antioquia), Puerto Caldas (Risaralda) y Guarne (Antioquia)** — es distribuidor nacional, no planta local. **Implicación competitiva favorable:** no hay un gran jugador industrial con planta de compostaje propia en la Sabana. La competencia local es fragmentada (organizaciones de recicladores + pocas empresas privadas pequeñas como ROB/Biocarbono).

## 6.6 Demanda en la Sabana de Bogotá

### Papa

| Indicador | Valor | Año |
|---|---|---|
| Hectáreas sembradas en Cundinamarca | **40.000 ha** | 2024 |
| Rendimiento | 24,42 ton/ha | 2024 |
| Participación en producción nacional | 36% | 2023–24 |
| Volumen abastecido a mercados | 537.000 ton | 2023 |
| Costo de producción (Diacol Capiro) | $34,5 millones/ha | 2024 |
| Municipios principales | Villapinzón, Chocontá, Tausa, La Calera, Subachoque | — |

**Dosis de abono orgánico:** recomendaciones agronómicas genéricas de **4–10 ton/ha** (rangos citados: "no menor a 6 ton/ha", "4–8 ton/ha", "5–10 ton/ha"). **Confianza media-baja** — provienen de sitios generales, no de guía técnica verificada de Fedepapa.

**Dimensionamiento del mercado (cálculo propio, ilustrativo):** 40.000 ha × 6 ton/ha = **240.000 ton/año de demanda potencial teórica** de abono orgánico sólo en papa en Cundinamarca. Una planta de 20 ton/día de entrada produciría ~2.550 ton/año de compost — **el 1,06% de ese mercado teórico**. La restricción del negocio no es la demanda agregada sino el precio, la logística de distribución y la penetración comercial.

### Flores

- **7.504 hectáreas** sembradas en Cundinamarca (Proflora 2025), líder nacional.
- ⚠️ Discrepancia entre fuentes: "71% de la producción de flores de exportación" vs. "66% del total de hectáreas (~8.900 ha nacionales)". Probablemente miden cosas distintas (volumen exportado vs. área). Se deja sin resolver.
- Existe investigación de la Universidad Nacional sobre compostaje de residuos de clavel y girasol para reincorporarlos al mismo sistema productivo; referencias de industria a sustratos con hasta 30% de compost.
- **Toneladas/ha aplicadas comercialmente y precio de compra por floricultoras: NO ENCONTRADO.**

### Hortalizas

**NO ENCONTRADO** — no cubierto en esta ronda. Se recomienda búsqueda dedicada.

### Precio al que compran los agricultores

**NO ENCONTRADO** un dato verificado específico para la Sabana. ✅ **Acción recomendada:** cotizar directamente con 3–5 agricultores de papa en Villapinzón, Chocontá y Subachoque. Es la validación de mercado más importante pendiente.

---

# 7. COSTOS DE MONTAJE Y OPERACIÓN DE UNA PLANTA DE COMPOSTAJE

## 7.1 Tecnologías disponibles

| Tecnología | Descripción | Nota |
|---|---|---|
| **Pilas volteadas (windrow)** | Aireación por volteo mecánico periódico | Menor CAPEX, mayor área y tiempo |
| **Aireación forzada** | Sistemas colombianos reportados con capacidad de 0,5 a 50 ton/día | Intermedio |
| **Compostaje acelerado en reactor** | Sistema cerrado, control de proceso | Mayor CAPEX, menor área y olores |
| **Vermicompostaje** | *Eisenia foetida*; 4–30 °C, humedad 30–60%, pH 6–8; reduce volumen de biosólidos >90% | Producto de mayor valor (humus) |
| **Biodigestión anaerobia** | Produce biogás (CH₄+CO₂) + digestato; no produce compost directamente | Complementaria, no sustituta |

## 7.2 ⚠️ CAPEX: vacío de información crítico

**NO ENCONTRADO** ninguna cifra de CAPEX específica y verificable **en COP** para plantas de compostaje colombianas de 5, 20 o 50 ton/día. Las búsquedas devolvieron tesis académicas cuyo contenido numérico no pudo extraerse.

### Referencias disponibles (usar sólo como orden de magnitud)

| Referencia | Escala | CAPEX | Advertencia |
|---|---|---|---|
| Biodigestores domésticos, Colombia | Doméstica | $5–50 millones COP | No es planta de compostaje |
| Planta de compostaje, Ancud (Chile) | No especificada | >$1.500 millones **CLP** | Moneda y contexto distintos |
| Informe MMA Chile | 7.800 ton/año (~21 ton/día) | ~$1.714 millones **CLP** (obra civil $831,78M + equipos $125M + maquinaria $702,71M + infraestructura $54,75M) | Moneda y contexto distintos |

> **Estas cifras están en pesos chilenos y corresponden a un contexto regulatorio y de costos de construcción distinto.** No deben usarse para presupuestar en Bogotá sin conversión y ajuste. Se incluyen únicamente porque el brief solicitó referencias de escala.

## 7.3 Área requerida

**NO ENCONTRADO** una cifra colombiana verificada de m²/ton-día. Único dato tangencial: la normativa **mexicana** exige sistemas de captación de lixiviados y caseta de vigilancia para plantas mayores a 5 ton/día (referencia de diseño de otro país, no aplicable jurídicamente en Colombia).

> ✅ **Acción recomendada:** solicitar cotización a integradores de equipos de compostaje y visitar la planta Biocarbono (40 ton/día, con Licencia CAR) como referencia real y local de CAPEX y área. Es el benchmark más cercano disponible.

---

# 8. LOGÍSTICA: VEHÍCULOS, COMBUSTIBLE, SALARIOS Y BODEGA

## 8.1 Vehículos

### Combustión — nuevos

| Vehículo | Precio observado | Confianza |
|---|---|---|
| Chevrolet NHR | Rangos: hasta $85M / $85–100M / >$100M COP | Media-baja (clasificados, sin precio de lista oficial) |
| JAC 3 toneladas | Hasta $75M / $75–95M / >$95M COP | Media-baja |
| Foton Aumark furgón | Hasta $75M / $75–100M / >$100M COP | Media-baja |

### Combustión — usados (NHR, referencia de mercado 2026)

| Año / km | Ciudad | Precio |
|---|---|---|
| 2020, 81.093 km | Bogotá | $99.999.000 |
| 2020, 88.000 km | Envigado | $113.000.000 |
| 2020, 89.000 km | Medellín | $110.000.000 |
| 2022, 68.000 km | Medellín | $115.800.000 |

### ⭐ Alternativa eléctrica: BYD T35 (lanzado en Colombia en 2026)

| Atributo | Valor |
|---|---|
| Precio estimado | **$140.000.000 COP** |
| Capacidad de carga | 2.700 kg |
| Batería / autonomía | 63 kWh / hasta 270 km |
| Carga rápida | ~1 hora |
| Ahorro en costo por km | **70–80%** vs. turbo-diésel |

> **Relevancia estratégica alta.** Una flota eléctrica refuerza la narrativa ambiental de Recoevo, califica para el descuento del art. 255 ET y la exclusión de IVA, y reduce el costo variable en el rubro más pesado de la operación. La autonomía de 270 km es holgada para rutas urbanas en Usme.

### Leasing / renting

Existen ofertas de Bancolombia Leasing, Renting Colombia, ALD Automotive, Arval y Rentek (plazos 12–72 meses). **Canon mensual exacto: NO ENCONTRADO.** Requiere cotización directa.

## 8.2 Combustibles y costos operativos

| Concepto | Valor | Fecha |
|---|---|---|
| **ACPM (diésel), Bogotá** | **$11.616/galón** | sept. 2026 |
| ACPM, promedio nacional | $11.320/galón | sept. 2026 |
| **Gasolina corriente, Bogotá** | **$15.871–$15.891/galón** | abril 2026 |
| Gasolina, promedio nacional | $15.449/galón | abril 2026 |

*Contexto: el Gobierno congeló los precios de gasolina y ACPM en septiembre de 2026 tras el terremoto del 10 de agosto de 2026 y la presión del sector transportador.*

| Concepto | Valor |
|---|---|
| Rendimiento camión pequeño | **20–30 km/galón** (rango conservador recomendado; una fuente reporta 9,2 km/L ≈ 34,8 km/gal para NHR, considerada optimista) |
| Mantenimiento preventivo | 80–120 COP/km |
| Mantenimiento correctivo | 60–100 COP/km |
| **Costo variable total de operación** | **2.300–2.500 COP/km** |
| Seguro todo riesgo | ~$250.000/mes |
| Seguros + licencias (anual) | $3.300.000–$6.300.000/año |
| SOAT 2026, camiones de carga | Tarifa diferencial ≈ **50%** del valor estándar (Decreto 2312 de 2023, vigente desde 1-ene-2026). **Valor exacto en COP: NO ENCONTRADO** |
| Peajes Cundinamarca (Cat. I) | Andes $15.200; El Roble $12.400; Mondoñedo $9.900. Invías actualizó +5,10% desde el 16-ene-2026 |
| Peaje ALO Sur (Bosa) | $7.600 autos / $8.100 camiones **(proyectado — la vía está en construcción desde agosto de 2026, plazo 4 años; NO aplica aún)** |

## 8.3 ⭐ Salarios y costo laboral 2026

### Cifras base — verificadas por doble vía

| Concepto | Valor 2026 |
|---|---|
| **SMLMV** | **$1.750.905 COP** |
| **Auxilio de transporte** | **$249.095 COP** |
| **Ingreso mínimo total** | **$2.000.000 COP** |
| Incremento vs. 2025 ($1.423.500) | **+23,0%** |
| Norma | **Decreto Transitorio 0159 del 19 de febrero de 2026** |
| Tope para auxilio de transporte | 2 SMLMV = $3.501.810 |

> **Nota sobre la validación de esta cifra.** El incremento del 23% es atípico frente al patrón histórico colombiano (6–10% anual), por lo que se verificó de forma independiente. **Confirmación 1:** el Consejo de Estado suspendió provisionalmente el Decreto 1469 de 2025 por falta de sustento técnico, y el Decreto Transitorio 0159 de 2026 ratificó las mismas cifras con la justificación requerida — lo que explica la fecha inusual de febrero. **Confirmación 2 (decisiva):** el VIAT publicado por Área Limpia para agosto de 2026 es $14.007,24/ton y la fórmula del Decreto 2412 de 2018 es VIAT = SMMLV × 0,80%; despejando, SMMLV = $14.007,24 ÷ 0,008 = **$1.750.905**. **Coincidencia exacta.** La cifra queda confirmada por un acto administrativo independiente.

### Factor prestacional — componentes

| Componente | % | ¿Exonerable por art. 114-1 ET? |
|---|---|---|
| Salud (empleador) | 8,5% | ✅ Sí |
| Pensión (empleador) | 12% | ❌ No |
| **ARL Clase IV — recolección de residuos** | **4,350%** | ❌ No |
| ARL Clase V | 6,960% | ❌ No |
| Cesantías | 8,33% | ❌ No |
| Intereses a las cesantías | 1% mensual (12% anual sobre saldo) | ❌ No |
| Prima de servicios | 8,33% | ❌ No |
| Vacaciones | 4,17% | ❌ No |
| SENA | 2% | ✅ Sí |
| ICBF | 3% | ✅ Sí |
| Caja de Compensación Familiar | 4% | ❌ **Nunca exonerada** |

**Clasificación ARL:** el **Decreto 1607 de 2002** clasifica "la recolección, rellenos sanitarios y/o reciclaje de basuras" dentro de eliminación de desperdicios y saneamiento; la práctica de mercado la ubica en **Clase IV (riesgo alto)**. Actividades con mayor exposición podrían llegar a Clase V.

**Exoneración art. 114-1 ET:** aplica a sociedades y personas jurídicas **declarantes de renta**, para trabajadores que devenguen **menos de 10 SMMLV** ($17.509.050 en 2026). Exonera salud (8,5%) + SENA (2%) + ICBF (3%) = **13,5 puntos porcentuales**.

### Factor prestacional total (cálculo propio)

| Escenario | ARL Clase IV | ARL Clase V |
|---|---|---|
| **Empresa exonerada** (art. 114-1) | **42,18%** | 44,79% |
| **Empresa NO exonerada** | **55,68%** | 58,29% |

### ⭐ Costo mensual total por trabajador (cálculo propio)

*Base de seguridad social y parafiscales = salario; base de cesantías y prima = salario + auxilio de transporte.*

| Perfil | Empresa exonerada (ARL IV) | Empresa NO exonerada (ARL IV) |
|---|---|---|
| **Operario con salario mínimo** | **$2.764.188/mes** | $3.000.560/mes |
| **Conductor de camión** ($2.200.000 base) | **$3.398.595/mes** | $3.695.595/mes |

*Salario de mercado de conductor: $1.991.598 (promedio "chófer de camión", Computrabajo) a $2.211.218–$2.932.270 (conductor de camión pesado, WageIndicator).*

> **Implicación:** constituirse como sociedad declarante de renta ahorra **~$236.000/mes por operario** (~$2,8 millones/año). Con 10 operarios son ~$28 millones/año. Es una decisión de estructuración societaria con impacto material.

## 8.4 Bodega industrial

| Zona | Precio | Confianza |
|---|---|---|
| Occidente de Bogotá (Calle 80/Fontibón, Clase A+) | **$35.170/m²/mes** | Media-alta (Cushman & Wakefield MarketBeat Q1-2026) |
| Bosa (sur) | $33.000/m²/mes (bodega 820 m² = $27.060.000/mes) | Baja (clasificados) |
| Puente Aranda | ~$14.583/m²/mes + IVA (bodega 2.400 m² a $35.000.000) | Baja (clasificados) |
| Autopista Sur | $12.000–$35.000/m²/mes según clase | Baja |
| Mosquera / Funza / Tocancipá | "Bien por debajo" de $35.170 — **cifra exacta NO ENCONTRADA** | — |
| **Usme** | **NO ENCONTRADO** precio publicado por m² | — |

**Contexto de mercado:** en el 1T-2026 el producto Clase A+ disponible en Bogotá "fue absorbido en su totalidad" (absorción neta de 37.133 m²), acelerando la relocalización logística hacia Funza, Mosquera, Cota y Zipaquirá por escasez de suelo. **Para Recoevo esto implica presión al alza en arriendos** y refuerza el argumento de buscar suelo en el sur (Usme/Tunjuelito), donde la competencia por espacio logístico Clase A es menor y la cercanía a la fuente de residuos reduce el costo de transporte.

**Para el modelo financiero se recomienda $18.000–$25.000/m²/mes** para bodega funcional (no Clase A+) en el sur de Bogotá, con verificación por cotización directa.

---

# 9. AHORROS DEMOSTRADOS DE LA RECOLECCIÓN INTELIGENTE

## 9.1 Casos de proveedores comerciales

| Proveedor | Resultado documentado |
|---|---|
| **Ecube Labs (CleanCUBE)** | 144 CleanCUBE reemplazando 400+ contenedores tradicionales → **86% de reducción en costos de recolección** |
| **Ecube Labs — Melbourne** | 500 compactadores solares → **hasta 70% de mejora en eficiencia de recolección** |
| **Sensoneo** | **≥40% de reducción en costos de recolección**; **hasta 60% de reducción en emisiones de carbono** |
| **Compology** | Caso Global Trash Solutions: **USD 6,2 millones en ahorros** (≈USD 1.700/contenedor/año); **40–50% de reducción en gasto total de residuos**. Reducción de contaminación de residuos del 24% en el primer mes |
| **Enevo (One Collect)** | Monitoreo ultrasónico de volumen, temperatura y movimiento. **% de ahorro específico: NO ENCONTRADO** |
| **Bigbelly** | **NO ENCONTRADO** caso con cifra de ahorro |

## 9.2 Evidencia académica

- **Abdallah, Adghim, Maraqa & Aldahab (2019)**, *"Simulation and optimization of dynamic waste collection routes"*, *Waste Management & Research* (SAGE). Compara recolección dinámica basada en SIG con la práctica convencional en Sharjah (EAU); identifica la variabilidad de generación como el principal impulsor del beneficio.
- Cifras agregadas de literatura sobre optimización dinámica (⚠️ **confianza media-baja**, el motor de búsqueda no permitió atribuir con certeza cada cifra a su paper): reducción de distancia de 256,40 a 140,44 km (**−45,23%**) en contexto rural; **16,4%** de reducción en distancia, 16,3% en tiempo y 16,4% en combustible comparando rutas dinámicas vs. estáticas; piloto en Pakistán con **32%** de mejora en eficiencia de ruta y **29%** de reducción de combustible.

## 9.3 Lectura crítica para Recoevo

> **Escepticismo necesario.** Las cifras más espectaculares (86%, 70%) provienen de **material comercial de los propios proveedores** y comparan un escenario de contenedores públicos sobredimensionados y con recolección de frecuencia fija muy ineficiente. **No son transferibles directamente** a un esquema de recolección **domiciliaria puerta a puerta** en Usme, donde la densidad de puntos es alta y la ruta ya es relativamente eficiente.
>
> **Rango defendible para el modelo financiero: 15–30% de reducción en kilómetros y costo de recolección**, consistente con la evidencia académica revisada por pares (16,4%) y no con el material de marketing. Usar 20% como caso base y 40% como escenario optimista.

---

# 10. CASO COREA DEL SUR / SEÚL Y OTROS BENCHMARKS

## 10.1 ⭐ Corea del Sur — el caso más comparable a Recoevo

### Cronología

| Año | Hito |
|---|---|
| 1995 | Sistema de pago por volumen de residuos (*Volume-Based Waste Fee*), sin separación específica de orgánicos |
| 2005 | **Prohibición legal** de disponer restos de comida en vertederos |
| 2013 | Implementación nacional del *Weight-Based Food Waste Fee* (WBFWF) con contenedores **RFID** |

### Funcionamiento

Los ciudadanos depositan residuos de comida en máquinas con identificación por radiofrecuencia (RFID). La máquina **pesa automáticamente** y cobra según el peso, debitando de la tarjeta del usuario; alternativamente se compran bolsas autorizadas por volumen.

### Costos para el ciudadano

| Concepto | Valor |
|---|---|
| Tarifa de procesamiento en Seúl | **130 won/kg** |
| Bolsa de 3 litros | 300 won (~USD 0,20) |
| Bolsa de 20 litros | ~USD 1,50 |
| **Costo mensual promedio por hogar** | **< USD 5** |
| Multas | Hogares >USD 70; empresas >10 millones de won (~USD 7.000) |

### Resultados

| Indicador | Valor |
|---|---|
| **Tasa de reciclaje de residuos alimentarios (nacional)** | **2,6% (1996) → 97,5% (2022)** |
| Volumen procesado (2022) | 4,56 millones ton/año; 4,44 millones recicladas |
| Destino del material (2022) | Alimento animal 49%, abono 25%, biogás 14% |
| **Reducción del desperdicio de comida en Seúl (2013–2023)** | **−23,9%** (de 3.181 a 2.419 ton/día) |
| Reducción en complejos de apartamentos de Seúl | **51%** promedio en cinco bloques |
| Ahorro acumulado en 6 años | 47.000 ton de reducción; **USD 8,4 millones** en costos de recolección |
| Cobertura de contenedores RFID | 81,6% de residentes en apartamentos; 37,9% en todos los tipos de vivienda |

### ⭐ La lección central para Recoevo

> **El sistema coreano funciona con un incentivo NEGATIVO, no positivo.** El ciudadano **paga** por el peso de residuos que genera; no recibe una recompensa por separar. La reducción del 23,9% en Seúl y del 97,5% en reciclaje nacional se logró combinando **(i) prohibición legal** de disponer orgánicos en relleno, **(ii) cobro por peso** que hace visible el costo, **(iii) multas severas** y **(iv) infraestructura de recepción ubicua**.
>
> **Recoevo propone lo contrario:** un incentivo positivo de ~$8.643/mes para el estrato 1. Los datos coreanos sugieren que **el driver del comportamiento no es la magnitud del premio sino la obligatoriedad, la conveniencia y la retroalimentación inmediata** (la máquina pesa y muestra el costo en el acto).
>
> **Recomendación de diseño:** el contenedor inteligente de Recoevo debería dar **retroalimentación inmediata y visible** (peso depositado y puntos ganados en el momento), replicando el mecanismo psicológico coreano, y el programa debería apoyarse en la norma social del conjunto residencial más que en el valor monetario individual. En Corea, la cobertura llegó al 81,6% **en apartamentos** — donde el contenedor es compartido y el comportamiento es observable socialmente. **Priorizar conjuntos residenciales multifamiliares en Usme antes que vivienda unifamiliar dispersa.**

## 10.2 San Francisco

| Hito | Detalle |
|---|---|
| 1996 | Primer programa de compostaje de residuos de comida a gran escala en EE. UU. |
| 2009 | **Ordenanza de Reciclaje y Compostaje Obligatorio** — primera en EE. UU. en exigir universalmente la separación de orgánicos (3 contenedores) |
| Desde 2012 | **>80% de desvío de residuos** del relleno sanitario |
| Operación | >500 ton/día de compostables; procesamiento en 60 días en Blossom Valley Organics; venta a granjas, viñedos y huertos locales |

**Lección:** nuevamente, **obligatoriedad**, no incentivo económico. Y el modelo comercial de venta de compost a agricultura local es exactamente el que Recoevo propone — con la diferencia de que en San Francisco el servicio se financia vía tarifa obligatoria.

## 10.3 Milán

| Indicador | Valor |
|---|---|
| Piloto | Noviembre 2012 (un distrito) |
| Cobertura total de la ciudad | Junio 2014 |
| Participación de orgánicos | 36,7% (2012) → 50% (may-2014) → 100% de cobertura (jun-2014) |
| Frecuencia | 2 veces por semana, contenedores marrones y bolsas compostables (Novamont Mater-Bi) |
| **Resultado** | **>90 kg de orgánico por habitante/año** — más del doble que Viena (45 kg) y Múnich (31 kg) |

**Lección:** Milán es el mejor benchmark de **densidad urbana europea** y demuestra que la recolección puerta a puerta con bolsa compostable y alta frecuencia puede alcanzar las mayores tasas de captura del continente en menos de dos años.

## 10.4 Barcelona

Primeros contenedores inteligentes de recogida selectiva de orgánicos en Sant Antoni (Eixample), con identificador/tarjeta que registra la actividad de cada vecino. Sistema de **"pago por generación"**: transición progresiva de tasa plana a tasa individualizada, con bonificaciones para quienes más reciclan. **Resultados cuantitativos: NO ENCONTRADO.**

## 10.5 Casos latinoamericanos

- **Bogotá:** desde 2018, esquema de separación en dos fracciones con reconocimiento del rol de los recicladores de base.
- **Támesis (Antioquia):** recuperación de biogás, biomasa y fertilizante líquido de residuos orgánicos urbanos.
- **"Santander Circular y Bajo en Carbono":** ruta especial de orgánicos en el Área Metropolitana de Bucaramanga, dirigida a grandes generadores.
- **Buenos Aires:** compostaje comunitario para huertas.
- **Startup privada latinoamericana comparable a Recoevo** (recolección domiciliaria de orgánicos triturados con sensores IoT): **NO ENCONTRADO.** Puede leerse como espacio en blanco competitivo o como señal de que el modelo no ha sido validado en la región.

---

# 11. FINANCIACIÓN, TRIBUTACIÓN Y CARBONO

## 11.1 Beneficios tributarios ambientales

### ⭐ Artículo 255 ET — Descuento por inversiones ambientales (VIGENTE)

| Atributo | Detalle |
|---|---|
| **Beneficio** | **Descuento del 25% del valor de las inversiones** en control, conservación y mejoramiento del medio ambiente, aplicado **contra el impuesto de renta** (no es deducción) |
| Requisito | Acreditación **previa** por la autoridad ambiental (**ANLA**, art. 1.2.1.18.55 del Decreto 1625 de 2016) |
| **Exclusión clave** | **No aplica** a inversiones exigidas por mandato de autoridad ambiental para mitigar impactos de actividad sujeta a licencia (compensaciones obligatorias) |
| Trámite | Certificación **CDIR** vía ventanilla **VITAL**; **plazo máximo 3 meses** |
| Marco reglamentario | **Decreto 2205 de 2017** y **Resolución ANLA 509 de 2018** |
| Documentos | Descripción de la inversión, ubicación, estado de ejecución, beneficios ambientales cuantificados, Formato 5, certificación de no obligatoriedad |
| Modificación | **Ley 2099 de 2021** agregó tratamiento especial para gestión eficiente de energía (basta certificación UPME) |
| Estado 2026 | **VIGENTE.** No derogado ni modificado por la Ley 2277 de 2022 |
| ⚠️ Pendiente | **Límite porcentual respecto al impuesto a cargo: NO ENCONTRADO** para el art. 255 específicamente. El art. 259 ET regula límites generales a la sumatoria de descuentos. **Validar con asesor tributario antes de proyectar el beneficio** |

### Artículo 158-2 ET — DEROGADO

**Derogado por el artículo 376 de la Ley 1819 de 2016.** Permitía *deducir* de la renta la inversión ambiental con tope del 20% de la renta líquida. Fue reemplazado conceptualmente por el art. 255 (deducción → descuento). **No citarlo como beneficio vigente.**

### ⭐ Exclusión de IVA — arts. 424 núm. 7 y 428 ET (VIGENTE)

- La venta o importación de equipos, elementos y maquinaria (nacionales o importados) destinados a la construcción, instalación, montaje y operación de **sistemas de control y/o monitoreo ambiental** está **EXCLUIDA de IVA** (el impuesto no se causa).
- **Certificación:** la **ANLA** expide el **Certificado de Exclusión de IVA (CEI)**.
- **Equipos elegibles observados:** maquinaria de reciclaje y procesamiento de residuos, tratamiento de aguas residuales y emisiones, proyectos de reducción de carbono. **Cubriría trituradoras, volteadoras de pila y sensores de monitoreo de temperatura, humedad y lixiviados.**
- **Requisitos:** uso exclusivamente ambiental; para importados, demostrar ausencia de producción nacional equivalente.
- **Impacto directo:** un ahorro del 19% sobre el CAPEX de equipos y sobre los contenedores inteligentes.
- Contacto ANLA: Cra 13A # 34-72, Bogotá. Tel. +57 (601) 254 0111. licencias@anla.gov.co

### ❌ Obras por Impuestos (art. 800-1 ET) — NO APLICA

Aplica a **ZOMAC** (Decreto 1650 de 2017) y municipios **PDET** (Decreto 893 de 2017). **Bogotá D.C. no figura en ninguno de los dos listados**, por lo que un proyecto en Usme **no calificaría**. *(Confianza media-alta; el listado oficial completo no pudo re-verificarse en esta sesión.)*

### Artículo 257 ET — Donaciones a ESAL

- Donaciones a entidades del **Régimen Tributario Especial**: **descuento del 25%** del valor donado (no son deducibles).
- **Caso especial:** donaciones de alimentos y bienes de aseo a **bancos de alimentos** del RTE: descuento de **hasta 37%** (**Ley 2380 de 2024**).
- **Aplicación para Recoevo:** si se estructura una alianza con una ESAL certificada (por ejemplo, una fundación aliada o un banco de alimentos que recupere excedentes antes de que se conviertan en residuo), las empresas patrocinadoras podrían acceder a este descuento. **Es la vía tributaria más limpia para canalizar patrocinio corporativo.**

## 11.2 Bonos de carbono e impuesto al carbono

### Impuesto Nacional al Carbono

| Atributo | Valor |
|---|---|
| **Tarifa 2026** | **$29.070,49 COP/tCO2e** |
| Vigencia | Desde el **1 de febrero de 2026** |
| Norma | **Resolución DIAN 000003 del 30 de enero de 2026** |
| Ajuste aplicado | +6,10% (IPC 2025 de 5,10% + 1 punto) |
| Tope legal | 3 UVT = 3 × $52.374 = **$157.122** |
| Base legal | Arts. 221–223, **Ley 1819 de 2016**, modificados por la **Ley 2277 de 2022** |
| Tarifa 2025 (referencia) | ~$27.399,14/tCO2e *(confianza media)* |
| **UVT 2026** | **$52.374** (Resolución DIAN 000238 de 2025) |

> ⚠️ **Discrepancia detectada y no resuelta.** Un artículo de *La República* menciona una tarifa de **$42.609/ton** con implementación gradual (2026: 40%, 2027: 60%, 2028: 80%, 2029: 100%). **No coincide** con la Resolución DIAN 000003 de 2026, confirmada por múltiples fuentes. **No usar la cifra de $42.609 sin verificación directa en el texto de la resolución.**

### No causación por certificados de carbono neutralidad

| Atributo | Detalle |
|---|---|
| Base legal | **Decreto 926 de 2017** (vigente desde 1-jun-2017), **Decreto 446 de 2020**, **Resolución MinAmbiente 1447 de 2018** |
| **Límite** | **Hasta el 50% del valor del impuesto**, aun si la neutralización supera ese porcentaje |
| Procedimiento | Solicitud previa a la causación ante el productor/importador, con declaración de verificación y evidencia de cancelación voluntaria de reducciones a favor del solicitante |
| Vigencia 2026 | ✅ Operativo |

### RENARE

- Base legal: Resolución MinAmbiente 1447 de 2018. Cuatro fases: factibilidad → formulación → implementación → cierre.
- Iniciativas registrables: NAMA, proyectos MDL/CDM, **PDBC** (Programas de Desarrollo Bajo en Carbono), REDD+.
- **Reactivado gradualmente desde el 31 de julio de 2025**; primera etapa exige registro en el Servicio de Autenticación Digital del Estado.
- Costos de registro: **NO ENCONTRADO.**

### Precio de la tonelada de CO2e en el mercado voluntario

| Dato | Valor | Nota |
|---|---|---|
| Referencia histórica Colombia | ~$20.500 COP/tCO2e (≈ USD 5) | Artículos de 2022–2023 |
| Tendencia 2024 (Ecosystem Marketplace vía Fedemaderas) | Menor volumen desde 2018, pero valor de mercado 1,9× el de 2018. Créditos de **remoción 381% más caros** que los de **reducción** | — |
| **Precio puntual 2025–2026** | **NO ENCONTRADO** | Consultar "State of the Voluntary Carbon Market 2025" |

### Metodologías aplicables

- **CDM AMS-III.F — "Avoidance of methane emissions through composting"**: metodología de pequeña escala del MDL, **reconocida también en el catálogo de Verra**. Calcula la línea base con un modelo de decaimiento de primer orden (FOD) del metano que se habría generado en el relleno, restando las emisiones del proyecto (transporte, energía de volteo, CH₄/N₂O residuales). **Es la metodología directamente aplicable a Recoevo.**
- **Verra VM0025:** referenciada en el catálogo de Verra para el sector residuos; **contenido técnico NO ENCONTRADO en detalle.**
- **Gold Standard:** marco de "Waste Handling & Disposal" compatible con metodologías CDM aprobadas.

### ⭐ Factor de emisión: tCO2e evitadas por tonelada de orgánico desviado

**No existe un factor global fijo.** El IPCC (Guidelines 2006, Vol. 5) y la CDM AMS-III.F usan un modelo FOD que depende de parámetros específicos del relleno: **Lo** (potencial de generación de metano), **DOC** (carbono orgánico degradable), **DOCf**, **MCF** (factor de corrección según manejo del relleno) y **k** (tasa de decaimiento según clima).

| Dato | Valor | Fuente |
|---|---|---|
| Emisión **neta del proceso** de compostaje | **−0,20 MTCO2e/ton** (sumidero neto: −0,24 por almacenamiento de carbono en suelo, +0,04 por transporte y volteo) | EPA, "Composting in WARM" (2012) |
| Emisión del proceso de bioestabilización | 31,64 g CO2e/kg = **0,0316 tCO2e/ton** | Estudio Universidad de Chile |
| Emisión evitada por reciclaje vs. relleno *(análogo, NO compostaje)* | **2,83 tCO2e/ton** | EPA, calculadora de equivalencias |
| **Rango recomendado para el modelo** | **0,3 – 1,5 tCO2e por tonelada desviada** | Síntesis de CDM AMS-III.F, EPA WARM y estudios de ciclo de vida |

> **Para el modelo financiero:** usar **0,8 tCO2e/ton** como caso base, con sensibilidad de 0,3 a 1,5. **⚠️ Advertencia crítica:** el factor real depende de si el relleno de comparación **captura biogás**. Doña Juana **sí tiene proyecto de captura y aprovechamiento de biogás**, lo que **reduce significativamente** el crédito por metano evitado, porque parte de ese metano ya se estaba capturando en la línea base. **Esto puede recortar el factor a la mitad o menos.** Es indispensable revisar el documento de diseño del proyecto de biogás de Doña Juana antes de proyectar ingresos por carbono.

### Cuantificación de ingresos por carbono (cálculo propio)

| Escala | tCO2e/año (@0,8) | Ingreso @ $29.070/tCO2e | Viabilidad frente al costo de certificación |
|---|---|---|---|
| 1 ton/día (365 ton/año) | 292 | **$8,5 millones/año** | ❌ No cubre la certificación |
| 5 ton/día | 1.460 | $42,4 millones/año | ⚠️ Marginal |
| 20 ton/día | 5.840 | **$169,8 millones/año** | ✅ Viable |
| 50 ton/día | 14.600 | $424,4 millones/año | ✅ Claramente viable |

**Costo de certificación/verificación: NO ENCONTRADO con fuente primaria** (las páginas de tarifas de Verra y Gold Standard devolvieron 403/404). Referencia general de industria (sin verificación en esta investigación): **USD 15.000–50.000+** para validación + verificación de un proyecto pequeño, incluyendo auditor acreditado (VVB), tarifas de registro y emisión, y consultoría del documento de diseño.

> **Conclusión sobre carbono:** es una fuente de ingresos **secundaria y condicionada a escala**. Por debajo de 10–20 ton/día el costo de certificación se come el beneficio. **No incluirla en el caso base de un piloto.**

## 11.3 Fuentes de financiación

| Fuente | Monto | Detalle | Confianza |
|---|---|---|---|
| **SENA Fondo Emprender** | Hasta **$780.000.000** | Capital semilla; postulación en fondoemprender.com; apoyo técnico gratuito en 46+ Centros de Desarrollo Empresarial | Media-alta |
| SENA Fondo Emprender *(cifra alterna)* | Hasta 180 SMMLV (≈$315.162.900) | ⚠️ Inconsistente con la anterior — verificar en la fuente oficial | Media |
| **iNNpulsa — Ruta de Emprendimiento Verde** | Convocatoria activa | **Dirigida a residentes de Bogotá** con emprendimientos de impacto ambiental (economía circular, mercados de carbono), vía CEmprende | Media |
| iNNpulsa — subsidios generales | Hasta **USD 30.000** | Startups de alto impacto | Media |
| **Bancóldex — Línea Sostenible Adelante** | Redescuento hasta **$700.000.000** | Economía circular, bioeconomía, gestión de cambio climático en mipymes | Media |
| Bancóldex — bolsa verde anunciada | **$100.000 millones** | Bolsa nacional. Tasas de interés: **NO ENCONTRADO** | Media |
| **BID Lab — "Too Good to Waste"** | Hasta **USD 200.000** | **Estudios de pre-inversión para proyectos de gestión de residuos sólidos, incluyendo compostaje y digestión anaerobia.** Abierto a Colombia | **Alta — altamente pertinente** |
| **MinCiencias — Plan ACTeI 2025-2026** | Recursos del SGR | Convocatoria 47 "Agro por la vida" (valorización de residuos orgánicos, economía circular agroalimentaria); Convocatoria 48 (bioproductos) | Media |
| FONAM | Por demanda | **Decreto 4317 de 2004**. Convocatoria vigente: **NO ENCONTRADO** | Media |
| Findeter | — | **NO ENCONTRADO** línea específica aplicable | — |
| GEF / PNUD / GIZ / USAID | — | Operan vía agencias implementadoras y APC Colombia. **NO ENCONTRADO** convocatoria específica | — |
| Corporación Ventures / capital de impacto | — | **NO ENCONTRADO** (búsqueda no ejecutada por agotamiento del cupo) | — |

> **Priorización recomendada de financiación:**
> 1. **Comité IAT (Decreto 2412 de 2018)** — mayor bolsa, compostaje explícitamente elegible, ventanilla 30 de marzo
> 2. **BID Lab "Too Good to Waste"** — USD 200.000 para pre-inversión, encaja exactamente con la etapa del proyecto
> 3. **SENA Fondo Emprender** — hasta $780 millones de capital semilla
> 4. **iNNpulsa Ruta Verde** — específica para Bogotá
> 5. **Bancóldex Línea Sostenible** — deuda para CAPEX

## 11.4 RSE y patrocinio corporativo

⚠️ **Transparencia:** el cupo de búsquedas web se agotó antes de poder verificar casos concretos y montos con fuentes primarias. **No se incluyen cifras de patrocinio**, conforme a la regla de no inventar datos.

Lo que puede afirmarse como **punto de partida para investigación** (conocimiento general, no dato citable): empresas como Grupo Nutresa, Grupo Éxito, Bavaria, Postobón, Alpina, Ecopetrol, Cemex y Tetra Pak mantienen programas públicos de sostenibilidad y economía circular en Colombia. **No se identificó ningún proyecto de compostaje en Bogotá patrocinado por estas empresas ni cifra de patrocinio verificada.**

✅ **Acción recomendada:** revisar los informes de sostenibilidad (ESG) 2024–2025 de cada compañía, que suelen publicar montos de inversión social y ambiental por proyecto. Combinar con la estructura del art. 257 ET (descuento del 25% por donación a ESAL) como argumento de venta al patrocinador.

## 11.5 Responsabilidad Extendida del Productor (REP)

| Pregunta | Respuesta |
|---|---|
| ¿Qué cubre la REP en Colombia? | **Resolución 1407 de 2018** (envases y empaques), modificada por las Resoluciones 2184 de 2019 y 1342 de 2020. Además: llantas usadas (Res. 1326/2017), pilas y acumuladores (Res. 1297/2010), medicamentos vencidos, RAEE (Res. 1512/2010), luminarias y plaguicidas |
| **¿Aplica a residuos ORGÁNICOS?** | ❌ **NO.** No existe, a septiembre de 2026, un esquema REP para residuos orgánicos ni para desperdicio de alimentos en Colombia |
| ¿Hay obligaciones para productores de alimentos? | ❌ No por vía REP. La **Ley 2380 de 2024** se enfoca en incentivos tributarios a la **donación** de alimentos, no en responsabilidad extendida |
| ¿Norma o proyecto de ley nuevo 2025–2026? | **NO ENCONTRADO** |

> **Implicación estratégica:** Recoevo **no puede** apoyarse en una obligación legal de los productores de alimentos para asegurar demanda o financiación. Al mismo tiempo, **la ausencia de REP para orgánicos es una oportunidad de incidencia de largo plazo**: si Colombia llegara a adoptarla, Recoevo estaría posicionado como operador establecido.

---

# 12. ⭐ TABLA MAESTRA DE PARÁMETROS PARA EL MODELO FINANCIERO

| # | Parámetro | Valor | Unidad | Año | Fuente | URL | Confianza |
|---|---|---|---|---|---|---|---|
| **A. TARIFAS DE ALCANTARILLADO Y ACUEDUCTO (EAAB)** |
| 1 | Alcantarillado E1 — cargo fijo | 2.072,43 | COP/suscriptor/mes | 2026 | EAAB Acuerdo JD 255/2026 | https://www.acueducto.com.co/wps/wcm/connect/EAB2/0de38561-cb70-4a6f-aed0-9e57707b182c/Acuerdo+255+de+2026.pdf | Alta |
| 2 | Alcantarillado E1 — cargo básico | 1.521,38 | COP/m³ | 2026 | EAAB Acuerdo JD 255/2026 | ídem | Alta |
| 3 | Alcantarillado E2 — cargo fijo | 4.144,85 | COP/suscriptor/mes | 2026 | EAAB Acuerdo JD 255/2026 | ídem | Alta |
| 4 | Alcantarillado E2 — cargo básico | 3.042,76 | COP/m³ | 2026 | EAAB Acuerdo JD 255/2026 | ídem | Alta |
| 5 | Alcantarillado E3 — cargo fijo / básico | 5.871,88 / 4.310,57 | COP | 2026 | EAAB Acuerdo JD 255/2026 | ídem | Alta |
| 6 | Alcantarillado E4 (costo pleno) — cargo fijo / básico | 6.908,09 / 5.071,26 | COP | 2026 | EAAB Acuerdo JD 255/2026 | ídem | Alta |
| 7 | Alcantarillado — cargo no básico E1–E4 | 5.071,26 | COP/m³ | 2026 | EAAB Acuerdo JD 255/2026 | ídem | Alta |
| 8 | Acueducto E1 — cargo fijo / básico | 2.740,76 / 969,35 | COP | 2026 | EAAB Acuerdo JD 255/2026 | ídem | Alta |
| 9 | Acueducto E2 — cargo fijo / básico | 5.481,53 / 1.938,69 | COP | 2026 | EAAB Acuerdo JD 255/2026 | ídem | Alta |
| 10 | **Factura alcantarillado E1 @10 m³** | **17.286,23** | **COP/mes** | 2026 | Cálculo propio sobre tarifas EAAB | — | Alta |
| 11 | **Factura alcantarillado E2 @10 m³** | **34.572,45** | **COP/mes** | 2026 | Cálculo propio sobre tarifas EAAB | — | Alta |
| 12 | **Valor de un incentivo del 50%, E1** | **8.643,12** | **COP/mes** | 2026 | Cálculo propio | — | Alta |
| 13 | **Valor de un incentivo del 50%, E2** | **17.286,23** | **COP/mes** | 2026 | Cálculo propio | — | Alta |
| 14 | Consumo promedio facturado Bogotá | 10,01 | m³/usuario/mes | 2024 | EAAB / Bogotá.gov.co | https://bogota.gov.co/mi-ciudad/habitat/racionamiento-de-agua-acueducto-balance-del-consumo-durante-el-2024 | Alta |
| 15 | Consumo promedio facturado Bogotá | 10,78 | m³/usuario/mes | 2023 | EAAB | ídem | Alta |
| 16 | Rango de consumo básico (>2.000 msnm) | 0–11 | m³/mes | 2016– | Resolución CRA 750/2016 | https://normas.cra.gov.co/gestor/docs/resolucion_cra_0750_2016.htm | Alta |
| 17 | Rango complementario / suntuario | >11–22 / >22 | m³/mes | 2016– | Resolución CRA 750/2016 | ídem | Alta |
| 18 | Incremento del alcantarillado por CRA 1032 | +28,2 | % | 2026 | Cálculo propio (Ac. 244 vs. Ac. 255) | — | Alta |
| **B. SUBSIDIOS Y MÍNIMO VITAL** |
| 19 | Subsidio estrato 1 (acueducto, alcantarillado, aseo) | 70 | % | 2022–2026 | Acuerdo 830/2021, Concejo de Bogotá | https://www.alcaldiabogota.gov.co/sisjur//normas/Norma1.jsp?i=120507 | Alta |
| 20 | Subsidio estrato 2 | 40 | % | 2022–2026 | Acuerdo 830/2021 | ídem | Alta |
| 21 | Subsidio estrato 3 | 15 | % | 2022–2026 | Acuerdo 830/2021 | ídem | Alta |
| 22 | Aporte solidario E5 / E6 (alcantarillado, consumo) | +51 / +61 | % | 2022–2026 | Acuerdo 830/2021 | ídem | Alta |
| 23 | Aporte solidario E5 / E6 (alcantarillado, cargo fijo) | +149 / +246 | % | 2022–2026 | Acuerdo 830/2021 | ídem | Alta |
| 24 | **Vencimiento del Acuerdo 830 de 2021** | **31-dic-2026** | Fecha | 2026 | Acuerdo 830/2021, art. 5 | ídem | Alta |
| 25 | Mínimo vital de agua | 6 | m³/mes gratis (E1 y E2) | 2012– | Decreto Distrital 064/2012; EAAB | https://www.acueducto.com.co/wps/portal/EAB2/institucionales/la-empresa/mínimo%20vital | Alta |
| 26 | Mínimo vital — alcance | Sólo acueducto, **no** alcantarillado | — | 2026 | EAAB | ídem | Alta |
| **C. ASEO Y REMUNERACIÓN POR APROVECHAMIENTO** |
| 27 | **⭐ VBA — Valor Base de Aprovechamiento, Bogotá** | **160.135,81** | **COP/tonelada** | ago-2026 | Área Limpia D.C. S.A.S. E.S.P. (ASE 5) | https://arealimpia.com.co/wp-content/uploads/2026/08/TARIFAS_ASE5_2608.pdf | Alta |
| 28 | **⭐ VIAT — Incentivo al Aprovechamiento y Tratamiento** | **14.007,24** | **COP/tonelada** | ago-2026 | Área Limpia D.C. (= 0,80% SMMLV) | ídem | Alta |
| 29 | CRT — Costo de Recolección y Transporte | 140.874,29 | COP/tonelada | ago-2026 | Área Limpia D.C. | ídem | Alta |
| 30 | CDF — Costo de Disposición Final | 47.266,94 | COP/tonelada | ago-2026 | Área Limpia D.C. | ídem | Alta |
| 31 | CTL — Costo de Tratamiento de Lixiviados | 26.336,85 | COP/tonelada | ago-2026 | Área Limpia D.C. | ídem | Alta |
| 32 | CCS no aprovechables / aprovechamiento | 3.292,07 / 987,64 | COP/suscriptor | ago-2026 | Área Limpia D.C. | ídem | Alta |
| 33 | CBLS — Barrido y Limpieza | 16.352,36 | COP/suscriptor | ago-2026 | Área Limpia D.C. | ídem | Alta |
| 34 | CLUS — Limpieza Urbana | 3.220,37 | COP/suscriptor | ago-2026 | Área Limpia D.C. | ídem | Alta |
| 35 | **Tarifa de aseo E1** | **13.462** | COP/mes | ago-2026 | Área Limpia D.C. (ASE 5) | ídem | Alta (ASE 5; Usme puede variar) |
| 36 | **Tarifa de aseo E2** | **27.446** | COP/mes | ago-2026 | Área Limpia D.C. (ASE 5) | ídem | Alta (ASE 5; Usme puede variar) |
| 37 | Tarifa de aseo E3 / E4 / E5 / E6 | 39.306 / 47.486 / 75.335 / 85.931 | COP/mes | ago-2026 | Área Limpia D.C. | ídem | Alta |
| 38 | Fórmula del VBA | VBA = (CRTp + CDFp)(1 − DINC) | — | 2015 | Res. CRA 720/2015, art. 34 | https://www.promoambientaldistrito.com/wp-content/uploads/2018/09/Resolucion-CRA-720-de-2015.pdf | Alta |
| 39 | Descuento al usuario por separación en la fuente | 4 | % sobre la tarifa de aprovechamiento | 2020 | Guía MinVivienda para el cálculo de la tarifa de aprovechamiento | https://www.minvivienda.gov.co/sites/default/files/documentos/guia-para-el-calculo-de-la-tarifa-de-aprovechamiento.pdf | Alta |
| 40 | Umbral de rechazo para acceder al descuento | <20 | % | 2020 | Guía MinVivienda | ídem | Alta |
| 41 | Reserva para Plan de Fortalecimiento Empresarial | hasta 15 (progresiva: 3/7/11/15) | % del VBA | 2017 | Res. CRA 788/2017, art. 2 | ídem | Alta |
| 42 | Porcentaje de recaudo real (ejemplo oficial) | 95 | % | 2020 | Guía MinVivienda | ídem | Media |
| 43 | Fórmula del VIAT | VIAT = SMMLV × 0,80% | — | 2018 | Decreto 2412/2018, art. 2.3.2.7.3 | https://normas.cra.gov.co/gestor/docs/decreto_2412_2018.htm | Alta |
| 44 | **Tamaño estimado del fondo IAT de Bogotá** | **≈34.600** | millones COP/año | 2026 | Cálculo propio (6.769 ton/día × 365 × $14.007,24) | — | Media |
| 45 | Fecha límite de radicación de proyectos al Comité IAT | **30 de marzo** | Anual | 2018– | Decreto 2412/2018 | ídem | Alta |
| 46 | Prestadores de aprovechamiento registrados en Bogotá | **488** | Organizaciones | abr-2026 | Listado OR Área Limpia | https://arealimpia.com.co/wp-content/uploads/2026/05/Listado_OR_Area_Limpia_30Abr2026.pdf | Alta |
| 47 | Residuos que ingresan a Doña Juana | 6.769 | ton/día | 1T-2026 | Concejo de Bogotá | https://concejodebogota.gov.co/relleno-sanitario-dona-juana-el-costo-social-y-ambiental-de-un-sistema/cbogota/2024-12-12/113750.php | Media-alta |
| 48 | Participación de orgánicos en lo dispuesto en Doña Juana | 50 | % | 2024–27 | PGIRS UAESP | https://www.uaesp.gov.co/sites/default/files/planeacion/pgirs2025/DTS_PGIRS_2024.pdf | Alta |
| **D. MERCADO DEL COMPOST** |
| 49 | Precio compost, bulto 50 kg | 33.915–39.900 | COP/bulto | 2026 | Tumatera.co | https://tumatera.co/products/bulto-compost-x-50-kg | Alta |
| 50 | Precio humus de lombriz granulado, bulto 40 kg | 84.900 | COP/bulto | 2026 | Homecenter Colombia | https://www.homecenter.com.co | Alta |
| 51 | Precio humus de lombriz, tonelada (volumen) | 395.000 | COP/ton | 2026 | Proveedor Bogotá vía Infoagro | https://www.infoagro.com/compraventa/oferta.asp?id=18090 | Media |
| 52 | **Precio gallinaza, venta directa a granel** | **130.000–260.000** | **COP/ton** | 2025 | QuiMiNet (clasificados) | https://www.quiminet.com/productos/gallinaza-compostada-152774826561/precios.htm | Baja |
| 53 | **Precio de compost recomendado para el modelo** | **250.000** (rango 130.000–400.000) | COP/ton | 2026 | Síntesis propia del canal agrícola a granel | — | Media |
| 54 | **Rendimiento del compostaje (caso base)** | **35** (rango 30–50) | % del peso fresco | — | Síntesis de fuentes en conflicto (§6.4) | https://www.compostandociencia.com/2021/12/cuanta-masa-pierde-un-compost/ | Media |
| 55 | Reducción de masa en compostaje | 50–70 | % | — | Vida Sostenible / Tierra.org | https://www.vidasostenible.org/hacer-compostaje-podria-reducir-hasta-un-50-de-nuestras-basuras/ | Media |
| 56 | Tiempo de trámite del registro ICA | 2 | días hábiles | 2026 | ICA | https://www.ica.gov.co/oferta-institucional/tramites/agricola/fertilizantes/tramite-numero-uno.aspx | Media |
| 57 | Costo del registro ICA | **NO ENCONTRADO** | COP | 2026 | Res. ICA 34487/2025 (anexo no accesible) | https://www.ica.gov.co/noticias/ica-actualiza-tarifas-servicios-sector-agro | — |
| 58 | Norma de registro de fertilizantes | Resolución ICA 150 de 2003 | — | 2003 | SUIN Juriscol | https://www.suin-juriscol.gov.co/viewDocument.asp?ruta=Resolucion/30042205 | Alta |
| 59 | Norma técnica de calidad del abono orgánico | NTC 5167, 2ª ed. (23-mar-2011) | — | 2011 | ICONTEC | https://tramites1.suit.gov.co/registro-web/suit_descargar_archivo?A=43051 | Alta (existencia); cifras NO ENCONTRADAS |
| 60 | Hectáreas de papa en Cundinamarca | 40.000 | ha | 2024 | Agronet | https://agronet.gov.co/noticias/cundinamarca-boyaca-narino-y-antioquia-representan-90-de-la-produccion-de-papa | Alta |
| 61 | Dosis de abono orgánico en papa | 4–10 | ton/ha | — | Recomendaciones agronómicas genéricas | — | Media-baja |
| 62 | Hectáreas de flores en Cundinamarca | 7.504 | ha | 2025 | Gobernación de Cundinamarca (Proflora 2025) | https://www.cundinamarca.gov.co/noticias/cundinamarca-florece-en-proflora-2025-corazon-de-la-floricultura-colombiana | Alta |
| 63 | Capacidad de la planta Biocarbono (competidor) | 40 | ton/día | 2026 | ROB / Biocarbono | https://residuosorganicosbogota.com | Media |
| 64 | CAPEX planta de compostaje en Colombia | **NO ENCONTRADO** | COP | — | — | — | — |
| 65 | Área requerida por escala | **NO ENCONTRADO** | m²/ton-día | — | — | — | — |
| **E. LOGÍSTICA Y COSTOS OPERATIVOS** |
| 66 | **SMLMV** | **1.750.905** | COP/mes | 2026 | Decreto Transitorio 0159 del 19-feb-2026 (verificado vía VIAT) | https://colombiamove.com/blog/salario-minimo-colombia-2026-guia/ | Alta (doble verificación) |
| 67 | **Auxilio de transporte** | **249.095** | COP/mes | 2026 | Decreto 0159/2026 | ídem | Alta |
| 68 | Ingreso mínimo total | 2.000.000 | COP/mes | 2026 | Decreto 0159/2026 | ídem | Alta |
| 69 | **ARL Clase IV (recolección de residuos)** | **4,350** | % del IBC | 2026 | Decreto 1607/2002; Coriesgos | https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/DIJ/Decreto-1607-de-2002.pdf | Alta |
| 70 | ARL Clase V | 6,960 | % del IBC | 2026 | Coriesgos | https://coriesgos.com/blog/arl-independientes-colombia-2026 | Alta |
| 71 | **Factor prestacional (empresa exonerada, ARL IV)** | **42,18** | % | 2026 | Cálculo propio | — | Media |
| 72 | **Factor prestacional (NO exonerada, ARL IV)** | **55,68** | % | 2026 | Cálculo propio | — | Media |
| 73 | **Costo mensual total de un operario (exonerada)** | **2.764.188** | COP/mes | 2026 | Cálculo propio | — | Media |
| 74 | **Costo mensual total de un conductor (exonerada)** | **3.398.595** | COP/mes | 2026 | Cálculo propio | — | Media |
| 75 | Exoneración art. 114-1 ET | 13,5 (salud 8,5 + SENA 2 + ICBF 3) | puntos % | 2026 | Estatuto Tributario art. 114-1 | https://estatuto.co/114-1 | Alta |
| 76 | Umbral de la exoneración art. 114-1 | <10 SMMLV = 17.509.050 | COP/mes | 2026 | Art. 114-1 ET | ídem | Alta |
| 77 | **Precio del diésel (ACPM), Bogotá** | **11.616** | COP/galón | sep-2026 | Zonar.co (Minhacienda/CREG) | https://zonar.com.co/blog/precio-del-acpm-en-colombia-septiembre-2026/ | Media |
| 78 | Precio de la gasolina corriente, Bogotá | 15.871–15.891 | COP/galón | abr-2026 | Infobae | https://www.infobae.com/colombia/2026/04/01/el-precio-de-la-gasolina-en-colombia-se-dispara-tras-incremento-de-375-el-galon-aumenta-su-valor-desde-el-1-de-abril/ | Alta |
| 79 | **Costo variable total de operación de camión** | **2.300–2.500** | COP/km | 2026 | Logitools.co | https://logitools.co/guias/costo-operativo-camion-colombia | Media |
| 80 | Mantenimiento preventivo + correctivo | 140–220 | COP/km | 2026 | Logitools.co | ídem | Media |
| 81 | Rendimiento de camión pequeño (recomendado) | 20–30 | km/galón | 2026 | Síntesis propia (fuentes en conflicto) | — | Baja-media |
| 82 | Precio de camión NHR usado (2020–2022) | 99.999.000–115.800.000 | COP | 2026 | Mercado Libre Colombia | https://vehiculos.mercadolibre.com.co/camiones/usados/camiones-usados-nhr_ITEM*CONDITION_2230581 | Media |
| 83 | **Precio de camión eléctrico BYD T35** | **140.000.000** | COP | 2026 | Valora Analitik | https://www.valoraanalitik.com/camion-electrico-llega-a-colombia-carga-en-una-hora-y-ahorra-costos/ | Alta |
| 84 | Capacidad de carga BYD T35 | 2.700 | kg | 2026 | Valora Analitik / El Carro Colombiano | ídem | Alta |
| 85 | Ahorro en costo/km del eléctrico vs. diésel | 70–80 | % | 2026 | Semana | https://www.semana.com/vehiculos/articulo/byd-presento-camiones-electricos-para-carga-y-proyecta-vender-200-unidades-en-colombia-durante-2026/202600/ | Media |
| 86 | Seguro todo riesgo de camión | ~250.000 | COP/mes | 2026 | Comparabien | https://comparabien.com.co/blog-consejos/cuanto-vale-seguro-todo-riesgo-vehiculo-colombia | Media |
| 87 | SOAT camiones de carga | ≈50% del valor estándar | % | 2026 | Decreto 2312/2023; Fasecolda | https://www.fasecolda.com/wp-content/uploads/Tarifas-SOAT-2026-referencia.pdf | Baja (valor exacto NO ENCONTRADO) |
| 88 | Arriendo de bodega, occidente de Bogotá (Clase A+) | 35.170 | COP/m²/mes | 1T-2026 | Cushman & Wakefield vía Semana | https://www.semana.com/economia/capsulas/articulo/la-sabana-de-bogota-concentra-la-expansion-industrial-ante-la-escasez-de-suelo-en-la-capital/202614/ | Media-alta |
| 89 | **Arriendo de bodega, sur de Bogotá (recomendado)** | **18.000–25.000** | COP/m²/mes | 2026 | Síntesis propia de clasificados | — | Baja |
| 90 | **Ahorro por optimización de rutas (recomendado)** | **20** (rango 15–40) | % | 2026 | Síntesis crítica §9.3 | https://journals.sagepub.com/doi/full/10.1177/0734242X19833152 | Media |
| **F. FINANCIACIÓN, TRIBUTACIÓN Y CARBONO** |
| 91 | **Descuento por inversión ambiental (art. 255 ET)** | **25** | % de la inversión | 2026 | Estatuto Tributario art. 255 | https://estatuto.co/255 | Alta |
| 92 | Plazo del trámite CDIR ante ANLA | 3 | meses (máximo) | 2026 | ANLA | https://www.anla.gov.co/01_anla/allcategories-es-es/224-tramites-y-servicios/tramites/certificaciones/descuento-impuesto | Alta |
| 93 | Exclusión de IVA para equipos ambientales | 19 (ahorro efectivo) | % del valor del equipo | 2026 | Arts. 424 núm. 7 y 428 ET; ANLA | https://www.anla.gov.co/01_anla/certificado-exclusion-iva-que-es-el-cei | Alta |
| 94 | Descuento por donación a ESAL (art. 257 ET) | 25 | % del valor donado | 2026 | Estatuto Tributario art. 257 | https://estatuto.co/257 | Alta |
| 95 | Descuento por donación a bancos de alimentos | hasta 37 | % del valor donado | 2024– | Ley 2380 de 2024 | https://www.crowe.com/co/news/nuevo_descuento_tributario_por_donaciones_segun_ley_2380_de_2024 | Media-alta |
| 96 | Art. 158-2 ET | **DEROGADO** (art. 376, Ley 1819/2016) | — | 2016 | Estatuto Tributario | https://estatuto.co/158-2 | Alta |
| 97 | **Impuesto nacional al carbono** | **29.070,49** | COP/tCO2e | 2026 | Resolución DIAN 000003 del 30-ene-2026 | https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0003_2026.htm | Alta |
| 98 | **UVT** | **52.374** | COP | 2026 | Resolución DIAN 000238/2025 | https://incp.org.co/publicaciones/infoincp-publicaciones/impuestos/2025/12/dian-fijo-en-52-374-en-valor-de-la-uvt-para-el-ano-gravable-2026/ | Alta |
| 99 | Tope legal del impuesto al carbono | 157.122 (3 UVT) | COP/tCO2e | 2026 | INCP | ídem | Alta |
| 100 | Límite de no causación por carbono neutralidad | 50 | % del impuesto | 2017– | Decreto 926/2017 | https://www.minambiente.gov.co/wp-content/uploads/2022/01/Decreto_926_de_2017_Actualizacion.pdf | Alta |
| 101 | **Factor de emisión evitada (caso base)** | **0,8** (rango 0,3–1,5) | tCO2e/ton de orgánico desviado | — | Síntesis CDM AMS-III.F / EPA WARM | https://verra.org/methodologies/avoidance-of-methane-emissions-through-composting/ | Media |
| 102 | Emisión neta del proceso de compostaje | −0,20 | MTCO2e/ton | 2012 | EPA "Composting in WARM" | https://archive.epa.gov/epawaste/conserve/tools/warm/pdfs/cmpstng_ovrview.pdf | Alta |
| 103 | Precio del CO2e en el mercado voluntario colombiano | ~20.500 (dato histórico) | COP/tCO2e | 2022–23 | La República | https://www.larepublica.co/especiales/bonos-sostenibles/con-bonos-de-20-500-es-posible-combatir-las-emisiones-de-carbono-de-las-empresas-3722112 | Baja (desactualizado) |
| 104 | Costo de certificación de carbono | 15.000–50.000 (referencia de industria) | USD | — | Sin fuente primaria — **NO ENCONTRADO** | — | Baja |
| 105 | **SENA Fondo Emprender** | hasta 780.000.000 | COP/proyecto | 2025 | Infobae | https://www.infobae.com/colombia/2025/03/26/fondo-emprender-del-sena-asi-puede-postularse-y-acceder-a-financiamientos-de-hasta-780-millones-de-pesos/ | Media-alta |
| 106 | **BID Lab "Too Good to Waste"** | hasta 200.000 | USD (pre-inversión) | 2026 | BID | https://www.iadb.org/es/blog/agua-saneamiento-y-residuos-solidos/convocatoria-de-propuestas-too-good-waste-para-proyectos-de-gestion-residuos-solidos | Alta |
| 107 | Bancóldex Línea Sostenible Adelante | hasta 700.000.000 | COP (redescuento) | 2026 | Bancóldex | https://www.bancoldex.com/credito-traves-de-aliados/lineas-de-credito/linea-sostenible-adelante | Media |
| 108 | iNNpulsa — subsidio general a startups | hasta 30.000 | USD | 2026 | ecosistemastartup.com | https://ecosistemastartup.com/convocatorias/innpulsa-colombia-emprendimiento-de-alto-impacto-2026/ | Media |
| 109 | Obras por Impuestos en Bogotá | **NO APLICA** (no es ZOMAC ni PDET) | — | 2026 | Decretos 1650/2017 y 893/2017 | https://www.fiducentral.com/obras-por-impuestos/normativa-oxi | Media-alta |
| 110 | REP aplicada a residuos orgánicos | **NO EXISTE** en Colombia | — | 2026 | Res. 1407/2018 y concordantes | — | Alta |
| **G. BENCHMARKS INTERNACIONALES** |
| 111 | Tasa de reciclaje de residuos de comida, Corea del Sur | 97,5 | % | 2022 | BBC Mundo vía El Mostrador | https://www.elmostrador.cl/agenda-pais/agenda-sustentable/2025/03/31/paga-por-tus-desperdicios-como-corea-del-sur-logra-reciclar-el-97-de-sus-residuos-de-alimentos/ | Alta |
| 112 | Tarifa RFID de residuos de comida, Seúl | 130 | won/kg | 2013– | Korea Herald | https://www.koreaherald.com/article/10638389 | Alta |
| 113 | Reducción del desperdicio de comida en Seúl (2013–2023) | −23,9 | % | 2026 | Korea Herald | ídem | Alta |
| 114 | Ahorro en costos de recolección, Seúl (6 años) | 8,4 | millones USD | 2026 | Korea Herald | ídem | Alta |
| 115 | Desvío de residuos del relleno, San Francisco | >80 | % | desde 2012 | NRDC | https://www.nrdc.org/resources/food-rescue-san-francisco-composting | Alta |
| 116 | Recolección de orgánicos per cápita, Milán | >90 | kg/habitante/año | 2012–14 | POCACITO | https://pocacito.eu/sites/default/files/FoodWasteRecycling_Milan.pdf | Media |
| 117 | Ahorro en recolección — Sensoneo | ≥40 | % | 2026 | IoT For All | https://www.iotforall.com/smart-waste-management | Media |
| 118 | Reducción del gasto en residuos — Compology | 40–50 | % | 2026 | RecyclingProductNews | https://www.recyclingproductnews.com/article/36734/compology-metering-technology-to-save-millions-in-waste-management-costs-for-fast-food-giants | Media |

> **Total: 118 parámetros** (se solicitaban mínimo 40).

---

# 13. BIBLIOGRAFÍA (APA 7)

**Normativa colombiana**

Comisión de Regulación de Agua Potable y Saneamiento Básico. (2015). *Resolución CRA 720 de 2015, por la cual se establece el régimen de regulación tarifaria al que deben someterse las personas prestadoras del servicio público de aseo que atiendan en municipios de más de 5.000 suscriptores en áreas urbanas*. https://www.promoambientaldistrito.com/wp-content/uploads/2018/09/Resolucion-CRA-720-de-2015.pdf (Consultado el 10 de septiembre de 2026)

Comisión de Regulación de Agua Potable y Saneamiento Básico. (2016). *Resolución CRA 750 de 2016, por la cual se modifica el rango de consumo básico*. https://normas.cra.gov.co/gestor/docs/resolucion_cra_0750_2016.htm (Consultado el 10 de septiembre de 2026)

Comisión de Regulación de Agua Potable y Saneamiento Básico. (2017). *Resolución CRA 788 de 2017*. [Citada en la Guía MinVivienda] (Consultado el 10 de septiembre de 2026)

Comisión de Regulación de Agua Potable y Saneamiento Básico. (2018). *Resolución CRA 853 de 2018, régimen tarifario para prestadores en municipios de hasta 5.000 suscriptores y esquemas diferenciados*. https://normas.cra.gov.co/gestor/docs/resolucion_cra_0853_2018.htm (Consultado el 10 de septiembre de 2026)

Comisión de Regulación de Agua Potable y Saneamiento Básico. (2019). *Concepto CRA 76081 de 2019*. https://normas.cra.gov.co/gestor/docs/concepto_cra_0076081_2019.htm (Consultado el 10 de septiembre de 2026)

Comisión de Regulación de Agua Potable y Saneamiento Básico. (2020). *Concepto CRA 85281 de 2020*. https://normas.cra.gov.co/gestor/docs/concepto_cra_0085281_2020.htm (Consultado el 10 de septiembre de 2026)

Comisión de Regulación de Agua Potable y Saneamiento Básico. (2026). *Resolución CRA 1032 de 2026, marco tarifario de acueducto y alcantarillado para prestadores de más de 5.000 suscriptores*. https://www.cra.gov.co/sites/default/files/documents/2026-03/Resoluci%C3%B3n%201032%20de%202026%20Marco%20tarifario%20de%20Acueducto%20y%20Alcantarillado%20mas%20de%205000%20suscriptores.pdf (Consultado el 10 de septiembre de 2026)

Concejo de Bogotá D.C. (2021). *Acuerdo 830 de 2021, por el cual se establecen los factores de subsidio y de aporte solidario para los servicios de acueducto, alcantarillado y aseo*. https://www.alcaldiabogota.gov.co/sisjur//normas/Norma1.jsp?i=120507 (Consultado el 10 de septiembre de 2026)

Congreso de la República de Colombia. (1994). *Ley 142 de 1994, por la cual se establece el régimen de los servicios públicos domiciliarios*. https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=2752 (Consultado el 10 de septiembre de 2026)

Congreso de la República de Colombia. (2016). *Ley 1819 de 2016, reforma tributaria estructural* (arts. 221-223 y 376). (Consultado el 10 de septiembre de 2026)

Congreso de la República de Colombia. (2022). *Ley 2277 de 2022, reforma tributaria para la igualdad y la justicia social*. https://www.dian.gov.co/impuestos/sociedades/Regimen-Tributario-Especial-RTE/Herramientas/Documents/Ley-2277-2022-Reforma-Tributaria.pdf (Consultado el 10 de septiembre de 2026)

Dirección de Impuestos y Aduanas Nacionales. (2026). *Resolución DIAN 000003 del 30 de enero de 2026* [tarifas del impuesto al carbono]. https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0003_2026.htm (Consultado el 10 de septiembre de 2026)

Ministerio de Ambiente y Desarrollo Sostenible. (2017). *Decreto 926 de 2017, no causación del impuesto al carbono por certificación de carbono neutralidad*. https://www.minambiente.gov.co/wp-content/uploads/2022/01/Decreto_926_de_2017_Actualizacion.pdf (Consultado el 10 de septiembre de 2026)

Ministerio de Salud y Protección Social. (2002). *Decreto 1607 de 2002, tabla de clasificación de actividades económicas para el Sistema General de Riesgos Profesionales*. https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/DIJ/Decreto-1607-de-2002.pdf (Consultado el 10 de septiembre de 2026)

Ministerio de Vivienda, Ciudad y Territorio. (2016). *Decreto 596 de 2016, esquema operativo de la actividad de aprovechamiento y formalización progresiva de los recicladores de oficio*. https://normas.cra.gov.co/gestor/docs/decreto_0596_2016.htm (Consultado el 10 de septiembre de 2026)

Ministerio de Vivienda, Ciudad y Territorio. (2018). *Decreto 2412 de 2018, Incentivo al Aprovechamiento y Tratamiento de Residuos Sólidos (IAT)*. https://normas.cra.gov.co/gestor/docs/decreto_2412_2018.htm (Consultado el 10 de septiembre de 2026)

Presidencia de la República de Colombia. (2026). *Decreto Transitorio 0159 del 19 de febrero de 2026* [salario mínimo legal mensual vigente 2026]. (Consultado el 10 de septiembre de 2026)

Superintendencia de Servicios Públicos Domiciliarios. (2008). *Concepto SSPD 458 de 2008* [sobre descuentos y exoneraciones en el pago de servicios públicos]. https://normas.cra.gov.co/gestor/docs/concepto_superservicios_0000458_2008.htm (Consultado el 10 de septiembre de 2026)

**Documentos tarifarios y técnicos**

Área Limpia D.C. S.A.S. E.S.P. (2026). *Costos de referencia y tarifas del servicio de aseo — agosto de 2026 (ASE 5, Bogotá D.C.)*. https://arealimpia.com.co/wp-content/uploads/2026/08/TARIFAS_ASE5_2608.pdf (Consultado el 10 de septiembre de 2026)

Área Limpia D.C. S.A.S. E.S.P. (2026). *Listado de organizaciones de recicladores prestadoras de la actividad de aprovechamiento — corte 30 de abril de 2026*. https://arealimpia.com.co/wp-content/uploads/2026/05/Listado_OR_Area_Limpia_30Abr2026.pdf (Consultado el 10 de septiembre de 2026)

Empresa de Acueducto y Alcantarillado de Bogotá E.S.P. (2026). *Acuerdo de Junta Directiva No. 244 del 11 de marzo de 2026 — Tarifas para la prestación de los servicios de acueducto y alcantarillado*. https://www.acueducto.com.co/wps/wcm/connect/EAB2/c2ca063c-0f4a-4d72-b400-239b084f0eeb/Tarifas+EAAB+Acuerdo+JD+No.+244+de+2026.pdf (Consultado el 10 de septiembre de 2026)

Empresa de Acueducto y Alcantarillado de Bogotá E.S.P. (2026). *Acuerdo de Junta Directiva No. 255 del 27 de mayo de 2026 y Estudio de costos y tarifas bajo la Resolución CRA 1032 de 2026*. Registro Distrital No. 8591. https://www.acueducto.com.co/wps/wcm/connect/EAB2/0de38561-cb70-4a6f-aed0-9e57707b182c/Acuerdo+255+de+2026.pdf (Consultado el 10 de septiembre de 2026)

Empresa de Acueducto y Alcantarillado de Bogotá E.S.P. (s.f.). *Mínimo Vital*. https://www.acueducto.com.co/wps/portal/EAB2/institucionales/la-empresa/mínimo%20vital (Consultado el 10 de septiembre de 2026)

Ministerio de Vivienda, Ciudad y Territorio y Alianza Nacional para el Reciclaje Inclusivo. (2020). *Guía para el cálculo de la tarifa de aprovechamiento y tips de comercialización de materiales*. https://www.minvivienda.gov.co/sites/default/files/documentos/guia-para-el-calculo-de-la-tarifa-de-aprovechamiento.pdf (Consultado el 10 de septiembre de 2026)

Unidad Administrativa Especial de Servicios Públicos. (2024). *Documento técnico de soporte del PGIRS 2024-2027 de Bogotá D.C.* https://www.uaesp.gov.co/sites/default/files/planeacion/pgirs2025/DTS_PGIRS_2024.pdf (Consultado el 10 de septiembre de 2026)

**Fuentes de mercado, costos y benchmarks**

Abdallah, M., Adghim, M., Maraqa, M., & Aldahab, E. (2019). Simulation and optimization of dynamic waste collection routes. *Waste Management & Research*, 37(8). https://journals.sagepub.com/doi/full/10.1177/0734242X19833152 (Consultado el 10 de septiembre de 2026)

Agencia de Noticias Agronet. (2024). *Cundinamarca, Boyacá, Nariño y Antioquia representan 90% de la producción de papa*. https://agronet.gov.co/noticias/cundinamarca-boyaca-narino-y-antioquia-representan-90-de-la-produccion-de-papa (Consultado el 10 de septiembre de 2026)

Alcaldía Mayor de Bogotá. (2024). *Racionamiento de agua: balance del consumo durante el 2024*. https://bogota.gov.co/mi-ciudad/habitat/racionamiento-de-agua-acueducto-balance-del-consumo-durante-el-2024 (Consultado el 10 de septiembre de 2026)

Autoridad Nacional de Licencias Ambientales. (s.f.). *Certificado de Exclusión de IVA (CEI)*. https://www.anla.gov.co/01_anla/certificado-exclusion-iva-que-es-el-cei (Consultado el 10 de septiembre de 2026)

Autoridad Nacional de Licencias Ambientales. (s.f.). *Certificación de descuento del impuesto sobre la renta por inversiones ambientales*. https://www.anla.gov.co/01_anla/allcategories-es-es/224-tramites-y-servicios/tramites/certificaciones/descuento-impuesto (Consultado el 10 de septiembre de 2026)

Banco Interamericano de Desarrollo. (2026). *Convocatoria de propuestas "Too Good to Waste" para proyectos de gestión de residuos sólidos*. https://www.iadb.org/es/blog/agua-saneamiento-y-residuos-solidos/convocatoria-de-propuestas-too-good-waste-para-proyectos-de-gestion-residuos-solidos (Consultado el 10 de septiembre de 2026)

Concejo de Bogotá D.C. (2024). *Relleno sanitario Doña Juana: el costo social y ambiental de un sistema*. https://concejodebogota.gov.co/relleno-sanitario-dona-juana-el-costo-social-y-ambiental-de-un-sistema/cbogota/2024-12-12/113750.php (Consultado el 10 de septiembre de 2026)

Environmental Protection Agency. (2012). *Composting in WARM (Waste Reduction Model)*. https://archive.epa.gov/epawaste/conserve/tools/warm/pdfs/cmpstng_ovrview.pdf (Consultado el 10 de septiembre de 2026)

Gobernación de Cundinamarca. (2025). *Cundinamarca florece en Proflora 2025, corazón de la floricultura colombiana*. https://www.cundinamarca.gov.co/noticias/cundinamarca-florece-en-proflora-2025-corazon-de-la-floricultura-colombiana (Consultado el 10 de septiembre de 2026)

Instituto Colombiano Agropecuario. (s.f.). *Trámites de fertilizantes y acondicionadores de suelos*. https://www.ica.gov.co/oferta-institucional/tramites/agricola/fertilizantes/tramite-numero-uno.aspx (Consultado el 10 de septiembre de 2026)

Instituto Nacional de Contadores Públicos. (2026). *Tarifas 2026 del impuesto a la gasolina, al ACPM y al carbono*. https://incp.org.co/publicaciones/infoincp-publicaciones/impuestos/2026/02/tarifas-2026-del-impuesto-a-la-gasolina-al-acpm-y-al-carbono/ (Consultado el 10 de septiembre de 2026)

Instituto para la Economía Social. (2025). *Más de 70.000 kilos de residuos orgánicos al mes se transforman en abono en las plazas distritales de mercado de Bogotá*. https://www.ipes.gov.co/index.php/informacion-de-interes/noticias/mas-de-70-000-kilos-de-residuos-organicos-al-mes-se-transforman-en-abono-en-las-plazas-distritales-de-mercado-de-bogota/1878 (Consultado el 10 de septiembre de 2026)

Korea Herald. (2026). *Seoul's food waste reduction over a decade*. https://www.koreaherald.com/article/10638389 (Consultado el 10 de septiembre de 2026)

Logitools. (2026). *Costo operativo de un camión en Colombia*. https://logitools.co/guias/costo-operativo-camion-colombia (Consultado el 10 de septiembre de 2026)

Natural Resources Defense Council. (s.f.). *Food rescue and composting in San Francisco*. https://www.nrdc.org/resources/food-rescue-san-francisco-composting (Consultado el 10 de septiembre de 2026)

POCACITO. (2014). *Food waste recycling in Milan* [Estudio de caso]. https://pocacito.eu/sites/default/files/FoodWasteRecycling_Milan.pdf (Consultado el 10 de septiembre de 2026)

Semana. (2026). *La Sabana de Bogotá concentra la expansión industrial ante la escasez de suelo en la capital*. https://www.semana.com/economia/capsulas/articulo/la-sabana-de-bogota-concentra-la-expansion-industrial-ante-la-escasez-de-suelo-en-la-capital/202614/ (Consultado el 10 de septiembre de 2026)

Valora Analitik. (2026). *Camión eléctrico llega a Colombia: carga en una hora y ahorra costos*. https://www.valoraanalitik.com/camion-electrico-llega-a-colombia-carga-en-una-hora-y-ahorra-costos/ (Consultado el 10 de septiembre de 2026)

Verra. (s.f.). *Avoidance of methane emissions through composting (AMS-III.F)*. https://verra.org/methodologies/avoidance-of-methane-emissions-through-composting/ (Consultado el 10 de septiembre de 2026)

Zonar. (2026). *Precio del ACPM en Colombia, septiembre 2026*. https://zonar.com.co/blog/precio-del-acpm-en-colombia-septiembre-2026/ (Consultado el 10 de septiembre de 2026)

---

# ANEXO — VACÍOS DE INFORMACIÓN Y ACCIONES PRIORITARIAS

## A.1 Datos marcados como NO ENCONTRADO

| # | Dato faltante | Criticidad | Cómo obtenerlo |
|---|---|---|---|
| 1 | **CAPEX de planta de compostaje en Colombia** (5, 20, 50 ton/día) | 🔴 Crítica | Cotización con integradores; visita a la planta Biocarbono (40 ton/día) |
| 2 | **Área requerida** en m²/ton-día | 🔴 Crítica | Ídem |
| 3 | **Precio de compra de compost por agricultores de la Sabana** | 🔴 Crítica | Cotizar con 3–5 productores de papa en Villapinzón, Chocontá, Subachoque |
| 4 | Cifras exactas de la NTC 5167 (materia orgánica, humedad, pH, C/N, metales, patógenos) | 🟠 Alta | Comprar la norma en ICONTEC |
| 5 | Costo del registro de venta ICA | 🟡 Media | Llamar al ICA, línea de Fertilizantes: (601) 2884800 |
| 6 | Umbral en ton/día que dispara Licencia Ambiental vs. PMA | 🟠 Alta | Consulta a la SDA y a la CAR Cundinamarca |
| 7 | Tarifa de aseo del operador de **Usme** (no ASE 5) por estrato | 🟡 Media | Pliego tarifario del concesionario del ASE correspondiente |
| 8 | Límite porcentual del descuento del art. 255 ET sobre el impuesto a cargo | 🟠 Alta | Asesor tributario; art. 259 ET |
| 9 | Precio actual del CO2e en el mercado voluntario colombiano | 🟡 Media | Ecosystem Marketplace, "State of the Voluntary Carbon Market 2025" |
| 10 | Costos reales de certificación Verra / Gold Standard | 🟡 Media | Cotización directa a un VVB acreditado |
| 11 | Canon de leasing/renting de camión | 🟡 Media | Cotización a Renting Colombia, Bancolombia Leasing |
| 12 | Valor exacto del SOAT 2026 para camión | 🟢 Baja | Simulador de Fasecolda / RUNT |
| 13 | Arriendo de bodega por m² en Usme y en Mosquera/Funza | 🟡 Media | Corredores inmobiliarios industriales; informe Colliers |
| 14 | Casos y montos reales de patrocinio corporativo ambiental en Bogotá | 🟡 Media | Informes de sostenibilidad ESG 2024–2025 de las compañías |
| 15 | Datos de hortalizas en Cundinamarca | 🟢 Baja | Agronet, Evaluaciones Agropecuarias Municipales |

## A.2 Las cinco acciones más urgentes

| Prioridad | Acción | Plazo | Costo | Por qué |
|---|---|---|---|---|
| **1** | **Consulta formal escrita a la CRA y a la SSPD:** ¿los residuos orgánicos domiciliarios compostados constituyen "residuos efectivamente aprovechados" remunerables vía VBA en un municipio de más de 5.000 suscriptores? ¿Puede una sociedad comercial en coprestación con una organización de recicladores ser remunerada? | Inmediato (respuesta en 30 días hábiles) | **$0** | Determina si existe la principal fuente de ingresos del negocio ($160.136/ton) |
| **2** | **Preparar y radicar proyecto ante el Comité IAT** (Decreto 2412 de 2018) | Antes del **30 de marzo de 2027** | Bajo | Fondo de ~$34.600 millones/año con el compostaje explícitamente elegible |
| **3** | **Rediseñar el mecanismo de incentivo** hacia las alternativas A/B/C de §4.3 y ajustar toda la comunicación del proyecto | Inmediato | $0 | El descuento en alcantarillado tal como está planteado es ilegal |
| **4** | **Iniciar conversaciones con organizaciones de recicladores del sur de Bogotá** (ARUPAF, ANRT, ARB y otras del listado de 488) | 1–3 meses | Bajo | Es la única vía realista de acceso al VBA, y aporta licencia social |
| **5** | **Incidencia ante el Concejo de Bogotá** para el nuevo acuerdo de subsidios 2027–2031 (reemplazo del Acuerdo 830 de 2021) | Segundo semestre de 2026 | Bajo | Ventana única que se cierra el 31 de diciembre de 2026 |

---

*Documento elaborado el 10 de septiembre de 2026. Todas las cifras provienen de las fuentes citadas; los cálculos derivados se identifican como "cálculo propio" y muestran su fórmula. Los datos no hallados se marcan como NO ENCONTRADO y se listan en el Anexo A.1 con su ruta de obtención.*
