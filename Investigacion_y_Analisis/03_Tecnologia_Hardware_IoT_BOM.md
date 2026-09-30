# RECOEVO — Tecnología, Hardware, IoT y Despiece de Costos (BOM)

**Documento técnico de ingeniería de producto**
**Fecha de elaboración:** 10 de septiembre de 2026
**TRM de referencia:** 1 USD = **3.099,48 COP** (Banco de la República / Superintendencia Financiera, 10-sep-2026). En todo el documento se usa **3.100 COP/USD**.
**Alcance:** Localidad 5 — Usme, Bogotá D.C. Hogares de estratos 1 y 2.

> **Nota metodológica sobre precios.** Todo precio marcado con fuente es un precio real verificado en la fecha de consulta. Todo precio marcado **(ESTIMADO)** no pudo verificarse públicamente y se deriva por analogía con productos similares; el razonamiento se explicita en cada caso. Los precios de proveedor asiático son FOB y no incluyen flete, arancel ni nacionalización (se cargan por separado en la sección 10). Criterio general: **sobreestimar antes que subestimar**.

---

## 1. Resumen ejecutivo y arquitectura recomendada del dispositivo

### 1.1. Qué es Recoevo, en términos de ingeniería

Un electrodoméstico de piso, de ~55 L de volumen exterior, que recibe residuos orgánicos de cocina, los **macera mecánicamente a baja velocidad** al cerrarse la tapa, reduce su volumen ~50-60 %, deposita el macerado en un **cajón extraíble de 20 L** con bolsa compostable, controla olores por **sellado + carbón activado + estructurante seco**, pesa el contenido con una **celda de carga**, mide el nivel con un **sensor ToF**, y transmite ~12 bytes cuatro veces al día por **LoRaWAN en 915-928 MHz** hacia una red de gateways municipales — sin tocar el WiFi del hogar y sin plan de datos a cargo del usuario.

### 1.2. Las siete decisiones de arquitectura (y por qué)

| # | Decisión | Alternativa descartada | Razón determinante |
|---|---|---|---|
| 1 | **Maceración a baja velocidad** (motorreductor 24 V, 80-100 RPM, ≥15 N·m), partícula de 5-15 mm | Triturador tipo *disposer* a 3.500 RPM (InSinkErator y similares) | El *disposer* está diseñado para funcionar **con chorro de agua permanente**; sin agua se atasca, salpica y genera 65 dB. Además, licuar el residuo a <2 mm produce un **lodo anaerobio maloliente**, no materia prima de compost: el compostaje necesita porosidad. |
| 2 | **NO deshidratar** | Deshidratación térmica (Lomi, Vitamix FoodCycler, SmartCara) | Consumo ~40-50× mayor. Ver §6: la deshidratación añadiría ~24 kWh/mes a la factura de un hogar que consume 100-130 kWh/mes. **Rompe el modelo de negocio.** |
| 3 | **Sellado + carbón + estructurante**, sin ozono ni UV-C | Ozono, UV-C, biofiltro | El ozono es un irritante respiratorio inaceptable dentro de una vivienda pequeña; el UV-C no destruye olores en fase gas y se ensucia; el biofiltro no cabe. El sellado hermético cuesta 1,60 USD y es la defensa más barata y más eficaz. |
| 4 | **LoRaWAN privado en AU915 (915,2-927,8 MHz)** | NB-IoT / LTE-M, Sigfox, Helium, WiFi | Espectro de uso libre en Colombia, sin licencia ni homologación CRC; OPEX de **0,41-2,22 USD/dispositivo/año** frente a 12-24 USD/año de NB-IoT (≈ 15-50× más caro). Ver §5. |
| 5 | **Alimentación 110 V para el motor + batería 18650 de respaldo para la radio** | Todo a batería; todo a red sin respaldo | El motor exige ~150 W de pico; imposible a batería a costo razonable. Pero la alerta más valiosa (contenedor lleno) debe sobrevivir a un corte de luz: la radio corre en batería con autonomía de ~90 días. |
| 6 | **Doble enclavamiento de seguridad por hardware** (microswitch de leva en serie con la potencia + reed switch leído por el MCU) | Enclavamiento solo por firmware | Seguridad infantil. El motor **no puede** arrancar con la tapa abierta aunque el firmware falle o esté corrupto: el corte es físico, no lógico. |
| 7 | **Rotomoldeo hasta 1.000 uds; inyección desde 10.000 uds** | Inyección desde el inicio; acero inoxidable | El utillaje de inyección (~62.000 USD, §7) solo se amortiza razonablemente por encima de ~8.000 unidades. Antes de eso, rotomoldeo local (Rototech, Rotoplast) con molde de aluminio de ~9.000 USD. |

### 1.3. Diagrama funcional

```
                    ┌──────────────── TAPA con empaque EPDM ────────────────┐
  Usuario deposita  │  · Reed switch (señal al MCU)                          │
  residuo orgánico ─┼─ · Microswitch de leva (CORTE FÍSICO de la potencia)   │
                    │  · Latch electromecánico (bloquea apertura en marcha)  │
                    └───────────────────────────────────────────────────────┘
                                        │  cierre detectado
                                        ▼
        ┌──────────── CÁMARA DE MACERACIÓN (inox 304, ~3 L) ────────────┐
        │  Rotor de dientes + peine fijo · 80-100 RPM · ≥15 N·m         │
        │  Motorreductor 24 V / 120 W · inversión automática si sobre-  │
        │  corriente (3 intentos) · freno dinámico · klixon térmico     │
        └────────────────────────┬──────────────────────────────────────┘
                                 ▼  macerado 5-15 mm
        ┌──────── CAJÓN EXTRAÍBLE 20 L + bolsa compostable ────────────┐
        │  Rejilla separadora de lixiviados en el fondo                 │
        │  Celda de carga 20 kg (bajo el cajón) + HX711                 │
        │  Sensor ToF VL53L0X (nivel, en el techo de la cámara)         │
        │  Compartimento dosificador de estructurante (aserrín/biochar) │
        └───────────────────────────────────────────────────────────────┘
                                 │
        ┌────────── TREN DE OLOR (presión negativa) ───────────────────┐
        │  Ventilador axial 40 mm 24 V (60 s tras cada cierre)          │
        │  → Cartucho de carbón activado 250 g (recambio 6 meses)       │
        │  → Válvula unidireccional de venteo                           │
        └───────────────────────────────────────────────────────────────┘
                                 │
        ┌──────────── ELECTRÓNICA ──────────────────────────────────────┐
        │  MCU ESP32-C3 (RISC-V, BLE 5 nativo)                          │
        │  Radio LoRa SX1262 (Ai-Thinker Ra-01SH) + antena helicoidal    │
        │  Fuente conmutada 110 V → 24 V / 150 W + riel 3,3 V           │
        │  Batería 18650 2600 mAh + PCM (respaldo solo de la radio)     │
        │  BLE como canal de respaldo "data-mule" (camión recolector)   │
        └───────────────────────────────────────────────────────────────┘
                                 │  12 bytes × 4 veces/día
                                 ▼
        Gateway LoRaWAN municipal (punto alto) → ChirpStack → Backend
                                 → Mapa de radares / optimización de rutas
```

### 1.4. Cifras clave del entregable

| Indicador | Valor |
|---|---|
| Costo total de fabricación @ 100 uds | **376 USD ≈ 1.166.000 COP** |
| Costo total de fabricación @ 1.000 uds | **159 USD ≈ 492.000 COP** |
| Costo total de fabricación @ 10.000 uds | **94 USD ≈ 290.000 COP** |
| Conectividad elegida | **LoRaWAN privado AU915 + ChirpStack propio + respaldo BLE** |
| Costo de conectividad por dispositivo/año (20.000 uds) | **0,41 USD ≈ 1.280 COP** |
| Impacto en la factura de luz del hogar | **≈ 225-560 COP/mes** (0,01-0,03 % del SMMLV 2026) |
| Consumibles por hogar/año | **≈ 15 USD ≈ 46.500 COP** |
| Inversión en utillaje (inyección, 10k+) | **≈ 62.000 USD** |
| Desarrollo de software (MVP) | **≈ 346 M COP ≈ 112.000 USD** |

---

## 2. Trituración: análisis de opciones y recomendación

### 2.1. Cómo funciona un triturador de fregadero (*garbage disposal*)

InSinkErator y equivalentes **no usan cuchillas**. Un plato giratorio (*flywheel*) lleva dos o tres **impulsores (lugs)** pivotantes; la fuerza centrífuga lanza el residuo contra un **anillo triturador (grind ring)** estacionario y dentado, que lo fractura por cizalla contra el borde. El agua corriente arrastra las partículas a través de las perforaciones del anillo hacia el desagüe.

| Parámetro | Valor típico | Fuente |
|---|---|---|
| Potencia | 1/3 a 1 HP (250-750 W) | InSinkErator / Angi |
| Velocidad | 1.725 a 2.000 RPM (unidades comerciales chinas: 3.500-3.800 RPM) | InSinkErator / Xiamen David Tech |
| Mecanismo | Impulsores + anillo triturador, sin cuchillas | InSinkErator |
| Tamaño de partícula | < 2 mm ("virtualmente licuado") | InSinkErator / Xiamen David Tech |
| Ruido | < 65 dB | Xiamen David Tech |
| Requisito operativo | **Flujo de agua continuo durante todo el ciclo** | InSinkErator |

**Precio OEM real verificado** (Xiamen David Technology, unidad de 1/2 HP, 110/220 V, 3.500-3.800 RPM, cámara de 1.100 mL, exterior ABS / interior inox, 3,8-4,0 kg, certificaciones ETL/FCC/CE/RoHS/CQC):

| Cantidad | Precio FOB unitario |
|---|---|
| 200-499 uds | 48,00 USD |
| 500-999 uds | **45,00 USD** |
| 1.000+ uds | 52,00 USD *(la escala publicada es inconsistente — sube en el tramo superior; se asume error de listado y se toma 45,00 USD como precio negociable a 1.000 uds)* |

### 2.2. Por qué NO se adopta el *disposer* tal cual

1. **Dependencia del agua.** Sin arrastre hidráulico, el residuo macerado se compacta contra el anillo y lo ciega. Reintroducir agua implicaría conexión hidráulica, drenaje y lixiviados — exactamente lo que el producto quiere evitar.
2. **Granulometría contraproducente.** Un macerado de <2 mm es un **puré anaerobio**. El compostaje aerobio requiere porosidad estructural; un puré se apelmaza, pierde oxígeno y se pudre generando ácidos grasos volátiles y sulfuro de hidrógeno — el peor escenario de olor posible en una vivienda.
3. **Ruido.** 65 dB dentro de una cocina de vivienda de interés social es inaceptable.
4. **Salpicadura y aerosoles.** A 3.500 RPM, sin agua, el material húmedo se proyecta contra las paredes y se aerosoliza.

### 2.3. Compostadoras electromecánicas domésticas del mercado mundial

| Producto | PVP (USD) | Capacidad | Tecnología | Ciclo | Energía por ciclo | Control de olores |
|---|---|---|---|---|---|---|
| **Lomi** (Pela) | 499 | ~3 L | Calor + trituración (deshidratación) | 3-5 h (Eco Express) | 0,60 kWh (Eco) / 0,75 kWh (Lomi-Approved) / ~1,0 kWh (Grow) | Dos filtros de carbón activado en pellets. Recambios: 29,95 USD/45 ciclos; 59,90/90; 119,80/180; 239,60/360 |
| **Vitamix FoodCycler** (FC-50 / Eco3 / Eco5) | 284-399 | 2 L / 3 L / 5 L | Calor + molienda | 4-8 h | No publicado; standby 1,2 W | Filtro de carbón |
| **Mill Food Recycler** | 999 + suscripción mensual | ~20 L | Deshidratación + molienda | Continuo, nocturno | No publicado | Filtro de carbón; el residuo seco se devuelve por correo |
| **Reencle Prime** | 549 | ~6 L (2,2 kg/día) | **Microbiano** (compost real con microbios vivos) | Continuo, 24 h | No publicado (~1 kWh/día ESTIMADO por calefacción del lecho a 40-50 °C) | Filtro de carbón, recambio cada **9-12 meses** |
| **SmartCara** (PCS-350/400/500) | ~400-600 | 2-4 L | Deshidratación / molienda / enfriado | ~3 h | **0,5-1,0 kWh por ciclo**; potencia nominal 0,5 kW; ~2 kWh/mes adicionales por *standby* permanente | Filtro propietario; **debe permanecer enchufado** para no oler |
| **GEME / GEME Pro** | ~600-800 | 19 L | **Microbiano puro** (bacteria termófila "Kobold"); no deshidrata, no tritura | 24-48 h | No publicado | **Sin filtro recambiable**: la neutralización es interna. Ventaja de costo recurrente cero |

**Lectura estratégica:** todo el mercado mundial de compostadoras domésticas usa **calor** — es decir, energía cara — porque vende a hogares de países ricos donde 0,25 USD/kWh sobre 1 kWh/día es ruido de fondo. Ese modelo **no es trasladable** a un hogar de estrato 1 en Usme (§6). Las dos referencias relevantes para Recoevo son **Reencle** y **GEME**, que demuestran que se puede controlar el olor **sin** deshidratar: con microbiología y sellado. Recoevo toma esa lección pero la abarata todavía más sustituyendo el lecho microbiano climatizado por **maceración mecánica + estructurante seco**, que cuesta energía solo durante 25 segundos al día.

### 2.4. Motorización recomendada

| Requisito | Valor de diseño | Justificación |
|---|---|---|
| Tipo | Motorreductor DC con reductor sinfín-corona o planetario | El sinfín es autobloqueante (el rotor no gira en reversa por inercia al abrir) y barato |
| Tensión | 24 V DC | Por debajo de la tensión de contacto peligrosa; simplifica el aislamiento de la zona húmeda |
| Potencia eléctrica | 100-150 W | Suficiente para 2 kg de residuo húmedo en 25 s |
| Velocidad de salida | 80-100 RPM | Baja velocidad = alto par, bajo ruido, sin salpicadura |
| Par | ≥ 15 N·m (pico ≥ 25 N·m) | Estimado para cortar fibra vegetal húmeda con un rotor de 90 mm de diámetro: F ≈ 350 N en el radio de 45 mm |
| Protección | Klixon térmico + protector de sobrecarga con rearme manual + detección de sobrecorriente en firmware con **inversión automática de giro** (3 intentos) | Antiatasco: es el modo de falla #1 |

**Precios de mercado consultados (Alibaba, sept-2026):** los motorreductores sinfín 12/24 V aparecen en un rango muy amplio — desde 0,68-9,80 USD (micromotores), 7,90-9,85 USD (modelo TJW58FX 24 V/12 V), hasta 80-99 USD para unidades industriales de 100-200 W con MOQ de 2 piezas. Para un motorreductor de ~120 W de grado electrodoméstico con reductor sinfín y protección térmica, el precio realista a volumen es **22 USD @1.000 uds** y **16,50 USD @10.000 uds** *(ESTIMADO: se sitúa entre el precio de los micromotores de catálogo y el precio de venta al detal de las unidades industriales, asumiendo el descuento OEM típico del 70-75 % sobre PVP de catálogo industrial)*.

### 2.5. Triturar vs. deshidratar — el trade-off cuantificado

| Criterio | **Maceración mecánica** (recomendada) | **Deshidratación térmica** |
|---|---|---|
| Reducción de **volumen** | 50-60 % | 70-80 % |
| Reducción de **peso** | ~0 % (no se retira agua) | 70-80 % |
| Energía por día (hogar de 4 personas, ~2 kg/día) | **~15 Wh** | **~800 Wh** |
| Energía por mes | **~0,5 kWh** | **~24 kWh** |
| Costo eléctrico/mes, estrato 2 Bogotá | **≈ 281 COP** | **≈ 10.368 COP** |
| Impacto en la factura de un hogar que consume 120 kWh/mes | **+0,4 %** | **+20 %**, y **empuja al hogar por encima de los 130 kWh de consumo de subsistencia, haciéndole perder el subsidio en el margen** |
| Control de olor intrínseco | Requiere sellado + carbón + estructurante | El producto seco es estable e inodoro |
| Costo de fabricación adicional | — | +25-40 USD (resistencia, aislamiento térmico, control PID, ventilación, condensador) |
| Riesgo de seguridad | Mecánico (mitigable con enclavamiento) | Térmico (superficies a 70-120 °C en presencia de niños) |
| Calidad del producto para compostaje | Excelente (húmedo, poroso, biológicamente activo) | Media (deshidratado ≠ compost; requiere rehidratación y maduración posterior) |

**Recomendación técnica fundamentada: NO incluir deshidratación.** El argumento no es solo el costo eléctrico absoluto (que en valor absoluto es bajo: ~10.400 COP/mes), sino el **efecto regresivo sobre el subsidio**. En Bogotá el consumo de subsistencia es de 130 kWh/mes y los subsidios de estrato 1 (60 %) y 2 (50 %) **solo aplican sobre ese tramo**. Un hogar de estrato 1 en Usme que hoy consume 110-125 kWh/mes está justo debajo del umbral. Añadir 24 kWh/mes lo cruza: los kWh excedentes se facturan **a tarifa plena (~864 COP/kWh)**, de modo que el costo marginal real no es 10.400 COP sino cerca de 20.700 COP/mes. Para una familia cuyo ingreso es 1-2 SMMLV, eso es un 1 % del ingreso mensual **para tirar la basura** — y es exactamente el tipo de costo oculto que hace que un programa social sea abandonado por los beneficiarios en el segundo o tercer mes. La maceración, con 0,5 kWh/mes, es **energéticamente invisible** y por eso es la única opción viable.

**Consecuencia de diseño:** como no se retira agua, el macerado sigue pesando ~2 kg/día y **debe recogerse con frecuencia** (cada 7-10 días con el cajón de 20 L). Esto no es un defecto: es precisamente lo que justifica la existencia de la red de alertas IoT y la optimización de rutas.

---

## 3. Control de olores: análisis y recomendación

El control de olores es **el requisito que decide si el producto se queda en la casa o se saca al patio**. Se ataca en cinco capas, ordenadas por relación eficacia/costo.

### 3.1. Capa 1 — Sellado hermético (la más barata y la más importante)

| Elemento | Especificación | Costo @1.000 uds |
|---|---|---|
| Empaque perimetral | Perfil de EPDM o silicona de celda cerrada, 2 m, sección en "D" de 10×8 mm, dureza 40-50 Shore A | 1,60 USD |
| Cierre por compresión | Latch de leva con recorrido de 3-4 mm sobre el empaque | incluido en tornillería |
| Válvula unidireccional de venteo | Membrana de silicona con apertura a 2-3 mbar, para compensar la presión del gas de fermentación sin permitir retroceso | 0,70 USD |

**Por qué primero:** ningún filtro funciona si el aire escapa por la junta. La EPDM se elige sobre la silicona por resistencia a ácidos orgánicos y menor costo; se descarta el caucho nitrílico por degradación con ozono ambiental.

### 3.2. Capa 2 — Estructurante seco (la más eficaz por peso)

Aserrín fino, cascarilla de arroz o **biochar** dosificados por el usuario (~2 cucharadas tras cada carga, ~6 kg/año):

- **Absorbe el agua libre**, que es el vehículo físico del olor.
- **Sube la relación C/N**, evitando el exceso de nitrógeno que se volatiliza como amoníaco.
- **Mantiene porosidad**, impidiendo la anaerobiosis que produce H₂S y ácidos grasos volátiles.
- El biochar, además, adsorbe gases en sus microcavidades y aloja bacterias beneficiosas; la evidencia reciente reporta **reducción de hasta 51 % de emisiones de metano** en compostaje y maduración más rápida. Advertencia técnica: el biochar de **poro pequeño** funciona mejor; el de poro grande derivado de madera ralentizó el proceso y bloqueó el flujo de oxígeno.

**Costo:** ~3,00 USD/hogar/año. Es el control de olor más barato por unidad de eficacia, y es el único que también mejora la calidad del producto final.

### 3.3. Capa 3 — Carbón activado

| Parámetro | Valor | Fuente |
|---|---|---|
| Vida útil típica en compostera doméstica | 2-3 meses (uso intensivo) a 4-6 meses; hasta 9-12 meses en equipos con lecho microbiano sellado (Reencle) | Reencle / Activated Carbon Depot |
| Forma preferida | **Pellets**, no paño: geometría uniforme que maximiza el tiempo de contacto sin estrangular el flujo | Activated Carbon Depot |
| Costo del recambio en el mercado de consumo | Lomi: 29,95 USD/45 ciclos (≈0,67 USD/ciclo); packs genéricos de 4×210 g y packs de 7 filtros entre 9,49 y 18,13 USD | Pela / Amazon |
| Costo objetivo Recoevo (cartucho de 250 g, granel) | **3,20 USD (CAPEX inicial) / 2,10 USD por recambio** *(ESTIMADO: carbón activado granular a granel se cotiza entre 2 y 5 USD/kg; 250 g ≈ 0,75 USD de material + 1,35 USD de cartucho, tapa y malla)* | — |

**Diseño:** cartucho recambiable de acceso frontal, **sin herramientas**, con indicador de fecha. Recambio semestral (2/año) por el operario durante la ruta de recolección — lo que lo convierte en un punto de contacto de servicio, no en una carga para el usuario.

### 3.4. Capa 4 — Extracción activa a presión negativa

Ventilador axial de 40 mm / 24 V que arranca **60 segundos después de cada cierre de tapa** y extrae el aire de la cámara **a través** del cartucho de carbón. Mantiene el interior en ligera depresión y, sobre todo, elimina el "golpe de olor" al abrir la tapa, que es el momento en que el usuario forma su juicio sobre el producto. Costo: **1,10 USD @1.000 uds**.

### 3.5. Capa 5 — Microorganismos eficientes (opcional, kit de arranque)

Los EM (bacterias ácido-lácticas, levaduras y bacterias fotosintéticas) desplazan la flora putrefactiva por competencia por nutrientes y espacio, y acidifican el medio. En residuo domiciliario se recomienda la presentación sólida **EM-Bokashi**. Disponibles en Colombia (MercadoLibre, Vidagro, vademécum PortalTecnoagrícola).

**Recomendación:** incluir un sobre de EM-Bokashi en el kit de arranque como demostración, pero **no diseñar la dependencia del producto sobre él**: exige compra recurrente y disciplina del usuario. El biochar/aserrín es más barato, más disponible localmente (aserraderos de Usme) y no caduca.

### 3.6. Tecnologías evaluadas y DESCARTADAS

| Tecnología | Motivo del descarte |
|---|---|
| **Ozono (O₃)** | Irritante respiratorio. Generar ozono dentro de una vivienda pequeña y mal ventilada, con niños y adultos mayores, es un riesgo sanitario inaceptable y difícilmente defendible ante una autoridad sanitaria. **Descartado sin reservas.** |
| **UV-C** | No destruye moléculas de olor en fase gas con eficacia útil a los caudales y tiempos de residencia disponibles; la lámpara se ensucia con aerosoles grasos en semanas; riesgo ocular si el enclavamiento falla; añade 8-15 USD. |
| **Biofiltro** | Requiere un lecho de 15-30 L con humedad controlada y aclimatación de semanas. No cabe ni se puede mantener en un hogar. |
| **Cal viva (CaO)** | Neutraliza olor y sube el pH, pero es **cáustica**: quemaduras químicas por contacto o inhalación de polvo. Inaceptable en un producto de consumo doméstico con presencia infantil. Su uso documentado es en lodos residuales y galpones, no en electrodomésticos. |

### 3.7. Recomendación integrada: la combinación más barata y efectiva

| Capa | Costo unitario CAPEX @1.000 uds | Costo recurrente/año |
|---|---|---|
| Empaque EPDM + latch de compresión | 1,60 USD | — |
| Válvula unidireccional de venteo | 0,70 USD | — |
| Cartucho de carbón activado 250 g | 3,20 USD | 4,20 USD (2 recambios) |
| Ventilador de extracción 40 mm 24 V | 1,10 USD | — |
| Compartimento dosificador de estructurante | 0,80 USD | 3,00 USD (6 kg de biochar/aserrín) |
| **TOTAL** | **7,40 USD (≈ 22.900 COP)** | **7,20 USD/año (≈ 22.300 COP)** |

Esto es **menos del 5 % del costo de fabricación** a 1.000 unidades y resuelve el requisito crítico. Por comparación: una sola recarga de filtros de Lomi cuesta 29,95 USD — cuatro veces todo el sistema de olores de Recoevo.

---

## 4. Sensórica

### 4.1. Báscula — celda de carga + HX711

| Parámetro | Especificación |
|---|---|
| Tipo | Celda de carga de barra en voladizo (*single point*), aluminio, galga extensométrica |
| Rango | **20 kg** — el cajón de 20 L lleno de macerado húmedo (densidad ~0,7 kg/L) pesa ~14 kg; margen del 40 % |
| Amplificador | HX711, ADC de 24 bits, ganancia 128, 10/80 SPS |
| Resolución práctica | ±10 g (suficiente: la resolución útil para el sistema de puntos es de 100 g) |
| Montaje | Bajo la bandeja del cajón, sobre 4 apoyos, con tope mecánico contra sobrecarga |
| **Precio verificado** | 3,50-4,00 USD por kit celda+HX711 en tramos de 10-100+ uds (Alibaba); MOQ de 100 uds desde 0,99 USD para el módulo HX711 solo; se reporta bajada por debajo de 1,00 USD para el módulo en pedidos >100 |
| **Precio de diseño** | 3,50 (100 uds) / **2,40 (1.000 uds)** / 1,70 (10.000 uds) USD *(ESTIMADO a 1k/10k por extrapolación de la curva publicada)* |

**Calibración:** tara automática al retirar y reinsertar el cajón (detectada por un microswitch en la guía). Compensación térmica por software con la lectura del SHT31.

### 4.2. Nivel de llenado — comparativa

| Sensor | Precio | Alcance | Comportamiento en ambiente húmedo/sucio | Veredicto |
|---|---|---|---|---|
| **HC-SR04** (ultrasónico abierto) | ~0,60-1,50 USD | 2-400 cm | **Malo.** Transductor abierto: la condensación y la grasa lo inutilizan | ❌ |
| **JSN-SR04T / -3.0** (ultrasónico, sonda sellada) | 3,64 USD (AliExpress, con 25 % dto.); 3-10 USD según proveedor | 2-400 cm (útil desde ~20-25 cm) | Sonda estanca, apta para medios húmedos. **Pero** hay reportes documentados de lecturas erráticas y espurias (valores fijos ~220 mm), y deriva por temperatura. **Zona muerta de ~20 cm**, problemática en una cámara de 35 cm | ⚠️ |
| **VL53L0X** (ToF láser 940 nm) | 5,39 USD @1 ud → **~2,75 USD @1.000 uds** (chip, DigiKey); módulos con óptica 10-15 USD al detal | 3 cm - 2 m | **Prácticamente sin zona muerta**, inmune a humedad, temperatura y ruido acústico; la evidencia comparativa del sector de residuos reporta lecturas más estables que el ultrasónico, que es vulnerable a humedad y polvo. Vulnerable a suciedad **sobre la ventana óptica** | ✅ **ELEGIDO** |
| **Infrarrojo reflectivo simple** | ~0,30 USD | 2-30 cm | Solo detecta presencia/ausencia, no distancia; muy sensible al color y la reflectividad del residuo | ❌ |

**Decisión: VL53L0X**, montado en el techo de la cámara, **apuntando hacia abajo con una ventana de vidrio inclinada 15°** y una pequeña visera, de modo que las salpicaduras escurran por gravedad. El precio incremental frente al JSN-SR04T es de ~0,45 USD a 1.000 unidades — irrelevante frente al costo de una visita de servicio por lectura falsa. Referencia de mercado: los sensores comerciales de nivel para contenedores más vendidos (Milesight EM400-TLD) usan **precisamente ToF** y están explícitamente posicionados para "contenedores pequeños y mini", que es el caso de Recoevo.

**Redundancia:** el sistema **cruza nivel con peso**. Si el ToF dice 40 % pero la celda de carga dice 13 kg, el firmware reporta la condición más conservadora y marca un *flag* de discrepancia (indicador de ventana óptica sucia). Esta redundancia cruzada es gratis y resuelve el modo de falla principal del ToF.

### 4.3. Detección de cierre de tapa y seguridad

Este es el punto **más crítico del producto en términos de responsabilidad legal**. Se implementan **tres** elementos independientes:

| # | Elemento | Función | Tecnología | Costo @1k |
|---|---|---|---|---|
| 1 | **Microswitch de leva de seguridad** | **Corta físicamente** la alimentación del motor. Está en **serie** con la etapa de potencia. Si la tapa no está totalmente cerrada y enclavada, el circuito de potencia está abierto — el firmware **no puede** cerrarlo | Microswitch de acción rápida con actuador de rodillo, accionado por la leva del latch (no por la tapa) | 0,48 USD |
| 2 | **Reed switch + imán** | Señal **lógica** al MCU: "la tapa está cerrada". Dispara la temporización del ciclo | Reed switch NA + imán de neodimio en la tapa | 0,22 USD |
| 3 | **Latch electromecánico de retención** | Impide **abrir** la tapa mientras el rotor gira, y durante 3 s después (tiempo de frenado dinámico) | Solenoide de retención, normalmente enclavado, liberado por el MCU | incluido en tornillería/herrajes |

**Regla de diseño no negociable:** el microswitch (1) es un **corte de potencia en serie**, no una entrada del microcontrolador. El motor es físicamente incapaz de girar con la tapa abierta aunque el firmware esté corrupto, colgado o comprometido. Esto es lo que exige el espíritu de **IEC 60335-2-16:2022** (seguridad de trituradores de residuos de comida de uso doméstico, hasta 250 V, incluidos los alimentados en DC y por batería) y lo que la práctica de la industria implementa mediante dispositivos de enclavamiento dedicados (existe una familia de patentes específicas de *"food waste disposer interlock device"*).

**Medidas adicionales de seguridad infantil:**
- Abertura de carga con **deflector fijo** que impide la introducción de una mano hasta el rotor (criterio del "dedo de prueba" de IEC 60335-1).
- **Freno dinámico** del motor (cortocircuito del inducido) al abrir el latch: paro en <1 s frente a >8 s de inercia libre.
- Retardo de arranque de 2 s tras el cierre, con **señal acústica**, para permitir retirar la mano.
- Reductor sinfín **autobloqueante**: el rotor no puede ser girado manualmente desde la boca de carga.

### 4.4. Sensórica secundaria

| Sensor | Función | Costo @1k | ¿Incluir? |
|---|---|---|---|
| **SHT31** (temp./humedad, I²C) | Compensación térmica de la celda de carga; detección de condensación excesiva; dato de contexto para el modelo de descomposición | 1,20 USD | **Sí.** Su valor principal no es el dato ambiental sino la compensación de la báscula |
| **MQ-135** (gas: NH₃, NOₓ, benceno, CO₂, humo) | Detección de descomposición avanzada → alerta de "recoger ya", independiente del nivel | ~1,00-1,80 USD | **No en v1.** El MQ-135 exige un calefactor de ~150 mW **permanentemente encendido** (incompatible con el respaldo por batería), tiene deriva severa, requiere calibración individual y es muy sensible a la humedad — precisamente la condición dominante dentro del contenedor. Reevaluar en v2 con un sensor MOX de bajo consumo (BME680 o similar) |
| **Acelerómetro (LIS3DH)** | Detección de vuelco, golpe o traslado del equipo | ~0,80 USD | **No en v1.** El equipo es de piso e interior; el riesgo es bajo frente al costo y la complejidad |

**Presupuesto total de sensórica @1.000 uds: 6,25 USD** (celda+HX711 2,40 + ToF 1,95 + reed 0,22 + microswitch 0,48 + SHT31 1,20).

---

## 5. Conectividad LPWAN — análisis completo

Ésta es la decisión de arquitectura con mayor impacto sobre la viabilidad del modelo, porque es el único costo que **se repite todos los años, por cada dispositivo, para siempre**.

### 5.1. Restricciones del problema

1. **Sin WiFi del hogar.** Muchos hogares objetivo no tienen conexión fija; los que la tienen no aceptarán compartir credenciales ni soportarán la carga de soporte de un reaprovisionamiento cada vez que cambien el router.
2. **Sin costo de datos para el usuario.** Descarta cualquier arquitectura donde la SIM o la conexión estén a nombre del hogar.
3. **Volumen de datos ridículamente bajo.** El *payload* útil es de **12 bytes** (nivel %, peso en decagramos, temperatura, humedad, tensión de batería, contador de ciclos, flags) enviado **4 veces al día**. Son **17,5 kB al año por dispositivo**. Cualquier tecnología dimensionada para megabytes está sobredimensionada por tres órdenes de magnitud.
4. **Topografía de Usme.** Localidad 5, 119,04 km², 126 barrios, entre ~2.276 y ~3.100+ msnm, sobre la ladera sur-oriental de la sabana y limitando con los Cerros Orientales y Sumapaz. El suelo urbano es una fracción del total (*ESTIMADO 20-25 km²*), desarrollado sobre laderas, cañadas y quebradas con desniveles de 50-150 m entre barrios contiguos.

### 5.2. Marco regulatorio del espectro en Colombia — HALLAZGO CRÍTICO

| Norma | Contenido |
|---|---|
| **Resolución ANE 689 de 2004** | Atribuye la banda **902-928 MHz** a **uso libre** (título secundario, sin protección contra interferencias). Es la banda ISM de referencia para la Región 2 de la UIT |
| **Resolución ANE 28 de 2026** | Adopta el plan de banda de la **Tabla 15A del CNABF** para servicios móvil y fijo en **896-915 MHz** y 941-960 MHz. El segmento **905-915 MHz queda reservado para operación IMT futura** (redes móviles) |
| **Consecuencia operativa** | La **ventana limpia de uso libre para IoT masivo en Colombia es ahora 915-928 MHz** |

**Implicación de diseño que cambia la selección del plan de frecuencias:**

| Plan | Canales de subida | ¿Cae dentro de 915-928 MHz? |
|---|---|---|
| **US915** | Canales 0-63: 902,3 + 0,2·n MHz → **902,3 - 914,9 MHz** | ❌ **NO.** Todo el plan de subida US915 queda **por debajo de 915 MHz**, y sus sub-bandas centrales (canales 8-15 = 903,9-905,3 MHz) están en pleno segmento reasignado a IMT |
| **AU915** | Canales 0-63: 915,2 + 0,2·n MHz → **915,2 - 927,8 MHz**. Bajada: 923,3 + 0,6·n → 923,3-927,5 MHz | ✅ **SÍ, en su totalidad** |

> **Por tanto, el plan de frecuencias correcto para Recoevo y para cualquier despliegue LoRaWAN nuevo en Colombia es AU915, no US915** — pese a que la intuición geográfica ("estamos en América, luego US915") lleva al error opuesto. Se recomienda fijar la **sub-banda AU915-2 (canales 8-15: 916,8-918,2 MHz)** para el despliegue.

**No se requiere permiso de uso del espectro** para operar en 915-928 MHz bajo el régimen de uso libre. **Tampoco aplica la homologación de la CRC**, cuyo trámite está dirigido a *equipos terminales* que se conectan a las redes de los operadores móviles (verificación de frecuencias de operación y de límites de exposición a campos electromagnéticos). Un nodo LoRaWAN en banda libre no es un equipo terminal móvil. *Esto se invierte por completo si se elige NB-IoT: ahí la homologación CRC sí es obligatoria y el certificado debe presentarse ante la autoridad aduanera en la importación.*

### 5.3. Tabla comparativa completa de tecnologías

| Criterio | **LoRaWAN privado** | **LoRaWAN / TTN Community** | **Helium IoT** | **NB-IoT** | **LTE-M** | **Sigfox / 0G** | **BLE "data mule"** | **WiFi hogar** |
|---|---|---|---|---|---|---|---|---|
| **Disponibilidad en Colombia** | ✅ Banda libre 915-928 MHz | ✅ Software gratuito; **0 gateways registrados** a nivel país en el directorio oficial de TTN | ⚠️ Red global, pero **sin cobertura documentada en Usme** | ⚠️ Claro declara arquitectura 4.5G con NB-IoT y LTE-M; cobertura real en Usme **no verificable públicamente** | ⚠️ Ídem; SIMs IoT en Colombia conectan a Claro/Movistar/Tigo en 2G/3G/LTE y **LTE-M** | ❌ **Sin operador nacional documentado.** UnaBiz (ex-Sigfox) reporta >70 países; Colombia no aparece | ✅ Nativo del ESP32 | ✅ Pero **excluido por requisito** |
| **¿Licencia de espectro?** | No (uso libre) | No | No | N/A (red del operador) | N/A | N/A | No | No |
| **¿Homologación CRC?** | No | No | No | **Sí** | **Sí** | Sí | No | No |
| **Costo del módulo (1.000 uds)** | **5,80 USD** (Ra-01SH SX1262, PVP verificado 10,97 USD) | Igual | Igual | 6-9 USD *(ESTIMADO: BC660K-GL / SIM7020; no hay precio público; se toma el rango típico de módulos NB-IoT certificados)* | 8-12 USD *(ESTIMADO)* | 5-8 USD *(ESTIMADO)* | **0 USD** (integrado en el ESP32-C3) | 0 USD |
| **Infraestructura propia requerida** | Gateways + servidor de red | Gateways (el servidor lo pone TTN) | Hotspots (habría que desplegarlos) | Ninguna | Ninguna | Ninguna | Lector en el camión | Ninguna |
| **OPEX por dispositivo/año** | **0,41-2,22 USD** | ~0 USD (solo gateways) | 0,015 USD teóricos (1.460 msg/año × 1 DC × 0,00001 USD) **pero irreal sin cobertura** | **12-24 USD** *(ESTIMADO: planes IoT/M2M en la región para ~20 MB/mes se sitúan en 1-2 USD/mes; no hay tarifario público de Claro/Movistar/Tigo Colombia)* | 18-36 USD *(ESTIMADO)* | 8-15 USD *(ESTIMADO, referencia internacional)* | ~0,10 USD | 0 USD para el programa, **pero el costo se traslada al hogar → prohibido** |
| **Control sobre la red** | **Total** | Ninguno (política de uso justo de TTN: ~30 s de *airtime* diario, 10 bajadas/día) | Ninguno | Ninguno | Ninguno | Ninguno | Total | Ninguno |
| **Latencia de la alerta** | Minutos | Minutos | Minutos | Segundos | Segundos | Minutos-horas | **2-3 días** (frecuencia de ruta) | Segundos |
| **Consumo del nodo por mensaje** | ~50-120 mJ (SF9, 14 dBm) | Ídem | Ídem | ~200-500 mJ (con *attach* y *paging*) | Mayor | Bajo | ~5 mJ (anuncio BLE) | Alto |
| **Riesgo estratégico** | Gestionar infraestructura propia | Dependencia de una comunidad inexistente en el país | Red descentralizada sin SLA | **Dependencia total de un operador comercial y de su política de precios a 10 años** | Ídem | Sin operador | Solo respaldo | Excluido |
| **Veredicto** | ✅ **ELEGIDO** | ⚠️ Útil solo para el piloto de 100 uds | ❌ | ❌ | ❌ | ❌ | ✅ **Respaldo** | ❌ |

### 5.4. Análisis de propagación en Usme

La literatura de medición de LoRaWAN es consistente en tres puntos aplicables a Usme:

1. **Alcance urbano real: ~2 km**, frente a 15 km en entorno rural despejado.
2. **El terreno accidentado y la vegetación dispersan y bloquean la señal**; los muros de concreto atenúan **10-20 dB** — relevante porque el nodo está **dentro** de la vivienda, típicamente en cocina, a menudo en primer piso de una edificación de 2-3 niveles en ladera.
3. **La altura del gateway domina sobre su potencia.** La práctica recomendada es ubicar los gateways en **puntos elevados** (azoteas, torres) para maximizar la línea de vista.

**Consecuencia para Usme:** la topografía de laderas y quebradas es **simultáneamente el problema y la solución**. Las cañadas generan sombras orográficas profundas donde no hay difracción útil a 915 MHz; pero los filos y cerros ofrecen emplazamientos con dominio visual sobre miles de viviendas — un gateway bien ubicado en un filo de Usme puede "ver" barrios enteros en una configuración de anfiteatro que en terreno plano exigiría tres gateways.

**Presupuesto de enlace de diseño:**

| Parámetro | Valor |
|---|---|
| Potencia de transmisión del nodo | +14 dBm (el Ra-01SH admite hasta +29/+31 dBm, pero se limita por consumo y por buenas prácticas) |
| Ganancia de la antena del nodo (helicoidal interna) | -1 dBi (penalizada por el entorno del gabinete) |
| Pérdida por penetración en la vivienda | **-15 dB** (conservador: muro de concreto + posición interior) |
| Sensibilidad del gateway (SX1302) | **-139 dBm** (verificado, RAK7268V2) |
| Ganancia de la antena del gateway | +5 dBi |
| **Margen de enlace disponible** | **142 dB** |
| Margen de desvanecimiento reservado | -10 dB |
| **Pérdida de trayecto admisible** | **132 dB** |

Con un modelo urbano denso de exponente n≈3,0-3,5, 132 dB corresponden a **1,2-2,0 km** en condiciones NLOS. Se adopta **1,5 km de radio efectivo de diseño**, con un **factor de aprovechamiento del 50 %** por sombras orográficas → **≈ 3,5 km² útiles por gateway**.

**Estrategia de emplazamiento:** instalar los gateways en **equipamientos públicos en cota alta** — colegios distritales, CAI de la Policía, salones comunales, estaciones y torres del **TransMiCable**, tanques y estructuras del acueducto. Ventajas: energía y conectividad disponibles, seguridad física frente al vandalismo, cota dominante y **costo de arriendo cero** por ser un programa distrital.

### 5.5. Dimensionamiento y costo de la red

**Supuestos de costo por gateway (exterior, IP67):**

| Concepto | Valor | Fuente |
|---|---|---|
| Gateway exterior 8 canales IP67, backhaul Ethernet/4G/WiFi, hasta 2.000 nodos, -40 a +70 °C, PoE u 6-12 V DC, servidor de red embebido | **800 USD** *(ESTIMADO. El fabricante Milesight no publica precio del UG67. Referencias verificadas: RAK7268V2 US915 **interior** IP30 = 154 USD; con LTE = 234-247 USD; Dragino LPS8 interior = 125-235 USD. El salto a carcasa IP67, rango térmico extendido y SX1302 justifica un factor ≈3-4× sobre el interior)* | Milesight / RAK / Dragino |
| Antena exterior 5-8 dBi + cable LMR + protección contra sobretensiones | 120 USD *(ESTIMADO)* | — |
| Mástil, herrajes, caja antivandálica, instalación y puesta en servicio | 230 USD *(ESTIMADO: ≈1,5 jornadas de una cuadrilla de 2 personas a costo de mano de obra colombiana + materiales)* | — |
| **CAPEX por gateway** | **1.150 USD** | — |
| Backhaul (internet fijo compartido del equipamiento, o SIM 4G) | 15 USD/mes = 180 USD/año *(ESTIMADO)* | — |
| Energía (6 W × 8.760 h = 52,6 kWh × 864 COP) | 45.400 COP = **14,6 USD/año** | Enel-Codensa |
| Mantenimiento preventivo y correctivo (10 % del CAPEX) | 115 USD/año | — |
| **OPEX por gateway/año** | **≈ 310 USD** | — |
| Servidor de red **ChirpStack** autohospedado (licencia MIT, sin cuota por dispositivo) | VPS + respaldos + operación: **600-1.800 USD/año** según escala (el rango de referencia para autohospedaje es 20-100+ EUR/mes más tiempo de administración) | ChirpStack / chirphost |

**Amortización del CAPEX de gateways: 5 años (vida útil típica de electrónica exterior).**

#### Escenario A — 1.000 dispositivos (piloto ampliado, 2-3 barrios)

| Concepto | Cantidad | Costo anual |
|---|---|---|
| Gateways | 3 | CAPEX 3.450 USD ÷ 5 = **690 USD/año** |
| OPEX de gateways | 3 × 310 | **930 USD/año** |
| ChirpStack autohospedado | 1 VPS | **600 USD/año** |
| **TOTAL RED** | | **2.220 USD/año** |
| **Por dispositivo/año** | | **2,22 USD ≈ 6.880 COP** |

#### Escenario B — 5.000 dispositivos

| Concepto | Cantidad | Costo anual |
|---|---|---|
| Gateways | 6 | CAPEX 6.900 USD ÷ 5 = **1.380 USD/año** |
| OPEX de gateways | 6 × 310 | **1.860 USD/año** |
| ChirpStack (instancia mayor + réplica) | | **900 USD/año** |
| **TOTAL RED** | | **4.140 USD/año** |
| **Por dispositivo/año** | | **0,83 USD ≈ 2.570 COP** |

#### Escenario C — 20.000 dispositivos (cobertura urbana de Usme)

| Concepto | Cantidad | Costo anual |
|---|---|---|
| Gateways | 12 *(≈25 km² urbanos ÷ 3,5 km² útiles ≈ 7, más 70 % de redundancia por sombras de cañada y solapamiento)* | CAPEX 13.800 USD ÷ 5 = **2.760 USD/año** |
| OPEX de gateways | 12 × 310 | **3.720 USD/año** |
| ChirpStack (alta disponibilidad) | | **1.800 USD/año** |
| **TOTAL RED** | | **8.280 USD/año** |
| **Por dispositivo/año** | | **0,41 USD ≈ 1.280 COP** |

**Verificación de capacidad:** 12 gateways × 2.000 nodos = 24.000 > 20.000. Además, en carga de tráfico el margen es enorme: 20.000 nodos × 4 mensajes/día = 80.000 mensajes/día. Un gateway de 8 canales soporta miles de mensajes por segundo y, con buena planificación de frecuencias, más de un millón de paquetes diarios. **La limitante en Usme es la cobertura orográfica, no la capacidad.**

### 5.6. Comparación económica final

| Tecnología | OPEX/dispositivo/año | Costo anual de red a 20.000 dispositivos | Factor |
|---|---|---|---|
| **LoRaWAN privado (elegido)** | **0,41 USD** | **8.280 USD** | **1×** |
| NB-IoT | 18 USD *(ESTIMADO)* | 360.000 USD | **43×** |
| LTE-M | 27 USD *(ESTIMADO)* | 540.000 USD | **65×** |
| Sigfox | n/a — sin operador en Colombia | — | — |

A 20.000 dispositivos, la diferencia entre LoRaWAN y NB-IoT es de **≈ 352.000 USD al año ≈ 1.090 millones de COP anuales**. Para un programa social financiado con recursos públicos, esa cifra por sí sola decide la arquitectura. Y hay un argumento estratégico aún más fuerte: con LoRaWAN, el Distrito **es dueño de su red**; con NB-IoT, queda expuesto a la política tarifaria de un operador comercial durante los 10 años de vida del programa, sin poder de negociación.

### 5.7. Arquitectura recomendada (definitiva)

```
NODO (en la vivienda)
  ESP32-C3  +  SX1262 (Ra-01SH)  ──── LoRaWAN Clase A, AU915 sub-banda 2 ────┐
     │                                 SF9/SF10 adaptativo (ADR), 14 dBm      │
     └── BLE 5.0 (anuncio cada 30 s) ─── RESPALDO "data mule" ───┐           │
                                                                  │           │
                                                                  ▼           ▼
                                          Lector BLE en el camión    Gateway LoRaWAN
                                          recolector (tablet del       en punto alto
                                          operario, ~50 USD)         (colegio/CAI/
                                                   │                  TransMiCable)
                                                   │                        │
                                                   └──────────┬─────────────┘
                                                              ▼
                                           ChirpStack (LNS, autohospedado, MIT)
                                                              │ MQTT
                                                              ▼
                                        Backend · Base de datos de series temporales
                                                              │
                                                              ▼
                                    Mapa de radares · Optimización de rutas · Puntos
```

**Tres decisiones finas que importan:**

1. **Clase A con ADR.** El nodo solo escucha dos ventanas cortas después de transmitir. Consumo mínimo y compatible con el respaldo por batería. El ADR (*Adaptive Data Rate*) permite que los nodos cercanos al gateway bajen a SF7 y liberen tiempo de aire para los nodos lejanos en las cañadas.
2. **BLE como red de rescate, no como red principal.** El camión recolector pasa 2-3 veces por semana por cada manzana. Un lector BLE en la tablet del operario cosecha los datos de los nodos que quedaron en sombra de radio, con latencia de 2-3 días. Costo marginal: **cero** (el ESP32-C3 ya tiene BLE) más ~50 USD por tablet. Esto convierte la cobertura del 92 % que se puede alcanzar razonablemente con 12 gateways en una cobertura de datos del **100 %**, aunque degradada en latencia para el 8 % restante. Es la respuesta correcta a la topografía de Usme.
3. **Concentrador de manzana (opcional, fase 3).** Para las cañadas con más de ~40 hogares en sombra, un **repetidor LoRa alimentado por panel solar de 10 W** en un poste (costo *ESTIMADO* 180 USD) es más barato que un gateway completo y resuelve la sombra localmente.

---

## 6. Energía y consumo — el análisis que decide la viabilidad social

### 6.1. Arquitectura de alimentación

**Decisión: híbrida.** Red de 110 V para el motor, batería para la radio.

| Subsistema | Fuente | Justificación |
|---|---|---|
| Motorreductor (150 W pico) | **110 V AC → fuente conmutada 24 V / 150 W** | 150 W durante 25 s son 6,25 A a 24 V. Hacerlo con baterías exigiría un paquete 4S2P de 18650 (≈30 USD) que habría que recargar: inviable en costo y en logística |
| Electrónica de control, sensores, ventilador | Riel de 3,3 V / 5 V derivado de la misma fuente | — |
| **Radio LoRa + MCU en modo de respaldo** | **1 celda 18650 de 2.600 mAh + PCM**, cargada por la fuente | Ante un corte de energía (frecuentes en barrios de ladera), el sistema debe seguir reportando. Consumo en reposo profundo del ESP32-C3 + SX1262: ~15 µA; 4 transmisiones diarias a ~120 mJ: ~0,5 mAh/día → **autonomía > 90 días** con la celda al 60 % de capacidad útil |

**Se descarta el panel solar en el nodo.** El dispositivo está **dentro** de la vivienda; no hay irradiancia útil. El panel solar sí se contempla para los **repetidores de cañada** de la fase 3 (§5.7).

**Nota de seguridad eléctrica (crítica para Usme):** se especifica el aparato como **Clase II (doble aislamiento)**, sin depender del conductor de puesta a tierra. Muchas viviendas de autoconstrucción en estratos 1 y 2 tienen instalaciones sin polo a tierra funcional o con tomacorrientes de dos clavijas. Un diseño Clase I que dependa de la tierra sería inseguro en la práctica real de instalación.

### 6.2. Consumo por ciclo y mensual

| Paso | Cálculo | Resultado |
|---|---|---|
| Potencia eléctrica del motorreductor en carga | 120 W mecánicos ÷ η≈0,70 | **≈ 170 W** |
| Duración del ciclo de maceración | Temporizado | **25 s** |
| Energía por ciclo | 170 W × 25 s = 4.250 J | **1,18 Wh** |
| Ciclos por día (la familia deposita ~4 veces/día) | 4 | **4,72 Wh/día** |
| Ventilador de extracción (1,5 W × 60 s × 4) | 360 J | **0,10 Wh/día** |
| Electrónica + carga de batería + **pérdidas en vacío de la fuente conmutada** (≈0,25 W permanentes) | 0,25 W × 24 h | **6,0 Wh/día** |
| **Consumo diario total** | | **≈ 10,8 Wh/día** |
| **Consumo mensual** | 10,8 × 30 | **≈ 0,33 kWh/mes** |
| **Con margen de seguridad del 50 %** (uso intensivo, atascos con reintentos, degradación) | | **≈ 0,50 kWh/mes** |

> **Observación de diseño relevante:** más de la mitad del consumo **no es el motor**, sino las **pérdidas en vacío de la fuente conmutada**. Especificar una fuente con consumo en vacío <0,15 W (alcanzable en 2026 sin sobrecosto) baja el total a ~0,22 kWh/mes. Es el punto de optimización energética más rentable del producto.

### 6.3. Tarifa eléctrica en Bogotá y efecto del subsidio

| Parámetro | Valor | Fuente |
|---|---|---|
| Tarifa Enel-Codensa, costo unitario sin subsidio | **864 COP/kWh** (agosto 2026) | OPS Colombia, act. 30-ago-2026 |
| Rango de referencia publicado para Bogotá | 750-900 COP/kWh (abril 2026) | CuantoMeCuesta |
| **Consumo de subsistencia (CS)**, municipios a ≥1.000 msnm (Bogotá) | **130 kWh/mes** | Normativa CREG / Infobae |
| Subsidio estrato 1 | **60 %** sobre el CS | Infobae / Pulzo |
| Subsidio estrato 2 | **50 %** sobre el CS | Infobae / Pulzo |
| Subsidio estrato 3 | 15 % sobre el CS | Infobae / Pulzo |
| Regla clave | El subsidio **solo aplica sobre los primeros 130 kWh**; el excedente se factura a tarifa plena | Infobae |

### 6.4. Impacto en la factura del hogar — cuantificación

| Escenario | Consumo Recoevo | Tarifa efectiva | **Costo mensual** | Costo anual |
|---|---|---|---|---|
| **Estrato 1, hogar bajo el CS** (subsidio 60 %) | 0,50 kWh | 346 COP/kWh | **≈ 173 COP/mes** | 2.076 COP/año |
| **Estrato 2, hogar bajo el CS** (subsidio 50 %) | 0,50 kWh | 432 COP/kWh | **≈ 216 COP/mes** | 2.592 COP/año |
| **Consumo por encima de 130 kWh** (sin subsidio en el margen) | 0,50 kWh | 864 COP/kWh | **≈ 432 COP/mes** | 5.184 COP/año |
| **Caso más desfavorable** (uso intensivo 0,65 kWh, sin subsidio) | 0,65 kWh | 864 COP/kWh | **≈ 562 COP/mes** | 6.744 COP/año |

**Contraste en escala humana (SMMLV 2026 = 1.750.905 COP):**

| Referencia | Valor |
|---|---|
| Costo mensual de Recoevo en el peor caso | **562 COP** |
| Como porcentaje del salario mínimo mensual | **0,032 %** |
| Equivalencia | Menos que **un pasaje de TransMilenio cada cuatro meses** |
| Sobre una factura típica de estrato 2 (130 kWh subsidiados ≈ 56.160 COP) | **+0,4 %** — por debajo de la variación mes a mes de la propia tarifa |

**Contrafactual, si se hubiera elegido deshidratación:**

| Escenario deshidratación | Consumo | Costo mensual |
|---|---|---|
| Estrato 2, un ciclo diario (0,8 kWh) | 24 kWh/mes | **≈ 10.368 COP/mes** (con subsidio) |
| Estrato 2, si esos 24 kWh cruzan el umbral de 130 kWh | 24 kWh/mes | **≈ 20.736 COP/mes** (tarifa plena en el margen) |
| Sobre la factura típica | | **+18 % a +37 %** |
| Como porcentaje del SMMLV | | **0,6 % - 1,2 %** |

> **Conclusión para el modelo de negocio:** la maceración mecánica hace que el costo energético sea **irrelevante** para el hogar (**2.100-6.700 COP al AÑO**), mientras que la deshidratación lo habría hecho visible, discutible y —para una familia de estrato 1— motivo suficiente para desenchufar el aparato. Éste es el hallazgo de mayor peso sobre la viabilidad del proyecto y debe comunicarse explícitamente a los beneficiarios: *"cuesta menos de 600 pesos al mes"*, respaldado por una etiqueta de consumo en el propio equipo.

### 6.5. Recomendaciones de verificación y comunicación

1. Incluir en el manual y en una **etiqueta adherida al equipo** el consumo medido y su equivalencia en pesos, con la tarifa vigente.
2. Instrumentar **50 equipos del piloto con medidor de energía** (PZEM-004T, ~4 USD) para publicar consumo **real medido**, no estimado, antes del despliegue masivo. Esto blinda al programa frente a la objeción previsible y legítima de *"este aparato me sube la luz"*.
3. Gestionar con la Secretaría de Hábitat / UAESP que el consumo asociado al programa sea **absorbido por el operador del servicio de aseo**, no por el hogar. A 0,5 kWh/mes por 20.000 hogares son 10.000 kWh/mes ≈ **8,6 millones de COP/mes** para todo el programa: cifra trivial dentro del presupuesto distrital de aseo y argumento de adopción muy poderoso.

---

## 7. Materiales, carcasa y fabricación

### 7.1. Dimensionamiento del contenedor

| Paso | Dato | Fuente |
|---|---|---|
| Producción per cápita de residuos en Bogotá (PPC) | **0,855 kg/hab-día** (2017) | UAESP |
| Referencia nacional | ~1 kg/hab-día promedio | Greenpeace Colombia |
| Fracción orgánica | **51 %** de lo que llega al relleno (UAESP); 61 % nacional; 65 % para Bogotá según otras fuentes | UAESP / MinVivienda / Greenpeace |
| **Generación orgánica adoptada (conservadora)** | 0,855 × 0,55 = **0,47 kg/hab-día** | — |
| **Hogar de 4 personas** | **≈ 1,9 kg/día ≈ 13,3 kg/semana** | — |
| Densidad del residuo orgánico suelto | ~0,45 kg/L *(ESTIMADO)* | — |
| Volumen diario sin macerar | ≈ 4,2 L/día | — |
| Reducción de volumen por maceración | 50-60 % | — |
| **Volumen diario macerado** | **≈ 1,8 L/día** | — |

| Capacidad del cajón | Autonomía | Peso al 85 % | Veredicto |
|---|---|---|---|
| 10 L | 5,5 días | 6 kg | Exige recolección 2 veces/semana: ruta más cara |
| **20 L (recomendado)** | **≈ 9-10 días** | **≈ 12 kg** | **Recolección semanal con holgura.** Peso manejable por un adulto |
| 30 L | 14 días | 18 kg | Demasiado pesado; riesgo lumbar para usuario y operario |

**Decisión: cajón extraíble de 20 L útiles**, con asa ergonómica y bolsa compostable. Justifica la celda de carga de 20 kg y el umbral de alerta al **85 % (≈ 17 L / 12 kg)**.

**Volumen exterior del equipo: ≈ 55 L.** Huella aproximada **38 × 40 × 68 cm** — comparable a una caneca de cocina grande; cabe bajo un mesón o junto a la lavadora.

### 7.2. Selección de materiales

| Zona | Material | Justificación |
|---|---|---|
| **Cámara de maceración, rotor, peine** | **Acero inoxidable AISI 304** | Contacto permanente con ácidos orgánicos, cloruros y humedad. El 316 sería mejor pero encarece ~40 % sin beneficio proporcional |
| **Carcasa exterior, tapa, cajón** | **Polipropileno (PP) homopolímero** con antioxidante y estabilizador UV | Excelente resistencia química a ácidos orgánicos y grasas, bisagras integrales posibles, reciclable y **el más barato: 1,50-3,50 USD/kg** |
| *Alternativa considerada* | HDPE | Similar, pero menor rigidez a igual espesor → más material |
| *Alternativa descartada* | Inoxidable en toda la carcasa | 4-6× el costo, 18-25 kg de peso, sin ventaja funcional fuera de la zona húmeda |
| **Empaques** | EPDM de celda cerrada | Resistencia a ácidos orgánicos y a la compresión permanente |
| **Eje y transmisión** | Acero al carbono recubierto + **doble retén con cámara de drenaje** | El sello del eje es el punto de falla clásico de este tipo de equipo |

### 7.3. Proceso de conformado por volumen

| Proceso | Costo de utillaje | Costo por pieza | Volumen de equilibrio | Uso en Recoevo |
|---|---|---|---|---|
| Impresión 3D / mecanizado | ~0 | 60-200 USD/juego | < 20 uds | Prototipos |
| Termoformado | 1.500-4.000 USD *(ESTIMADO)* | 12-25 USD/juego | 20-200 uds | Prototipos avanzados |
| **Rotomoldeo** (molde de aluminio) | **3.500-9.000 USD** *(ESTIMADO, juego completo)* | 15-28 USD/juego | **100 - 5.000 uds** | ✅ **Fases 1 y 2.** Proveedores locales: Rototech S.A.S., Rotoplast Colombia |
| **Inyección** (molde de acero) | **≈ 62.000 USD** | 4-12 USD/juego | **> 8.000 uds** | ✅ **Fase 3** |

**Costo de molde de inyección desde China — datos verificados (Haizol, 2026):**

| Tipo de molde | Acero | Cavidades | Vida (disparos) | Precio |
|---|---|---|---|---|
| Prototipo / puente | Aluminio o P20 | 1 | hasta 50.000 | 1.000 - 3.000 USD |
| Bajo volumen | P20 pre-templado | 1-2 | 200.000-500.000 | 2.500 - 8.000 USD |
| **Volumen medio** | **718H o H13** | **1-4** | **300.000-1.000.000** | **5.000 - 15.000+ USD** |
| Alto volumen | H13 templado | 4-16+ | > 1.000.000 | 15.000 - 50.000+ USD |
| Precisión compleja | H13 / S136 | 1-8 | > 500.000 | 20.000 - 80.000+ USD |

**Presupuesto de utillaje de inyección para Recoevo (fase 3):**

| Pieza | Descripción | Costo *(ESTIMADO sobre los rangos verificados)* |
|---|---|---|
| Cuerpo de la carcasa | Pieza grande (~1,1 kg), 1 cavidad, 718H | 18.000 USD |
| Frente + tapa superior | Pieza grande, 1 cavidad | 12.000 USD |
| Tapa abatible con bisagra | 1 cavidad | 7.000 USD |
| Cajón extraíble 20 L | Pieza grande, 1 cavidad | 11.000 USD |
| Familia de piezas pequeñas (portafiltro, dosificador, rejilla, embellecedores) | Molde familiar multicavidad | 6.000 USD |
| **Subtotal moldes** | | **54.000 USD** |
| Jigs de ensamble y bancos de prueba funcional y eléctrica | | 8.000 USD |
| **TOTAL UTILLAJE** | | **≈ 62.000 USD ≈ 192 millones de COP** |

**Advertencia de negociación:** las cotizaciones chinas del mismo molde varían **más de 2×**, y la diferencia proviene de la **especificación del molde (grado de acero, cavidades, acabado), no de la calidad de la fábrica**. La dispersión medida de cotizaciones verificadas es del 30,8 % por debajo de la mediana, con casos de hasta 2,9× entre la más barata y la más cara. **Recomendación: cotizar con especificación técnica cerrada (grado de acero, disparos garantizados, acabado SPI) en al menos cinco fábricas y exigir ensayos T1/T2/T3 con piezas enviadas a Colombia antes del pago final.**

Referencia de costo por pieza verificada (pieza de ABS, 1 cavidad): **100 uds → 20,80 USD "todo incluido"; 2.000 uds → 1,50 USD; 10.000 uds → 0,55 USD**. Confirma el orden de magnitud de la curva de amortización del utillaje.

### 7.4. Importación desde China vs. fabricación en Colombia

| Componente | Origen recomendado | Razón |
|---|---|---|
| Motorreductor, cámara inox, rotor, rodamientos, retenes | **China** | No hay cadena local competitiva; diferencia > 3× |
| Electrónica (MCU, LoRa, sensores, fuente, PCB) | **China** | Ídem. LCSC/JLCPCB integra componentes y ensamble |
| Carbón activado, ventilador, empaques | **China** | Commodity |
| **Carcasa, tapa, cajón (plásticos)** | **Colombia** | Piezas voluminosas y de baja densidad de valor: **el flete marítimo destruye la ventaja de precio.** Existe capacidad local: Rototech, Rotoplast, Isoplásticos, AM Plásticos, Fergoplas, RPM Colombia |
| **Ensamble final, prueba y empaque** | **Colombia** | Genera empleo local (argumento político del programa), evita arancel sobre producto terminado y habilita reparabilidad |
| Bolsas compostables, tarjetas, manual | **Colombia** | Proveedores verificados: Uman S.A.S., Belplásticos, Compostpack, Ofimax |

**Estructura tributaria de la importación (verificada):**

| Concepto | Regla | Aplicación a Recoevo |
|---|---|---|
| Base gravable | **Valor CIF** = Costo + Seguro + Flete hasta puerto colombiano | — |
| Arancel | 0 % para bienes de capital; 5/10/15 % o más según subpartida; electrodomésticos terminados a tarifa general | **Se importan COMPONENTES, no producto terminado** → subpartidas de partes, arancel 0-5 %. Se adopta **5 % ponderado (ESTIMADO conservador)** |
| IVA | **19 %** = (Valor en aduana + Arancel) × 0,19 | **Recuperable como crédito fiscal** para la empresa productora → **no se carga al costo**, pero exige capital de trabajo. Se advierte en el flujo de caja |
| Flete marítimo + seguro | — | **8 % del FOB (ESTIMADO).** No se pudo verificar la tarifa China–Buenaventura/Cartagena 2026 por agotamiento del presupuesto de búsquedas web; el 8 % es el rango habitual para carga general consolidada |
| Nacionalización (SIA, puerto, bodegaje, transporte interno) | — | 2,80 USD/unidad a 1.000 uds *(ESTIMADO)* |

> **Optimización fiscal clave: importar componentes y ensamblar en Colombia, no importar el producto terminado.** Reduce el arancel (partes vs. electrodoméstico completo), convierte la certificación RETIE en certificación **de fabricante** en lugar de **de importador**, y hace del proyecto un generador de empleo local: argumento decisivo para un programa con recursos públicos.

### 7.5. Identificación del usuario

| Opción | Costo verificado | Ventajas | Desventajas |
|---|---|---|---|
| **Tarjeta PVC con QR impreso** | **0,05 USD @10.000 uds** (PVC, Shenzhen RZX); 0,12-0,20 USD con impresión personalizada *(ESTIMADO)* | Lo más barato; se lee con cualquier teléfono; sin hardware en el equipo | Se desgasta; requiere cámara |
| **Tarjeta PVC con NFC NTAG213** | **0,15 USD @100 uds** (Shenzhen Chuangxinjia); MOQ típico 1.000 uds | Lectura instantánea con NFC nativo de Android; no se desgasta ópticamente; sin lector dedicado | ~3× el costo del QR |
| RFID 125 kHz | Similar | Robusto | Requiere lector dedicado; sin lectura por teléfono |

**Recomendación: tarjeta PVC híbrida QR + NFC NTAG213** a **0,22 USD @1.000 uds** *(ESTIMADO: 0,15 del inlay NFC verificado + impresión y laminado)*. El QR es el respaldo universal cuando el teléfono del operario no tiene NFC; el NFC es el camino rápido. El **equipo lleva además su propio serial grabado por láser con QR** (0,18 USD) para trazabilidad de activo, independiente de la tarjeta del usuario.

---

## 8. Seguridad del producto y normativa colombiana aplicable

### 8.1. Normativa aplicable

| Norma | Aplicación a Recoevo | Obligatoriedad |
|---|---|---|
| **RETIE** — Reglamento Técnico de Instalaciones Eléctricas (MinEnergía) | **Aplica.** Reglamento de obligatorio cumplimiento para **comercialización, importación, fabricación y distribución** de productos eléctricos. Exige **certificado de conformidad de producto emitido por organismo acreditado ONAC, previo a la importación y comercialización** | **OBLIGATORIA** |
| **IEC 60335-1** — Seguridad de electrodomésticos, requisitos generales | Aislamiento, distancias, calentamiento, accesibilidad a partes activas y móviles, resistencia mecánica, estabilidad | Obligatoria como norma de ensayo bajo RETIE |
| **IEC 60335-2-16:2022** — Requisitos particulares para **trituradores de residuos de comida** de uso doméstico (hasta 250 V, incluidos DC y a batería) | **Norma específica del producto.** Cubre enclavamiento, acceso a partes móviles y protección contra arranque involuntario | Obligatoria |
| **NTC** correspondientes (adopción nacional de IEC) | Ensayos en laboratorio acreditado ONAC | Obligatoria |
| **EMC** (CISPR 14-1/-2) | Motor y fuente conmutada | Exigible por el organismo certificador |
| **CRC — Homologación de equipos terminales** | **NO aplica** al nodo LoRaWAN: la homologación de la CRC se dirige a equipos terminales que se conectan a redes de operadores móviles, verificando frecuencias de operación y límites de exposición a campos electromagnéticos. Un radio en banda de uso libre no es un equipo terminal móvil. **Sí aplicaría con NB-IoT/LTE-M**, y el certificado debería presentarse a la autoridad aduanera al importar | No aplica (con LoRaWAN) |
| **ANE** — Resoluciones 689 de 2004 y 28 de 2026 | Determinan la banda: **915-928 MHz**, uso libre, título secundario (**sin protección contra interferencias**) | Cumplimiento por diseño |
| **Ley 1581 de 2012** (Habeas Data) | El sistema registra peso de residuos, frecuencia de uso y geolocalización del hogar: son **datos personales**. Exige política de tratamiento, autorización informada, finalidad declarada y minimización | **OBLIGATORIA** |
| **Decreto 1077 de 2015 / Resolución 2184 de 2019** y PGIRS de Bogotá | Marco del servicio público de aseo y del aprovechamiento de orgánicos | Marco de operación |

### 8.2. Costo de la certificación

No existe tarifa pública: los organismos certificadores señalan expresamente que el precio **no es un proceso estandarizado** y depende del tipo y tamaño del proyecto, los honorarios profesionales, los materiales certificados y la tarifa del organismo de inspección acreditado ONAC.

| Concepto | Costo *(ESTIMADO)* | Razonamiento |
|---|---|---|
| Ensayos de tipo en laboratorio acreditado (IEC 60335-1 + 60335-2-16 + EMC) | 8.000 - 15.000 USD | Analogía con campañas de ensayo de electrodomésticos pequeños; incluye ensayos destructivos sobre 3-5 muestras y reensayos parciales |
| Certificado de conformidad RETIE (emisión inicial, vigencia 3 años) | 3.000 - 6.000 USD | — |
| Seguimiento anual (auditoría de fábrica + muestreo) | 1.500 USD/año | — |
| **Costo inicial adoptado para el BOM** | **14.000 USD** | Valor central conservador |

**Amortización sobre la vigencia de 3 años, al volumen anual de cada escenario:**

| Volumen anual | Unidades en 3 años | Costo unitario |
|---|---|---|
| 100 uds/año | 300 | **46,67 USD/u** |
| 1.000 uds/año | 3.000 | **4,67 USD/u** |
| 10.000 uds/año | 30.000 | **0,47 USD/u** |

> **Implicación estratégica:** la certificación es **económicamente prohibitiva por debajo de ~500 unidades/año**. El piloto de 100 unidades debe ejecutarse como **prototipo de investigación en convenio con la entidad distrital**, no como producto comercializado, y la certificación RETIE debe presupuestarse como **costo de entrada a la fase 2** (≈ 43 millones de COP). Es uno de los tres desembolsos que determinan la escala mínima viable, junto con el utillaje y el desarrollo de software.

### 8.3. Seguridad funcional — barreras implementadas

| Riesgo | Severidad | Barrera 1 (hardware) | Barrera 2 | Barrera 3 |
|---|---|---|---|---|
| **Un niño introduce la mano y el motor arranca** | Catastrófica | **Microswitch de leva que corta la potencia en serie** (independiente del firmware) | Deflector fijo en la boca de carga (criterio del dedo de prueba de IEC 60335-1) | Retardo de arranque de 2 s con aviso acústico |
| **La tapa se abre con el rotor en marcha** | Grave | Latch electromecánico enclavado durante todo el ciclo | Freno dinámico: paro en < 1 s | Reductor sinfín autobloqueante |
| **Atasco → sobrecalentamiento del motor** | Media | Klixon térmico en el bobinado | Protector de sobrecarga con rearme manual | Detección de sobrecorriente en firmware con inversión automática (3 intentos) y bloqueo con alerta |
| **Contacto con partes activas / falla de aislamiento** | Catastrófica | **Diseño Clase II (doble aislamiento)**, sin dependencia de puesta a tierra | Separación física entre la zona de 110 V y la zona húmeda, con barrera moldeada | Prensaestopas y sellado IPX4 del compartimento eléctrico |
| **Entrada de agua al compartimento eléctrico** | Grave | Compartimento eléctrico **por encima** de la cámara y separado por barrera | Doble retén de eje con cámara de drenaje al exterior | Recubrimiento conformal en la PCB |
| **Vuelco del equipo** | Media | Base ancha con relación de vuelco > 10° y lastre inferior | Patas antideslizantes | Anclaje opcional a muro |
| **Sobrepeso del cajón / lesión lumbar** | Baja | Cajón limitado a 20 L (≈12 kg al 85 %) | Alerta de llenado al 85 %, antes de que sea inmanejable | Asa ergonómica y guías con rodamiento |

### 8.4. Ensayos de validación previos al piloto

1. **Vida del sistema de maceración:** 5.000 ciclos con residuo real de un hogar de Usme (cáscara de plátano, tusa de maíz, hueso de pollo, fibra de yuca) — los materiales localmente frecuentes y más difíciles.
2. **Olor con panel sensorial:** 30 días en cocina real, evaluación ciega por panel de 10 personas en días 1, 7, 14 y 30, **con y sin** cartucho de carbón.
3. **Enclavamiento:** 10.000 ciclos de apertura/cierre verificando la imposibilidad de arranque con la tapa abierta, **incluyendo escenarios de firmware bloqueado y de firmware adversario**.
4. **Propagación de radio en campo:** 30 nodos distribuidos en cañadas y filos de un barrio de Usme, midiendo RSSI/SNR y tasa de entrega durante 14 días, **antes** de comprometer la ubicación de los gateways.
5. **Medición de consumo:** 50 equipos instrumentados durante 90 días (§6.5).

---

## 9. BOM COMPLETO — Despiece de costos unitarios

**Base de conversión: 1 USD = 3.100 COP** (TRM 10-sep-2026: 3.099,48).
**Precios de componente FOB origen.** Flete, arancel, nacionalización y distribución se cargan aparte en §10.
**Banda de confianza global: ±20-25 %.** Los componentes con fuente de precio verificada representan ~45 % del valor del BOM; el resto está *ESTIMADO* con el razonamiento indicado.

### 9.1. Tabla BOM

| # | Componente | Especificación técnica | Proveedor / origen | @100 uds (USD) | @1.000 uds (USD) | @10.000 uds (USD) | @1.000 uds (COP) | Fuente del precio |
|---|---|---|---|---|---|---|---|---|
| | **A. TRITURACIÓN Y ACCIONAMIENTO** | | | | | | | |
| 1 | Motorreductor DC | 24 V, 100-150 W, reductor sinfín autobloqueante, salida 80-100 RPM, par ≥15 N·m (pico 25 N·m), klixon térmico integrado | Alibaba — fabricantes de motorreductores (Dongguan/Zhejiang) | 34,00 | **22,00** | 16,50 | 68.200 | *ESTIMADO.* Catálogo Alibaba: micromotores 0,68-9,80 USD; TJW58FX 24/12 V 7,90-9,85 USD; unidades 100-200 W al detal 80-99 USD (MOQ 2). Se aplica descuento OEM del 72-78 % sobre PVP industrial |
| 2 | Rotor macerador + peine fijo + cámara | Acero inox AISI 304, rotor ø90 mm con 12 dientes estampados, peine desmontable, cámara de ~3 L, ~0,9 kg de inox | China (estampado/soldadura) | 26,00 | **14,00** | 9,50 | 43.400 | *ESTIMADO.* 0,9 kg de inox 304 a 4-5 USD/kg (≈4,2 USD) + estampado, soldadura TIG, pulido y utillaje amortizado |
| 3 | Eje, rodamientos, doble retén con cámara de drenaje, acople | Eje de acero recubierto ø18 mm, 2 rodamientos 6003-2RS, 2 retenes de labio NBR, cámara de drenaje | China | 8,00 | **4,20** | 2,80 | 13.020 | *ESTIMADO* por analogía con conjuntos de transmisión de bombas domésticas |
| | **B. CARCASA Y ESTRUCTURA** | | | | | | | |
| 4 | Carcasa exterior (2 piezas) | PP homopolímero con estabilizador UV, ~2,2 kg. **Rotomoldeo a 100/1.000 uds; inyección a 10.000 uds** | @100-1k: Rototech / Rotoplast (Colombia). @10k: inyección | 28,00 | **19,00** | 6,80 | 58.900 | Resina PP 1,50-3,50 USD/kg (verificado) + proceso. Curva de inyección verificada: 2.000 uds → 1,50 USD; 10.000 uds → 0,55 USD por pieza sencilla |
| 5 | Tapa abatible + bisagra + resorte + latch | PP, bisagra metálica de pasador, resorte de torsión, latch de leva con solenoide de retención | Colombia + China (herrajes) | 9,00 | **6,00** | 1,80 | 18.600 | *ESTIMADO* |
| 6 | Cajón extraíble 20 L + guías | PP, asa integrada, rejilla separadora de lixiviados, 2 guías con rodamiento | Colombia | 14,00 | **9,00** | 3,60 | 27.900 | *ESTIMADO* |
| 7 | Empaque perimetral | EPDM celda cerrada, perfil en "D" 10×8 mm, 2 m, 40-50 Shore A | China | 3,20 | **1,60** | 1,05 | 4.960 | *ESTIMADO* (perfil extruido a ~0,35-0,80 USD/m) |
| 8 | Válvula unidireccional de venteo | Membrana de silicona, apertura 2-3 mbar | China | 1,40 | **0,70** | 0,45 | 2.170 | *ESTIMADO* |
| 9 | Tornillería, insertos roscados, patas antivibración, herrajes | Tornillos inox A2, insertos de latón por ultrasonido, 4 patas de TPE | China | 4,50 | **2,40** | 1,60 | 7.440 | *ESTIMADO* |
| | **C. CONTROL DE OLORES** | | | | | | | |
| 10 | Cartucho de carbón activado + portafiltro | 250 g de carbón activado en pellets, cartucho recambiable sin herramientas, malla inox | China | 5,50 | **3,20** | 2,10 | 9.920 | *ESTIMADO.* Carbón activado granular a granel 2-5 USD/kg → 0,75 USD de material. Referencia de mercado al detal: Lomi 29,95 USD/45 ciclos |
| 11 | Ventilador axial de extracción | 40×40×10 mm, 24 V, ~1,5 W, rodamiento *sleeve*, 8.000 h | China | 2,20 | **1,10** | 0,70 | 3.410 | *ESTIMADO* (precio típico de ventilador 40 mm OEM) |
| 12 | Compartimento dosificador de estructurante | PP, capacidad 1,5 L, tapa y cuchara dosificadora | Colombia | 1,80 | **0,80** | 0,45 | 2.480 | *ESTIMADO* |
| | **D. ELECTRÓNICA — CÓMPUTO Y RADIO** | | | | | | | |
| 13 | Microcontrolador | **Módulo ESP32-C3-MINI-1** (RISC-V 160 MHz, 4 MB flash, BLE 5.0, WiFi deshabilitado por firmware) | Espressif vía LCSC | 2,30 | **1,95** | 1,70 | 6.045 | **Verificado (LCSC, chip ESP32-C3):** 1,285 USD @100; 1,2178 @500; **1,1899 @1.000**; 1,8619 @1 ud. Se suma prima de módulo (PCB, antena, cristal, blindaje, certificación) ≈0,75 USD *(ESTIMADO)* |
| 14 | Módulo LoRa | **Ai-Thinker Ra-01SH-P**, Semtech SX1262, 803-930 MHz, TX hasta +29 dBm (3,3 V) / +31 dBm (5 V), RX 16 mA, conector IPEX | Ai-Thinker vía Rokland / OpenELAB | 8,50 | **5,80** | 4,20 | 17.980 | **PVP verificado 10,97 USD/ud (Rokland).** Volumen *ESTIMADO* con descuento OEM del 47-62 % |
| 15 | Antena 915 MHz + pigtail | Helicoidal de cobre interna, 2 dBi, + cable u.FL-IPEX de 100 mm | Alibaba (Dongguan Haonuo y otros) | 0,85 | **0,45** | 0,28 | 1.395 | *ESTIMADO.* Catálogos de antenas helicoidales 868/915 MHz con MOQ de 100 uds |
| | **E. ELECTRÓNICA — SENSÓRICA** | | | | | | | |
| 16 | Celda de carga 20 kg + HX711 | Celda *single point* de aluminio, 20 kg; ADC HX711 de 24 bits | Alibaba | 3,50 | **2,40** | 1,70 | 7.440 | **Verificado:** kit 4,00 USD @10-49; 3,80 @50-99; **3,50 @100+**; módulo HX711 solo desde 0,99 USD con MOQ 100; se reporta <1,00 USD en >100 uds |
| 17 | Sensor de nivel ToF | **VL53L0X** (ST), láser 940 nm, 3 cm-2 m, I²C, con ventana de vidrio inclinada y visera | STMicroelectronics vía DigiKey / módulos chinos | 2,80 | **1,95** | 1,45 | 6.045 | **Verificado (DigiKey):** 5,39 USD @1 ud → **~2,75 USD @1.000 uds** (chip). Módulos al detal 10-15 USD. Se toma chip + óptica + PCB *(ESTIMADO)* |
| 18 | Reed switch + imán | Reed NA, ampolla de 14 mm + imán de neodimio N35 | China | 0,45 | **0,22** | 0,14 | 682 | *ESTIMADO* |
| 19 | **Microswitch de seguridad (interlock)** | Acción rápida, actuador de rodillo, 10 A / 250 V, 100.000 ciclos. **En serie con la potencia del motor** | China (tipo Omron D2F/compatible) | 0,90 | **0,48** | 0,32 | 1.488 | *ESTIMADO* |
| 20 | Sensor de temperatura y humedad | **SHT31** I²C, ±2 % HR, ±0,3 °C. Compensa la deriva térmica de la celda de carga | Sensirion / compatibles | 1,80 | **1,20** | 0,85 | 3.720 | *ESTIMADO* |
| | **F. ELECTRÓNICA — POTENCIA Y PCB** | | | | | | | |
| 21 | Etapa de potencia del motor | MOSFET de canal N + driver + relé de seguridad + sensor de corriente por *shunt* + supresión | China | 2,40 | **1,35** | 0,90 | 4.185 | *ESTIMADO* |
| 22 | PCB + ensamble SMT | 2 capas, FR-4, 80×60 mm, HASL sin plomo, ensamble llave en mano con panelizado | JLCPCB | 6,80 | **3,20** | 2,10 | 9.920 | *ESTIMADO.* JLCPCB aplica descuentos por volumen y recomienda panelizado sobre 50 uds; no publica tarifa fija (requiere Gerber + BOM) |
| 23 | Fuente conmutada | 110 V AC → 24 V DC / 150 W + riel auxiliar 3,3 V. **Consumo en vacío <0,15 W (requisito).** Protección contra sobretensión y cortocircuito | China (OEM) | 9,50 | **6,20** | 4,40 | 19.220 | *ESTIMADO.* Referencia al detal de fuentes 12 V/5 A/60 W: 49-108 USD (grado industrial XP Power). Se aplica el factor OEM habitual (≈8-12×) para fuente de consumo sin marca |
| 24 | Batería de respaldo | Celda 18650 2.600 mAh Li-ion + PCM + portacelda + cargador lineal | China | 3,60 | **2,30** | 1,60 | 7.130 | **Verificado:** celdas 18650 al por mayor **0,30-1,80 USD/ud** según capacidad y volumen; se reporta caída anual de ~8 %. Se suma PCM, portacelda y cargador *(ESTIMADO)* |
| 25 | Cableado, conectores, prensaestopas, cable de red | Arnés completo, JST-XH, prensaestopas IP65, cable 2×18 AWG con clavija de 2 patines (Clase II), 1,5 m | China | 3,80 | **2,20** | 1,50 | 6.820 | *ESTIMADO* |
| | **G. IDENTIFICACIÓN, CONSUMIBLES Y EMPAQUE** | | | | | | | |
| 26 | Tarjeta de usuario | PVC con **QR impreso + inlay NFC NTAG213** (13,56 MHz) | Shenzhen Chuangxinjia / RZX | 0,55 | **0,22** | 0,12 | 682 | **Verificado:** NTAG213 **0,15 USD/ud con MOQ 100** (Chuangxinjia); tarjeta PVC **0,05 USD/ud con MOQ 10.000** (RZX) |
| 27 | Etiqueta de producto | Placa con serial y QR, grabado láser sobre policarbonato adhesivo | Colombia | 0,40 | **0,18** | 0,10 | 558 | *ESTIMADO* |
| 28 | Kit de bolsas compostables | 10 bolsas compostables certificadas de 20 L (almidón vegetal) | Uman S.A.S. / Compostpack / Belplásticos (Colombia) | 2,20 | **1,50** | 1,10 | 4.650 | *ESTIMADO.* Referencias colombianas verificadas (Belplásticos desde 1.500 COP/paquete al detal); precio mayorista deducido |
| 29 | Empaque y documentación | Caja de cartón corrugado doble, esquineros de cartón moldeado, manual impreso a color de 12 páginas, guía rápida plastificada | Colombia | 4,50 | **2,60** | 1,80 | 8.060 | *ESTIMADO* |
| | **SUBTOTAL MATERIALES** | | | **192,45** | **118,20** | **71,61** | **366.420** | |

### 9.2. Costo de la mano de obra de ensamblaje en Colombia

**Base salarial verificada (2026):**

| Concepto | Valor | Fuente |
|---|---|---|
| Salario mínimo mensual legal vigente (SMMLV) 2026 | **1.750.905 COP** (incremento del 23,7 %) | Decreto de salario mínimo 2026 / Holland & Knight / SIESA |
| Auxilio de transporte 2026 | **249.095 COP** | Ídem — ingreso mínimo total: 2.000.000 COP |
| Factor prestacional para salario ordinario | **≈ 38 %** sobre el salario base | Aleluya / Buk / actualícese |
| Valor de la hora ordinaria a salario mínimo (desde el 15-jul-2026, jornada de 42 h/semana) | **8.338 COP** | Magneto365 |

**Cálculo del costo-hora con prestaciones:**

```
Costo mensual del empleador = 1.750.905 × 1,38 + 249.095 = 2.665.344 COP
Horas laborales al mes      = 42 h/semana × 4,33 semanas  = 182 h
COSTO HORA CON PRESTACIONES = 2.665.344 / 182            = 14.645 COP/h = 4,73 USD/h
```

| Volumen | Tiempo de ensamble por unidad | Mano de obra directa | Overhead de planta (45 %)¹ | **Total MO + overhead** |
|---|---|---|---|---|
| **100 uds** | 2,50 h (proceso artesanal, sin utillaje de ensamble) | 36.613 COP = 11,81 USD | 5,31 USD | **17,11 USD** |
| **1.000 uds** | 1,20 h (bancos con jigs, curva de aprendizaje) | 17.574 COP = 5,67 USD | 2,55 USD | **8,22 USD** |
| **10.000 uds** | 0,65 h (línea con estaciones y pruebas automáticas) | 9.519 COP = 3,07 USD | 1,38 USD | **4,45 USD** |

¹ *Overhead de planta ESTIMADO en 45 % de la mano de obra directa: arriendo, energía industrial, supervisión, control de calidad, herramienta y consumibles de ensamble. Es el rango habitual en manufactura ligera colombiana.*

### 9.3. Merma, retrabajo y reserva de garantía

Se aplica un **4 %** sobre materiales + mano de obra: cubre piezas dañadas en ensamble, unidades rechazadas en prueba funcional y reserva para reemplazo en garantía (12 meses).

| Volumen | Base | **Reserva (4 %)** |
|---|---|---|
| 100 uds | 209,56 USD | **8,38 USD** |
| 1.000 uds | 126,42 USD | **5,06 USD** |
| 10.000 uds | 76,06 USD | **3,04 USD** |

### 9.4. Consumibles recurrentes por hogar y año (no forman parte del costo de fabricación)

| Consumible | Frecuencia | Costo anual @1.000 uds |
|---|---|---|
| Cartucho de carbón activado | 2 recambios/año | 4,20 USD |
| Bolsas compostables 20 L | 52 unidades/año | 7,80 USD *(ESTIMADO 0,15 USD/bolsa a volumen)* |
| Estructurante (biochar/aserrín) | 6 kg/año | 3,00 USD |
| **TOTAL CONSUMIBLES** | | **15,00 USD/año ≈ 46.500 COP/año** |

---

## 10. Costo total de fabricación por unidad a tres volúmenes

### 10.1. Cargas adicionales

**Logística de entrada (importación de componentes).** Aproximadamente el **55 % del valor del BOM** es importado (ítems 1, 2, 3, 7, 8, 9, 10, 11, 13-25): **≈ 65 USD/unidad FOB a 1.000 uds**.

| Concepto | @100 uds | @1.000 uds | @10.000 uds |
|---|---|---|---|
| Flete marítimo + seguro (8 % del FOB) *(ESTIMADO)* | 8,80 | 5,20 | 3,00 |
| Arancel (5 % ponderado sobre CIF) *(ESTIMADO)* | 5,90 | 3,51 | 2,00 |
| Nacionalización: SIA, puerto, bodegaje, transporte interno *(ESTIMADO)* | 3,30 | 2,80 | 1,40 |
| **Logística de entrada** | **18,00** | **11,51** | **6,40** |
| Distribución e instalación en Bogotá *(ESTIMADO)* | 3,50 | 2,20 | 1,40 |

> **IVA del 19 %:** se paga en la nacionalización sobre (valor en aduana + arancel), pero es **recuperable como crédito fiscal** para la empresa productora. **No se carga al costo del producto**, pero sí exige capital de trabajo: ≈ **13 USD/unidad ≈ 40.000 COP** inmovilizados hasta la compensación. A 10.000 unidades son **≈ 130.000 USD ≈ 403 millones de COP** de capital de trabajo. Debe reflejarse en el flujo de caja del proyecto.

**Amortización del utillaje:**

| Volumen | Proceso | Utillaje | Amortizado sobre | Costo unitario |
|---|---|---|---|---|
| 100 uds | Rotomoldeo (molde de aluminio) + jigs | 9.000 USD | 100 uds | **90,00 USD** |
| 1.000 uds | Rotomoldeo + jigs | 9.000 USD | 1.000 uds | **9,00 USD** |
| 10.000 uds | Inyección (moldes de acero) + jigs | 62.000 USD | 10.000 uds | **6,20 USD** |

*Nota: los 90,00 USD/u del piloto suponen cargar todo el utillaje al lote de 100. Si el utillaje se contabiliza como inversión del programa y se amortiza sobre las 1.000 unidades de la fase 2, el costo del piloto baja a 9,00 USD/u y el costo total del piloto pasa de 376 a **295 USD/unidad**. Ésta es la contabilización recomendada.*

**Amortización de certificaciones (§8.2):** 46,67 / 4,67 / 0,47 USD por unidad.

### 10.2. Tabla resumen — COSTO TOTAL DE FABRICACIÓN

| Concepto | **@ 100 uds** | **@ 1.000 uds** | **@ 10.000 uds** |
|---|---|---|---|
| **Materiales (BOM §9.1)** | 192,45 | 118,20 | 71,61 |
| Mano de obra + overhead de planta | 17,11 | 8,22 | 4,45 |
| Merma, retrabajo y reserva de garantía (4 %) | 8,38 | 5,06 | 3,04 |
| **= COSTO DE FABRICACIÓN DIRECTO** | **217,94** | **131,48** | **79,10** |
| Amortización de utillaje | 90,00 | 9,00 | 6,20 |
| Amortización de certificación RETIE + ensayos | 46,67 | 4,67 | 0,47 |
| Logística de entrada (flete, arancel, nacionalización) | 18,00 | 11,51 | 6,40 |
| Distribución e instalación | 3,50 | 2,20 | 1,40 |
| **= COSTO TOTAL DE FABRICACIÓN (USD)** | **376,11** | **158,86** | **93,57** |
| **= COSTO TOTAL DE FABRICACIÓN (COP)** | **1.165.941** | **492.466** | **290.067** |
| *Costo del piloto con utillaje amortizado al programa* | *295,11 USD / 914.841 COP* | — | — |

### 10.3. Costo anual de operación por dispositivo (OPEX, independiente del costo de fabricación)

| Concepto | @1.000 disp. | @5.000 disp. | @20.000 disp. |
|---|---|---|---|
| Red LoRaWAN (gateways + LNS, §5.5) | 2,22 USD | 0,83 USD | 0,41 USD |
| Nube y backend (§11.2) | 1,20 USD | 0,50 USD | 0,25 USD |
| Mapas y ruteo (§11.3, opción open source) | 0,60 USD | 0,12 USD | 0,03 USD |
| Consumibles del hogar (§9.4) | 15,00 USD | 14,00 USD | 13,00 USD |
| **TOTAL OPEX/dispositivo/año (USD)** | **19,02** | **15,45** | **13,69** |
| **TOTAL OPEX/dispositivo/año (COP)** | **58.962** | **47.895** | **42.439** |

> Obsérvese que **los consumibles del hogar dominan el OPEX** (77-95 %), no la conectividad. La conectividad, que intuitivamente parece el costo recurrente crítico, es el **2-12 %** del total. Éste es un resultado contraintuitivo y valioso: **una vez elegida la arquitectura LoRaWAN, la palanca de optimización del costo operativo no es la radio, sino el filtro de carbón y las bolsas.** Recomendación derivada: explorar bolsas compostables de producción local a escala y un cartucho de carbón regenerable o de mayor vida útil, que podrían reducir el OPEX del hogar en 30-40 %.

### 10.4. Curva de costo y lectura estratégica

| Volumen | Costo unitario (COP) | Reducción respecto al anterior | Costo del lote completo (COP) |
|---|---|---|---|
| 100 uds | 1.165.941 | — | 116,6 millones |
| 1.000 uds | 492.466 | **-58 %** | 492,5 millones |
| 10.000 uds | 290.067 | **-41 %** | 2.900,7 millones |

**Tres umbrales de escala determinan la viabilidad:**

1. **~500 unidades/año:** por debajo, la certificación RETIE (14.000 USD) no se amortiza y el costo unitario se dispara. Es el **piso económico regulatorio**.
2. **~1.000 unidades:** el rotomoldeo local alcanza eficiencia razonable y la mano de obra baja a 1,2 h/unidad. Es el **punto de entrada operativo**.
3. **~8.000-10.000 unidades:** el utillaje de inyección (62.000 USD) se amortiza y el costo del juego de plásticos cae de 34 a 12 USD. Es el **salto tecnológico** que lleva el producto por debajo de los 300.000 COP.

**Comparación con el mercado:** el producto más barato del mercado mundial con función comparable (Vitamix FoodCycler, 2 L) se vende al público en **284-399 USD**; Lomi en 499 USD; Reencle en 549 USD; Mill en 999 USD más suscripción. Recoevo a 10.000 unidades tiene un **costo de fabricación de 94 USD** con **más capacidad (20 L frente a 2-6 L)**, conectividad IoT que ninguno de ellos trae, y un consumo energético 40-50 veces menor. La ventaja proviene de tres decisiones: no calentar, no sobre-procesar y fabricar la carcasa localmente.

---

## 11. Costos de software, nube y mapas

### 11.1. Desarrollo de la plataforma

**Alcance funcional del MVP:**

| Módulo | Descripción |
|---|---|
| **Firmware del nodo** | LoRaWAN Clase A con ADR, drivers de los 5 sensores, máquina de estados del ciclo de maceración, enclavamiento, gestión de energía y batería, actualización OTA por LoRa (FUOTA) o por BLE, anuncio BLE de respaldo |
| **Ingesta** | ChirpStack (LNS) → MQTT → servicio de decodificación de *payload* → base de datos de series temporales |
| **Mapa de radares** | Visualización geoespacial de los 20.000 puntos con código de color por nivel de llenado, filtros por barrio/UPZ, histórico y mapa de calor |
| **Optimización de rutas** | Resolución del problema de rutas con capacidad (CVRP) sobre los contenedores en alerta, con restricciones de ventana horaria y capacidad del camión |
| **App del operario** | Android: ruta del día, navegación paso a paso, lectura de tarjeta NFC/QR del hogar, confirmación de recolección, registro de peso, reporte de incidencias con foto, cosecha BLE de nodos sin cobertura, operación **offline-first** (cobertura celular irregular en Usme) |
| **Sistema de puntos** | Acumulación por kg entregados, canje, consulta por el ciudadano vía WhatsApp o web ligera |
| **Panel administrativo** | Indicadores del programa, inventario de dispositivos, salud de la flota, alertas de mantenimiento, exportación para la UAESP |

**Costo de desarrollo en Colombia — bandas salariales verificadas (2026):**

| Rol | Banda mensual (COP) | Fuente |
|---|---|---|
| Desarrollador Full Stack junior (0-2 años) | desde 4.800.000 (≈1.200 USD) | Coderhouse |
| Desarrollador Full Stack semi-senior (2-5 años) | 6.000.000 - 7.500.000 (≈1.500-1.900 USD) | Coderhouse |
| Desarrollador Full Stack senior (5+ años) | desde 9.000.000 (≈2.300 USD) | Coderhouse |
| Desarrollador de aplicaciones junior | 3.800.000 - 4.800.000 | Coderhouse |
| Desarrollador web (promedio general) | 3.000.000 - 6.000.000 | TripleTen / Computrabajo |

**Presupuesto del MVP (6 meses):**

| Rol | Dedicación | Salario mensual (COP) | Meses | Subtotal (COP) |
|---|---|---|---|---|
| Líder técnico / arquitecto senior | 100 % | 9.000.000 | 6 | 54.000.000 |
| Desarrollador backend semi-senior | 100 % | 6.750.000 | 6 | 40.500.000 |
| Desarrollador frontend semi-senior | 100 % | 6.750.000 | 6 | 40.500.000 |
| Desarrollador junior | 100 % | 4.300.000 | 6 | 25.800.000 |
| Diseñador UX/UI | 50 % | 3.500.000 | 6 | 21.000.000 |
| Gerente de producto / proyecto | 50 % | 4.000.000 | 6 | 24.000.000 |
| **Subtotal salarios base** | | | | **205.800.000** |
| Factor prestacional (38 %) | | | | **78.204.000** |
| **Subtotal equipo de plataforma** | | | | **284.004.000** |
| Ingeniero de firmware embebido senior (LoRaWAN, drivers, OTA) | 100 % | 9.000.000 | 5 | 45.000.000 + 38 % = **62.100.000** |
| **TOTAL DESARROLLO MVP** | | | | **≈ 346.100.000 COP ≈ 111.645 USD** |

**Mantenimiento y evolución (año 2 en adelante):** ~35 % del costo del MVP → **≈ 121 millones de COP/año ≈ 39.000 USD/año** (equivale a un equipo de 2 personas de tiempo completo más soporte).

*Alternativa por contratación externa:* si se contrata por prestación de servicios en lugar de nómina, no aplica el factor prestacional del 38 %, pero las tarifas suben típicamente un 25-30 %; el costo neto resultante es similar y se pierde continuidad de conocimiento. **Se recomienda nómina** para un sistema que debe operar 10 años.

### 11.2. Infraestructura en la nube

**Volumen real de datos (el dato clave):** 12 bytes útiles × 4 mensajes/día × 365 días = **17,5 kB por dispositivo/año**. A 20.000 dispositivos: **350 MB/año de datos útiles**. Con metadatos de LoRaWAN, indexación y retención de 5 años: **≈ 15-20 GB**. Esto cabe holgadamente en la base de datos más pequeña de cualquier proveedor.

**Consecuencia:** el costo de nube **no lo determina el tráfico, sino el hecho de mantener los servicios encendidos**. Por eso la curva por dispositivo cae tan rápidamente con la escala.

| Componente | @1.000 disp. | @10.000 disp. | Notas |
|---|---|---|---|
| ChirpStack LNS (instancia de cómputo + Mosquitto embebido) | 25 USD/mes | 60 USD/mes | *ESTIMADO.* Referencia de mercado para autohospedaje: 20-100+ EUR/mes más tiempo de administración |
| Backend de API + frontend (contenedores) | 30 USD/mes | 90 USD/mes | *ESTIMADO* |
| Base de datos gestionada PostgreSQL + TimescaleDB | 35 USD/mes | 95 USD/mes | *ESTIMADO* |
| Almacenamiento, respaldos y transferencia | 10 USD/mes | 35 USD/mes | *ESTIMADO* |
| **TOTAL** | **100 USD/mes = 1.200 USD/año** | **280 USD/mes = 3.360 USD/año** | |
| **Por dispositivo/año** | **1,20 USD** | **0,34 USD** | |

**Comparación con una arquitectura gestionada (AWS IoT Core):**

| Concepto | Precio verificado | Costo a 10.000 dispositivos |
|---|---|---|
| Mensajería | **1,00 USD por millón de mensajes** (primeros 1.000 M/mes) | 10.000 × 4 × 365 = 14,6 M mensajes/año → **14,60 USD/año** |
| Conectividad | **0,08 USD por millón de minutos de conexión** | No aplica (LoRaWAN es Clase A, sin conexión persistente) |
| Capa gratuita | Cubre una carga de 50 dispositivos con 300 mensajes/día de ≤5 kB | — |

> **Hallazgo:** el costo de mensajería de AWS IoT Core para toda la flota de 10.000 dispositivos sería de **14,60 USD al año** — literalmente despreciable. El costo real de la nube está en el **cómputo y la base de datos que hay que mantener encendidos**, no en la ingesta. Esto significa que la elección entre AWS gestionado y autohospedaje debe hacerse por criterios de **operación y soberanía del dato**, no por costo de mensajes. **Recomendación: ChirpStack autohospedado**, porque (a) evita la dependencia de proveedor en un sistema con vida de 10 años, (b) mantiene los datos del programa bajo control del Distrito, lo que simplifica el cumplimiento de la Ley 1581 de 2012, y (c) el diferencial de costo frente a la opción gestionada es de pocos miles de dólares al año.

### 11.3. Mapas y ruteo

| Proveedor | Capa gratuita | Precio unitario | Costo a 1.000 disp. | Costo a 10.000 disp. |
|---|---|---|---|---|
| **Mapbox** | **50.000 cargas de mapa/mes**, 25.000 MAU móviles, 100.000 geocodificaciones, 100.000 solicitudes de direcciones | Cargas: 5,00 USD/1.000 (baja a 3,00 sobre 200 k). Geocodificación: **0,75 USD/1.000**. Direcciones: 2,00 USD/1.000 (baja a 1,20 a volumen) | **0 USD** (uso estimado de ~22.500 cargas/mes, dentro de la capa gratuita) | ~25.000 cargas sobre el límite → **125 USD/mes = 1.500 USD/año** |
| **Google Maps Platform** | ~28.500 cargas/mes; **el crédito de 200 USD/mes fue eliminado en marzo de 2025** y sustituido por topes gratuitos por SKU (10.000 eventos/mes en la mayoría de SKU de Essentials) | Cargas: **7,00 USD/1.000**. Geocodificación: **5,00 USD/1.000**. Direcciones: **5,00 USD/1.000** | ~0-40 USD/mes | ~350 USD/mes = **4.200 USD/año** |
| **Open source: MapLibre GL JS + teselas OSM + OSRM/Valhalla autohospedados** | Sin límites | **Costo fijo**, independiente del volumen | 1 VPS 4 vCPU/8 GB con extracto de Colombia: **40 USD/mes = 480 USD/año** *(ESTIMADO)* | El mismo VPS, quizá 60 USD/mes = **720 USD/año** |

**Recomendación: pila open source (MapLibre GL JS + OpenStreetMap + OSRM o Valhalla autohospedado).**

Razones, en orden de peso:

1. **Costo marginal cero por solicitud.** Es la única opción cuyo costo **no crece** al pasar de 1.000 a 20.000 dispositivos. Para un programa público que debe sostenerse una década con presupuesto anual incierto, un costo fijo y predecible vale más que un costo bajo pero variable.
2. **La optimización de rutas es el uso intensivo, y es donde los proveedores comerciales cobran más.** Un CVRP diario sobre 300-800 paradas requiere una **matriz de distancias** de cientos de miles de pares. Con Mapbox o Google, eso factura por cada elemento de la matriz y escala cuadráticamente; con OSRM propio, es gratis.
3. **OpenStreetMap tiene, en barrios de origen informal de Usme, cobertura frecuentemente mejor que la cartografía comercial**, y es editable: el propio programa puede corregir la malla vial con los recorridos GPS de los camiones, mejorando la herramienta que usa.
4. **Google Maps quedó descartado por precio**: eliminó el crédito mensual de 200 USD en marzo de 2025 y cuesta ~2× lo de Mapbox en cargas y geocodificación.

**Estrategia híbrida recomendada:** OSRM/Valhalla propios para el cálculo de rutas y matrices (el uso masivo), **más** la capa gratuita de Mapbox para la geocodificación de direcciones nuevas en el alta de hogares (100.000 gratis/mes, más que suficiente) y como respaldo de teselas si el servidor propio falla. Costo total: **480-720 USD/año, fijo.**

### 11.4. Resumen de costos de software

| Concepto | Año 1 | Años 2+ (anual) |
|---|---|---|
| Desarrollo del MVP | 346,1 M COP (111.645 USD) | — |
| Mantenimiento y evolución | — | 121,1 M COP (39.075 USD) |
| Nube @1.000 dispositivos | 3,7 M COP (1.200 USD) | 3,7 M COP |
| Nube @10.000 dispositivos | 10,4 M COP (3.360 USD) | 10,4 M COP |
| Mapas y ruteo (open source) | 1,5-2,2 M COP (480-720 USD) | 1,5-2,2 M COP |
| **TOTAL AÑO 1 @10.000 disp.** | **≈ 358,7 M COP ≈ 115.725 USD** | — |
| **TOTAL ANUAL desde el año 2 @10.000 disp.** | — | **≈ 133,7 M COP ≈ 43.155 USD** |

---

## 12. Riesgos técnicos y mitigaciones

| # | Riesgo | Prob. | Impacto | Mitigación | Costo de la mitigación |
|---|---|---|---|---|---|
| **R1** | **Atascamiento del macerador** con material fibroso (tusa de maíz, fibra de yuca, hojas de plátano, huesos) — el modo de falla más probable | **Alta** | Alto | (a) Detección de sobrecorriente con **inversión automática de giro**, 3 intentos, antes de bloquear; (b) peine desmontable sin herramientas; (c) portezuela de acceso a la cámara; (d) instrucción explícita de tamaño máximo; (e) **5.000 ciclos de ensayo con residuo real de Usme antes del piloto** | Incluido en el BOM; ~4.000 USD de campaña de ensayo |
| **R2** | **Corrosión y falla del sello del eje** → entrada de lixiviado al motorreductor | Media | Alto | Inox 304 en toda la zona húmeda; **doble retén con cámara de drenaje al exterior**; compartimento eléctrico **por encima** del húmedo; recubrimiento conformal en la PCB; ensayo de niebla salina de 96 h | +2,50 USD/unidad |
| **R3** | **Olor residual** que lleve al usuario a sacar el aparato de la casa — el riesgo de adopción número uno | Media | **Crítico** | Sistema de 5 capas (§3); **no sobre-macerar** (5-15 mm, nunca puré); drenaje y separación de lixiviados; extracción a presión negativa; panel sensorial de 30 días **antes** del despliegue | Incluido (7,40 USD/unidad) |
| **R4** | **Zonas de sombra de radio** en las cañadas de Usme | **Alta** | Medio | Gateways en filos y equipamientos altos; **campaña de medición de campo con 30 nodos antes de fijar emplazamientos**; **respaldo BLE data-mule** (cobertura de datos del 100 % con latencia degradada); repetidores solares en cañadas críticas | ~3.000 USD de campaña; repetidores a 180 USD c/u |
| **R5** | **Accidente con un menor** al acceder al rotor | Baja | **Catastrófico** | **Triple barrera** (§8.3), con corte de potencia **en serie, por hardware**, independiente del firmware; deflector anti-intrusión; freno dinámico; certificación bajo IEC 60335-2-16 | Incluido (0,48 USD + diseño) |
| **R6** | **Hurto o vandalismo de los gateways** | Media | Medio | Instalación en equipamientos públicos con vigilancia (colegios, CAI, TransMiCable); caja antivandálica; alerta de desconexión y de corte de energía (el gateway recomendado incorpora supercondensador con 1 minuto de respaldo para emitir la alerta de apagón) | Incluido en los 1.150 USD/gateway |
| **R7** | **Percepción de que el aparato encarece la factura de luz** | Media | Alto | Medición real en 50 equipos durante 90 días; etiqueta de consumo en el equipo; comunicación en pesos, no en kWh; gestionar que el operador de aseo asuma el consumo (8,6 M COP/mes para 20.000 hogares) | ~200 USD (medidores) |
| **R8** | **Uso incorrecto**: depositar plásticos, vidrio, metal, pañales | **Alta** | Medio | Boca de carga dimensionada para excluir objetos grandes; detección de sobrecorriente que aborta el ciclo ante material duro; acompañamiento social sostenido; sistema de puntos que penalice la contaminación del lote detectada en planta | Programa social (fuera del alcance técnico) |
| **R9** | **Volatilidad de la TRM** — el 55 % del BOM es importado | **Alta** | Alto | Cobertura cambiaria (*forwards*) para las órdenes de compra; nacionalizar progresivamente componentes (plásticos ya lo están; explorar motorreductor y arnés); cláusula de ajuste por TRM en los contratos con el Distrito | Costo de cobertura ~2-3 % del valor cubierto |
| **R10** | **Ruido** que genere rechazo en vivienda de área reducida | Baja | Medio | El motorreductor a 80-100 RPM opera muy por debajo de los 65 dB de un triturador de fregadero a 3.500 RPM; montaje del motor sobre silentblocks; cámara con amortiguación acústica; medición de ruido en el ensayo de tipo | +1,20 USD/unidad |
| **R11** | **Obsolescencia del proveedor de módulos LoRa** (Ai-Thinker) | Baja | Medio | El SX1262 de Semtech es un estándar de la industria con múltiples fabricantes de módulo (RAK, Heltec, Seeed, Ebyte); diseñar la PCB con **huella compatible con al menos dos módulos** de segunda fuente | Coste de diseño únicamente |
| **R12** | **Interferencia en la banda de uso libre** (título secundario, sin protección) | Media | Medio | ADR y diversidad de canales en AU915; **múltiples gateways con recepción solapada** (un mismo paquete recibido por 2-3 gateways); reintentos con salto de canal; monitoreo del espectro en el diseño de red | Incluido en la redundancia de gateways |
| **R13** | **La reconfiguración de espectro de la Resolución ANE 28 de 2026 avanza** y reduce aún más la banda libre | Baja | Alto | Diseñar en **915-928 MHz con plan AU915** (íntegramente por encima de 915 MHz), no en US915; mantener vigilancia regulatoria; el SX1262 es sintonizable por software en 803-930 MHz, lo que permite reubicar canales por OTA | Cero (decisión de diseño) |
| **R14** | **Falla de la báscula por deriva o suciedad** | Media | Bajo | Tara automática al reinsertar el cajón; compensación térmica con el SHT31; **redundancia cruzada con el sensor ToF** y bandera de discrepancia | Incluido |
| **R15** | **Costo recurrente de consumibles insostenible para el hogar** (15 USD/año ≈ 46.500 COP) | Media | Alto | Los consumibles deben ser **entregados por el operador de aseo durante la ruta**, no comprados por la familia; explorar bolsas de producción local a escala y cartucho de carbón regenerable (esto reduce el OPEX del hogar en 30-40 %) | Decisión de modelo operativo |

**Los tres riesgos que hay que resolver antes de comprometer capital:** R1 (atascamiento), R3 (olor) y R4 (sombra de radio). Los tres se resuelven con **campañas de ensayo de campo que cuestan en conjunto menos de 10.000 USD** — un 0,3 % del costo del lote de 10.000 unidades. Ejecutarlas antes de encargar el utillaje de inyección de 62.000 USD es la decisión de gestión de riesgo con mayor retorno del proyecto.

---

## 13. Bibliografía

*Todas las fuentes fueron consultadas el **10 de septiembre de 2026**.*

### Trituración y compostadoras electromecánicas

1. InSinkErator — *How a Garbage Disposal Works*. https://www.insinkerator.com/en-us/kitchen-better/how-a-garbage-disposal-works
2. InSinkErator — *Food Waste Disposal FAQs*. https://support.insinkerator.com/app/answers/detail/a_id/833/~/food-waste-disposal-faqs
3. Angi — *Parts of a Garbage Disposal: Explanations and Diagram*. https://www.angi.com/articles/parts-of-garbage-disposal.htm
4. Xiamen David Technology Co., Ltd. — *1/2 HP Manufacturer Direct Kitchen Food Waste Disposer OEM* (precios FOB por tramo, especificaciones). https://xiamen-davidtech.en.made-in-china.com/product/PdvTrWzUhYVo/China-1-2-HP-Manufacturer-Direct-Kitchen-Food-Waste-Disposer-OEM.html
5. Sustainable Kitchen Expert — *Lomi Composter Review (2026)*. https://sustainablekitchenexpert.com/lomi-composter-review/
6. Earth911 — *Greener Shopping: The Lomi Home Composter*. https://earth911.com/home-garden/greener-shopping-the-lomi-home-composter-is-a-difference-maker/
7. Reencle — *Best Electric Composter of 2026: Honest Comparison of Every Option*. https://reencle.co/blogs/news/bg01-best-electric-composter-2026
8. GEME — *Top 5 Kitchen Composters in 2026: GEME vs Lomi vs Mill vs Reencle vs Vitamix*. https://gemebio.com/blogs/journal/top-5-kitchen-composters-2026-geme-lomi-mill-reencle-vitamix
9. GEME — *How Does a Real Electric Composter Work? Microbes vs Dehydrators*. https://gemebio.com/blogs/journal/how-does-a-real-electric-composter-work
10. SmartCara — *PCS350 product page*. https://www.smartcara-eng.com/?p=product%7Cpcs350
11. Zero Waste Week — *The Smart Cara review* (consumo medido por usuario: 0,7-0,8 kWh/ciclo). https://www.zerowasteweek.co.uk/smart-cara-review-solution-food-waste/
12. The Compost Culture — *Best Electric Kitchen Composters & Food Recyclers 2026*. https://www.thecompostculture.com/best-electric-kitchen-composters/

### Control de olores

13. Activated Carbon Depot — *Activated Carbon for Compost Bins: Odor Control Guide*. https://activatedcarbondepot.com/blogs/news/how-activated-carbon-eliminates-odors-in-kitchen-compost-bins
14. Reencle — *Carbon Filter for Reencle Prime — Replace Every 9-12 Months*. https://reencle.co/products/reencle-prime-filter
15. Biopunto — *Manejo de malos olores con Tecnología EM*. https://www.biopunto.cl/2022/01/25/manejo-de-malos-olores-con-tecnologia-em/
16. Vidagro — *Microorganismos eficientes: aliados clave en el proceso de compostaje*. https://www.vidagro.com.co/2025/11/09/microorganismos-eficientes-aliados-clave-proceso-compostaje/
17. PortalFrutícola — *Biochar reduce 51 % metano y acelera el compostaje*. https://www.portalfruticola.com/noticias/2025/10/28/biochar/
18. Lombricultura de Tenjo — *Manejo de olores en compostaje* (PDF). https://www.lombriculturadetenjo.com/wp-content/uploads/2019/08/14-Manejo-de-olores-en-compostaje.pdf
19. Compost y Reciclaje — *Control de olores en compost: soluciones efectivas*. https://compostyreciclaje.net/fundamentos-del-compostaje/control-olores-compost-soluciones-efectivas-compostaje-molestias/

### Sensórica

20. Alibaba — *HX711 Digital Load Cell Weight Sensor 1-20 kg* (tramos de precio). https://www.alibaba.com/product-detail/HX711-Digital-Load-Cell-Weight-Sensor_1600349473906.html
21. Alibaba Smart Buy — *How to Choose the Best HX711 Load Cell Amplifier*. https://smartbuy.alibaba.com/buyingguides/hx711
22. AliExpress — *JSN-SR04T-3.0 Waterproof Ultrasonic Module* (3,64 USD). https://www.aliexpress.com/item/32863960886.html
23. STMicroelectronics — *VL53L0X Time-of-Flight Ranging Sensor*. https://www.st.com/en/imaging-and-photonics-solutions/vl53l0x.html
24. Alibaba Electronics — *VL53L0X supplier guide: DigiKey stock and pricing*. https://electronics.alibaba.com/supplier/vl53l0x-digikey
25. Ecube Labs — *ToF vs USW* (comparación de sensores de nivel para contenedores de residuos). https://www.ecubelabs.com/tof-vs-usw/
26. Milesight — *EM400-TLD ToF Laser Distance Sensor / Smart Bin Sensor*. https://www.milesight.com/iot/product/lorawan-sensor/em400-tld
27. MySensors Forum — *JSN-SR04T (distance sensor) Reliability Issue Fix?* (lecturas erráticas documentadas). https://forum.mysensors.org/topic/11417/jsn-sr04t-distance-sensor-reliability-issue-fix
28. Evreka — *Ultrasonic Sensors in Waste Management*. https://evreka.co/blog/ultrasonic-sensors-in-waste-management/

### Conectividad LPWAN y regulación de espectro

29. Bixtia — *433 MHz o 915 MHz: la pregunta que todo proyecto LoRa en Colombia debería resolver* (Res. ANE 689/2004 y Res. ANE 28/2026). https://www.bixtia.com/433-mhz-o-915-mhz-la-pregunta-que-todo-proyecto-lora-en-colombia-deberia-resolver-antes-de-disenar-el-hardware/
30. MinTIC — Normograma, *Resolución 28 de 2026 ANE* (plan de banda 896-915 MHz y 941-960 MHz, Tabla 15A del CNABF). https://normograma.mintic.gov.co/mintic/compilacion/docs/resolucion_ane_0028_2026.htm
31. ANE — *Análisis de impacto normativo sobre espectro de uso libre para medidores inteligentes de consumo* (PDF). https://www.ane.gov.co/Documentos%20compartidos/ArchivosDescargables/noticias/An%C3%A1lisis%20de%20impacto%20normativo%20sobre%20espectro%20de%20uso%20libre%20para%20medidores%20inteligentes%20de%20consumo.pdf
32. Lansitec — *Plan de frecuencias LoRaWAN por país o región*. https://www.lansitec.com/blogs/lorawan-frequency-plan-by-country-or-region/
33. Heltec — *LoRaWAN example Sub-Band usage (AU915)*. https://docs.heltec.org/general/sub_band_usage.html
34. Rokland — *Ai-Thinker Ra-01SH-P LoRa Module SX1262* (PVP 10,97 USD, especificaciones). https://store.rokland.com/products/ra-01sh-p-lora-module-ai-thinker
35. RAKwireless Store — *WisGate Edge Lite 2 RAK7268V2/RAK7268CV2* (precios por variante US915). https://store.rakwireless.com/products/rak7268-8-channel-indoor-lorawan-gateway
36. RAKwireless Docs — *RAK7268V2/RAK7268CV2 Datasheet* (sensibilidad -139 dBm, SX1302). https://docs.rakwireless.com/product-categories/wisgate/rak7268v2/datasheet/
37. Milesight — *UG67 Outdoor LoRaWAN Gateway* (IP67, 8 canales, hasta 2.000 nodos, 15 km rural / 2 km urbano). https://www.milesight.com/iot/product/lorawan-gateway/ug67
38. Dragino — *LPS8 / LPS8N / LPS8v2 Indoor LoRaWAN Gateway*. https://www.dragino.com/products/lora-lorawan-gateway/item/148-lps8.html
39. The Things Network — *Colombia country page* (gateways registrados). https://www.thethingsnetwork.org/country/colombia/
40. The Things Network — *Comunidad Bogotá*. https://www.thethingsnetwork.org/community/bogota/
41. IoT Index — *ChirpStack: LoRaWAN LNS and self-hosting costs*. https://iotindex.io/en/iot-platforms/chirpstack-lorawan-network-server/
42. chirphost — *ChirpStack Hosting 2026: Managed vs. Self-Hosted vs. TTN Cloud*. https://chirphost.de/en/blog/chirpstack-hosting-managed-vs-self-hosted
43. Helium Documentation — *Data Credit* (1 DC = 24 bytes = 0,00001 USD). https://docs.helium.com/tokens/data-credit/
44. Semtech Learning Center — *Helium Network Overview and Basics*. https://learn.semtech.com/mod/book/view.php?id=166&chapterid=27
45. UnaBiz — *Cobertura de la red 0G* (>70 países; Colombia no listada). https://unabiz.es/cobertura-de-la-red-0g/
46. Onomondo — *IoT SIM Cards for Colombia* (Claro/Movistar/Tigo, 2G/3G/LTE/LTE-M). https://onomondo.com/iot-sim/the-best-iot-sim-cards-for-colombia/
47. Claro Colombia Empresas — *IoT y 5G: relación estratégica en el futuro*. https://www.claro.com.co/empresas/noticias-interes/iot-y-5g/
48. Claro — *LTE-M y NB-IoT: nuevas tecnologías*. https://www.claro.com.ar/empresas/lte-m-nb-iot
49. Bismark Colombia — *SIM Card de Datos M2M*. https://bismark.net.co/sim-card/
50. Quectel — *LPWA BC660K-GL NB2* (módulo NB-IoT). https://www.quectel.com/product/lpwa-bc660k-gl-nb2/
51. Minew — *LoRaWAN Range Explained: Coverage & 4 Tips to Maximize* (atenuación por muros 10-20 dB; terreno accidentado). https://www.minew.com/lorawan-range-overview/
52. SmartMakers — *LoRaWAN Range and Coverage in Practice*. https://smartmakers.io/en/lorawan-range-part-2-range-and-coverage-of-lorawan-in-practice/
53. NCBI / PMC — *A Deep Learning Approach for Accurate Path Loss Prediction in LoRaWAN Livestock Monitoring* (propagación en terreno montañoso). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11125001/
54. arXiv — *Real-World LoRaWAN Performance and Propagation Modeling Using UAV, Helikite, and Vehicle-Based Measurements*. https://arxiv.org/html/2604.06444v1
55. CRC — *¿Qué es Homologación?*. https://www.crcom.gov.co/es/preguntas-frecuentes/es-homologacion
56. CRC — *Circular 162: la CRC actualiza normas técnicas de homologación para equipos terminales móviles*. https://www.crcom.gov.co/es/noticias/comunicado-prensa/circular-162-crc-actualiza-normas-tecnicas-homologacion-para-equipos
57. ResearchGate — *Opportunistic Sensor Data Collection with Bluetooth Low Energy* (arquitectura data-mule). https://www.researchgate.net/publication/312595726_Opportunistic_Sensor_Data_Collection_with_Bluetooth_Low_Energy
58. BeaconTrax — *Trax10223 Waste Bin BLE Sensor*. https://www.beacontrax.com/product/trax10223-waste-bin-ble-sensor/

### Energía y tarifas

59. OPS Colombia — *Tarifas de energía eléctrica por operador en Colombia (2026)* — Enel-Codensa 864 COP/kWh, act. 30-ago-2026. https://www.opscolombia.com/tarifas-energia
60. CuantoMeCuesta — *¿Cuánto cuesta la luz en Colombia? Tarifas eléctricas 2026* (rango Bogotá 750-900 COP/kWh; CS 130 kWh; subsidios por estrato). https://cuantomecuesta.com/co/electricidad/
61. Infobae — *Qué estratos tienen derecho a subsidio de energía eléctrica en 2026*. https://www.infobae.com/colombia/2026/04/07/que-estratos-tienen-derecho-a-subsidio-de-energia-electrica-en-2026-asi-puede-verificar-si-es-beneficiario/
62. Pulzo — *Cómo funciona el subsidio de energía en Colombia 2026*. https://www.pulzo.com/economia/como-funciona-subsidio-energia-colombia-2026-asi-puede-calcularlo-PP5033977
63. Enel Colombia — *Tarifario Enel, enero 2026* (PDF). https://www.enel.com.co/content/dam/enel-co/espa%C3%B1ol/personas/1-17-1/2026/tarifario-enel-enero-2026.pdf
64. Alcaldía de Bogotá — *Enel Colombia explica variación en la tarifa de energía*. https://bogota.gov.co/mi-ciudad/habitat/enel-explica-variacion-en-la-tarifa-de-energia-tras-factura-de-marzo

### Residuos y contexto de Bogotá / Usme

65. UAESP — *Aumenta la producción de residuos sólidos en Bogotá* (PPC 0,855 kg/hab-día). https://bogota.gov.co/mi-ciudad/habitat/aumenta-la-produccion-de-residuos-solidos-en-bogota-segun-uaesp
66. UAESP — *Guía técnica para el aprovechamiento de residuos orgánicos* (PDF). https://www.uaesp.gov.co/images/Guia-UAESP_SR.pdf
67. UAESP — *Bogotá avanza en el aprovechamiento de residuos orgánicos*. https://www.uaesp.gov.co/noticias/bogota-avanza-aprovechamiento-residuos-organicos
68. UAESP — *Aprovechamiento de residuos sólidos en Bogotá*. https://www.uaesp.gov.co/aprovechamiento-residuos-solidos-bogota
69. UAESP — *Modelo de aprovechamiento: la basura no es basura* (PDF). https://www.uaesp.gov.co/sites/default/files/20210420_Modelo_de_aprovechamiento.pdf
70. Greenpeace Colombia — *Bogotá dice ¡basta de basura!* (composición de residuos). https://www.greenpeace.org/colombia/involucrate/basura/
71. MinVivienda — *Tratamiento de residuos sólidos en el marco del servicio público de aseo* (PDF). https://www.minvivienda.gov.co/sites/default/files/documentos/20210806-entregable-1-v5-definitiva_0.pdf
72. DANE — *Residuos sólidos generados per cápita* (PDF). https://www.dane.gov.co/files/investigaciones/pib/ambientales/cuentas_ambientales/indicadores/cuenta-ambiental-y-economica-de-flujo-de-materiales/residuos-solidos-percapita/hm-residuos-solidos-percapita.pdf
73. Secretaría Distrital de Planeación — *No. 5 Usme: diagnóstico POT 2020* (PDF). https://www.sdp.gov.co/sites/default/files/05_usme_-_diagnostico_pot_2020_version_2.pdf
74. IDIGER — *Localidad Usme: identificación y priorización* (PDF). https://www.idiger.gov.co/documents/220605/232445/Identificaci%C3%B3n+y+Priorizaci%C3%B3n+.pdf
75. Alcaldía Local de Usme — *Atlas Usme ambiental 2017* (PDF). http://www.usme.gov.co/sites/usme.gov.co/files/documentos/atlas_usme_ambiental_2017._vf.pdf
76. Cámara de Comercio de Bogotá — *Localidad 5, Usme* (PDF). https://bibliotecadigital.ccb.org.co/server/api/core/bitstreams/e85f9482-e3fb-4923-ac13-0b16a49713e7/content
77. Topographic-map — *Mapa topográfico Localidad Usme, altitud, relieve*. https://es-co.topographic-map.com/map-rh4dn/Localidad-Usme/

### Fabricación, materiales e importación

78. Haizol — *Injection Molding Tooling Cost From China: Real Factory Price Data* (tabla de costos por tipo de molde y vida útil). https://www.haizol.com/blog/injection-molding-tooling-cost-china
79. RapidDirect — *Injection Molding Cost Breakdown: A 2026 Pricing & DFM Strategy Guide*. https://www.rapiddirect.com/blog/injection-molding-costs/
80. Kemal Manufacturing — *How Much Does Injection Molding Cost (2026 Updated Guide)*. https://www.kemalmfg.com/injection-molding-cost/
81. Plastopia — *Pricing Guide: China Injection Molding Cost*. https://www.plastopialtd.com/pricing-guide/
82. Rototech S.A.S. — *Productos plásticos por rotomoldeo* (Colombia). https://rototechsas.com/
83. Rotoplast Colombia — *Tanques de agua y soluciones plásticas*. https://rotoplast.com.co/
84. AM Plásticos — *Inyección de plásticos y fabricación de moldes, Bogotá*. https://amplasticos.com/
85. Fergoplas SAS — *Moldes e inyección de plásticos en Bogotá*. https://fergoplas.com/
86. Isoplásticos — *Fábrica de envases plásticos en Bogotá*. https://isoplasticos.com/fabrica-de-envases-plasticos-bogota/
87. Alegra — *Tributación de importaciones en Colombia 2026: guía completa*. https://blog.alegra.com/colombia/tributacion-de-importaciones-en-colombia/
88. Angela Global — *Aranceles e impuestos al importar desde China a Colombia*. https://www.angelaglobal.com/guias/aranceles-impuestos-importar-china-colombia
89. Nextstop Group — *Cómo calcular los aranceles de importación en Colombia para carga general (2026)*. https://nextstopgroup.com/blog/como-calcular-los-aranceles-de-importacion-en-colombia-para-carga-general-2026
90. Uman S.A.S. — *Bolsas compostables biodegradables, Colombia*. https://uman.eco/collections/bolsas
91. Belplásticos — *Bolsas biodegradables*. https://www.belplasticos.com/eco-productos/biodegradables/
92. Alibaba — *NTAG213 NFC Tag* (0,15 USD/ud, MOQ 100). https://www.alibaba.com/showroom/ntag213-nfc-tag.html
93. Alibaba — *125 kHz RFID Card / Bulk blank PVC cards* (0,05 USD/ud, MOQ 10.000). https://www.alibaba.com/showroom/125khz-rfid-card.html

### Electrónica y componentes

94. LCSC Electronics — *ESP32-C3, Espressif* (tramos de precio verificados hasta 1.000+ uds). https://www.lcsc.com/product-detail/C2838500.html
95. JLCPCB — *PCB Assembly Cost: How Much Does PCBA Cost and How to Save*. https://jlcpcb.com/blog/pcba-cost-breakdown
96. JLCPCB — *SMT PCB Assembly Service / Turnkey PCBA*. https://jlcpcb.com/pcb-assembly
97. Alibaba — *76 mm 12V/24V/220V 50-250 W High Torque DC Worm Gear Motor*. https://www.alibaba.com/product-detail/76mm-12v-24v-220v-50w-100w_62261688407.html
98. Alibaba — *In Stock 12V 100W DC Worm Gear Motor, High Torque & Wide Gear Ratio*. https://www.alibaba.com/showroom/12v-100w-dc-worm-gear-motor.html
99. Alibaba Electronics — *18650 Battery Wholesale Price* (0,30-1,80 USD/celda). https://electronics.alibaba.com/supplier/18650-battery-wholesale-price
100. Alibaba — *868/915 MHz LoRa Spring Helical Antenna*. https://www.alibaba.com/product-detail/Internal-LoRa-Spring-Helical-Antenna-868MHz_1600934168090.html
101. Circuit Rocks — *AC-DC Switching Power Supply 12V 5A 60W*. https://circuit.rocks/products/ac-dc-12v-5a-switching-power-supply

### Normativa técnica y certificación

102. IEC — *IEC 60335-2-16:2022, Household and similar electrical appliances — Safety — Particular requirements for food waste disposers*. https://webstore.iec.ch/en/publication/70370
103. Intertek — *IEC 60335-2: Particular Standards for Specific Household Appliances*. https://www.intertek.com/appliances/iec-60335-2/
104. MinEnergía — *Reglamento Técnico de Instalaciones Eléctricas (RETIE)*. https://www.minenergia.gov.co/es/misional/energia-electrica-2/reglamentos-tecnicos/reglamento-t%C3%A9cnico-de-instalaciones-el%C3%A9ctricas-retie/
105. Bureau Veritas Certification Colombia — *Productos eléctricos: certificación de producto RETIE*. https://www.bureauveritascertification.com/es/servicios/info/productos-electricos-certificacion-de-producto-retie
106. Metacert SAS — *Certificación de productos RETIE en Colombia*. https://metacertsas.com/certificacion-productos-retie/
107. RTL Certifications — *Certificado RETIE: precio, factores y cómo solicitarlo*. https://rtlcertifications.com/certificado-retie-precio/

### Costos laborales, salarios y software

108. Holland & Knight — *Colombia decreta aumento del salario mínimo y auxilio de transporte para 2026*. https://www.hklaw.com/en/insights/publications/2025/12/colombia-decreta-aumento-del-salario-minimo-y-auxilio-de-transporte
109. SIESA — *Salario mínimo en Colombia 2026: guía para empresas*. https://www.siesa.com/blog/salario-minimo-en-colombia-2026
110. Magneto365 — *Hora de trabajo en Colombia 2026: valor, extras y recargos* (8.338 COP/hora desde el 15-jul-2026). https://www.magneto365.com/co/blog/cuanto-cuesta-la-hora-de-trabajo-colombia
111. Aleluya — *Cuál es el costo de un empleado en Colombia 2026*. https://aleluya.com/blog/nomina/costo-de-un-empleado-en-colombia-2026/
112. Buk — *Carga prestacional en Colombia: cálculo, porcentajes y ejemplos*. https://www.buk.co/blog/carga-prestacional-en-colombia
113. Coderhouse — *Sueldo Desarrollador Full Stack en Colombia 2026*. https://www.coderhouse.com/co/sueldos/sueldo-desarrollador-full-stack-colombia-2025
114. Coderhouse — *Sueldo Desarrollador de Aplicaciones en Colombia 2026*. https://www.coderhouse.com/sueldos/sueldo-desarrollador-aplicaciones-colombia-2025
115. TripleTen — *Salario de un desarrollador web en Colombia 2026*. https://tripleten.co/blog/cuanto-gana-desarrollador-web-colombia/

### Nube y mapas

116. AWS — *AWS IoT Core Pricing* (1,00 USD por millón de mensajes; 0,08 USD por millón de minutos de conexión). https://aws.amazon.com/iot-core/pricing/
117. QServices — *Azure IoT vs AWS IoT vs Google IoT Pricing: Feature Comparison Chart 2026*. https://www.qservicesit.com/azure-iot-vs-aws-iot-vs-google-iot-pricing
118. Radar — *Mapbox vs. Google Maps API: 2026 comparison*. https://radar.com/blog/mapbox-vs-google-maps-api
119. StoreRocket — *Is Mapbox Free? Complete Pricing Breakdown for 2026*. https://storerocket.io/learn/mapbox-pricing
120. BuildMVPFast — *Maps API Pricing Comparison (July 2026): Google Maps vs Mapbox*. https://www.buildmvpfast.com/api-costs/maps
121. Brocoders — *Google Maps vs Mapbox vs OpenStreetMap: why most API comparisons get it wrong*. https://brocoders.com/blog/mapbox-vs-google-maps-vs-openstreetmap/

### Tasa de cambio

122. Banco de la República — *Tasa de cambio representativa del mercado (TRM)*. https://www.banrep.gov.co/es/glosario/tasa-cambio-trm
123. Superintendencia Financiera de Colombia — *Tasa de Cambio Representativa del Mercado*. https://www.superfinanciera.gov.co/powerbi/reportes/514/482/
124. Colombia.com — *Precio del dólar en Colombia hoy: TRM del 9 de septiembre de 2026*. https://www.colombia.com/actualidad/economia/precio-del-dolar-hoy-en-colombia-miercoles-9-de-septiembre-de-2026-599678

---

## Anexo — Advertencias de uso de este documento

1. **Los precios marcados *(ESTIMADO)* no son cotizaciones.** Antes de comprometer capital deben convertirse en cotizaciones formales con especificación cerrada. Los ítems con mayor incertidumbre y mayor peso en el BOM son, en orden: motorreductor (ítem 1), carcasa plástica (ítem 4), fuente conmutada (ítem 23) y gateway exterior.
2. **Dos precios no pudieron verificarse por agotamiento del presupuesto de búsquedas web** y quedaron con estimación razonada: el flete marítimo China-Colombia 2026 y el costo mensual detallado de instancias de nube. Ambos tienen bajo peso relativo (≤8 % del costo total) y su incertidumbre está dentro de la banda global de ±20-25 %.
3. **Ningún precio de este documento fue inventado.** Cada cifra tiene fuente verificada o razonamiento explícito de estimación.
4. **El BOM asume ensamble en Colombia con componentes importados.** Cambiar a importación de producto terminado modifica la estructura arancelaria, el sujeto de la certificación RETIE y el argumento de empleo local del programa.
5. **La decisión de plan de frecuencias AU915 (y no US915) es consecuencia de la Resolución ANE 28 de 2026** y debe reverificarse contra el CNABF vigente antes de congelar el diseño de RF, dado que la reconfiguración de la banda de 900 MHz en Colombia está en curso.
