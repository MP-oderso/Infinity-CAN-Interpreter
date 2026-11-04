from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq
import h5py

max_path = Path(__file__).resolve().parent #für die Pfadbestimmung
main_path = max_path.parent.parent
temp_path = main_path / "temp"
data_path = main_path / "data"
print(f"max_path: {max_path}")
print(f"main_path: {main_path}")
print(f"temp_path: {temp_path}")
print(f"data_path: {data_path}")

signal, zeit, wert = [], [], []
testdatei = h5py.File(temp_path / "measurement_22.mat", "r") #measuerement_22 von 2026-09-13_18-01-41

for name, daten in testdatei.items():
    signal.extend([name] * daten.shape[1])
    zeit.extend(daten[0])
    wert.extend(daten[1])

pq.write_table(
    pa.table(
        {'signal': signal, 'zeit': zeit, 'wert': wert},
    ),
    data_path / 'Measurement_22.parquet',
    compression='zstd',
    compression_level=6
)
print(f"Datei erfolgreich erstellt: {data_path / 'Measurement_22.parquet'}")