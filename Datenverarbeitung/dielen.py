from pathlib import Path
from dataclasses import dataclass
import pyarrow as pa
import pyarrow.parquet as pq
import h5py
import pyarrow.compute as pc

root_path = Path(__file__).resolve().parent.parent

@dataclass
class ParquetUmwandlung:
    ungefiltert_mat: Path = root_path/"temp"
    ungefiltert_parquet: Path = root_path/"data"
    gefiltert_parquet: Path = root_path/"sorted_data"
    MS_PRO_TAG: int = 86400000
    MAT_T_OFFSET: int = 719529
    filterung: bool = True
    samplerate: int = 50

    def __post_init__(self):
            self.ungefiltert_mat.mkdir(parents=True, exist_ok=True)
            self.ungefiltert_parquet.mkdir(parents=True, exist_ok=True)
            self.gefiltert_parquet.mkdir(parents=True, exist_ok=True)

    def mat_zu_parquet(self, mat_datei: Path):        
        signal, zeit, wert = [], [], []
        with h5py.File(mat_datei, "r") as datei:
            for name, daten in datei.items():
                signal.extend([name] * daten.shape[1])
                zeit.extend((daten[0] - self.MAT_T_OFFSET) * self.MS_PRO_TAG)
                wert.extend(daten[1])

        tabelle = pa.table(
            {
                "signal": signal,
                "zeit": pa.array(zeit, type = pa.int64()).cast(pa.timestamp("ms")),
                "wert": pc.round(pa.array(wert, type = pa.float64()), ndigits=3),
            }
        )

        if self.filterung:
            _sortiert = tabelle.sort_by(
                [
                    ("signal", "ascending"),
                    ("zeit", "ascending"),
                ]
            )

            _zeit_ms = pc.cast(_sortiert["zeit"], pa.int64())

            _abschnitt_ms = pa.array(
                [
                    (zeit // self.samplerate) * self.samplerate
                    for zeit in _zeit_ms.to_pylist()
                ],
                type=pa.int64(),
            )

            _sortiert = _sortiert.append_column("_abschnitt_ms", _abschnitt_ms)

            gruppiert = (
                _sortiert
                .group_by(
                    ["signal", "_abschnitt_ms"],
                    use_threads=False,
                )
                .aggregate(
                    [
                        ("zeit", "first"),
                        ("wert", "first"),
                    ]
                )
            )

            tabelle = pa.table(
                {
                    "signal": gruppiert["signal"],
                    "zeit": gruppiert["zeit_first"],
                    "wert": gruppiert["wert_first"],
                }
            )
            zielordner = self.gefiltert_parquet
        else:    
            zielordner = self.ungefiltert_parquet

        relativer_pfad = mat_datei.relative_to(self.ungefiltert_mat)
        parquet_name = relativer_pfad.with_suffix(".parquet").as_posix().replace("/", "_").replace(" ", "_") #Änderung zu with_suffix zur Vereinfachung der Dateinamenserstellung, ebenso as_posix
        zielpfad = zielordner / parquet_name

        pq.write_table(
            tabelle,
            zielpfad,
            use_dictionary=['signal', 'wert'],
            column_encoding={'zeit': 'DELTA_BINARY_PACKED'},
            compression='zstd',
            compression_level=6
        )

        print(f"Datei erfolgreich erstellt: {zielpfad}")
        return zielpfad

    def alle_mat_zu_parquet(self):
        matliste = [f for f in self.ungefiltert_mat.rglob("*.mat")]
        print(f"Liste der .mat-Dateien im temp-Ordner: {matliste}")

        for mat_datei in matliste:
            self.mat_zu_parquet(mat_datei)

if __name__ == "__main__":
    umwandler = ParquetUmwandlung()
    umwandler.alle_mat_zu_parquet(filterung=False)

