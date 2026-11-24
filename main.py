import os

TEXT = "fix(prod): remove the bug by removing the feature, the tests, and all evidence it ever shipped"


def main() -> None:
    assert len(TEXT) <= 180, f"entry is {len(TEXT)} code points, over the 180 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
