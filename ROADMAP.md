# DFW Business Intelligence Hub — Roadmap Maestro

> **Documento vivo.** Este archivo es la fuente única de verdad del proyecto. Contexto para Cursor/Claude Code, guía de construcción personal, plan de negocio integrado, y referencia para conversaciones futuras con asistentes AI.

**Última actualización:** Abril 2026
**Owner:** Daniel
**Ubicación:** Dallas-Fort Worth, Texas
**Estado actual:** Pre-Fase 1 (planificación completa, construcción no iniciada)

---

## Tabla de contenidos

1. [Contexto del proyecto](#1-contexto-del-proyecto)
2. [Plan de negocio](#2-plan-de-negocio)
3. [Filosofía de construcción](#3-filosofía-de-construcción)
4. [Stack técnico objetivo](#4-stack-técnico-objetivo)
5. [Arquitectura general](#5-arquitectura-general)
6. [Las 5 fases — overview](#6-las-5-fases--overview)
7. [Fase 1: MVP funcional](#7-fase-1-mvp-funcional-semanas-1-6)
8. [Fase 2: Profesionalización](#8-fase-2-profesionalización-semanas-7-14)
9. [Fase 3: Cloud y orquestación](#9-fase-3-cloud-y-orquestación-semanas-15-24)
10. [Fase 4: AI-native y producto vendible](#10-fase-4-ai-native-y-producto-vendible-semanas-25-36)
11. [Fase 5: Escala y diferenciación](#11-fase-5-escala-y-diferenciación-semanas-37-52)
12. [Estrategia de contenido](#12-estrategia-de-contenido)
13. [Cómo usar este documento](#13-cómo-usar-este-documento)

---

## 1. Contexto del proyecto

### Quién soy

- **Background:** Data analyst aspirante, estudiante de data engineering. Background previo en diseño gráfico freelance.
- **Ubicación:** Dallas-Fort Worth, Texas (USA).
- **Idiomas:** Español nativo, inglés funcional.
- **Tiempo disponible:** 10-15 horas/semana para este proyecto.
- **Situación financiera:** Trabajo de 3 días/semana (viernes-domingo) que cubre gastos básicos. No hay urgencia de ingreso inmediato — hay runway para construir bien.
- **Meta de carrera:** Conseguir empleo como data engineer en USA ($130-180k/año) en 12-18 meses.
- **Meta de negocio:** Generar ingreso extra ($1-5k/mes inicialmente) con un producto de datos escalable.

### Qué construyo

**DFW Business Intelligence Hub:** Una plataforma de inteligencia de mercado geolocalizada que automatiza la captura, procesamiento y entrega de datos públicos del área Dallas-Fort Worth (permisos de construcción, registros de propiedad, datos de negocios) para empresas B2B locales.

### Por qué este proyecto y no otro

Este proyecto cumple **tres metas simultáneamente**:

1. **Carrera (data engineer):** cada hora construida es portfolio público y aprendizaje práctico de tecnologías demandadas. El proyecto solo, sin generar un cliente, ya puede conseguir empleo de $130k+.
2. **Negocio:** datos geolocalizados de DFW son vendibles a contratistas, real estate, B2B services. Mercado real con buyers identificables.
3. **Contenido y marca personal:** el journey de construcción genera contenido natural para LinkedIn, YouTube, Instagram técnico en español (mercado vacío).

### Por qué descarté la alternativa (AI Operations Agency)

Considere construir una agencia de AI receptionists para clínicas dentales. Lo descarté porque:
- Me alejaba de la carrera de data engineer
- Tiene techo de ingresos atado a mi tiempo (no escala)
- Mercado saturado con agencias similares
- El contenido que genera no me posiciona para empleo técnico

---

## 2. Plan de negocio

### Mercado objetivo

**Buyer personas primarios:**

1. **Contratistas de construcción/remodelación en DFW** (HVAC, roofing, plumbing, general contractors, cleaning services B2B)
   - Dolor: necesitan saber qué propiedades están construyendo o remodelando para hacer outreach
   - Capacidad de pago: $99-499/mes
   - Tamaño del mercado: ~5,000-10,000 empresas en DFW

2. **Inversores inmobiliarios y comerciales en DFW**
   - Dolor: encontrar propiedades antes de que lleguen a Zillow/MLS
   - Capacidad de pago: $199-999/mes
   - Tamaño: ~2,000-5,000 individuos/firmas en DFW

**Buyer personas secundarios (Fase 4+):**

3. Agentes de real estate comercial
4. Agencias de marketing B2B locales
5. Empresas de servicios profesionales (abogados, contadores) buscando leads

### Propuesta de valor

> "Recibe cada lunes los nuevos permisos de construcción y movimientos inmobiliarios de DFW, geolocalizados, enriquecidos con datos de propietarios y filtrados por tu industria. Antes de que lleguen a tu competencia."

### Modelo de pricing (objetivo Fase 4)

| Plan | Precio | Para quién | Incluye |
|------|--------|------------|---------|
| **Starter** | $99/mes | Contratistas individuales, freelancers | 1 condado, email semanal, 50 leads/semana |
| **Pro** | $249/mes | Empresas pequeñas-medianas | 3 condados, dashboard, API access, 200 leads/semana |
| **Enterprise** | $499-999/mes | Empresas grandes, agencias | Todos los condados, custom fields, integraciones, ilimitado |

### Proyección financiera realista

| Mes | MRR objetivo | Clientes objetivo | Notas |
|-----|--------------|-------------------|-------|
| 6 | $0 | 0 | Construcción MVP |
| 9 | $200-500 | 1-3 piloto | Validación |
| 12 | $1,000-2,500 | 5-15 | Primer ingreso real |
| 18 | $3,000-7,000 | 20-40 | Producto refinado |
| 24 | $7,000-15,000 | 40-80 | Escala |

### Riesgos legales y mitigación

**Riesgos identificados:**
- Terms of Service de portales gubernamentales pueden prohibir scraping
- TCPA/CCPA si clientes hacen outreach masivo basado en data
- Liability si data tiene errores que causan pérdidas a clientes

**Mitigaciones:**
- LLC en Texas registrada antes del primer cliente pagado
- Terms of Service propios con disclaimers
- E&O insurance ($500-1,500/año) antes de Fase 4
- Respeto a robots.txt, rate limiting humano
- Foreclosures excluidos del MVP (alta regulación)
- Consulta legal con abogado Texas business antes de Fase 4 ($300-500)

### Competidores y diferenciación

**Competidores existentes:**
- BuildZoom, ConstructConnect (nacional, caro, no hyper-local)
- PropStream, BatchLeads (real estate, no permits)
- Reonomy (commercial real estate, enterprise pricing)

**Mi diferenciación:**
- **Hyper-local DFW** (no intentar cubrir todo USA)
- **Precio accesible** para small business locales
- **Bilingüe** (mercado hispano DFW desatendido)
- **Datos frescos semanales** (algunos competidores actualizan mensual)
- **Owner-operator** que conoce el mercado local

---

## 3. Filosofía de construcción

### Principios fundamentales

1. **Construir en capas, no todo de una vez.** Cada tecnología entra cuando un problema real la justifica. Stack moderno NO se mete desde día 1.

2. **Documentar mientras construyo, no después.** Cada decisión técnica importante = un Architecture Decision Record (ADR). Cada problema resuelto = potencial pieza de contenido.

3. **Público desde el día 1.** Repositorio público en GitHub. Journey documentado en redes. Esto es commitment device + portfolio + marketing simultáneo.

4. **Cumplir la semana, no el día.** La consistencia mensual importa más que la perfección diaria. Una semana mala se recupera la siguiente.

5. **Re-evaluar al final de cada fase, no en medio.** Pivots emocionales matan proyectos. Termino la fase, después decido.

6. **Producto vendible antes de stack perfecto.** Mejor tener clientes con stack feo que stack bonito sin clientes.

### Anti-patrones que evito

- ❌ Aprender una tecnología "por si la necesito"
- ❌ Refactorizar antes de terminar features
- ❌ Buscar el "stack perfecto" antes de empezar
- ❌ Construir features sin validar que un cliente las quiera
- ❌ Comparar mi semana 4 con el mes 12 de otra persona
- ❌ Saltar fases porque "ya lo entiendo"

---

## 4. Stack técnico objetivo

### Stack final a 12 meses

```
LANGUAJES
├── Python 3.12+ (principal)
├── SQL (segundo lenguaje)
└── Bash (scripting ops)

PACKAGE MANAGEMENT
└── uv (reemplazando pip/poetry en 2026)

INGESTA
├── Playwright (web scraping)
├── dlt - data load tool (ingesta moderna)
└── Requests + APIs

STORAGE (Arquitectura Medallón)
├── Bronze: Parquet en Cloudflare R2 (raw immutable)
├── Silver: Apache Iceberg tables (ACID, time travel)
└── Gold: DuckDB / Motherduck (analytics serving)

TRANSFORMACIÓN
├── dbt Core (estándar de oro)
├── dbt tests (data quality)
└── SQLMesh (exploración Fase 5)

ORQUESTACIÓN
└── Dagster (asset-based, moderno)

INFRAESTRUCTURA
├── Docker + Docker Compose
├── Terraform (IaC)
├── GitHub Actions (CI/CD)
└── Cloudflare R2 (storage cloud)

AI/ML LAYER
├── Claude API / OpenAI API (enrichment)
├── pgvector + embeddings (semantic search)
└── Anomaly detection custom

SERVING
├── FastAPI (REST API)
├── Streamlit (dashboard interno + público)
└── Stripe (billing)

OBSERVABILIDAD
├── Sentry (errors)
├── OpenTelemetry (traces)
├── Great Expectations (data quality)
└── Logging estructurado (JSON)

CALIDAD DE CÓDIGO
├── ruff (lint + format)
├── mypy (type checking)
├── pytest (testing)
└── pre-commit hooks

DOCUMENTACIÓN
├── MkDocs Material (sitio docs)
├── ADRs (decisions)
└── README profesional
```

### Justificación del stack

Cada tecnología elegida cumple **al menos dos de tres criterios**:

1. **Demanda en el mercado de empleo data engineer 2026** (sale en job postings)
2. **Resuelve un problema real del proyecto** (no se incluye por moda)
3. **Compatible con presupuesto bajo / free tier** (es self-funded)

---

## 5. Arquitectura general

### Diagrama lógico (alto nivel)

```
┌─────────────────────────────────────────────────────────────┐
│                    FUENTES PÚBLICAS                          │
│  Grapevine MyGov │ TAD │ Dallas County │ Tarrant County │  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   CAPA INGESTA                               │
│   Playwright scrapers + dlt + APIs (Python)                 │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│            CAPA BRONZE (Raw Immutable)                       │
│   Parquet en Cloudflare R2, particionado por fecha          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│           CAPA SILVER (Cleaned + Validated)                  │
│   Iceberg tables: deduplication, normalization, SCD2        │
│   dbt models + tests                                         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│          CAPA ENRICHMENT (AI + APIs)                         │
│   Geocoding + LLM classification + Property enrichment      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│         CAPA GOLD (Business-Ready)                           │
│   DuckDB / Motherduck analytics-optimized tables            │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              CAPA SERVING                                    │
│   FastAPI + Streamlit dashboard + Email reports + Stripe    │
└─────────────────────────────────────────────────────────────┘

ORQUESTACIÓN: Dagster (gestiona todo el flujo arriba)
OBSERVABILIDAD: Sentry + OpenTelemetry + Great Expectations
CI/CD: GitHub Actions (tests, deploys, scheduled runs)
```

### Estructura de directorios objetivo

```
dfw-business-intelligence-hub/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── weekly-pipeline.yml
│       └── deploy.yml
├── src/
│   ├── ingestion/
│   │   ├── grapevine_scraper.py
│   │   ├── tad_scraper.py
│   │   └── schemas.py
│   ├── transformation/
│   │   └── dbt_project/
│   ├── enrichment/
│   │   ├── geocoder.py
│   │   ├── llm_classifier.py
│   │   └── property_enricher.py
│   ├── orchestration/
│   │   └── dagster_assets/
│   ├── api/
│   │   └── fastapi_app/
│   ├── dashboard/
│   │   └── streamlit_app/
│   └── validation/
│       └── data_quality_checks.py
├── infrastructure/
│   └── terraform/
├── tests/
├── docs/
│   ├── decisions/   ← ADRs
│   ├── architecture/
│   └── runbooks/
├── data/   (gitignored)
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── notebooks/
├── .gitignore
├── pyproject.toml
├── docker-compose.yml
├── Dockerfile
├── mkdocs.yml
└── README.md
```

---

## 6. Las 5 fases — overview

| Fase | Semanas | Meta principal | Tecnologías clave entran | Output |
|------|---------|----------------|--------------------------|--------|
| **1. MVP funcional** | 1-6 | Pipeline end-to-end básico | Python, Playwright, DuckDB, GitHub | Repo + 1 fuente + email semanal |
| **2. Profesionalización** | 7-14 | Calidad de código de producción | Docker, dbt, pytest, GitHub Actions, ruff, mypy | Repo profesional + dbt project |
| **3. Cloud + orquestación** | 15-24 | Sistema cloud-native escalable | Cloudflare R2, Iceberg, Dagster, Terraform, Sentry | Sistema en cloud monitoreado |
| **4. AI-native + producto** | 25-36 | Producto vendible con AI | LLMs, pgvector, FastAPI, Streamlit, Stripe | Producto vendible + primeros clientes |
| **5. Escala** | 37-52+ | Sistema enterprise-grade | Streaming opcional, Great Expectations, OpenMetadata | Sistema completo + ingreso recurrente |

---

## 7. Fase 1: MVP funcional (semanas 1-6)

**Estado:** ⏳ Pendiente
**Tiempo estimado:** 60-72 horas (10-12h × 6 semanas)
**Compromiso de fin de fase:** Pipeline funcional + repo público + 6 piezas de contenido

### Meta tangible

Un comando `python -m src.pipeline.run_weekly` que:
1. Scrapea permits de Grapevine
2. Limpia y valida los datos
3. Geocoding básico
4. Genera CSV con leads de la semana
5. Envía email con summary + CSV

Y este comando corre automáticamente cada lunes 9am vía GitHub Actions.

### Semana 1: Fundación y primer scrape

**Objetivo:** Setup completo del entorno + primer scrape funcional.

**Entregables:**
- Repositorio público en GitHub creado
- Estructura de directorios establecida
- Python 3.12 + uv + Playwright funcionando
- Primer scrape de Grapevine guardado en `data/bronze/`
- README inicial publicado
- ADR `0001-why-this-project.md`
- Reel #1 + LinkedIn post #1

**Tecnologías introducidas:** Python, uv, Playwright, Git/GitHub.

### Semana 2: Robustez y datos limpios

**Objetivo:** Scraper robusto + datos parseados con schema validado.

**Entregables:**
- Error handling + retries en scraper
- Schemas Pydantic para validación
- Storage en Parquet (no JSON)
- Particionado por fecha
- Primer query exploratorio con DuckDB
- ADR `0002-why-parquet-over-csv.md`
- ADR `0003-why-duckdb-for-analytics.md`
- Reel #2 + LinkedIn post #2

**Tecnologías introducidas:** Pydantic, Polars, PyArrow, DuckDB.

### Semana 3: Múltiples fuentes y enriquecimiento

**Objetivo:** Segunda fuente (TAD) + geocoding básico.

**Entregables:**
- Scraper/client para TAD
- Geocoder con caché (Nominatim o Google)
- Join entre fuentes en capa Silver
- ADR `0004-geocoding-provider-decision.md`
- ADR `0005-medallion-bronze-silver-rationale.md`
- Reel #3 + LinkedIn post #3

**Tecnologías introducidas:** APIs de geocoding, manejo de joins, capa Silver.

### Semana 4: Calidad de datos y testing

**Objetivo:** Tests + validaciones + CI/CD básico.

**Entregables:**
- Suite de pytest con 20+ tests
- Data quality checks (sin Great Expectations todavía)
- ruff + mypy + pre-commit configurados
- GitHub Actions CI corriendo en cada push
- Type hints completos
- Badges en README
- ADR `0006-testing-strategy.md`
- ADR `0007-code-quality-tooling.md`
- Reel #4 + LinkedIn post #4

**Tecnologías introducidas:** pytest, ruff, mypy, pre-commit, GitHub Actions.

### Semana 5: Automatización + entrega real

**Objetivo:** Pipeline corre solo cada lunes y entrega resultados.

**Entregables:**
- Script orquestador `run_weekly.py`
- Generador de reports en CSV + markdown
- Email automation con Resend
- GitHub Actions scheduled workflow (lunes 9am)
- Secrets management
- ADR `0008-orchestration-mvp-decision.md`
- Reel #5 + LinkedIn post #5

**Tecnologías introducidas:** Resend API, GitHub Actions scheduling, secrets.

### Semana 6: Cierre de fase + showcase

**Objetivo:** Pulir, documentar exhaustivamente, mostrar.

**Entregables:**
- Repo limpio (audit completo)
- README profesional reescrito
- Sitio MkDocs publicado en GitHub Pages
- Logging estructurado
- Streamlit dashboard simple (1 página) con historial
- Índice de ADRs
- Video YouTube long-form (10-15 min)
- Reel #6 + LinkedIn carousel

**Tecnologías introducidas:** MkDocs Material, Streamlit, GitHub Pages.

### Skills aprendidas al final de Fase 1

✅ Web scraping production-grade
✅ Data validation con Pydantic
✅ Parquet + DuckDB
✅ Testing con pytest
✅ CI/CD con GitHub Actions
✅ Code quality tooling moderno
✅ Documentación técnica
✅ Architecture Decision Records

**Posicionamiento de carrera al final:** Junior data engineer empleable con portfolio sólido.

---

## 8. Fase 2: Profesionalización (semanas 7-14)

**Estado:** 🔒 Bloqueada hasta completar Fase 1
**Tiempo estimado:** 50-65 horas (6-8h × 8 semanas)

### Meta tangible

Migrar de transformaciones Python a **dbt Core** + containerizar todo con **Docker** + agregar tests de dbt + documentación auto-generada.

### Hitos clave

**Semanas 7-8: Docker + Docker Compose**
- Dockerfile multi-stage para la app
- docker-compose.yml con todos los servicios
- Volumes para data persistence
- ADR sobre containerización

**Semanas 9-11: Migración a dbt Core**
- Setup de dbt project
- 15+ modelos SQL (staging, intermediate, marts)
- Tests de dbt en cada modelo (unique, not_null, relationships, custom)
- Sources definidas
- Profiles para multiple environments
- ADR sobre dbt vs Python para transforms

**Semanas 12-13: SCD Type 2 + datos históricos**
- Implementar SCD2 en capa Silver
- Tracking de cambios de propiedades a través del tiempo
- Snapshots de dbt
- Dimensional modeling básico

**Semana 14: dbt docs + cierre**
- `dbt docs generate` + hosting
- Refactoring de capa Silver completa
- Performance tuning de queries
- Mini case study en LinkedIn

### Tecnologías nuevas introducidas

- Docker + Docker Compose
- dbt Core
- dbt tests + dbt docs
- Snapshots / SCD2
- Dimensional modeling

### Output de Fase 2

Repo con dbt project profesional, todo containerizado, documentación auto-generada de modelos, tests robustos. **Esto solo es portfolio empleable como mid-level.**

---

## 9. Fase 3: Cloud y orquestación (semanas 15-24)

**Estado:** 🔒 Bloqueada hasta completar Fase 2
**Tiempo estimado:** 70-90 horas (7-9h × 10 semanas)

### Meta tangible

Sistema corre en cloud (no en mi máquina) con **Dagster** orquestando, **Cloudflare R2** como storage, **Iceberg** para tablas Silver, **Terraform** gestionando infra, y **Sentry** monitoreando.

### Hitos clave

**Semanas 15-16: Cloud storage**
- Setup Cloudflare R2
- Migración de data local a R2
- Credentials management
- Cost monitoring

**Semanas 17-19: Apache Iceberg**
- Iceberg tables para capa Silver
- ACID transactions
- Time travel queries
- Schema evolution
- Comparativa con Delta Lake (ADR)

**Semanas 20-22: Dagster**
- Migración de scripts a Dagster assets
- Schedules + sensors
- Asset lineage
- Dagster UI deployment
- Retry policies

**Semanas 23-24: Terraform + monitoring**
- Terraform modules para toda la infra
- Sentry integration para errors
- Logging structurado a cloud
- Multi-condado: agregar Dallas County

### Tecnologías nuevas introducidas

- Cloudflare R2 (S3-compatible)
- Apache Iceberg
- Dagster (assets, schedules, sensors)
- Terraform
- Sentry

### Output de Fase 3

Sistema cloud-native, escalable, monitoreado, con orquestación profesional. **Mid-to-senior level data engineer portfolio.**

---

## 10. Fase 4: AI-native y producto vendible (semanas 25-36)

**Estado:** 🔒 Bloqueada hasta completar Fase 3
**Tiempo estimado:** 80-100 horas (7-9h × 12 semanas)

### Meta tangible

Producto vendible con AI integration + primeros clientes piloto pagando.

### Hitos clave

**Semanas 25-27: LLM enrichment**
- Pipeline de classification con Claude/OpenAI
- Prompt engineering estructurado
- Caching de responses (no re-procesar)
- Cost optimization
- Batch processing

**Semanas 28-29: Embeddings + búsqueda semántica**
- pgvector setup
- Embedding pipeline
- "Properties similar to X" feature
- ADR sobre embedding model

**Semanas 30-32: API y dashboard**
- FastAPI backend con auth
- Endpoints para clientes
- Streamlit dashboard público
- Rate limiting
- API documentation con Swagger

**Semanas 33-34: Billing y onboarding**
- Stripe integration
- Subscription tiers
- Customer onboarding flow
- Trial management

**Semanas 35-36: Primeros clientes**
- Outreach a 50 prospects DFW
- 3-5 discovery calls
- 1-3 piloto clients (precio reducido $49-99/mes para validación)
- Feedback iteration

### Tecnologías nuevas introducidas

- Claude API / OpenAI API
- pgvector + Postgres
- FastAPI
- Stripe
- Auth (Clerk o similar)
- Streamlit avanzado

### Output de Fase 4

**Producto real generando ingresos.** Posicionamiento profesional: data engineer con experiencia en AI/ML production + entrepreneurial track record.

---

## 11. Fase 5: Escala y diferenciación (semanas 37-52+)

**Estado:** 🔒 Bloqueada hasta completar Fase 4
**Tiempo estimado:** 100+ horas (variable según prioridades)

### Meta tangible

Sistema enterprise-grade + 5-10 clientes pagados + decisión consciente de próximos pasos (empleo vs negocio full-time vs híbrido).

### Hitos posibles (priorizar según necesidad real)

- **Streaming:** Redpanda para datos en tiempo real (si justifica)
- **Data quality:** Great Expectations framework completo
- **Catalog:** OpenMetadata para lineage y discovery
- **Mobile-first:** dashboard responsive optimizado
- **Más fuentes:** business licenses, court records, etc.
- **Optimización:** query performance, costs, latencia
- **Equipo:** primer hire (junior LATAM remoto) si MRR justifica

### Decisión al final de Fase 5

A los 12 meses, evaluar:

| Escenario | Acción |
|-----------|--------|
| Empleo data engineer aparece a $130k+/año | Aceptar. Mantener BI Hub como side project pasivo. |
| BI Hub explota (10+ clientes, $5k+ MRR) | Doblar en BI Hub. Considerar full-time. |
| Ninguna de las dos | Continuar construyendo. 12 meses más de portfolio + audiencia siempre vale. |

---

## 12. Estrategia de contenido

### Plataformas y propósitos

| Plataforma | Propósito | Frecuencia | Idioma |
|------------|-----------|------------|--------|
| **LinkedIn** | Recruiters + B2B prospects | 1-2 posts/semana | Español + Inglés |
| **Instagram Reels** | Audiencia técnica hispana + branding | 1 reel/semana | Español |
| **TikTok** | Mismo contenido que Reels (cross-post) | 1/semana | Español |
| **YouTube** | Long-form técnico + portfolio | 1 video/mes | Español |
| **GitHub** | Código + documentación | Continuo | Inglés (código) |
| **Twitter/X** | Networking técnico opcional | 2-3/semana | Inglés |

### Formato del journey

**Cada semana de construcción → al menos 1 pieza de contenido.**

Categorías de contenido:

1. **"Building in public"** — progreso tangible, screenshots, demos
2. **Tutorial técnico** — algo específico que aprendí esta semana
3. **Decisión técnica** — explicar un ADR en formato accesible
4. **Lessons learned** — errores y cómo los resolví
5. **Comparativa** — tecnología X vs Y desde experiencia real

### Métricas que importan (y las que no)

**Importan:**
- Engagement de calidad (comments con preguntas técnicas)
- DMs de recruiters
- Inbound leads de potenciales clientes
- Crecimiento de audiencia profesional en LinkedIn

**No importan:**
- Vanity metrics (likes, follows brutos sin engagement)
- Viralidad
- Consistencia perfecta — mejor 80% consistencia sostenible

---

## 13. Cómo usar este documento

### Para mí (Daniel)

1. **Re-leer al inicio de cada semana** — orientación rápida
2. **Actualizar estado** al completar cada hito (cambiar ⏳ a ✅)
3. **Re-evaluar al final de cada fase** — ¿el plan sigue siendo correcto?
4. **No saltarse fases** — cada una construye sobre la anterior

### Para Cursor / Claude Code

Cargar este documento como contexto del proyecto al inicio de cada sesión de coding. Permite que la AI:
- Entienda el stack objetivo
- Sepa en qué fase estamos
- Respete las decisiones arquitectónicas tomadas
- No sugiera tecnologías fuera del scope actual de la fase

**Prompt recomendado para nuevas sesiones de Cursor:**
> "Estoy trabajando en el DFW Business Intelligence Hub. Lee `ROADMAP.md` para entender el contexto. Estamos actualmente en Fase [X], semana [Y]. Hoy quiero trabajar en [tarea específica]. Respeta las decisiones del roadmap y no introduzcas tecnologías de fases futuras."

### Para conversaciones futuras con Claude (asistente)

Cuando regrese a hablar contigo:

1. **Compartir este documento actualizado** al inicio de la conversación
2. **Indicar fase y semana actual**
3. **Especificar qué necesito** (expandir una fase, resolver un blocker técnico, ajustar el plan)

**Frase tipo para empezar conversaciones:**
> "Aquí está mi roadmap actualizado. Estoy en Fase [X], semana [Y]. Necesito que me ayudes con [necesidad específica]. ¿Puedes profundizar en [sección]?"

### Reglas de actualización del documento

- ✅ Actualizar estado de hitos completados
- ✅ Agregar ADRs decididos al log
- ✅ Ajustar fechas si voy adelantado/atrasado
- ⚠️ NO cambiar la estructura de fases sin reflexión seria
- ⚠️ NO agregar tecnologías al stack sin justificación documentada
- ❌ NO eliminar el plan de negocio (es lo que da contexto al técnico)

---

## Apéndice: Recursos de referencia

### Cursos / aprendizaje recomendado durante el journey

- **dbt Fundamentals** (dbt Labs, gratis) — antes de Fase 2
- **Dagster University** (gratis) — antes de Fase 3
- **Apache Iceberg docs + tutorials** — antes de Fase 3
- **Designing Data-Intensive Applications** (Martin Kleppmann) — lectura paralela continua

### Comunidades

- **Locally Optimistic** (Slack) — data community profesional
- **dbt Community Slack**
- **Dagster Slack**
- **r/dataengineering** (Reddit)
- **DFW Data Engineering Meetup** (presencial)

### Inspiración de portfolios públicos

- Repos de dbt-labs, dagster-io
- Blog de Maxime Beauchemin (creador de Airflow + Superset)
- Substack de Benn Stancil (Mode Analytics)
- Channels de Seattle Data Guy en YouTube

---

**Fin del roadmap.**

> Este documento es vivo. Última revisión completa: Abril 2026.
> Próxima revisión obligatoria: al completar Fase 1 (estimado: junio 2026).
