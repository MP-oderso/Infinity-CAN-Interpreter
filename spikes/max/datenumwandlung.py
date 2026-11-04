from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq
import h5py
import pyarrow.compute as pc

max_path = Path(__file__).resolve().parent #für die Pfadbestimmung
main_path = max_path.parent.parent
temp_path = main_path / "temp"
data_path = main_path / "data"

signal, zeit, wert = [], [], []
testdatei = h5py.File(temp_path / "measurement_22.mat", "r") #measuerement_22 von 2026-09-13_18-01-41

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
    data_path / 'Measurement_22.parquet',
    use_dictionary=['signal', 'wert'],
    column_encoding={'zeit': 'DELTA_BINARY_PACKED'},
    compression='zstd',
    compression_level=6
)
print(f"Datei erfolgreich erstellt: {data_path / 'Measurement_22.parquet'}")