"""
Scraper de permits de la ciudad de Grapevine, TX.

Semana 1, Fase 1 — versión esqueleto.

Filosofía de esta versión:
- Capturar raw data sin parsearla en exceso. La normalización es Semana 2-3.
- Guardar en data/bronze/ particionado por fecha de scrape (no fecha del permit).
- Si el portal expone un endpoint JSON, preferirlo sobre Playwright (más rápido,
  más estable). Si no, usar Playwright para renderizar y extraer.

Cómo correr:
    uv run python -m src.ingestion.grapevine_scraper

Output:
    data/bronze/grapevine/permits/dt=YYYY-MM-DD/raw.json
    data/bronze/grapevine/permits/dt=YYYY-MM-DD/_meta.json
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# =============================================================================
# CONFIGURACIÓN — AJUSTAR EN DÍA 3 (exploración del portal)
# =============================================================================

# URL del portal de permits de Grapevine TX (verificar en Día 3)
# Pista: probablemente algo como https://grapevinetx.mygov.us/...
BASE_URL = "https://www.grapevinetexas.gov/"  # ← REEMPLAZAR

# Ruta donde se guarda el bronze
BRONZE_ROOT = Path("data/bronze/grapevine/permits")

# Headers para requests HTTP (si encontraste endpoint JSON)
HEADERS = {
    "User-Agent": "DFW-BI-Hub/0.1 (research; danielostos1999@gmail.com)",
    "Accept": "application/json, text/html",
}

# Rate limiting: segundos entre requests (sé respetuoso)
REQUEST_DELAY_SECONDS = 2.0


# =============================================================================
# OPCIÓN A — Endpoint JSON (preferido si existe)
# =============================================================================


def fetch_permits_via_api() -> list[dict[str, Any]] | None:
    """
    Si encontraste un endpoint JSON en el Network tab del Día 3,
    impleméntalo aquí. Devuelve None si no hay endpoint disponible.
    """
    import httpx  # noqa: PLC0415  (import local: solo si se usa esta opción)

    # Ejemplo placeholder — reemplazar con la URL real:
    # endpoint = f"{BASE_URL}/api/permits?days=7"
    # try:
    #     response = httpx.get(endpoint, headers=HEADERS, timeout=30.0)
    #     response.raise_for_status()
    #     return response.json()
    # except httpx.HTTPError as exc:
    #     print(f"⚠ API no disponible o cambió: {exc}", file=sys.stderr)
    #     return None

    return None  # Placeholder — quitar cuando implementes


# =============================================================================
# OPCIÓN B — Playwright (fallback si no hay endpoint JSON)
# =============================================================================


def fetch_permits_via_playwright() -> list[dict[str, Any]]:
    """
    Scrape del portal renderizado. Estos selectores son placeholders —
    reemplázalos en el Día 4 con los que identificaste con `playwright codegen`.
    """
    from playwright.sync_api import sync_playwright

    permits: list[dict[str, Any]] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=HEADERS["User-Agent"],
            viewport={"width": 1280, "height": 800},
        )
        page = context.new_page()

        print(f"→ Navegando a {BASE_URL}", flush=True)
        page.goto(BASE_URL, wait_until="domcontentloaded", timeout=30_000)

        # ─────────────────────────────────────────────────────────────────────
        # AJUSTAR EN DÍA 4: navegación al listado de permits
        # ─────────────────────────────────────────────────────────────────────
        # Ejemplo:
        # page.click("text=Permits")
        # page.wait_for_selector("table.permits-list", timeout=10_000)
        # rows = page.query_selector_all("table.permits-list tr.permit-row")
        # for row in rows:
        #     permits.append({
        #         "permit_number": row.query_selector(".permit-number").inner_text(),
        #         "address": row.query_selector(".address").inner_text(),
        #         "type": row.query_selector(".type").inner_text(),
        #         "issued_date": row.query_selector(".date").inner_text(),
        #     })

        # Mientras no haya selectores reales, capturamos el HTML de la home
        # para tener algo no-vacío en bronze (Día 4 lo reemplaza).
        permits.append(
            {
                "_placeholder": True,
                "_url": page.url,
                "_title": page.title(),
                "_html_snippet": page.content()[:5000],
            }
        )

        time.sleep(REQUEST_DELAY_SECONDS)
        browser.close()

    return permits


# =============================================================================
# Bronze writer
# =============================================================================


def save_to_bronze(permits: list[dict[str, Any]], source: str) -> Path:
    """Guarda raw + metadata en bronze, particionado por fecha de scrape."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    partition_dir = BRONZE_ROOT / f"dt={today}"
    partition_dir.mkdir(parents=True, exist_ok=True)

    raw_path = partition_dir / "raw.json"
    meta_path = partition_dir / "_meta.json"

    raw_payload = json.dumps(permits, ensure_ascii=False, indent=2)
    raw_path.write_text(raw_payload, encoding="utf-8")

    meta = {
        "source": source,
        "scraped_at_utc": datetime.now(timezone.utc).isoformat(),
        "record_count": len(permits),
        "raw_sha256": hashlib.sha256(raw_payload.encode("utf-8")).hexdigest(),
        "scraper_version": "0.1.0",
        "base_url": BASE_URL,
    }
    meta_path.write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    return raw_path


# =============================================================================
# Entrypoint
# =============================================================================


def main() -> int:
    print("─" * 60)
    print(f"DFW BI Hub — Grapevine permits scraper")
    print(f"Started: {datetime.now(timezone.utc).isoformat()}")
    print("─" * 60)

    # Intenta primero la API (más rápido, más estable)
    permits = fetch_permits_via_api()
    source = "api"

    if permits is None:
        print("→ API no disponible, usando Playwright")
        permits = fetch_permits_via_playwright()
        source = "playwright"

    if not permits:
        print("✗ No se obtuvieron permits", file=sys.stderr)
        return 1

    output_path = save_to_bronze(permits, source=source)
    print(f"✓ Saved {len(permits)} permits to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
