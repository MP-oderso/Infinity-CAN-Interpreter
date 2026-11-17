from dataclasses import dataclass
from datenumwandlung import main_path
import pyarrow.parquet as pq
import pyarrow as pa

@dataclass
class parquett_filter:
    
    path_in: str="main_path/data"
    path_out: str="main_path/sorted_data"
    filename: str="measurment"

@classmethod
def read_parquet(self):
    self.table = pq.read_table(self.path_in / self.filename)
    return self.table

@classmethod
def dowmsample_data(self,samplerate):
    self.samplerate = samplerate
    self.sampled_table =self.table.filter((self.table['zeit'] % self.samplerate) == 0)
    del self.table
    return self.sampled_table

@classmethod
def write_parquett(self):
    pq.write_table(
        pa.table(self.sampled_data),
        data_path / self.filename,
        use_dictionary=['signal', 'wert'],
        column_encoding={'zeit': 'DELTA_BINARY_PACKED'},
        compression='zstd',
        compression_level=6    
    )
   
    


        

    