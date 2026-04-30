# Architecture Decision Records (ADRs)

Cada decisión técnica importante del DFW Business Intelligence Hub vive aquí como un ADR. Inspirado en el formato de Michael Nygard, adaptado al proyecto.

## Por qué ADRs

- **Memoria de contexto.** En 6 meses no recordaré por qué elegí Iceberg sobre Delta Lake. El ADR sí.
- **Material de portfolio.** Cada ADR es contenido para LinkedIn / blog / interview.
- **Disciplina de pensamiento.** Escribir la decisión obliga a justificarla.

## Cómo crear un ADR nuevo

1. Copia [`_template.md`](./_template.md) a `NNNN-titulo-corto.md` con el siguiente número disponible.
2. Llena las secciones. Si una sección no aplica, escribe explícitamente "no aplica" en lugar de eliminarla.
3. Estado inicial: `Propuesto`. Pasa a `Aceptado` cuando lo decides definitivamente.
4. Linkéalo desde el índice de abajo.

## Índice

| # | Título | Estado | Fecha |
|---|--------|--------|-------|
| [0001](./0001-why-this-project.md) | Por qué construyo el DFW Business Intelligence Hub | Aceptado | 2026-04-30 |

## Convenciones

- Numeración correlativa, sin saltos.
- Slugs en kebab-case y en inglés (`0002-why-parquet-over-csv.md`) para que el repo sea legible para audiencia técnica internacional.
- El cuerpo del ADR puede estar en español o inglés según el target del momento. ADR 0001 está en español porque su audiencia primaria es Daniel + audiencia hispana.
- Un ADR no se edita después de aceptarse. Si la decisión cambia, se crea un ADR nuevo que marca al anterior como "Reemplazado por ADR-XXXX".
