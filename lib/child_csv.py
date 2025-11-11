from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from lib.parent_class import ParentClass, CSVConfig


class childCSV(ParentClass):
    def __init__(self, config: CSVConfig):
        super().__init__(config)    
        self.df = self.read_csv()     

    def _ensure_output_dir(self) -> Path:
        out_dir = Path("Output Data")
        out_dir.mkdir(parents=True, exist_ok=True)
        return out_dir

    def _require_cols(self, cols):
        missing = [c for c in cols if c not in self.df.columns]
        if missing:
            raise KeyError(f"Missing required column(s): {missing}")

    def violin_plot(self):
        column = "Beats Per Minute"
        self._require_cols([column])

        df = self.df
        plt.figure(figsize=self.config.fig_size)
        plt.title(f"{self.config.title_prefix}: Violin ({column})")
        plt.grid(True, linestyle="--", alpha=0.3)

        data = [df[column].dropna().values]
        plt.violinplot(dataset=data, showmeans=True, showmedians=True)
        plt.xticks([1], [column])
        plt.ylabel(column)
        plt.ylim(0, 200) 

        out_path = self._ensure_output_dir() / "Output_Data_Bpm.png"
        plt.tight_layout()
        plt.savefig(out_path, dpi=200, bbox_inches="tight")
        plt.show()
        print(f"Saved violin plot -> {out_path.resolve()}")

    def box_whisker_year(self):
        column = "Year"
        self._require_cols([column])

        df = self.df.copy()
        # filter 2010–2019
        df = df[(df[column] >= 2010) & (df[column] <= 2019)].dropna(subset=[column])
        if df.empty:
            raise ValueError("No rows found for Year in [2010, 2019].")

        plt.figure(figsize=self.config.fig_size)
        plt.title(f"{self.config.title_prefix}: Box & Whisker (Years 2010–2019)")
        plt.grid(True, linestyle="--", alpha=0.3)

        plt.boxplot([df[column].values], notch=True, vert=True)
        plt.xticks([1], ["Years 2010–2019"])
        plt.ylabel(column)
        plt.ylim(2010, 2019)

        out_path = self._ensure_output_dir() / "Output_Data_Year.png"
        plt.tight_layout()
        plt.savefig(out_path, dpi=200, bbox_inches="tight")
        plt.show()
        print(f"Saved year box plot -> {out_path.resolve()}")

    def scatter_dance_vs_energy(self):
        x, y = "Danceability", "Energy"
        self._require_cols([x, y])

        df = self.df.dropna(subset=[x, y]).copy()

        plt.figure(figsize=self.config.fig_size)
        plt.title(f"{self.config.title_prefix}: {x} vs {y}")
        plt.grid(True, linestyle="--", alpha=0.3)

        plt.scatter(df[x], df[y], alpha=0.8)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.xlim(0, 200)
        plt.ylim(0, 200)

        out_path = self._ensure_output_dir() / "Output_Data_DanceVsEnergy.png"
        plt.tight_layout()
        plt.savefig(out_path, dpi=200, bbox_inches="tight")
        plt.show()
        print(f"Saved scatter plot -> {out_path.resolve()}")

    def query_artist_search(self, artist_name: str, *, save_csv: bool = True) -> pd.DataFrame:
        """Boolean indexing: return rows where 'artist' contains name (case-insensitive)."""
        for c in ["artist", "title"]:
            if c not in self.df.columns:
                raise KeyError(f"Required column missing: {c!r}")

        df = self.df.copy()
        mask = df["artist"].astype("string").str.contains(artist_name, case=False, na=False)
        out = df[mask].copy()

        preferred = [
            "artist", "title", "Year", "Beats Per Minute",
            "Danceability", "Energy", "Genre", "Popularity", "Rank",
        ]
        keep = [c for c in preferred if c in out.columns]
        if keep:
            out = out[keep]

        if save_csv:
            out_path = self._ensure_output_dir() / "Output_Data_Artist_Search.csv"
            out.to_csv(out_path, index=False)
            print(f"Saved artist search CSV ({len(out)} rows) -> {out_path.resolve()}")

        return out
