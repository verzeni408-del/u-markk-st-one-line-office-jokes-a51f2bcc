#!/usr/bin/env python3
"""One-line office joke entry writer (stdlib only)."""

JOKE = (
    "My performance review said I need to be more visible, so HR "
    "scheduled a meeting to discuss why nobody noticed I quit in March."
)


def main():
    text = " ".join(JOKE.split())
    assert 1 <= len(text) <= 199, "entry must be 1-199 characters"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print("wrote %d chars" % len(text))


if __name__ == "__main__":
    main()
