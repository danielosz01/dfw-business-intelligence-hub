# ADR 0001 — Por qué construyo el DFW Business Intelligence Hub

- **Estado:** Aceptado
- **Fecha:** 2026-04-30
- **Autor:** Daniel Ostos
- **Decisores:** Daniel (owner único)

---

## Contexto

Soy data analyst aspirante en transición a data engineering, viviendo en Dallas-Fort Worth. Tengo un trabajo de 3 días/semana que cubre gastos básicos, lo que me da runway sin urgencia inmediata. Mi meta es doble: empleo de data engineer en USA ($130-180k/año en 12-18 meses) **e** ingreso extra recurrente desde un producto de datos.

Dispongo de 10-15 horas/semana para construir. Necesito decidir qué proyecto perseguir antes de invertir esas horas.

## Alternativas consideradas

### Alternativa A — DFW Business Intelligence Hub (elegida)

Plataforma de inteligencia de mercado geolocalizada que automatiza captura de datos públicos de DFW (permits de construcción, registros de propiedad, datos de negocios) y los entrega enriquecidos a empresas B2B locales.

### Alternativa B — AI Operations Agency (descartada)

Agencia que vende AI receptionists / automation a clínicas dentales y servicios profesionales locales.

## Decisión

**Construir el DFW Business Intelligence Hub.**

## Justificación

La Alternativa A cumple **tres metas simultáneamente** que la Alternativa B solo cumple parcialmente:

| Criterio | A: BI Hub | B: AI Agency |
|----------|-----------|--------------|
| **Carrera (data engineer)** | ✅ Cada hora es portfolio público de tecnologías demandadas (Python, dbt, Dagster, Iceberg, etc.) | ❌ Aleja del rol técnico, posiciona como solutions engineer/agency operator |
| **Negocio escalable** | ✅ Producto de datos con margen alto, sin techo atado a mi tiempo | ❌ Servicio agency: ingresos atados a horas/clientes, mercado saturado |
| **Contenido y marca personal** | ✅ Journey de construcción genera contenido técnico natural en español (mercado vacío) | ⚠️ Genera contenido de "case studies" pero no posiciona para empleo técnico |
| **Runway requerido** | ✅ Self-funded, free tiers cubren MVP | ✅ Self-fundable también |
| **Validación local** | ✅ DFW tiene 7M+ habitantes, miles de contratistas y B2B services | ✅ Igual válido localmente |
| **Riesgo legal** | ⚠️ ToS de portales gubernamentales requieren cuidado | ⚠️ TCPA/regulaciones de telefonía |

Específicamente, descarté la Alternativa B porque:

1. **Me aleja de la carrera de data engineer.** El stack que aprendería (n8n, Vapi, Make, GHL) no se valora en job postings de data engineer de $130k+. Los 12 meses de construcción serían portfolio para un rol que no quiero.
2. **Tiene techo de ingresos atado a mi tiempo.** Una agencia escala contratando, no automatizando, salvo que pivotee a producto — y si voy a pivotear a producto, mejor empezar como producto desde el día 1.
3. **Mercado saturado.** Hay miles de "AI agencies" surgiendo en YouTube/X. Diferenciarme requiere energía de marketing que prefiero invertir en construcción técnica.
4. **El contenido que genera no me posiciona para empleo técnico.** Reels de "cómo conseguí 3 clientes con AI receptionists" no atraen recruiters de data engineering.

La Alternativa A, en cambio:

1. **Es portfolio público desde el día 1.** El repo + el journey en LinkedIn son visibles para recruiters. Antes de tener un solo cliente pagado, ya puede conseguirme empleo de $130k+.
2. **Apila tecnologías demandadas en su orden natural de aprendizaje.** El roadmap introduce Playwright → Pydantic → dbt → Dagster → Iceberg → FastAPI en fases, cada una justificada por un problema real del proyecto.
3. **El contenido en español es mercado vacío.** Hay docenas de canales de data engineering en inglés, casi ninguno consistente en español. Posicionamiento natural.
4. **Hyper-local DFW como diferenciador.** Los grandes (BuildZoom, Reonomy, ConstructConnect) no compiten en hyper-local con precios accesibles. Hay espacio.

## Consecuencias

### Positivas

- Cada hora invertida cumple las tres metas (carrera + negocio + contenido). Eficiencia de tiempo alta.
- Si el negocio no despega, sigue siendo el mejor portfolio que podría construir para empleo data engineer.
- El stack del roadmap es defendible en interviews — cada decisión tiene un ADR.
- Mercado real con buyers identificables (contratistas, inversores inmobiliarios) en DFW.

### Negativas / Riesgos

- **Riesgo legal:** Terms of Service de portales gubernamentales pueden prohibir scraping. Mitigación: respetar robots.txt, rate limiting humano, foreclosures excluidos del MVP, LLC + E&O insurance antes de Fase 4, consulta legal antes de cobrar a clientes.
- **Tiempo a primer revenue:** ~9-12 meses según el roadmap. Comparado con la AI Agency que podría facturar al mes 2-3.
- **Concentración geográfica:** todo el TAM está atado a DFW. Mitigación: validar producto en DFW primero, luego replicar en Austin/Houston/SA en Fase 5+.
- **Stack ambicioso:** 5 fases con muchas tecnologías. Riesgo de overengineering. Mitigación: las reglas de la Filosofía de construcción del roadmap (capas, no todo de una vez; producto vendible antes de stack perfecto).

### Indicadores que invalidarían esta decisión

Re-evaluaría el proyecto si en algún punto del journey:

- No consigo terminar la Fase 1 en 8 semanas (3x el estimado de 6) — señal de scope mal calibrado.
- A los 12 meses no tengo ni empleo data engineer ofrecido ni un solo cliente piloto pagado — señal de que el mercado o la ejecución no funcionan.
- Surge una oportunidad clara de empleo data engineer durante la Fase 1-2 que no requiere terminar el proyecto — el proyecto ya cumplió su rol como portfolio, lo paso a side project pasivo.

## Referencias

- [`ROADMAP.md`](../../ROADMAP.md) — secciones 1, 2 y 6.
- Conversación de planificación inicial con Claude (abril 2026).
