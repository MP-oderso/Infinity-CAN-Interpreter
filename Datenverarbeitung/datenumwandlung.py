from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq
import h5py
import pyarrow.compute as pc

root_path = Path(__file__).resolve().parent.parent #für die Pfadbestimmung
temp_path = root_path / "temp"
data_path = root_path / "data"

def umwandlung_mat_zu_parquet(mat_datei: str, parquet_datei: str):
    signal, zeit, wert = [], [], []
    testdatei = h5py.File(temp_path / mat_datei, "r") #measuerement_22 von 2026-09-13_18-01-41

    for name, daten in testdatei.items():
        signal.extend([name] * daten.shape[1])
        zeit.extend((daten[0] -719529) * 86400000) # Umrechnung von MATLAB-Datum in Unix-Zeitstempel in Milisekunden               "-719529) * 86400000)" von KI
        wert.extend(daten[1])

    pq.write_table(
        pa.table(
          {
            'signal': signal,
            'zeit': pa.array(zeit, type=pa.int64()).cast(pa.timestamp('ms')),
            'wert': pc.round(pa.array(wert, type=pa.float64()), ndigits=3),
        }
        ),
        data_path / parquet_datei,
        use_dictionary=['signal', 'wert'],
        column_encoding={'zeit': 'DELTA_BINARY_PACKED'},
        compression='zstd',
        compression_level=6
    )
    print(f"Datei erfolgreich erstellt: {data_path / parquet_datei}")

url = "https://hochschulekempten-my.sharepoint.com/:f:/g/personal/stmmseif_hochschulekempten_onmicrosoft_com/IgDZN0bQJv3pQarjiJU8889jAQrw3zdKSNzvk75zhwHT6-Q?e=oMu64C"


matliste = [str(f.relative_to(temp_path)) for f in temp_path.rglob("*.mat")]
print(f"Liste der .mat-Dateien im temp-Ordner: {matliste}")

for mat_datei in matliste:
    parquet_datei = mat_datei.replace(".mat", ".parquet").replace("\\", "_").replace(" ", "_")
    umwandlung_mat_zu_parquet(mat_datei, parquet_datei)
