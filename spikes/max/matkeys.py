import h5py
import pathlib as path 

temp_path = path.Path(__file__).parent.parent.parent / "temp"

#von KI geschriebener code um zu sehen welche Variablen in der .mat-Datei enthalten sind

mat_file_path = temp_path / "measurement_22.mat"

# .mat-Datei im Lesemodus öffnen
with h5py.File(mat_file_path, "r") as mat_file:
    # Alle Keys (Variablennamen) abgreifen
    all_keys = list(mat_file.keys())
    
    # MATLAB-interne Metadaten ausblenden
    user_variables = [key for key in all_keys if not key.startswith('#')]
    
    print("--- Gefundene Variablen (Spalten) in der .mat-Datei ---")
    for var in user_variables:
        # Optional: Dimensionen (Shape) und Datentyp direkt mit ausgeben
        shape = mat_file[var].shape
        dtype = mat_file[var].dtype
        print(f"Name: '{var}' | Form: {shape} | Datentyp: {dtype}")