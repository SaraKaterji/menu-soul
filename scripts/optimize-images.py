"""Resize oversized PNGs and emit WebP copies for faster page loads."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1] / "assets"
MAX_WIDTH = 1400
WEBP_QUALITY = 82
BUTTON_QUALITY = 90


def quality_for(name: str) -> int:
    lowered = name.lower()
    if "button" in lowered or "btn" in lowered:
        return BUTTON_QUALITY
    return WEBP_QUALITY


def optimize(path: Path) -> tuple[int, int, int, int]:
    original_size = path.stat().st_size
    webp_path = path.with_suffix(".webp")
    with Image.open(path) as im:
        image = im.convert("RGBA")
        width, height = image.size
        if width > MAX_WIDTH:
            ratio = MAX_WIDTH / width
            image = image.resize(
                (MAX_WIDTH, max(1, round(height * ratio))),
                Image.Resampling.LANCZOS,
            )
        image.save(
            webp_path,
            "WEBP",
            quality=quality_for(path.name),
            method=4,
        )
    after = webp_path.stat().st_size
    if after >= original_size:
        webp_path.unlink()
        return original_size, original_size, width, width
    return original_size, after, width, image.size[0]


def main() -> None:
    Image.MAX_IMAGE_PIXELS = None
    total_in = 0
    total_out = 0
    print(f"{'PNG KB':>9} {'WEBP KB':>9} {'save':>7}  name", flush=True)
    for path in sorted(ROOT.glob("*.png")):
        before, after, old_w, new_w = optimize(path)
        total_in += before
        total_out += after
        if after == before and not path.with_suffix(".webp").exists():
            note = "  kept PNG (webp was larger)"
        elif new_w != old_w:
            note = f"  resized {old_w}->{new_w}"
        else:
            note = ""
        print(
            f"{before / 1024:9.1f} {after / 1024:9.1f} "
            f"{(1 - after / before) * 100:6.1f}%  {path.name}{note}",
            flush=True,
        )
    print(
        f"\nTotal PNG {total_in / 1024 / 1024:.2f} MB -> "
        f"served {total_out / 1024 / 1024:.2f} MB "
        f"({(1 - total_out / total_in) * 100:.1f}% smaller)",
        flush=True,
    )


if __name__ == "__main__":
    main()
