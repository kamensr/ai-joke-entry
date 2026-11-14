import os

JOKE = (
    "My AI coding agent finished in 3 minutes what used to take me 3 days. "
    "Now I spend those 3 days reviewing what it finished in 3 minutes."
)


def main() -> None:
    out = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 280
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
