"""Compose card thumbnails for the SimpleVox and flashcard-songs project cards.

Colors/fonts mirror the real flashcard-songs app palette; card content is real
vocabulary from the shipped deck. Run: python tools/make_card_images.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.font_manager import FontProperties

OUT_DIR = r"C:\Coding Projects\john-draper.github.io\images"

# Windows CJK-capable fonts (app uses Yu Gothic)
CJK = FontProperties(fname=r"C:\Windows\Fonts\YuGothR.ttc")
CJK_B = FontProperties(fname=r"C:\Windows\Fonts\YuGothB.ttc")

# flashcard-songs app palette
PINK_BG, PINK, PINK_DEEP = "#fff0f7", "#e85d9c", "#c43c79"
GOLD, GREEN, INK = "#f5b945", "#3fb57a", "#3a2230"
SOFT = "#9a6a86"


def rounded(ax, x, y, w, h, fc, ec="none", lw=0, r=0.03, alpha=1.0, z=2):
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle=f"round,pad=0,rounding_size={r}",
                         fc=fc, ec=ec, lw=lw, alpha=alpha, zorder=z)
    ax.add_patch(box)
    return box


def make_flashcards(path):
    fig, ax = plt.subplots(figsize=(14.2, 8.0), dpi=150)
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.6); ax.axis("off")
    fig.patch.set_facecolor(PINK_BG)

    # header
    ax.text(0.55, 5.05, "Song Lyric Flashcards", fontproperties=CJK_B,
            fontsize=30, color=INK, va="center")
    ax.text(0.57, 4.55, "self-contained HTML decks  ·  offline Android app (APK)",
            fontsize=15, color=SOFT, va="center")

    # back card (tilted, showing the answer side)
    b = matplotlib.transforms.Affine2D().rotate_deg_around(7.4, 1.6, 7) + ax.transData
    rounded(ax, 4.85, 0.62, 4.45, 3.15, "#ffffff", z=3)
    ax.text(7.07, 2.95, "ts\u016bchi", fontsize=34, color=INK,
            ha="center", va="center")
    ax.text(7.07, 2.15, "notification", fontsize=22, color=PINK_DEEP,
            ha="center", va="center")
    ax.text(7.07, 1.25, "\u2713  studied", fontsize=15, color=GREEN,
            ha="center", va="center")
    for p in ax.texts[-3:]:
        p.set_transform(b)
    ax.patches[-1].set_transform(b)
    # shadow under back card
    rounded(ax, 4.95, 0.5, 4.45, 3.15, "#00000012", z=2)
    ax.patches[-1].set_transform(b)

    # front card (question side)
    rounded(ax, 0.75, 0.55, 4.6, 3.4, "#ffffff", z=5)
    rounded(ax, 0.75, 3.5, 4.6, 0.45, PINK, z=6)
    ax.text(3.05, 3.72, "card 23 / 86", fontsize=14, color="white",
            ha="center", va="center", zorder=7)
    ax.text(3.05, 2.45, "\u901a\u77e5", fontproperties=CJK_B, fontsize=64,
            color=INK, ha="center", va="center", zorder=7)
    ax.text(3.05, 1.62, "\u3064\u3046\u3061", fontproperties=CJK, fontsize=24,
            color=SOFT, ha="center", va="center", zorder=7)
    ax.text(3.05, 1.08, "tap to flip", fontsize=12, color=PINK,
            ha="center", va="center", zorder=7)

    # progress bar
    rounded(ax, 5.9, 4.62, 3.4, 0.34, "#ffffff", z=4)
    rounded(ax, 5.9, 4.62, 1.7, 0.34, GREEN, z=5)
    ax.text(9.42, 4.79, "17 / 86 studied", fontsize=13, color=INK,
            ha="left", va="center")

    fig.savefig(path, facecolor=PINK_BG, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)


def make_simplevox(path):
    INK2, TEAL, SLATE = "#22303c", "#2a9d8f", "#457b9d"
    stages = [
        ("1", "Transcribe", "WhisperX word-level\ntimestamps"),
        ("2", "Match", "profanity \u2192 clean\neuphemism"),
        ("3", "Speak", "edge-tts neural\nvoice"),
        ("4", "Splice", "duration-matched\naudio swap (ffmpeg)"),
    ]
    fig, ax = plt.subplots(figsize=(14.2, 8.0), dpi=150)
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.6); ax.axis("off")
    fig.patch.set_facecolor("white")

    ax.text(0.55, 5.05, "SimpleVox", fontsize=30, color=INK2,
            fontweight="bold", va="center")
    ax.text(0.57, 4.55, "profanity filter for video  \u00b7  only the audio track is edited, video stays lossless",
            fontsize=15, color="#64748b", va="center")

    y0, w, h = 1.55, 2.0, 2.1
    xs = [0.45, 2.85, 5.25, 7.65]
    for (num, title, sub), x in zip(stages, xs):
        rounded(ax, x, y0, w, h, "#f1f5f9", ec=SLATE, lw=1.6, r=0.12, z=3)
        rounded(ax, x + 0.16, y0 + h - 0.62, 0.5, 0.46, TEAL, r=0.08, z=4)
        ax.text(x + 0.41, y0 + h - 0.39, num, fontsize=17, color="white",
                ha="center", va="center", fontweight="bold", zorder=5)
        ax.text(x + 0.82, y0 + h - 0.39, title, fontsize=18, color=INK2,
                ha="left", va="center", fontweight="bold", zorder=5)
        ax.text(x + w / 2, y0 + 0.72, sub, fontsize=13.5, color="#475569",
                ha="center", va="center", zorder=5)

    for x in xs[:-1]:
        arrow = FancyArrowPatch((x + w + 0.06, y0 + h / 2),
                                (x + w + 0.34, y0 + h / 2),
                                arrowstyle="-|>", mutation_scale=26,
                                color=TEAL, lw=2.4, zorder=6)
        ax.add_patch(arrow)

    ax.text(0.45, 0.85, "input: any video file(s)", fontsize=13, color="#64748b",
            ha="left", va="center")
    ax.text(9.65, 0.85, "output: clean video", fontsize=13, color=TEAL,
            ha="right", va="center", fontweight="bold")

    fig.savefig(path, facecolor="white", bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)


if __name__ == "__main__":
    make_flashcards(fr"{OUT_DIR}\flashcards_card.png")
    make_simplevox(fr"{OUT_DIR}\simplevox_pipeline.png")
    print("done")
