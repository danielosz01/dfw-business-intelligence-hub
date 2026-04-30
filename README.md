DFW Business Intelligence Hub
> Plataforma de inteligencia de mercado geolocalizada para Dallas-Fort Worth. Captura, procesa y entrega datos públicos (permits de construcción, registros de propiedad, datos de negocios) para empresas B2B locales.
[!Status]()
[!Python]()
[!License]()
***¿Qué es esto?
Un pipeline de datos en arquitectura medallón (Bronze / Silver / Gold) que automatiza la captura de fuentes públicas de DFW y entrega leads geolocalizados a contratistas, inversores inmobiliarios y servicios B2B locales.
Estado actual: Fase 1 (MVP funcional) — semana 1 de 6.
¿Por qué público?
Este repositorio cumple tres funciones simultáneas:
Portfolio técnico para conseguir empleo como data engineer.
Producto comercial vendible a empresas B2B en DFW.
Contenido educativo sobre data engineering moderno en español.
El roadmap completo está en ROADMAP.md.
Stack
Python 3.12 · uv · Playwright · Pydantic · DuckDB · Parquet · dbt · Dagster
Cloudflare R2 · Apache Iceberg · FastAPI · Streamlit · Stripe · Sentry
Cada tecnología entra en una fase específica documentada en el roadmap. No se agrega nada por moda.
Quickstart
# Pre-requisitos: uv (https://astral.sh/uv) y Python 3.12 gestionado por uv
git clone git@github.com:<usuario>/dfw-business-intelligence-hub.git
cd dfw-business-intelligence-hub
uv sync
uv run playwright install chromium
# Correr el scraper de la semana
uv run python -m src.ingestion.grapevine_scraper
El raw output se guarda en data/bronze/grapevine/permits/dt=YYYY-MM-DD/.
Estructura
src/
├── ingestion/      Scrapers + clients de APIs públicas
├── transformation/ dbt project (Fase 2+)
├── enrichment/     Geocoding + LLM classification (Fase 3+)
├── orchestration/  Dagster assets (Fase 3+)
├── api/            FastAPI (Fase 4+)
├── dashboard/      Streamlit (Fase 4+)
├── validation/     Data quality checks
└── pipeline/       Orquestador del weekly run
docs/
├── decisions/      Architecture Decision Records
├── architecture/   Diagramas y notas
└── runbooks/       Operación
data/               (gitignored) Bronze / Silver / Gold local
infrastructure/     Terraform (Fase 3+)
Architecture Decision Records
Decisiones técnicas importantes están versionadas en docs/decisions/. Empezamos con ADR 0001 — Why this project.
Roadmap
5 fases en 52 semanas. Detalle completo en ROADMAP.md.
Fase	Semanas	Output
MVP funcional	1-6	Pipeline end-to-end + email semanal
Profesionalización	7-14	Docker + dbt + tests
Cloud + orquestación	15-24	R2 + Iceberg + Dagster
AI-native + producto	25-36	Producto vendible + primeros clientes
Escala	37-52+	Sistema enterprise + ingreso recurrente
Journey público
Sigo el progreso en:
LinkedIn: linkedin.com/in/danielostos ← actualiza
Instagram / TikTok: técnico en español
YouTube: long-form mensual
Licencia
MIT — ver LICENSE.
Disclaimer
Este proyecto consume datos públicos respetando los Terms of Service de cada fuente y rate limiting razonable. Los datos no se redistribuyen sin valor agregado. Foreclosures y registros con regulación elevada quedan fuera del scope del MVP.