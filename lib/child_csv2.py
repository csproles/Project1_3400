import pandas as pd
import seaborn as sns
from .parent_class import ParentClass

class BabyNamesCSV(ParentClass):

    def __init__(self, config: CSVConfig):
        super().__init__(config)        
        self.df = self.read_csv()         

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

        output_folder = Path("Output Data")
        output_folder.mkdir(parents=True, exist_ok=True)

        out_path = out_dir / "Output_Data_Bpm.png"
        plt.tight_layout()
        plt.savefig(out_path, dpi=200, bbox_inches="tight")
        plt.show()

        print(f"saved plot to: {out_path.resolve()}")

    def box_whisker_year(self):
        column = "Year"

        self._require_cols([column])

        df = self.df.copy()

        df[column] = pd.to_numeric(df[column], errors="coerce")

        df = df[(df[column] >= 2010) & (df[column] <= 2019)].dropna(subset=[column])

        if df.empty:
            raise ValueError("no rows found between 2010 and 2019")

        plt.figure(figsize=self.config.fig_size)
        plt.title("Spotify Data: Year Distribution (2010–2019)")
        plt.grid(True, linestyle="--", alpha=0.3)

        plt.boxplot([df[column].values], notch=True, vert=True)

        plt.xticks([1], ["Years 2010-2019"])
        plt.ylabel("Year")

        out_dir = Path("Output Data")
        out_dir.mkdir(parents=True, exist_ok=True)

        out_path = out_dir / "Output_Data_Year.png"

        plt.tight_layout()
        plt.savefig(out_path, dpi=200, bbox_inches="tight")
        plt.show()

        print(f"saved year box plot: {out_path.resolve()}")
    def scatter_dance_vs_energy(self):
        x = "Danceability"
        y = "Energy"

        self._require_cols([x, y])

        df = self.df.copy()

        df[x] = pd.to_numeric(df[x], errors="coerce")
        df[y] = pd.to_numeric(df[y], errors="coerce")

        df = df.dropna(subset=[x, y])

        plt.figure(figsize=self.config.fig_size)
        plt.title("Spotify Data: Danceability vs Energy")
        plt.grid(True, linestyle="--", alpha=0.3)

        plt.scatter(df[x], df[y], alpha=0.8)

        plt.xlabel(x)
        plt.ylabel(y)

        out_dir = Path("Output Data")
        out_dir.mkdir(parents=True, exist_ok=True)

        out_path = out_dir / "Output_Data_DanceVsEnergy.png"
        plt.tight_layout()
        plt.savefig(out_path, dpi=200, bbox_inches="tight")
        plt.show()

        print(f"saved scatter plot: {out_path.resolve()}")
    def _ensure_output_dir(self) -> Path:
        out = Path("Output Data")
        out.mkdir(parents=True, exist_ok=True)
        return out

    def query_artist_search(
        self,
        artist_name: str,
        *,
        save_csv: bool = True,
    ) -> pd.DataFrame:

        df = self.df.copy()

        if "artist" not in df.columns:
            raise KeyError("Column 'artist' not found in dataset")
        if "title" not in df.columns:
            raise KeyError("Column 'title' not found in dataset")

        mask = df["artist"].astype("string").str.contains(artist_name, case=False, na=False)
        out = df[mask].copy()

        preferred = [
            "artist", "title", "Year", "Beats Per Minute",
            "Danceability", "Energy", "Genre", "Popularity", "Rank"
        ]
        keep = [c for c in preferred if c in out.columns]
        if keep:
            out = out[keep]

        if save_csv:
            out_dir = self._ensure_output_dir()
            csv_path = out_dir / "Output_Data_Artist_Search.csv"
            out.to_csv(csv_path, index=False)
            print(f"Saved artist search results -> {csv_path.resolve()}")

        return out
